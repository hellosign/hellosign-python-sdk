from hellosign_sdk.tests.functional_tests import BaseTestCase
from hellosign_sdk.resource.unclaimed_draft import UnclaimedDraft
from hellosign_sdk.utils.exception import HSException
import os


class TestUnclaimedDraft(BaseTestCase):

    def test_unclaimed_draft(self):
        ''' Test creating an unclaimed draft '''

        files = [os.path.dirname(os.path.realpath(__file__)) + "/docs/nda.pdf"]
        signers = [{"name": "Signer Name", "email_address": "signer@example.com"}]
        cc_email_addresses = ["receiver@example.com"]
        draft_type = UnclaimedDraft.UNCLAIMED_DRAFT_REQUEST_SIGNATURE_TYPE

        try:
            self.client.create_unclaimed_draft(
                test_mode=True, 
                files=[], 
                file_urls=[], 
                draft_type=draft_type, 
                subject="Test unclaimed draft", 
                message="Please do not reply to the messages", 
                signers=signers, 
                cc_email_addresses=cc_email_addresses)
            self.fail('Validation error expected')
        except HSException:
            pass

        result = self.client.create_unclaimed_draft(
                test_mode=True, 
                files=files, 
                file_urls=[], 
                draft_type=draft_type, 
                subject="Test unclaimed draft", 
                message="Please do not reply to the messages", 
                signers=signers, 
                cc_email_addresses=cc_email_addresses)

        self.assertEquals(isinstance(result, UnclaimedDraft), True)

    def test_embedded_unclaimed_draft(self):
        ''' Test creating an embedded unclaimed draft '''

        files = [os.path.dirname(os.path.realpath(__file__)) + "/docs/nda.pdf"]
        signers = [{"name": "Signer Name", "email_address": "signer@example.com"}]
        cc_email_addresses = ["receiver@example.com"]
        draft_type = UnclaimedDraft.UNCLAIMED_DRAFT_REQUEST_SIGNATURE_TYPE

        try:
            # Missing required parameter
            # test_mode=False, client_id=None, is_for_embedded_signing=False, requester_email_address=None, files=None, file_urls=None, draft_type=None, 
            # subject=None, message=None, signers=None, cc_email_addresses=None, signing_redirect_url=None, requesting_redirect_url=None, form_fields_per_document=None
            self.client.create_embedded_unclaimed_draft(
                test_mode=True, 
                client_id=self.client_id, 
                is_for_embedded_signing=True, 
                requester_email_address="user@example.com", 
                files=[], 
                file_urls=[], 
                draft_type=draft_type, 
                subject="Test unclaimed draft", 
                message="Please do not reply to the messages", 
                signers=signers, 
                cc_email_addresses=cc_email_addresses)
            self.fail('Validation error expected')
        except HSException:
            pass

        result = self.client.create_embedded_unclaimed_draft(
                test_mode=True, 
                client_id=self.client_id, 
                is_for_embedded_signing=True, 
                requester_email_address="user@example.com", 
                files=files, 
                file_urls=[], 
                draft_type=draft_type, 
                subject="Test unclaimed draft", 
                message="Please do not reply to the messages", 
                signers=signers, 
                cc_email_addresses=cc_email_addresses)
        self.assertEquals(isinstance(result, UnclaimedDraft), True)
