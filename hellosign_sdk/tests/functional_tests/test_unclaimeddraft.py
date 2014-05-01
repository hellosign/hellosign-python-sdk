from unittest import TestCase
from hellosign_sdk.tests.test_helper import api_key, client_id
from hellosign_sdk.hsclient import HSClient
from hellosign_sdk.resource.unclaimed_draft import UnclaimedDraft
from hellosign_sdk.utils.exception import BadRequest
import os


class TestUnclaimedDraft(TestCase):

    def setUp(self):
        self.client = HSClient(api_key=api_key)

    def test_unclaimed_draft(self):
        ''' Test creating an unclaimed draft '''

        files = [os.path.dirname(os.path.realpath(__file__)) + "/docs/nda.pdf"]
        signers = [{"name": "Signer Name", "email_address": "signer@example.com"}]
        cc_email_addresses = ["receiver@example.com"]

        try:
            self.client.create_unclaimed_draft("1", client_id, "1", "user@example.com", [], [], UnclaimedDraft.UNCLAIMED_DRAFT_REQUEST_SIGNATURE_TYPE, "Test unclaimed draft", "Please do not reply to the messages", signers, cc_email_addresses)
            self.fail('BadRequest was expected')
        except BadRequest:
            pass

        result = self.client.create_unclaimed_draft("1", client_id, "1", "user@example.com", files, [], UnclaimedDraft.UNCLAIMED_DRAFT_REQUEST_SIGNATURE_TYPE, "Test unclaimed draft", "Please do not reply to the messages", signers, cc_email_addresses)
        self.assertEquals(isinstance(result, UnclaimedDraft), True)
