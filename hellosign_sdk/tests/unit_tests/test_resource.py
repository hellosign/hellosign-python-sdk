from unittest import TestCase
from hellosign_sdk.tests.test_helper import api_key
from hellosign_sdk.hsclient import HSClient
from hellosign_sdk.utils.exception import *
from hellosign_sdk.resource.resource import Resource
from hellosign_sdk.resource.account import Account
from hellosign_sdk.resource.embedded import Embedded
from hellosign_sdk.resource.reusable_form import ReusableForm
from hellosign_sdk.resource.signature_request import SignatureRequest
from hellosign_sdk.resource.team import Team
from hellosign_sdk.resource.unclaimed_draft import UnclaimedDraft


class TestException(TestCase):

    def setUp(self):
        self.client = HSClient(api_key=api_key)

    def test_account(self):
        account = Account({'account_id': '123456790', 'is_paid_hf': False,
                          'quotas': {'documents_left': 3, 'templates_left': 0,
                          'api_signature_requests_left': 0},
                          'role_code': 'a', 'is_paid_hs': False, 'callback_url':
                          'http://www.example.com/callback',
                          'email_address': 'user@example.com'})
        self.assertEquals(account.account_id, '123456790')
        self.assertEquals(account.is_paid_hf, False)
        self.assertEquals(account.quotas['documents_left'], 3)
        self.assertEquals(account.quotas['templates_left'], 0)
        self.assertEquals(account.quotas['api_signature_requests_left'], 0)
        self.assertEquals(account.role_code, 'a')
        self.assertEquals(account.is_paid_hs, False)
        self.assertEquals(account.callback_url, 'http://www.example.com/callback')
        self.assertEquals(account.email_address, 'user@example.com')

    def test_embedded(self):
        embedded = Embedded({'sign_url': 'https://example.com/test/',
                            'expires_at': 1394859405})
        self.assertEquals(embedded.sign_url, 'https://example.com/test/')
        self.assertEquals(embedded.expires_at, 1394859405)

    def test_resource(self):
        resource = Resource({'custom_attribute_1': 'Value',
                            'custom_attribute_2': False})
        self.assertEquals(resource.custom_attribute_1, 'Value')
        self.assertEquals(resource.custom_attribute_2, False)

        resource = Resource({'custom_key': {'custom_attribute_1': 'Value',
                            'custom_attribute_2': False}}, 'custom_key')
        self.assertEquals(resource.custom_attribute_1, 'Value')
        self.assertEquals(resource.custom_attribute_2, False)

        try:
            resource = Resource({'custom_key': {'custom_attribute_1': 'Value',
                                'custom_attribute_2': False}}, 'no_key')
        except KeyError:
            pass
        try:
            resource.not_existed_key
        except AttributeError:
            pass
        try:
            resource = Resource({'custom_attribute_1': 'Value',
                                'custom_attribute_2': False})
            resource.custom_attribute_1 = 'New Value'
            resource.not_existed_key = 'Value'
        except AttributeError:
            pass
        resource.json_data = {'key': 'value'}
        self.assertEquals(resource.json_data, {'key': 'value'})
        json_data = resource.json_data
        self.assertEquals(json_data, {'key': 'value'})

    # TODO: fulfill all the attributes of Reusable Form
    def test_reusable_form(self):
        reusable_form = ReusableForm(
            {'reusable_form_id': 123456789,
             'title': 'Test', 'message': 'Test Message',
             'signer_roles': [{'name': 'signer_1', 'order': 1},
                              {'name': 'signer_2', 'order': 2}],
             'cc_roles': [{'name': 'role_1'}, {'name': 'role_2'}]})
        self.assertEquals(reusable_form.reusable_form_id, 123456789)
        self.assertEquals(reusable_form.title, 'Test')
        self.assertEquals(reusable_form.message, 'Test Message')
        self.assertEquals(
            reusable_form.signer_roles, [{'name': 'signer_1', 'order': 1},
                                         {'name': 'signer_2', 'order': 2}])
        self.assertEquals(reusable_form.cc_roles,
                          [{'name': 'role_1'}, {'name': 'role_2'}])

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
        self.assertEquals(sn.test_mode, '0')
        self.assertEquals(sn.signature_request_id, 123456789)
        self.assertEquals(sn.requester_email_address, 'user@example.com')
        self.assertEquals(sn.title, 'Test')
        self.assertEquals(sn.subject, 'Test subject')
        self.assertEquals(sn.message, 'Test message')
        self.assertEquals(sn.is_complete, False)
        self.assertEquals(sn.has_error, False)
        self.assertEquals(sn.files_url, 'http://files.example.com/file.pdf')
        self.assertEquals(sn.signing_url, 'http://example.com/sign_url')
        self.assertEquals(sn.details_url, 'http://example.com/details_url')
        self.assertEquals(sn.cc_email_addresses, ['user_1@example.com', 'user_2@example.com'])
        self.assertEquals(sn.signing_redirect_url, 'http://example.com/signing_redirect_url')
        self.assertEquals(sn.custom_fields, [
            {'name': 'custom_attribute_1', 'type': 'text'},
            {'name': 'custom_attribute_2', 'type': 'text'}])
        self.assertEquals(
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
        self.assertEquals(team.name, 'Test team')
        self.assertEquals(len(team.accounts), 2)
        for i in range(len(team.accounts)):
          a = team.accounts[i]
          self.assertTrue(isinstance(a, Account))
          self.assertEquals(a.account_id, data['accounts'][i]['account_id'])
        for i in range(len(team.invited_accounts)):
          a = team.invited_accounts[i]
          self.assertTrue(isinstance(a, Account))
          self.assertEquals(a.account_id, data['invited_accounts'][i]['account_id'])

    def test_unclaimed_draft(self):
        ud = UnclaimedDraft({
             'claim_url': 'http://example.com/claim_url',
             'signing_redirect_url': 'http://example.com/signing_redirect_url',
             'test_mode': '0'
            })
        self.assertEquals(ud.claim_url, 'http://example.com/claim_url')
        self.assertEquals(ud.signing_redirect_url, 'http://example.com/signing_redirect_url')
        self.assertEquals(ud.test_mode, '0')
