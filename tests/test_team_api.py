import unittest

from hellosign_sdk import ApiClient, Configuration, apis
from test_utils import get_fixture_data, MockPoolManager, deserialize


class TestTeamApi(unittest.TestCase):
    def setUp(self):
        self.configuration = Configuration()
        self.api_client = ApiClient(self.configuration)
        self.mock_pool = MockPoolManager(self)
        self.api_client.rest_client.pool_manager = self.mock_pool

        self.api = apis.TeamApi(self.api_client)

    def test_team_add_member(self):
        request_class = 'TeamAddMemberRequest'
        request_data = get_fixture_data(request_class)['default']

        response_class = 'TeamGetResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='application/json',
            data=request_data,
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')
        obj = deserialize(request_data, f'models.{request_class}')

        result = self.api.team_add_member(obj)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)

    def test_team_create(self):
        request_class = 'TeamCreateRequest'
        request_data = get_fixture_data(request_class)['default']

        response_class = 'TeamGetResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='application/json',
            data=request_data,
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')
        obj = deserialize(request_data, f'models.{request_class}')

        result = self.api.team_create(obj)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)

    def test_team_delete(self):
        self.skipTest('skipping test_team_create')

    def test_team_get(self):
        response_class = 'TeamGetResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='application/json',
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')

        result = self.api.team_get()

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)

    def test_team_update(self):
        request_class = 'TeamUpdateRequest'
        request_data = get_fixture_data(request_class)['default']

        response_class = 'TeamGetResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='application/json',
            data=request_data,
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')
        obj = deserialize(request_data, f'models.{request_class}')

        result = self.api.team_update(obj)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)

    def test_team_remove_member(self):
        request_class = 'TeamRemoveMemberRequest'
        request_data = get_fixture_data(request_class)['default']

        response_class = 'TeamGetResponse'
        response_data = get_fixture_data(response_class)['default']

        self.mock_pool.expect_request(
            content_type='application/json',
            data=request_data,
            response=response_data
        )
        expected = deserialize(response_data, f'models.{response_class}')
        obj = deserialize(request_data, f'models.{request_class}')

        result = self.api.team_remove_member(obj)

        self.assertEqual(result.__class__.__name__, response_class)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
