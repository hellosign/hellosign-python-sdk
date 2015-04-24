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

from requests.auth import AuthBase

class HSAccessTokenAuth(AuthBase):
    ''' Authentication object using HelloSign's access token '''

    def __init__(self, access_token, access_token_type, refresh_token=None, expires_in=None, state=None):
        ''' Initialziation of the object

        Args:
            access_token (str): Access token
            access_token_type (str): Access token type
            refresh_token (str):
            expires_in (int): Seconds after which the token will expire
            state (str):

        '''

        self.access_token = access_token
        self.access_token_type = access_token_type
        self.refresh_token = refresh_token
        self.expires_in = expires_in
        self.state = state

    def __call__(self, r):
        r.headers['Authorization'] = "%s %s" % (self.access_token_type, self.access_token)
        return r

    @classmethod
    def from_response(self, response_data):
        ''' Builds a new HSAccessTokenAuth straight from response data 

        Args:
            response_data (dict): Response data to use

        Returns:
            A HSAccessTokenAuth objet

        '''
        return HSAccessTokenAuth(
            response_data['access_token'],
            response_data['token_type'], 
            response_data['refresh_token'],
            response_data['expires_in'], 
            response_data.get('state') # Not always here
        )
