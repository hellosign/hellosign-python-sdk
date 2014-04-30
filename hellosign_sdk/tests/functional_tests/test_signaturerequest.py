from unittest import TestCase
from hellosign_sdk.tests.test_helper import api_key, client_id
from hellosign_sdk.hsclient import HSClient
from hellosign_sdk.resource.signature_request import SignatureRequest
from hellosign_sdk.utils.exception import Forbidden, HSException
import tempfile
import os


class TestSignatureRequest(TestCase):

    def setUp(self):
        self.client = HSClient(api_key=api_key)

    def test_signature_request_get_and_list(self):
        srl = self.client.get_signature_request_list()
        self.assertTrue(isinstance(srl, list))
        if len(srl) > 0:
            self.assertTrue(isinstance(srl[0], SignatureRequest))
            sr = self.client.get_signature_request(srl[0].signature_request_id)
            self.assertTrue(isinstance(sr, SignatureRequest))
            # Remind
            signer = srl[0].signatures[0].signer_email_address
            try:
                new_sr = self.client.remind_signature_request(srl[0].signature_request_id, signer)
                self.assertEquals(isinstance(new_sr, SignatureRequest), True)
            except Forbidden:
                pass
            # Download
            f = tempfile.NamedTemporaryFile(delete=True)
            temp_filename = f.name
            f.close()
            result = self.client.get_signature_request_file(srl[0].signature_request_id, temp_filename)
            self.assertTrue(result)

            result = self.client.get_signature_request_final_copy(srl[0].signature_request_id, temp_filename)
            self.assertTrue(result)

    def test_signature_request_send(self):
        files = [os.path.dirname(os.path.realpath(__file__)) + "/docs/nda.pdf"]
        signers = [{"name": "Signer Name", "email_address": "demo@example.com"}]
        cc_email_addresses = ["demo1@example.com", "demo2@example.com"]

        sr = self.client.send_signature_request("1", files, [], "A test signature request", "Test request", "This is a demo message", "", signers, cc_email_addresses)
        self.assertEquals(isinstance(sr, SignatureRequest), True)
        self.assertEquals(sr.title, "A test signature request")
        self.assertEquals(sr.subject, "Test request")
        self.assertEquals(sr.message, "This is a demo message")

        try:
            self.client.send_signature_request("1", None, [], "Test create signature request", "Ky giay no", "Ky vao giay no di, le di", "", signers, cc_email_addresses) # Error
        except HSException:
            pass
        result = self.client.cancel_signature_request(sr.signature_request_id)
        self.assertTrue(result)

        # create embedded
        sr = self.client.send_signature_request_embedded("1", client_id, files, [], "A test signature request", "Test request", "This is a demo message", "", signers, cc_email_addresses)

        self.assertEquals(isinstance(sr, SignatureRequest), True)
        self.assertEquals(sr.title, "A test signature request")
        self.assertEquals(sr.subject, "Test request")
        self.assertEquals(sr.message, "This is a demo message")

        result = self.client.cancel_signature_request(sr.signature_request_id)
        self.assertTrue(result)
