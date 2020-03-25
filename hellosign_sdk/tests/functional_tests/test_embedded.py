from hellosign_sdk.tests.functional_tests import BaseTestCase
from hellosign_sdk.resource import Embedded, UnclaimedDraft, SignatureRequest
from hellosign_sdk.utils import HSException, NotFound
import os

#
# The MIT License (MIT)
# 
# Copyright (C) 2014 hellosign.com
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#


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
            emb_sig_req = self.client.send_signature_request_embedded(test_mode=True,  
                                                                        client_id=self.client_id, 
                                                                        files=files, 
                                                                        subject=subject, 
                                                                        title=subject, 
                                                                        message=message, 
                                                                        signers=signers, 
                                                                        cc_email_addresses=cc_email_addresses)
            self.assertTrue(isinstance(emb_sig_req, SignatureRequest))
            self.assertEqual(len(emb_sig_req.signatures), 1)
        except HSException as e:
            self.fail(e.message)

        # Get sign url
        emb = self.client.get_embedded_object(emb_sig_req.signatures[0].signature_id)
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
            emb_sig_req = self.client.send_signature_request_embedded_with_template(test_mode=True,
                                                                                    client_id=self.client_id, 
                                                                                    template_id=template_id, 
                                                                                    subject=subject, 
                                                                                    title=subject, 
                                                                                    message=message, 
                                                                                    signers=signers,
                                                                                    allow_decline=True)

            self.assertTrue(isinstance(emb_sig_req, SignatureRequest))
            self.assertEqual(len(emb_sig_req.signatures), 1)
        except HSException as e:
            self.fail(e.message)

        # Get sign url
        emb = self.client.get_embedded_object(emb_sig_req.signatures[0].signature_id)
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
            draft = self.client.create_embedded_unclaimed_draft(test_mode=True, 
                                                                client_id=self.client_id, 
                                                                is_for_embedded_signing=True, 
                                                                requester_email_address=requester_email_address, 
                                                                files=files, 
                                                                draft_type=UnclaimedDraft.UNCLAIMED_DRAFT_REQUEST_SIGNATURE_TYPE, 
                                                                subject=subject, 
                                                                message=message, 
                                                                signers=signers)
            self.assertTrue(isinstance(draft, UnclaimedDraft))
            self.assertTrue(draft.claim_url is not None)
        except HSException as e:
            self.fail(e.message)

    def test_embedded_requesting_without_signers(self):
        ''' Test embedded requesting without signers '''

        files = [os.path.dirname(os.path.realpath(__file__)) + "/docs/nda.pdf"]
        requester_email_address = "requester@example.com"
        signers = None # No signers, the request will input them manually
        subject = "Test embedded request"
        message = "This is the message"

        try:
            draft = self.client.create_embedded_unclaimed_draft(test_mode=True, 
                                                                client_id=self.client_id, 
                                                                is_for_embedded_signing=True, 
                                                                requester_email_address=requester_email_address, 
                                                                files=files, 
                                                                draft_type=UnclaimedDraft.UNCLAIMED_DRAFT_REQUEST_SIGNATURE_TYPE, 
                                                                subject=subject, 
                                                                message=message, 
                                                                signers=signers)
            self.assertTrue(isinstance(draft, UnclaimedDraft))
            self.assertTrue(draft.claim_url is not None)
        except HSException as e:
            self.fail(e.message)

    def test_embedded_template_edit_url(self):
        ''' Tests the embedded template edit url endpoint '''

        # Similar to the delete_template function, we can't actually test this for success without human interaction. Instead, we'll be checking for a 404 - Template not found status code, which means our parameters are correct

        template_id = 'ax5d921d0d3ccfcd594d2b8c897ba774d89c9234' #random

        try:
            self.client.get_template_edit_url(template_id)
            self.fail('Expected error, got success')
        except NotFound:
            pass
        except BaseException as e:
            self.fail('Expected Not Found, but got %s' % e)
