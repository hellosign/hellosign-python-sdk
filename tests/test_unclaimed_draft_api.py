import unittest

from hellosign_sdk import ApiClient, Configuration, apis
from test_utils import get_fixture_data, MockPoolManager, deserialize, get_base_path


class TestUnclaimedDraftApi(unittest.TestCase):
    def setUp(self):
        self.configuration = Configuration()
        self.api_client = ApiClient(self.configuration)
        self.mock_pool = MockPoolManager(self)
        self.api_client.rest_client.pool_manager = self.mock_pool

        self.api = apis.UnclaimedDraftApi(self.api_client)

    def test_unclaimed_draft_create(self):
        request_class = 'UnclaimedDraftCreateRequest'
        request_data = get_fixture_data(request_class)['default']

        response_class = 'UnclaimedDraftCreateResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='multipart/form-data',
            data=request_data,
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')
        obj = deserialize(request_data, f'models.{request_class}')
        obj.file = [open(f'{get_base_path()}/pdf-sample.pdf', 'rb')]

        result = self.api.unclaimed_draft_create(obj)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)

    def test_unclaimed_draft_create_embedded(self):
        request_class = 'UnclaimedDraftCreateEmbeddedRequest'
        request_data = get_fixture_data(request_class)['default']

        response_class = 'UnclaimedDraftCreateResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='multipart/form-data',
            data=request_data,
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')
        obj = deserialize(request_data, f'models.{request_class}')
        obj.file = [open(f'{get_base_path()}/pdf-sample.pdf', 'rb')]

        result = self.api.unclaimed_draft_create_embedded(obj)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)

    def test_unclaimed_draft_create_embedded_with_template(self):
        request_class = 'UnclaimedDraftCreateEmbeddedWithTemplateRequest'
        request_data = get_fixture_data(request_class)['default']

        response_class = 'UnclaimedDraftCreateResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='multipart/form-data',
            data=request_data,
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')
        obj = deserialize(request_data, f'models.{request_class}')
        obj.file = [open(f'{get_base_path()}/pdf-sample.pdf', 'rb')]

        result = self.api.unclaimed_draft_create_embedded_with_template(obj)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)

    def test_unclaimed_draft_edit_and_resend(self):
        signature_request_id = '2f9781e1a83jdja934d808c153c2e1d3df6f8f2f'

        request_class = 'UnclaimedDraftEditAndResendRequest'
        request_data = get_fixture_data(request_class)['default']

        response_class = 'UnclaimedDraftCreateResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='application/json',
            data=request_data,
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')
        obj = deserialize(request_data, f'models.{request_class}')

        result = self.api.unclaimed_draft_edit_and_resend(signature_request_id, obj)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
