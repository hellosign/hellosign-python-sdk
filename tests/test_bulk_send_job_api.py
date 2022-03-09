import unittest

from hellosign_sdk import ApiClient, Configuration, apis
from test_utils import get_fixture_data, MockPoolManager, deserialize


class TestBulkSendJobApi(unittest.TestCase):
    def setUp(self):
        self.configuration = Configuration()
        self.api_client = ApiClient(self.configuration)
        self.mock_pool = MockPoolManager(self)
        self.api_client.rest_client.pool_manager = self.mock_pool

        self.api = apis.BulkSendJobApi(self.api_client)

    def test_bulk_send_job_get(self):
        bulk_send_job_id = '6e683bc0369ba3d5b6f43c2c22a8031dbf6bd174'

        response_class = 'BulkSendJobGetResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='application/json',
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')

        result = self.api.bulk_send_job_get(bulk_send_job_id)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)

    def test_bulk_send_job_list(self):
        page = 1
        page_size = 20

        response_class = 'BulkSendJobListResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='application/json',
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')

        result = self.api.bulk_send_job_list(page=page, page_size=page_size)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
