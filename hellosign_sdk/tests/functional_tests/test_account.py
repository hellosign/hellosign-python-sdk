from unittest import TestCase
from hellosign_sdk.tests.test_helper import api_key
from hellosign_sdk.hsclient import HSClient
from hellosign_sdk.resource.account import Account
from hellosign_sdk.utils.exception import BadRequest, Unauthorized
from time import time

class TestAccount(TestCase):

    def setUp(self):
        self.client = HSClient(api_key=api_key)

    def test_create_account(self):
        ''' Test creating new accounts '''

        # Bad account data
        try:
            self.client.create_account("not valid email@example.com", "password")
            self.fail()
        except BadRequest:
            pass
        try:
            self.client.create_account("", "password")
            self.fail()
        except BadRequest:
            pass
        try:
            self.client.create_account("email@example.com", "")
            self.fail()
        except BadRequest:
            pass

        # Valid account creation
        email = "py-sdk-test-%s@example.com" % time()
        pwd = "somepassword"
        try:
            result = self.client.create_account(email, pwd)
            self.assertEquals(isinstance(result, Account), True)
        except:
            self.fail()

        # Already exists
        try:
            self.client.create_account(email, pwd)
            self.fail()
        except BadRequest, e:
            self.assertTrue(e.message.find('account already exists') > 0)

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
        print "RESULT = %s" % result
        self.assertEquals(isinstance(result, Account), True)
        self.assertEquals(result.callback_url, new_callback_url)

    def test_account_verify(self):
        ''' Test verifying the existence of a given account '''
        self.client.get_account_info()
        acct = self.client.account
        if acct.is_paid_hs:
            self.assertTrue(self.client.verify_account(email=acct.email_address))
            self.assertFalse(self.client.verify_account(email='not-an-account@example.com'))
        else:
            print "WARNING: Skipping test_account_verify because it requires a paid API plan"
