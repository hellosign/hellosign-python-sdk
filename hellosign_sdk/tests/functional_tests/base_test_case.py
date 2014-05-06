from unittest import TestCase
from hellosign_sdk import HSClient
from hellosign_sdk.tests import test_helper

class BaseTestCase(TestCase):
    ''' Base for all test cases '''

    def setUp(self):
        params = {
            'api_key': test_helper.api_key
        }
        try:
            params['env'] = test_helper.env
        except AttributeError:
            pass
        self.client = HSClient(**params)
        self.client_id = test_helper.client_id
