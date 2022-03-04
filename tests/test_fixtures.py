import io
import json
import unittest
from metadict import MetaDict

from hellosign_sdk import ApiClient, Configuration, models
from test_utils import get_fixture_data, get_base_path


class TestFixtures(unittest.TestCase):
    def test_is_valid(self):
        configuration = Configuration()
        api_client = ApiClient(configuration)

        fixtures = [
            'AccountCreateRequest',
            'AccountUpdateRequest',
            'AccountVerifyRequest',
            'ApiAppCreateRequest',
            'ApiAppUpdateRequest',
            'EmbeddedEditUrlRequest',
            'OAuthTokenGenerateRequest',
            'OAuthTokenRefreshRequest',
            'ReportCreateRequest',
            'SignatureRequestBulkCreateEmbeddedWithTemplateRequest',
            'SignatureRequestBulkSendWithTemplateRequest',
            'SignatureRequestCreateEmbeddedRequest',
            'SignatureRequestCreateEmbeddedWithTemplateRequest',
            'SignatureRequestRemindRequest',
            'SignatureRequestSendRequest',
            'SignatureRequestSendWithTemplateRequest',
            'SignatureRequestUpdateRequest',
            'TeamAddMemberRequest',
            'TeamCreateRequest',
            'TeamRemoveMemberRequest',
            'TeamUpdateRequest',
            'TemplateAddUserRequest',
            'TemplateCreateEmbeddedDraftRequest',
            'TemplateRemoveUserRequest',
            'TemplateUpdateFilesRequest',
            'UnclaimedDraftCreateEmbeddedRequest',
            'UnclaimedDraftCreateEmbeddedWithTemplateRequest',
            'UnclaimedDraftCreateRequest',
            'UnclaimedDraftEditAndResendRequest',
        ]

        for fixture in fixtures:
            fixture_data = get_fixture_data(fixture)

            for key, fixt_data in fixture_data.items():
                class_type = eval(f'models.{fixture}')
                yanked_files = {}
                data_no_files = {}
                data_with_files = {}

                openapi_types = class_type.openapi_types
                for param, param_value in openapi_types.items():
                    if param not in fixt_data.keys():
                        continue

                    if param_value == (io.IOBase,):
                        loaded = open(f'{get_base_path()}/{fixt_data[param]}', 'rb')
                        yanked_files[param] = loaded
                        loaded.close()
                        data_with_files[param] = f'{get_base_path()}/{fixt_data[param]}'
                    elif param_value == ([io.IOBase],):
                        yanked_files[param] = []
                        data_with_files[param] = []
                        for file_v in fixt_data[param]:
                            loaded = open(f'{get_base_path()}/{file_v}', 'rb')
                            yanked_files[param].append(loaded)
                            loaded.close()
                            data_with_files[param].append(f'{get_base_path()}/{file_v}')
                    else:
                        data_no_files[param] = fixt_data[param]
                        data_with_files[param] = fixt_data[param]

                obj = api_client.deserialize(
                    response=MetaDict({'data': json.dumps(data_no_files)}),
                    response_type=[class_type],
                    _check_type=True,
                )

                for yanked_key, yanked_file in yanked_files.items():
                    obj[yanked_key] = yanked_file

                self.assertEqual(obj.__class__.__name__, class_type.__name__)
                self.assertEqual(obj.to_dict(), data_with_files)


if __name__ == '__main__':
    unittest.main()
