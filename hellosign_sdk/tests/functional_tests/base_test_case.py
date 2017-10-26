from unittest import TestCase
from hellosign_sdk import HSClient
from hellosign_sdk.tests import test_helper

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


class BaseTestCase(TestCase):
    ''' Base for all test cases '''

    def setUp(self):
        params = {
            'api_key': test_helper.api_key
        }
        try:
            params['env'] = test_helper.env
        except AttributeError:
            params['env'] = 'production'
        try:
            ok_to_run_functional_tests = test_helper.ok_to_run_functional_tests
        except AttributeError:
            ok_to_run_functional_tests = False
        self.client = HSClient(**params)
        self.client_id = test_helper.client_id
        self.client_secret = test_helper.client_secret

        if params['env'] == 'production' and not ok_to_run_functional_tests:
            raise Exception(
                'We advise against running the tests against your personal '
                'account as they perform destructive actions. Please set '
                "ok_to_run_functional_tests=True in test_helper.py"
            )
