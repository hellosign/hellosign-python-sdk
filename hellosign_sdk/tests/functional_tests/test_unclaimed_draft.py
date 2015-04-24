from hellosign_sdk.tests.functional_tests import BaseTestCase
from hellosign_sdk.resource import UnclaimedDraft
from hellosign_sdk.utils import HSException
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


class TestUnclaimedDraft(BaseTestCase):

    def test_unclaimed_draft(self):
        ''' Test creating an unclaimed draft '''

        files = [os.path.dirname(os.path.realpath(__file__)) + "/docs/nda.pdf"]
        signers = [{"name": "Signer Name", "email_address": "signer@example.com"}]
        cc_email_addresses = ["receiver@example.com"]
        draft_type = UnclaimedDraft.UNCLAIMED_DRAFT_REQUEST_SIGNATURE_TYPE
        metadata = {
            'account_id': '123',
            'company_name': 'Acme Co.'
        }

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
                cc_email_addresses=cc_email_addresses,
                metadata=metadata)

        self.assertEquals(isinstance(result, UnclaimedDraft), True)

    def test_embedded_unclaimed_draft(self):
        ''' Test creating an embedded unclaimed draft '''

        files = [os.path.dirname(os.path.realpath(__file__)) + "/docs/nda.pdf"]
        signers = [{"name": "Signer Name", "email_address": "signer@example.com"}]
        cc_email_addresses = ["receiver@example.com"]
        draft_type = UnclaimedDraft.UNCLAIMED_DRAFT_REQUEST_SIGNATURE_TYPE
        metadata = {
            'account_id': '123',
            'company_name': 'Acme Co.'
        }

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
                cc_email_addresses=cc_email_addresses,
                metadata=metadata)
        self.assertEquals(isinstance(result, UnclaimedDraft), True)

    def test_create_embedded_unclaimed_draft_with_template(self):
        ''' Test creating an embedded unclaimed draft from a template '''

        signers = [{
                    "name": "Signer Name", 
                    "email_address": "signer@example.com",
                    "role_name": "Signer"
                  }]
        metadata = {
            'account_id': '123',
            'company_name': 'Acme Co.'
        }

        template = self._get_one_template()
        template_id = template.template_id

        try:
            # Missing required parameter
            self.client.create_embedded_unclaimed_draft_with_template(
                test_mode=True, 
                client_id=self.client_id, 
                is_for_embedded_signing=True, 
                #missing - template_id
                requester_email_address='user@example.com', 
                title='MyDraft', 
                subject='Unclaimed Draft Email Subject', 
                message='Email Message', 
                signers=signers, 
                signing_redirect_url='http://url.com', 
                requesting_redirect_url='http://url.com', 
                metadata=metadata)
            self.fail('Validation error expected')
        except HSException:
            pass

        returned = self.client.create_embedded_unclaimed_draft_with_template(
            test_mode=True, 
            client_id=self.client_id, 
            is_for_embedded_signing=True, 
            template_id=template_id, 
            requester_email_address='user@example.com', 
            title='MyDraft', 
            subject='Unclaimed Draft Email Subject', 
            message='Email Message', 
            signers=signers, 
            signing_redirect_url='http://url.com', 
            requesting_redirect_url='http://url.com', 
            metadata=metadata)

        self.assertEquals(isinstance(returned, UnclaimedDraft), True)

    def _get_one_template(self, exclude=None):
        ''' Get one template from the current account '''
        template_list = self.client.get_template_list()
        if not template_list or len(template_list) == 0:
            self.fail('CREATE A TEMPLATE BEFORE RUNNING THIS TEST')
        if exclude is None:
            return template_list[0]
        else:
            for t in template_list:
                if t.template_id != exclude.template_id:
                    return t
            self.fail('CREATE A SECOND TEMPLATE BEFORE RUNNING THIS TEST')
