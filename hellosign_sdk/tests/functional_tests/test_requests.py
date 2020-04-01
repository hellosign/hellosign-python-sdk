from hellosign_sdk.tests.functional_tests import BaseTestCase
from hellosign_sdk.utils import HSRequest
from time import time

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


class TestRequests(BaseTestCase):

    TEST_WARNING_NAME = 'fake_warning'
    TEST_WARNING_MSG = 'Fake warning message'

    def _add_test_warning_to_response(self, response):
        ''' Add a fake test warning to the given response '''
        if response:
            response['warnings'] = [{
                'warning_name': self.TEST_WARNING_NAME,
                'warning_msg': self.TEST_WARNING_MSG
            }]
        return response

    def _check_warnings(self, warnings):
        ''' Check that the given warnings are as expected '''
        self.assertIsNotNone(warnings)
        self.assertIsInstance(warnings, list)
        self.assertIs(len(warnings), 1)
        self.assertIsInstance(warnings[0], dict)
        self.assertIsNotNone(warnings[0].get('warning_name'))
        self.assertEqual(warnings[0]['warning_name'], self.TEST_WARNING_NAME)
        self.assertIsNotNone(warnings[0].get('warning_msg'))
        self.assertEqual(warnings[0]['warning_msg'], self.TEST_WARNING_MSG)

    def test_warnings(self):
        ''' Test warning accessibility '''
        
        t = time()
        self.client.response_callback = self._add_test_warning_to_response
        acct = self.client.create_account("demo-%s@example.com" % t)

        # Get last warnings
        last_warnings = self.client.get_last_warnings()
        self._check_warnings(last_warnings)

        # Get object warnings
        obj_warnings = acct.get_warnings()
        self._check_warnings(obj_warnings)

        # Last warnings get cleared by new requests
        self.client.response_callback = None
        self.client.create_account("demo-%s@example.com" % (t+1))
        self.assertIsNone(self.client.get_last_warnings())

    def test_user_agent(self):
        ''' Test that the user agent is correctly sent '''

        self.client.create_account("demo-%s@example.com" % time())

        req_headers = self.client.request.headers
        self.assertIsNotNone(req_headers)
        self.assertIsInstance(req_headers, dict)
        self.assertIsNotNone(req_headers.get('User-Agent'))
        self.assertEqual(req_headers['User-Agent'], HSRequest._get_user_agent())

        parts = req_headers['User-Agent'].split('/')
        self.assertIs(len(parts), 2)
        self.assertEqual(parts[0], 'hellosign-python-sdk')
        parts = parts[1].split('.')
        self.assertIs(len(parts), 3)
        try:
            int(parts[0])
            int(parts[1])
        except ValueError:
            self.fail('Invalid version number')
        self.assertEqual(parts[2], '5')
