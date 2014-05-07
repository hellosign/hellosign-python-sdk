import os
import requests
from exception import *


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
    USER_AGENT = "HelloSign Python SDK"
    
    parameters = None
    headers = { 'User-Agent': USER_AGENT }
    http_status_code = 0
    verify_ssl = True

    def __init__(self, auth, env="production"):
        self.auth = auth
        self.env = env
        self.debug = (self.env != 'production')
        self.verify_ssl = (not self.debug)

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
            print "GET: %s, headers=%s" % (url, headers)

        get_headers = self.headers
        get_parameters = self.parameters
        if get_parameters is None:
            # In case self.parameters is still empty
            get_parameters = {}
        if headers is not None:
            get_headers.update(headers)
        if parameters is not None:
            get_parameters.update(parameters)

        response = requests.get(url, headers=get_headers, params=get_parameters, auth=self.auth, verify=self.verify_ssl)
        self.http_status_code = response.status_code
        self._check_error(response)
        if get_json is True:
            return response.json()
        return response

    def get_file(self, url, filename, headers=None):
        ''' Get a file from a url and save it as `filename`

        Args:
            url (str): URL to send the request to

            filename (str): File name to save the file as, this can be either
                a full path or a relative path

            headers (str, optional): custom headers

        Returns:
            True if file is downloaded and written successfully, False
            otherwise.

        '''

        if self.debug:
            print "GET FILE: %s, headers=%s" % (url, headers)

        get_headers = self.headers
        if headers is not None:
            get_headers.update(headers)

        response = requests.get(url, headers=get_headers, auth=self.auth, verify=self.verify_ssl)
        
        self.http_status_code = response.status_code
        try:
            self._check_error(response)
            fd = os.open(filename, os.O_CREAT | os.O_RDWR)
            with os.fdopen(fd, "w+b") as f:
                f.write(response.content)
        except:
            return False
        
        return True

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
            print "POST: %s, headers=%s" % (url, headers)

        post_headers = self.headers
        if headers is not None:
            post_headers.update(headers)
        response = requests.post(url, headers=post_headers, data=data, auth=self.auth, files=files, verify=self.verify_ssl)
        self.http_status_code = response.status_code
        self._check_error(response)
        if get_json is True:
            return response.json()
        return response

    # TODO: use a expected key in returned json, if the returned key does not match, return false...
    def _check_error(self, response):
        ''' Check for HTTP error code from the response, raise exception if
        there's any

        Args:
            response (object): Object returned by requests' `get` and `post`
                methods

        Raises:
            HTTPError: If the status code of response is either 4xx or 5xx

        Returns:
            True if status code is not error code
        
        '''

        # If status code is 4xx or 5xx, that should be an error
        if response.status_code >= 400:
            # I intended to return False here but raising a meaningful exception
            # may make senses more.
            try:
                raise self._check_http_error_code(response.status_code)(
                    str(response.status_code) + " error: " +
                    response.json()["error"]["error_msg"], response.status_code)
            # This is to catch error when we post get oath data
            except TypeError:
                raise self._check_http_error_code(response.status_code)(
                    str(response.status_code) + " error: " +
                    response.json()["error_description"], response.status_code)
        # Return True if everything looks OK
        return True

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
