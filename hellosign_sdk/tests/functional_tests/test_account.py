from hellosign_sdk.tests.functional_tests import BaseTestCase
from hellosign_sdk import HSClient
from hellosign_sdk.resource import Account
from hellosign_sdk.utils import BadRequest, Unauthorized, HSException, HSAccessTokenAuth
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


class TestAccount(BaseTestCase):

    def test_create_account(self):
        ''' Test creating new accounts '''

        # Bad account data
        try:
            self.client.create_account("not valid email@example.com")
            self.fail()
        except BadRequest:
            pass
        try:
            self.client.create_account("")
            self.fail()
        except BadRequest:
            pass

        # Valid account creation
        try:
            
            email = "py-sdk-test-%s@example.com" % time()
            result = self.client.create_account(email)
            self.assertEquals(isinstance(result, Account), True)

            # Should work too if giving a password, even though it's not used
            email = "py-sdk-test-%s@example.com" % time()
            result = self.client.create_account(email, "something")
            self.assertEquals(isinstance(result, Account), True)
            
        except HSException as e:
            self.fail(e.message)

        # Already exists
        try:
            self.client.create_account(email)
            self.fail()
        except BadRequest as e:
            self.assertTrue(e.message.lower().find('account already exists') > 0)

        # Created via app
        email = "py-sdk-test-%s@example.com" % time()
        try:
            acct = self.client.create_account(email, client_id=self.client_id, client_secret=self.client_secret)
            self.assertTrue(acct is not None)
            self.assertEquals(acct.email_address, email)
            self.assertTrue(hasattr(acct, 'oauth'))
            self.assertTrue(acct.oauth is not None)
            self.assertTrue(isinstance(acct.oauth, HSAccessTokenAuth))
        except HSException as e:
            self.fail(e.message)


    def test_get_account_info(self):
        ''' Test retrieving account information '''

        # Valid account
        result = self.client.get_account_info()
        self.assertEquals(isinstance(result, Account), True)

        # Account does not exist
        try:
            new_client = HSClient(api_key='non valid api key')
            new_client.get_account_info()
            self.fail()
        except Unauthorized:
            pass

    def test_update_account_info(self):
        ''' Test updating account info '''

        # We update nothing, but the api returns an Account object, so it is considered successful
        result = self.client.get_account_info()
        self.assertEquals(isinstance(result, Account), True)

        # Invalid callback url
        try:
            self.client.account.callback_url = 'not valid url'
            self.client.update_account_info()
            self.fail()
        except BadRequest:
            pass

        # Valid update
        new_callback_url = 'http://www.example.com/mycallback'
        self.client.account.callback_url = new_callback_url
        result = self.client.update_account_info()
        self.assertEquals(isinstance(result, Account), True)
        self.assertEquals(result.callback_url, new_callback_url)

    def test_account_verify(self):
        ''' Test verifying the existence of a given account '''
        self.client.get_account_info()
        acct = self.client.account
        if acct.is_paid_hs:
            self.assertTrue(self.client.verify_account(email_address=acct.email_address))
            self.assertFalse(self.client.verify_account(email_address='not-an-account@example.com'))
        else:
            print("WARNING: Skipping test_account_verify because it requires a paid API plan")
