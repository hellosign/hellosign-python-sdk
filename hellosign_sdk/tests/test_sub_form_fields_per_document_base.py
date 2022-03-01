import os
import json
import unittest
from metadict import MetaDict

from hellosign_openapi_python_sdk import ApiClient, Configuration, models
from hellosign_openapi_python_sdk.models import SignatureRequestSendRequest


class TestSubFormFieldsPerDocumentBase(unittest.TestCase):
    def test_is_valid(self):
        configuration = Configuration()
        api_client = ApiClient(configuration)

        file = open(
            os.path.realpath('.') + '/../../oas/test_fixtures/SubFormFieldsPerDocument.json', 'r'
        )
        fixture_data = json.load(file)
        file.close()

        for ftype, data in fixture_data.items():
            payload = {
                'signers': [],
                'form_fields_per_document': [[data]]
            }

            obj = api_client.deserialize(
                response=MetaDict({'data': json.dumps(payload)}),
                response_type=[SignatureRequestSendRequest],
                _check_type=True,
            )

            form_fields_per_document = obj.form_fields_per_document[0][0]
            class_type = eval(f'models.{ftype}')

            self.assertEqual(form_fields_per_document.__class__.__name__, class_type.__name__)
            self.assertEqual(form_fields_per_document.to_dict(), data)


if __name__ == '__main__':
    unittest.main()
