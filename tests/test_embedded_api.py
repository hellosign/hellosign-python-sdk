import unittest

from hellosign_sdk import ApiClient, Configuration, apis
from test_utils import get_fixture_data, MockPoolManager, deserialize


class TestEmbeddedApi(unittest.TestCase):
    def setUp(self):
        self.configuration = Configuration()
        self.api_client = ApiClient(self.configuration)
        self.mock_pool = MockPoolManager(self)
        self.api_client.rest_client.pool_manager = self.mock_pool

        self.api = apis.EmbeddedApi(self.api_client)

    def test_embedded_edit_url(self):
        template_id = '5de8179668f2033afac48da1868d0093bf133266'

        request_class = 'EmbeddedEditUrlRequest'
        request_data = get_fixture_data(request_class)['default']

        response_class = 'EmbeddedEditUrlResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='application/json',
            data=request_data,
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')
        obj = deserialize(request_data, f'models.{request_class}')

        result = self.api.embedded_edit_url(template_id, obj)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)

    def test_embedded_sign_url(self):
        signature_id = '50e3542f738adfa7ddd4cbd4c00d2a8ab6e4194b'

        response_class = 'EmbeddedSignUrlResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='application/json',
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')

        result = self.api.embedded_sign_url(signature_id)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
