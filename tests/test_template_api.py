import unittest

from hellosign_sdk import ApiClient, Configuration, apis
from test_utils import get_fixture_data, MockPoolManager, deserialize, get_base_path


class TestTemplateApi(unittest.TestCase):
    def setUp(self):
        self.configuration = Configuration()
        self.api_client = ApiClient(self.configuration)
        self.mock_pool = MockPoolManager(self)
        self.api_client.rest_client.pool_manager = self.mock_pool

        self.api = apis.TemplateApi(self.api_client)

    def test_template_add_user(self):
        template_id = 'f57db65d3f933b5316d398057a36176831451a35'

        request_class = 'TemplateAddUserRequest'
        request_data = get_fixture_data(request_class)['default']

        response_class = 'TemplateGetResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='application/json',
            data=request_data,
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')
        obj = deserialize(request_data, f'models.{request_class}')

        result = self.api.template_add_user(template_id, obj)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)

    def test_template_create_embedded_draft(self):
        request_class = 'TemplateCreateEmbeddedDraftRequest'
        request_data = get_fixture_data(request_class)['default']

        response_class = 'TemplateCreateEmbeddedDraftResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='multipart/form-data',
            data=request_data,
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')
        obj = deserialize(request_data, f'models.{request_class}')
        obj.file = [open(f'{get_base_path()}/pdf-sample.pdf', 'rb')]

        result = self.api.template_create_embedded_draft(obj)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)

    def test_template_delete(self):
        self.skipTest('skipping test_template_delete')

    def test_template_files(self):
        self.skipTest('skipping test_template_files')

    def test_template_get(self):
        template_id = 'f57db65d3f933b5316d398057a36176831451a35'

        response_class = 'TemplateGetResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='application/json',
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')

        result = self.api.template_get(template_id)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)

    def test_template_list(self):
        account_id = 'all'

        response_class = 'TemplateListResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='application/json',
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')

        result = self.api.template_list(account_id=account_id)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)

    def test_template_remove_user(self):
        template_id = '21f920ec2b7f4b6bb64d3ed79f26303843046536'

        request_class = 'TemplateRemoveUserRequest'
        request_data = get_fixture_data(request_class)['default']

        response_class = 'TemplateGetResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='application/json',
            data=request_data,
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')
        obj = deserialize(request_data, f'models.{request_class}')

        result = self.api.template_remove_user(template_id, obj)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)

    def test_template_update_files(self):
        template_id = '21f920ec2b7f4b6bb64d3ed79f26303843046536'

        request_class = 'TemplateUpdateFilesRequest'
        request_data = get_fixture_data(request_class)['default']

        response_class = 'TemplateUpdateFilesResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='multipart/form-data',
            data=request_data,
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')
        obj = deserialize(request_data, f'models.{request_class}')
        obj.file = [open(f'{get_base_path()}/pdf-sample.pdf', 'rb')]

        result = self.api.template_update_files(template_id, obj)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
