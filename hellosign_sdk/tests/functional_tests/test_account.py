from unittest import TestCase
from hellosign_sdk.tests.test_helper import api_key
from hellosign_sdk.hsclient import HSClient
from hellosign_sdk.resource.account import Account
from hellosign_sdk.utils.exception import BadRequest


class TestAccount(TestCase):

    def setUp(self):
        self.client = HSClient(api_key=api_key)

    def test_get_account_info(self):
        result = self.client.get_account_info()
        self.assertEquals(result, True)
        self.assertEquals(isinstance(self.client.account, Account), True)

        new_client = HSClient(api_key='non valid api key')
        result = new_client.get_account_info()
        self.assertEquals(result, False)

    def test_update_account_info(self):
        # We update nothing, but the api returns an Account object, so it is
        # considered successful
        result = self.client.get_account_info()
        self.assertEquals(result, True)
        result = self.client.update_account_info()
        self.assertEquals(result, True)

        self.client.account.callback_url = 'not valid url'
        account = self.client.update_account_info()
        self.assertEquals(account, False)

    def test_account_verify(self):
        self.client.get_account_info()
        acct = self.client.account
        self.assertTrue(self.client.verify_account(email=acct.email_address))
        self.assertFalse(self.client.verify_account(email='not-an-account@example.com'))

    def test_create_account_with_invalid_info(self):
        try:
            self.client.create_account("not valid email@example.com",
                                       "password")
        except BadRequest:
            pass
        try:
            self.client.create_account("", "password")
        except BadRequest:
            pass
        try:
            self.client.create_account("email@example.com", "")
        except BadRequest:
            pass
