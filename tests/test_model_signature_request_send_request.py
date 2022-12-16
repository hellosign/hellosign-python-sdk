import unittest

from hellosign_sdk import models


class TestModelSignatureRequestSendRequest(unittest.TestCase):
    def test_is_valid(self):
        signer_1 = models.SubSignatureRequestSigner(
            email_address="s1@example.com",
            name="Jack",
            order=0,
        )

        signer_2 = models.SubSignatureRequestSigner(
            email_address="s2@example.com",
            name="Jill",
            order=1,
        )

        attachments_1 = models.SubAttachment(
            name="Example Attachment",
            signer_index=0,
        )

        custom_field_1 = models.SubCustomField(
            name="custom_field_1",
            value="Custom Field 1",
            required=True,
            editor="1",
        )

        custom_field_2 = models.SubCustomField(
            name="custom_field_2",
            value="Custom Field 2",
            required=False,
            editor="2",
        )

        signing_options = models.SubSigningOptions(
            draw=True,
            type=True,
            upload=True,
            phone=True,
            default_type="draw",
        )

        field_options = models.SubFieldOptions(
            date_format="DD - MM - YYYY",
        )

        data_text = models.SubFormFieldsPerDocumentTextMerge(
            document_index=0,
            api_id="field1",
            auto_fill_type="name",
            name="full_name",
            type="text-merge",
            signer="1",
            width=100,
            height=16,
            x=112,
            y=328,
        )

        data = models.SignatureRequestSendRequest(
            title="NDA with Acme Co.",
            subject="The NDA we talked about",
            message="Please sign this NDA and then we can discuss more. Let me know if you have any questions.",
            signers=[signer_1, signer_2],
            cc_email_addresses=[
                "cc1@example.com",
                "cc2@example.com",
            ],
            file_url=["https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"],
            metadata={
                "custom_id": 1234,
                "custom_text": "NDA #9",
            },
            attachments=[attachments_1],
            signing_options=signing_options,
            field_options=field_options,
            test_mode=True,
            custom_fields=[custom_field_1, custom_field_2],
            form_fields_per_document=[data_text],
        )

        self.assertEqual(
            data.form_fields_per_document[0].__class__.__name__,
            models.SubFormFieldsPerDocumentTextMerge.__name__
        )


if __name__ == '__main__':
    unittest.main()
