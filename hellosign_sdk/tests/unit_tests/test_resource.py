from unittest import TestCase
from hellosign_sdk.tests.test_helper import api_key
from hellosign_sdk import HSClient
from hellosign_sdk.resource import Resource, Account, Embedded, Template, SignatureRequest, Team, UnclaimedDraft
from hellosign_sdk.utils.exception import *

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


class TestException(TestCase):

    def setUp(self):
        self.client = HSClient(api_key=api_key)

    def test_account(self):
        account = Account({
          'account_id': '123456790', 
          'quotas': {
            'documents_left': 3, 
            'templates_left': 0,
            'api_signature_requests_left': 0
          },
          'role_code': 'a', 
          'is_paid_hf': False,
          'is_paid_hs': False, 
          'callback_url': 'http://www.example.com/callback',
          'email_address': 'user@example.com'
        })
        self.assertEqual(account.account_id, '123456790')
        self.assertEqual(account.is_paid_hf, False)
        self.assertEqual(account.quotas['documents_left'], 3)
        self.assertEqual(account.quotas['templates_left'], 0)
        self.assertEqual(account.quotas['api_signature_requests_left'], 0)
        self.assertEqual(account.role_code, 'a')
        self.assertEqual(account.is_paid_hs, False)
        self.assertEqual(account.callback_url, 'http://www.example.com/callback')
        self.assertEqual(account.email_address, 'user@example.com')

    def test_embedded(self):
        embedded = Embedded({'sign_url': 'https://example.com/test/', 'expires_at': 1394859405})
        self.assertEqual(embedded.sign_url, 'https://example.com/test/')
        self.assertEqual(embedded.expires_at, 1394859405)

    def test_resource(self):
        resource = Resource({'custom_attribute_1': 'Value', 'custom_attribute_2': False})
        self.assertEqual(resource.custom_attribute_1, 'Value')
        self.assertEqual(resource.custom_attribute_2, False)

        resource = Resource({'custom_key': {'custom_attribute_1': 'Value', 'custom_attribute_2': False}}, 'custom_key')
        self.assertEqual(resource.custom_attribute_1, 'Value')
        self.assertEqual(resource.custom_attribute_2, False)

        try:
            resource = Resource({'custom_key': {'custom_attribute_1': 'Value', 'custom_attribute_2': False}}, 'no_key')
        except KeyError:
            pass
        try:
            resource.not_existed_key
        except AttributeError:
            pass
        try:
            resource = Resource({'custom_attribute_1': 'Value', 'custom_attribute_2': False})
            resource.custom_attribute_1 = 'New Value'
            resource.not_existed_key = 'Value'
        except AttributeError:
            pass
        resource.json_data = {'key': 'value'}
        self.assertEqual(resource.json_data, {'key': 'value'})
        json_data = resource.json_data
        self.assertEqual(json_data, {'key': 'value'})

    # TODO: fulfill all the attributes of Template
    def test_template(self):
        template = Template({
          'template_id': 123456789,
          'title': 'Test', 'message': 'Test Message',
          'signer_roles': [
            {'name': 'signer_1', 'order': 1},
            {'name': 'signer_2', 'order': 2}
          ],
          'cc_roles': [
            {'name': 'role_1'}, 
            {'name': 'role_2'}
          ]})
        self.assertEqual(template.template_id, 123456789)
        self.assertEqual(template.title, 'Test')
        self.assertEqual(template.message, 'Test Message')
        self.assertEqual(template.signer_roles, [
          {'name': 'signer_1', 'order': 1},
          {'name': 'signer_2', 'order': 2}
        ])
        self.assertEqual(template.cc_roles, [{'name': 'role_1'}, {'name': 'role_2'}])

    # TODO: fulfill attributes
    def test_signature_request(self):
        sn = SignatureRequest(
            {
            'test_mode': '0', 'signature_request_id': 123456789,
             'requester_email_address': 'user@example.com', 'title': 'Test',
             'subject': 'Test subject', 'message': 'Test message',
             'is_complete': False, 'has_error': False,
             'files_url': 'http://files.example.com/file.pdf',
             'signing_url': 'http://example.com/sign_url',
             'details_url': 'http://example.com/details_url',
             'cc_email_addresses': ['user_1@example.com', 'user_2@example.com'],
             'signing_redirect_url': 'http://example.com/signing_redirect_url',
             'custom_fields': [{'name': 'custom_attribute_1', 'type': 'text'},
                               {'name': 'custom_attribute_2', 'type': 'text'}],
                'response_data': [
                    {'api_id': 99999999, 'signature_id': 88888888,
                     'name': 'Field name 1', 'value': 'Field value 1',
                     'type': 'text'},
                    {'api_id': 99999998, 'signature_id': 88888887,
                     'name': 'Field name 2', 'value': 'Field value 2',
                     'type': 'text'}]
            })
        self.assertEqual(sn.test_mode, '0')
        self.assertEqual(sn.signature_request_id, 123456789)
        self.assertEqual(sn.requester_email_address, 'user@example.com')
        self.assertEqual(sn.title, 'Test')
        self.assertEqual(sn.subject, 'Test subject')
        self.assertEqual(sn.message, 'Test message')
        self.assertEqual(sn.is_complete, False)
        self.assertEqual(sn.has_error, False)
        self.assertEqual(sn.files_url, 'http://files.example.com/file.pdf')
        self.assertEqual(sn.signing_url, 'http://example.com/sign_url')
        self.assertEqual(sn.details_url, 'http://example.com/details_url')
        self.assertEqual(sn.cc_email_addresses, ['user_1@example.com', 'user_2@example.com'])
        self.assertEqual(sn.signing_redirect_url, 'http://example.com/signing_redirect_url')
        self.assertEqual(sn.custom_fields, [
            {'name': 'custom_attribute_1', 'type': 'text'},
            {'name': 'custom_attribute_2', 'type': 'text'}])
        self.assertEqual(
            sn.response_data,
            [
                {'api_id': 99999999, 'signature_id': 88888888,
                 'name': 'Field name 1', 'value': 'Field value 1',
                 'type': 'text'},
                {'api_id': 99999998, 'signature_id': 88888887,
                 'name': 'Field name 2', 'value': 'Field value 2',
                 'type': 'text'}
            ])

    def test_team(self):
        data = {
            'name': 'Test team',
            'accounts': [
                {'account_id': 123456789, 'email_address': 'user_1@example.com', 'role_code': 'O'},
                {'account_id': 123456799, 'email_address': 'user_2@example.com', 'role_code': 'M'}],
            'invited_accounts': [
                {'account_id': 1234570, 'email_address': 'user_3@example.com'},
                {'account_id': 1234571, 'email_address': 'user_4@example.com'}
            ]}
        team = Team(data)
        self.assertEqual(team.name, 'Test team')
        self.assertEqual(len(team.accounts), 2)
        for i in range(len(team.accounts)):
          a = team.accounts[i]
          self.assertTrue(isinstance(a, Account))
          self.assertEqual(a.account_id, data['accounts'][i]['account_id'])
        for i in range(len(team.invited_accounts)):
          a = team.invited_accounts[i]
          self.assertTrue(isinstance(a, Account))
          self.assertEqual(a.account_id, data['invited_accounts'][i]['account_id'])

    def test_unclaimed_draft(self):
        ud = UnclaimedDraft({
             'claim_url': 'http://example.com/claim_url',
             'signing_redirect_url': 'http://example.com/signing_redirect_url',
             'test_mode': '0'
            })
        self.assertEqual(ud.claim_url, 'http://example.com/claim_url')
        self.assertEqual(ud.signing_redirect_url, 'http://example.com/signing_redirect_url')
        self.assertEqual(ud.test_mode, '0')
