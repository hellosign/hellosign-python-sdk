from hellosign_sdk.tests.functional_tests import BaseTestCase
from hellosign_sdk.resource import Embedded, UnclaimedDraft, SignatureRequest
from hellosign_sdk.utils import HSException
import os

class TestEmbedded(BaseTestCase):

    def test_embedded_signing(self):
        ''' Test embedded signing with a file '''

        files = [os.path.dirname(os.path.realpath(__file__)) + "/docs/nda.pdf"]
        signers = [{"name": "Signer Name", "email_address": "signer@example.com"}]
        cc_email_addresses = ["receiver@example.com"]
        subject = "Test embedded signature request"
        message = "This is the message"

        # Create request
        try:
            emb_sig_req = self.client.send_signature_request_embedded(True, self.client_id, files, None, subject, subject, message, None, signers, cc_email_addresses)
            self.assertTrue(isinstance(emb_sig_req, SignatureRequest))
            self.assertEquals(len(emb_sig_req.signatures), 1)
        except HSException, e:
            self.fail(e.message)

        # Get sign url
        emb = self.client.get_embeded_object(emb_sig_req.signatures[0].signature_id)
        self.assertTrue(isinstance(emb, Embedded))
        self.assertTrue(emb.sign_url is not None)

    def test_embedded_signing_with_template(self):
        ''' Test embedded signing with a template '''

        template_list = self.client.get_template_list()
        if not template_list or len(template_list) == 0:
            self.fail('CREATE A TEMPLATE BEFORE RUNNING THIS TEST (one role: Signer)')
        
        template_id = template_list[0].template_id
        signers = [{
            'role_name': 'Signer',
            'name': 'Signer Name', 
            'email_address': 'signer@example.com'
        }]
        subject = "Test embedded signature request from template"
        message = "This is the message"

        # Create request
        try:
            emb_sig_req = self.client.send_signature_request_embedded_with_template(True, self.client_id, template_id, subject, subject, message, None, signers)
            self.assertTrue(isinstance(emb_sig_req, SignatureRequest))
            self.assertEquals(len(emb_sig_req.signatures), 1)
        except HSException, e:
            self.fail(e.message)

        # Get sign url
        emb = self.client.get_embeded_object(emb_sig_req.signatures[0].signature_id)
        self.assertTrue(isinstance(emb, Embedded))
        self.assertTrue(emb.sign_url is not None)

    def test_embedded_requesting_with_signers(self):
        ''' Test embedded requesting with signers '''

        files = [os.path.dirname(os.path.realpath(__file__)) + "/docs/nda.pdf"]
        requester_email_address = "requester@example.com"
        signers = [{
            "name": "Signer Name", 
            "email_address": "signer@example.com"
        }]
        subject = "Test embedded request"
        message = "This is the message"

        try:
            draft = self.client.create_embedded_unclaimed_draft(True, self.client_id, True, requester_email_address, files, None, UnclaimedDraft.UNCLAIMED_DRAFT_REQUEST_SIGNATURE_TYPE, subject, message, signers)
            self.assertTrue(isinstance(draft, UnclaimedDraft))
            self.assertTrue(draft.claim_url is not None)
        except HSException, e:
            self.fail(e.message)

    def test_embedded_requesting_without_signers(self):
        ''' Test embedded requesting without signers '''

        files = [os.path.dirname(os.path.realpath(__file__)) + "/docs/nda.pdf"]
        requester_email_address = "requester@example.com"
        signers = None # No signers, the request will input them manually
        subject = "Test embedded request"
        message = "This is the message"

        try:
            draft = self.client.create_embedded_unclaimed_draft(True, self.client_id, True, requester_email_address, files, None, UnclaimedDraft.UNCLAIMED_DRAFT_REQUEST_SIGNATURE_TYPE, subject, message, signers)
            self.assertTrue(isinstance(draft, UnclaimedDraft))
            self.assertTrue(draft.claim_url is not None)
        except HSException, e:
            self.fail(e.message)
