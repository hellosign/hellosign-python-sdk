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

    warned = False

    def setUp(self):
        params = {
            'api_key': test_helper.api_key
        }
        try:
            params['env'] = test_helper.env
        except AttributeError:
            params['env'] = 'production'
        self.client = HSClient(**params)
        self.client_id = test_helper.client_id
        self.client_secret = test_helper.client_secret

        if params['env'] == 'production' and not BaseTestCase.warned:
            BaseTestCase.warned = True
            print("\n\n")
            print(" ==================================================================")
            print(" = WARNING: We advise against running the tests against your      =")
            print(" = personal account as they perform destructive actions.          =")
            print(" ==================================================================")
            while True:
                resp = input(' > Continue (type yes or hit Ctrl+C to exit)?')
                if resp == 'yes':
                    # Continue to tests
                    break
                elif resp == 'no':
                    # Stop here
                    import sys
                    sys.exit()
                else:
                    # Ask question again
                    pass 
            print()

        print()
