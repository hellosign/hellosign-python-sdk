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

    def _send_test_signature_request(self, embedded=False, text_tags=False):
        ''' Send a test signature request '''

        files = [os.path.dirname(os.path.realpath(__file__)) + "/docs/nda.pdf"]
        signers = [{
            "name": "Signer Name", 
            "email_address": "demo@example.com"
        }]
        cc_email_addresses = ["demo1@example.com", "demo2@example.com"]
        
        title = 'A test signature request'
        subject = 'Test %srequest' % ('embedded ' if embedded else '')
        message = 'This is a test message'

        if not embedded:
            sig_req = self.client.send_signature_request(True, files, [], title, subject, message, "", signers, cc_email_addresses)
        elif text_tags:
            files[0] = os.path.dirname(os.path.realpath(__file__)) + "/docs/nda-text-tags.pdf"
            signers.append({
                'name': 'Other Signer Name',
                'email_address': 'demo+2@example.com'
            })
            sig_req = self.client.send_signature_request_embedded(True, client_id, files, [], title, subject, message, "", signers, cc_email_addresses, use_text_tags=True)
        else:
            sig_req = self.client.send_signature_request_embedded(True, client_id, files, [], title, subject, message, "", signers, cc_email_addresses)

        self.assertEquals(isinstance(sig_req, SignatureRequest), True)
        self.assertEquals(sig_req.title, title)
        self.assertEquals(sig_req.subject, subject)
        self.assertEquals(sig_req.message, message)
        self.assertEquals(len(sig_req.signatures), 1)
        self.assertEquals(len(sig_req.cc_email_addresses), 2)

        return sig_req

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

        # Listing
        sig_req_list = self.client.get_signature_request_list()
        self.assertTrue(isinstance(sig_req_list, list))
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

        # Sent reminder
        try:
            self.client.remind_signature_request(sig_req.signature_request_id, signer)
        except Forbidden, e:
            self.fail(e.message)

    def test_signature_request_file(self):
        ''' Test retrieving signature request files '''
        
        sig_req = self._get_one_signature_request()

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

        # Final copy (DEPRECATED)
        result = self.client.get_signature_request_final_copy(sig_req.signature_request_id, temp_filename)
        self.assertTrue(result)

    def test_signature_request_send(self):
        ''' Test sending signature requests '''

        sig_req = self._send_test_signature_request()

        cc_email_addresses = sig_req.cc_email_addresses
        signers = [{
            'name': sig_req.signatures[0].signer_name,
            'email_address': sig_req.signatures[0].signer_email_address
        }]

        # Invalid - no files
        try:
            self.client.send_signature_request("1", None, [], "Test create signature request", "Ky giay no", "Ky vao giay no di, le di", "", signers, cc_email_addresses) # Error
            self.fail("HSException was excepted")
        except HSException, e:
            self.assertTrue(e.message.find('One of the following fields is required') >= 0)

        # Cancel signature request
        try:
            self.client.cancel_signature_request(sig_req.signature_request_id)
        except HSException, e:
            self.fail(e.message)

        # Try with text tags
        sig_req2 = self._send_test_signature_request(text_tags=True)

        # Cancel signature request
        try:
            self.client.cancel_signature_request(sig_req2.signature_request_id)
        except HSException, e:
            self.fail(e.message)

    def test_embedded_signature_request_send(self):
        ''' Test sending embedded signature requests '''
        sig_req = self._send_test_signature_request(embedded=True)
        try:
            self.client.cancel_signature_request(sig_req.signature_request_id)
        except HSException, e:
            self.fail(e.message)
