from hellosign_sdk.tests.functional_tests import BaseTestCase
from hellosign_sdk.resource import ResourceList, SignatureRequest, Signature
from hellosign_sdk.utils import Forbidden, HSException
from time import sleep
import tempfile
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


class TestSignatureRequest(BaseTestCase):

    def _send_test_signature_request(self, embedded=False, use_text_tags=False, use_template=False, use_multi_templates=False):
        ''' Send a test signature request '''

        files = None
        template_id = None
        template_ids = None

        if use_template:
            template = self._get_one_template()
            template_id = template.template_id
            signers = [{
                "role_name": "Signer",
                "name": "Signer Name", 
                "email_address": "demo@example.com"
            }]
            cc_email_addresses = None
        elif use_multi_templates:
            t1 = self._get_one_template()
            t2 = self._get_one_template(exclude=t1)
            template_ids = [t1.template_id, t2.template_id]
            signers = [{
                "role_name": "Signer",
                "name": "Signer Name", 
                "email_address": "demo@example.com"
            }]
            cc_email_addresses = None
        else:
            files = [os.path.dirname(os.path.realpath(__file__)) + "/docs/nda.pdf"]
            signers = [{
                "name": "Signer Name", 
                "email_address": "demo@example.com"
            }]
            cc_email_addresses = ["demo1@example.com", "demo2@example.com"]
        
        title = 'A test signature request'
        subject = 'Test %srequest%s' % ('embedded ' if embedded else '', ' with template' if use_template else '')
        message = 'This is a test message'
        metadata = {
            'account_id': '123',
            'company_name': 'Acme Co.'
        }

        if not embedded:
            if use_template or use_multi_templates:
                sig_req = self.client.send_signature_request_with_template(test_mode=True, 
                                                                            template_id=template_id, 
                                                                            template_ids=template_ids,
                                                                            title=title, 
                                                                            subject=subject, 
                                                                            message=message, 
                                                                            signers=signers, 
                                                                            ccs=cc_email_addresses,
                                                                            metadata=metadata)
            else:
                sig_req = self.client.send_signature_request(test_mode=True, 
                                                                files=files, 
                                                                title=title, 
                                                                subject=subject, 
                                                                message=message, 
                                                                signers=signers, 
                                                                cc_email_addresses=cc_email_addresses,
                                                                metadata=metadata)
        elif use_text_tags:
            files[0] = os.path.dirname(os.path.realpath(__file__)) + "/docs/nda-text-tags.pdf"
            signers.append({
                'name': 'Other Signer Name',
                'email_address': 'demo+2@example.com'
            })
            sig_req = self.client.send_signature_request_embedded(test_mode=True, 
                                                                    client_id=self.client_id, 
                                                                    files=files, 
                                                                    title=title, 
                                                                    subject=subject, 
                                                                    message=message, 
                                                                    signers=signers, 
                                                                    cc_email_addresses=cc_email_addresses, 
                                                                    use_text_tags=True,
                                                                    metadata=metadata)
        else:
            sig_req = self.client.send_signature_request_embedded(test_mode=True, 
                                                                    client_id=self.client_id, 
                                                                    files=files, 
                                                                    title=title, 
                                                                    subject=subject, 
                                                                    message=message, 
                                                                    signers=signers, 
                                                                    cc_email_addresses=cc_email_addresses,
                                                                    metadata=metadata)

        self.assertEquals(isinstance(sig_req, SignatureRequest), True)
        self.assertEquals(sig_req.title, title)
        self.assertEquals(sig_req.subject, subject)
        self.assertEquals(sig_req.message, message)
        self.assertEquals(len(sig_req.signatures), 1)
        self.assertEquals(len(sig_req.cc_email_addresses), 0 if use_template or use_multi_templates else 2)
        self.assertEquals(sig_req.metadata is not None, True)
        self.assertEquals(len(sig_req.metadata), len(metadata))
        for (k, v) in metadata.items():
            self.assertEquals(sig_req.metadata[k], v)

        return sig_req

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

    def _get_one_signature_request(self):
        ''' Retrieve one signature request from the current account '''
        sig_req_list = self.client.get_signature_request_list()
        if len(sig_req_list) == 0:
            sig_req = self._send_test_signature_request()
        else:
            sig_req = sig_req_list[0]
        return sig_req

    def test_signature_request_get_and_list(self):
        ''' Test get signature requests '''

        self._send_test_signature_request()

        # Wait a little bit for the file to be ready
        sleep(5) 

        # Listing
        sig_req_list = self.client.get_signature_request_list()
        self.assertTrue(isinstance(sig_req_list, ResourceList))
        self.assertTrue(len(sig_req_list) > 0)
        for sig_req in sig_req_list:
            self.assertTrue(isinstance(sig_req, SignatureRequest))    
        
        # Get a signature request
        sig_req = self.client.get_signature_request(sig_req_list[0].signature_request_id)
        self.assertTrue(isinstance(sig_req, SignatureRequest))

    def test_signature_request_reminder(self):
        ''' Test sending a reminder for a signature request '''

        sig_req = self._get_one_signature_request()
        signer = sig_req.signatures[0].signer_email_address

        # Wait a little bit for the file to be ready
        sleep(5)

        # Sent reminder
        try:
            self.client.remind_signature_request(sig_req.signature_request_id, signer)
        except Forbidden as e:
            self.fail(e.message)

    def test_signature_request_file(self):
        ''' Test retrieving signature request files '''
        
        sig_req = self._get_one_signature_request()

        # Wait a little bit for the file to be ready
        sleep(10) 

        # Download PDF file
        f = tempfile.NamedTemporaryFile(delete=True)
        temp_filename = f.name
        f.close()
        self.assertTrue(self.client.get_signature_request_file(sig_req.signature_request_id, temp_filename))

        # Download ZIP file
        f = tempfile.NamedTemporaryFile(delete=True)
        temp_filename = f.name
        f.close()
        self.assertTrue(self.client.get_signature_request_file(sig_req.signature_request_id, temp_filename, file_type='zip'))

    def test_signature_request_send(self):
        ''' Test sending signature requests '''

        # Send signature request
        sig_req = self._send_test_signature_request()

        cc_email_addresses = sig_req.cc_email_addresses
        signers = [{
            'name': sig_req.signatures[0].signer_name,
            'email_address': sig_req.signatures[0].signer_email_address
        }]

        # Invalid - no files
        try:
            self.client.send_signature_request(test_mode=True, 
                                                files=[], 
                                                title="Test create signature request", 
                                                subject="Ky giay no", 
                                                message="Ky vao giay no di, le di", 
                                                signers=signers, 
                                                cc_email_addresses=cc_email_addresses)
            self.fail("HSException was excepted")
        except HSException as e:
            self.assertTrue(e.message.find('One of the following fields is required') >= 0)

        # Cancel signature request
        try:
            self.client.cancel_signature_request(sig_req.signature_request_id)
        except HSException as e:
            self.fail(e.message)

        # Try with text tags
        sig_req2 = self._send_test_signature_request(use_text_tags=True)

        # Cancel signature request
        try:
            self.client.cancel_signature_request(sig_req2.signature_request_id)
        except HSException as e:
            self.fail(e.message)

    def test_signature_request_send_with_template(self):
        ''' Test sending signature requests from templates '''

        # Send signature request with one template
        sig_req1 = self._send_test_signature_request(use_template=True)

        # Send signature request with two templates
        sig_req2 = self._send_test_signature_request(use_multi_templates=True)

        # Cancel signature requests
        try:
            self.client.cancel_signature_request(sig_req1.signature_request_id)
            sleep(2)
            self.client.cancel_signature_request(sig_req2.signature_request_id)
        except HSException as e:
            self.fail(e.message)

    def test_embedded_signature_request_send(self):
        ''' Test sending embedded signature requests '''
        sig_req = self._send_test_signature_request(embedded=True)
        try:
            self.client.cancel_signature_request(sig_req.signature_request_id)
        except HSException as e:
            self.fail(e.message)

    def test_signature_request_helpers(self):
        ''' Test signature request helpers '''

        comp1 = {
            "signature_id": "78caf2a1d01cd39cea2bc1cbb340dac3",
            "api_id": "80c678_1",
            "name": "Needs Express Shipping",
            "value": True,
            "type": "checkbox"
        }
        comp2 = {
            "signature_id": "78caf2a1d01cd39cea2bc1cbb340dac3",
            "api_id": "80c678_2",
            "name": "Shipping Address",
            "value": "1212 Park Avenuee",
            "type": "text"
        }
        comp3 = {
            "signature_id": "78caf2a1d01cd39cea2bc1cbb340dac3",
            "api_id": "80c678_3",
            "name": "DateSigned",
            "value": "09\/01\/2012",
            "type": "text"
        }

        sig_data = {
            "signature_id": "78caf2a1d01cd39cea2bc1cbb340dac3",
            "signer_email_address": "john@example.com",
            "signer_name": "John Doe",
            "order": None,
            "status_code": "signed",
            "signed_at": 1346521550,
            "last_viewed_at": 1346521483,
            "last_reminded_at": None,
            "has_pin" : False
        }

        sig_req_data = {
            "signature_request_id": "fa5c8a0b0f492d768749333ad6fcc214c111e967",
            "title": "Purchase Agreement",
            "subject": "Purchase Agreement",
            "message": "Please sign and return.",
            "is_complete": True,
            "has_error": False,
            "custom_fields": [],
            "response_data": [comp1, comp2, comp3],
            "signing_url": None,
            "signing_redirect_url": None,
            "details_url": "https:\/\/staging.hellosign.com\/home\/manage?locate=fa5c8a0b0f492d768749333ad6fcc214c111e967",
            "requester_email_address": "me@hellosign.com",
            "signatures": [sig_data],
            "cc_email_addresses": []
        }
        sig_req = SignatureRequest(sig_req_data)

        comps = sig_req.find_response_component(api_id=comp1['api_id'])
        self.assertEquals(len(comps), 1)
        self.assertEquals(comps[0], comp1)

        comps = sig_req.find_response_component(signature_id=comp1['signature_id'])
        self.assertEquals(len(comps), 3)
        self.assertEquals(comps[0], comp1)
        self.assertEquals(comps[1], comp2)
        self.assertEquals(comps[2], comp3)

        comps = sig_req.find_response_component(api_id='3j2k3j21k32')
        self.assertEquals(len(comps), 0)

        s = sig_req.find_signature(signature_id=sig_data['signature_id'])
        self.assertTrue(s is not None)
        self.assertTrue(isinstance(s, Signature), "Expected Signature but got %s" % s.__class__.__name__)
        self.assertEquals(s.json_data, sig_data)

        s = sig_req.find_signature(signer_email_address=sig_data['signer_email_address'])
        self.assertTrue(s is not None)
        self.assertTrue(isinstance(s, Signature), "Expected Signature but got %s" % s.__class__.__name__)
        self.assertEquals(s.json_data, sig_data)

        s = sig_req.find_signature(signature_id='j32kj32k13j')
        self.assertEquals(s, None)
