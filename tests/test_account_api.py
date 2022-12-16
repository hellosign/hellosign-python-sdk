import unittest
import random

from hellosign_sdk import ApiClient, ApiException, Configuration, apis
from test_utils import get_fixture_data, MockPoolManager, deserialize


class TestAccountApi(unittest.TestCase):
    def setUp(self):
        self.configuration = Configuration()
        self.api_client = ApiClient(self.configuration)
        self.mock_pool = MockPoolManager(self)
        self.api_client.rest_client.pool_manager = self.mock_pool

        self.api = apis.AccountApi(self.api_client)

    def test_http_code_range(self):
        request_class = 'AccountCreateRequest'
        request_data = get_fixture_data(request_class)['default']

        response_class = 'ErrorResponse'
        response_data = get_fixture_data(response_class)['default']

        code = random.randrange(400, 499)

        self.mock_pool.expect_request(
            content_type='application/json',
            data=request_data,
            response=response_data,
            status=code,
        )
        expected = deserialize(response_data, f'models.{response_class}')
        obj = deserialize(request_data, f'models.{request_class}')

        try:
            self.api.account_create(obj)
        except ApiException as e:
            self.assertEqual(e.body.__class__.__name__, response_class)
            self.assertEqual(e.body, expected)

    def test_account_create(self):
        request_class = 'AccountCreateRequest'
        request_data = get_fixture_data(request_class)['default']

        response_class = 'AccountCreateResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='application/json',
            data=request_data,
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')
        obj = deserialize(request_data, f'models.{request_class}')

        result = self.api.account_create(obj)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)

    def test_account_get(self):
        response_class = 'AccountGetResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='application/json',
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')

        result = self.api.account_get(email_address="jack@example.com")

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)

    def test_account_update(self):
        request_class = 'AccountUpdateRequest'
        request_data = get_fixture_data(request_class)['default']

        response_class = 'AccountGetResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='application/json',
            data=request_data,
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')
        obj = deserialize(request_data, f'models.{request_class}')

        result = self.api.account_update(obj)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)

    def test_account_verify(self):
        request_class = 'AccountVerifyRequest'
        request_data = get_fixture_data(request_class)['default']

        response_class = 'AccountVerifyResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='application/json',
            data=request_data,
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')
        obj = deserialize(request_data, f'models.{request_class}')

        result = self.api.account_verify(obj)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
