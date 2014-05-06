from unittest import TestCase
from hellosign_sdk.tests.test_helper import api_key
from hellosign_sdk import HSClient
from hellosign_sdk.utils.exception import *


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
