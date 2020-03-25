from unittest import TestCase
from hellosign_sdk.utils import HSRequest, HSAccessTokenAuth

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


class TestHSAccessTokenAuth(TestCase):

    def test_init(self):
        auth = HSAccessTokenAuth(
            access_token="369c76ae6185f3b7",
            access_token_type="Bearer",
            refresh_token="6a8949c799991e12dac70cb135095680",
            expires_in=10000, state="demo"
        )
        self.assertEqual(auth.access_token, "369c76ae6185f3b7")
        self.assertEqual(auth.access_token_type, "Bearer")
        self.assertEqual(auth.refresh_token, "6a8949c799991e12dac70cb135095680")
        self.assertEqual(auth.expires_in, 10000)
        self.assertEqual(auth.state, "demo")

    def test_call(self):
        auth = HSAccessTokenAuth(access_token="thetoken", access_token_type="thetokentype")
        request = HSRequest(auth)
        response = request.get(url='http://httpbin.org/headers')
        self.assertEqual(response['headers']['Authorization'], 'thetokentype thetoken')
