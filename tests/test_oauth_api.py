import unittest

from hellosign_sdk import ApiClient, Configuration, apis
from test_utils import get_fixture_data, MockPoolManager, deserialize


class TestOAuthApi(unittest.TestCase):
    def setUp(self):
        self.configuration = Configuration()
        self.api_client = ApiClient(self.configuration)
        self.mock_pool = MockPoolManager(self)
        self.api_client.rest_client.pool_manager = self.mock_pool

        self.api = apis.OAuthApi(self.api_client)

    def test_token_generate(self):
        request_class = 'OAuthTokenGenerateRequest'
        request_data = get_fixture_data(request_class)['default']

        response_class = 'OAuthTokenResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='application/json',
            data=request_data,
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')
        obj = deserialize(request_data, f'models.{request_class}')

        result = self.api.oauth_token_generate(obj)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)

    def test_token_refresh(self):
        request_class = 'OAuthTokenRefreshRequest'
        request_data = get_fixture_data(request_class)['default']

        response_class = 'OAuthTokenResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='application/json',
            data=request_data,
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')
        obj = deserialize(request_data, f'models.{request_class}')

        result = self.api.oauth_token_refresh(obj)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
