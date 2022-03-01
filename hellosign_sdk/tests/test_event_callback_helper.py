import os
import json
import unittest
from metadict import MetaDict

from hellosign_openapi_python_sdk import ApiClient, Configuration, EventCallbackHelper
from hellosign_openapi_python_sdk.models import EventCallbackApiAppRequest


class TestEventCallbackHelper(unittest.TestCase):
    def test_is_valid(self):
        configuration = Configuration()
        api_client = ApiClient(configuration)

        file = open(
            os.path.realpath('.') + '/../../oas/test_fixtures/EventCallbackHelper.json', 'r'
        )
        fixture_data = json.load(file)
        file.close()

        api_key = '324e3b0840f065eb51f3fd63231d0d33daa35d4ed10d27718839e81737065782'
        api_key_rev = api_key[::-1]

        for key, value in fixture_data.items():
            data = MetaDict()
            data.data = json.dumps({'json': value})

            obj = api_client.deserialize(
                response=data,
                response_type=[EventCallbackApiAppRequest],
                _check_type=True,
            )

            self.assertTrue(EventCallbackHelper.is_valid(api_key, obj.json.event))
            self.assertFalse(EventCallbackHelper.is_valid(api_key_rev, obj.json.event))


if __name__ == '__main__':
    unittest.main()
