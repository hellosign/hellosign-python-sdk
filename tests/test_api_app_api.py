import unittest

from hellosign_sdk import ApiClient, Configuration, apis
from test_utils import get_fixture_data, MockPoolManager, deserialize, get_base_path


class TestApiAppApi(unittest.TestCase):
    def setUp(self):
        self.configuration = Configuration()
        self.api_client = ApiClient(self.configuration)
        self.mock_pool = MockPoolManager(self)
        self.api_client.rest_client.pool_manager = self.mock_pool

        self.api = apis.ApiAppApi(self.api_client)

    def test_api_app_create(self):
        request_class = 'ApiAppCreateRequest'
        request_data = get_fixture_data(request_class)['default']

        response_class = 'ApiAppGetResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='multipart/form-data',
            data=request_data,
            response=response_data
        )

        obj = deserialize(request_data, f'models.{request_class}')
        obj.custom_logo_file = open(f'{get_base_path()}/pdf-sample.pdf', 'rb')

        expected = deserialize(response_data, f'models.{response_class}')

        result = self.api.api_app_create(obj)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)

    def test_api_app_get(self):
        client_id = '0dd3b823a682527788c4e40cb7b6f7e9'

        response_class = 'ApiAppGetResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='application/json',
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')

        result = self.api.api_app_get(client_id)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)

    def test_api_app_update(self):
        client_id = '0dd3b823a682527788c4e40cb7b6f7e9'

        request_class = 'ApiAppUpdateRequest'
        request_data = get_fixture_data(request_class)['default']

        response_class = 'ApiAppGetResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='multipart/form-data',
            data=request_data,
            response=response_data
        )

        obj = deserialize(request_data, f'models.{request_class}')
        obj.custom_logo_file = open(f'{get_base_path()}/pdf-sample.pdf', 'rb')

        expected = deserialize(response_data, f'models.{response_class}')

        result = self.api.api_app_update(client_id, obj)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)

    def test_api_app_delete(self):
        self.skipTest('skipping test_api_app_delete')

    def test_api_app_list(self):
        page = 1
        page_size = 20

        response_class = 'ApiAppListResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='application/json',
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')

        result = self.api.api_app_list(page=page, page_size=page_size)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
