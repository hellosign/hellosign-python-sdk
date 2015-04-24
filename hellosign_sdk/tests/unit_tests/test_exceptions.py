from unittest import TestCase
from hellosign_sdk.tests.test_helper import api_key
from hellosign_sdk import HSClient
from hellosign_sdk.utils.exception import *

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


class TestException(TestCase):

    def setUp(self):
        self.client = HSClient(api_key=api_key)

    def test_hsexception(self):
        error = HSException("Message")
        self.assertEqual(str(error), "Message")
        self.assertEqual(error.type, "HSException")

    def test_no_auth_method(self):
        error = NoAuthMethod("No authentication information found")
        self.assertEquals(str(error), "No authentication information found")
        self.assertEquals(error.type, "NoAuthMethod")

    def test_http_error(self):
        error = BadRequest("Bad Request", 400)
        self.assertEquals(str(error), "Bad Request")
        self.assertEquals(error.http_code, 400)
        self.assertEquals(error.type, "BadRequest")
