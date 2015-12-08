import os
import requests
import json
from .exception import *

#
# The MIT License (MIT)
# 
# Copyright (C) 2014 hellosign.com
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#


class HSRequest(object):
    ''' Object to handle HTTP requests

    Although we have greate requests package which can handle the HTTP request
    beautifully, we need this class to fit better our need like sending the
    requests with authentication information, download files, check HTTP
    errors...

    Attributes:
        DEFAULT_ENCODING (str): Default encoding for requests
        USER_AGENT (str): HTTP User agent used when sending requests
        parameters (dict): Some parameters for GET requests
        headers (dict): Custome headers for every requests
        http_status_code (int): HTTP status code returned of requests

    '''

    DEFAULT_ENCODING = "UTF-8"
    USER_AGENT = "hellosign-python-sdk"

    parameters = None
    http_status_code = 0
    verify_ssl = True
    warnings = None
    response_callback = None
    headers = None

    def __init__(self, auth, env="production"):
        self.auth = auth
        self.env = env
        self.debug = (self.env != 'production')
        self.verify_ssl = (not self.debug)

    def get_warnings(self):
        ''' Return the list of warnings associated with this request, or None if there aren't any '''
        if self.warnings and len(self.warnings) > 0:
            return self.warnings

    def get_file(self, url, path_or_file=None, headers=None, filename=None):
        ''' Get a file from a url and save it as `filename`

        Args:
            url (str): URL to send the request to

            path_or_file (str or file): A writable File-like object or a path to save the file to.

            filename (str): [DEPRECATED] File name to save the file as, this can be either
                a full path or a relative path

            headers (str, optional): custom headers

        Returns:
            True if file is downloaded and written successfully, False
            otherwise.

        '''
        path_or_file = path_or_file or filename

        if self.debug:
            print("GET FILE: %s, headers=%s" % (url, headers))

        self.headers = self._get_default_headers()
        if headers is not None:
            self.headers.update(headers)

        response = requests.get(url, headers=self.headers, auth=self.auth, verify=self.verify_ssl)

        self.http_status_code = response.status_code
        try:
            # No need to check for warnings here
            self._check_error(response)
            try:
                path_or_file.write(response.content)
            except AttributeError:
                fd = os.open(path_or_file, os.O_CREAT | os.O_RDWR)
                with os.fdopen(fd, "w+b") as f:
                    f.write(response.content)
        except:
            return False

        return True

    def get(self, url, headers=None, parameters=None, get_json=True):
        ''' Send a GET request with custome headers and parameters

        Args:
            url (str): URL to send the request to
            headers (str, optional): custom headers
            parameters (str, optional): optional parameters

        Returns:
            A JSON object of the returned response if `get_json` is True,
            Requests' response object otherwise

        '''

        if self.debug:
            print("GET: %s, headers=%s" % (url, headers))

        self.headers = self._get_default_headers()
        get_parameters = self.parameters
        if get_parameters is None:
            # In case self.parameters is still empty
            get_parameters = {}
        if headers is not None:
            self.headers.update(headers)
        if parameters is not None:
            get_parameters.update(parameters)

        response = requests.get(url, headers=self.headers, params=get_parameters, auth=self.auth, verify=self.verify_ssl)
        json_response = self._process_json_response(response)

        return json_response if get_json is True else response

    def post(self, url, data=None, files=None, headers=None, get_json=True):
        ''' Make POST request to a url

        Args:
            url (str): URL to send the request to
            data (dict, optional): Data to send
            files (dict, optional): Files to send with the request
            headers (str, optional): custom headers

        Returns:
            A JSON object of the returned response if `get_json` is True,
            Requests' response object otherwise

        '''

        if self.debug:
            print("POST: %s, headers=%s" % (url, headers))

        self.headers = self._get_default_headers()
        if headers is not None:
            self.headers.update(headers)

        response = requests.post(url, headers=self.headers, data=data, auth=self.auth, files=files, verify=self.verify_ssl)
        json_response = self._process_json_response(response)
        
        return json_response if get_json is True else response


    ####  HELPERS  ########################################

    def _get_json_response(self, resp):
        ''' Parse a JSON response '''
        if resp is not None and resp.text is not None:
            try:
                text = resp.text.strip('\n')
                if len(text) > 0:
                    return json.loads(text)
            except ValueError as e:
                if self.debug:
                    print("Could not decode JSON response: \"%s\"" % resp.text)
                raise e

    @classmethod
    def _get_user_agent(cls):
        ''' Get the user agent to be sent '''
        from hellosign_sdk import HSClient
        return cls.USER_AGENT + '/' + HSClient.version

    def _get_default_headers(self):
        ''' Return the default headers to send '''
        return {
            'User-Agent': HSRequest._get_user_agent()
        }

    def _process_json_response(self, response):
        ''' Process a given response '''

        json_response = self._get_json_response(response)
        
        if self.response_callback is not None:
            json_response = self.response_callback(json_response)
            response._content = json.dumps(json_response)

        self.http_status_code = response.status_code
        self._check_error(response, json_response)
        self._check_warnings(json_response)

        return json_response

    def _check_error(self, response, json_response=None):
        ''' Check for HTTP error code from the response, raise exception if there's any

        Args:
            response (object): Object returned by requests' `get` and `post`
                methods

            json_response (dict): JSON response, if applicable

        Raises:
            HTTPError: If the status code of response is either 4xx or 5xx

        Returns:
            True if status code is not error code
        
        '''

        # If status code is 4xx or 5xx, that should be an error
        if response.status_code >= 400:
            json_response = json_response or self._get_json_response(response)
            err_cls = self._check_http_error_code(response.status_code)
            try:
                raise err_cls("%s error: %s" % (response.status_code, json_response["error"]["error_msg"]), response.status_code)
            # This is to catch error when we post get oauth data
            except TypeError:
                raise err_cls("%s error: %s" % (response.status_code, json_response["error_description"]), response.status_code)

        # Return True if everything is OK
        return True

    def _check_warnings(self, json_response):
        ''' Extract warnings from the response to make them accessible

        Args:
            json_response (dict): JSON response
        
        '''

        self.warnings = None
        if json_response:
            self.warnings = json_response.get('warnings')

        if self.debug and self.warnings:
            for w in self.warnings:
                print("WARNING: %s - %s" % (w['warning_name'], w['warning_msg']))

    def _check_http_error_code(self, code):
        return {
            400: BadRequest,
            401: Unauthorized,
            402: PaymentRequired,
            403: Forbidden,
            404: NotFound,
            405: MethodNotAllowed,
            406: NotAcceptable,
            408: RequestTimeout,
            409: Conflict,
            410: Gone,
            414: RequestURITooLong,
            415: UnsupportedMediaType,
            416: RequestedRangeNotSatisfiable,
            500: InternalServerError,
            501: MethodNotImplemented,
            502: BadGateway,
            503: ServiceUnavailable,
            504: GatewayTimeout
        }.get(code, HTTPError)
