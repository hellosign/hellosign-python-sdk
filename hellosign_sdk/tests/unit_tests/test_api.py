from unittest import TestCase
from hellosign_sdk.tests.test_helper import api_key
from hellosign_sdk.hsclient import HSClient
from hellosign_sdk.utils.request import HSRequest
from hellosign_sdk.utils.exception import BadRequest, NotFound, Unauthorized
from requests.auth import HTTPBasicAuth


class Api(TestCase):

    def setUp(self):
        self.client = HSClient(api_key=api_key)

    def test_endpoint(self):
        self.assertEqual(self.client.API_URL, "https://api.hellosign.com/v3")
        self.assertEqual(self.client.ACCOUNT_CREATE_URL, "https://api.hellosign.com/v3/account/create")
        self.assertEqual(self.client.ACCOUNT_INFO_URL, "https://api.hellosign.com/v3/account")
        self.assertEqual(self.client.ACCOUNT_UPDATE_URL, "https://api.hellosign.com/v3/account")

        self.assertEqual(self.client.SIGNATURE_REQUEST_INFO_URL, "https://api.hellosign.com/v3/signature_request/")
        self.assertEqual(self.client.SIGNATURE_REQUEST_LIST_URL, "https://api.hellosign.com/v3/signature_request/list")
        self.assertEqual(self.client.SIGNATURE_REQUEST_DOWNLOAD_PDF_URL, "https://api.hellosign.com/v3/signature_request/files/")
        self.assertEqual(self.client.SIGNATURE_REQUEST_CREATE_URL, "https://api.hellosign.com/v3/signature_request/send")
        self.assertEqual(self.client.SIGNATURE_REQUEST_CREATE_WITH_TEMPLATE_URL, "https://api.hellosign.com/v3/signature_request/send_with_reusable_form")
        self.assertEqual(self.client.SIGNATURE_REQUEST_REMIND_URL, "https://api.hellosign.com/v3/signature_request/remind/")
        self.assertEqual(self.client.SIGNATURE_REQUEST_CANCEL_URL, "https://api.hellosign.com/v3/signature_request/cancel/")
        self.assertEqual(self.client.SIGNATURE_REQUEST_CREATE_EMBEDDED_URL, "https://api.hellosign.com/v3/signature_request/create_embedded")
        self.assertEqual(self.client.SIGNATURE_REQUEST_CREATE_EMBEDDED_WITH_TEMPLATE_URL, "https://api.hellosign.com/v3/signature_request/create_embedded_with_reusable_form")

        self.assertEqual(self.client.EMBEDDED_OBJECT_GET_URL, "https://api.hellosign.com/v3/embedded/sign_url/")

        self.assertEqual(self.client.UNCLAIMED_DRAFT_CREATE_URL, "https://api.hellosign.com/v3/unclaimed_draft/create")

        self.assertEqual(self.client.TEMPLATE_GET_URL, "https://api.hellosign.com/v3/reusable_form/")
        self.assertEqual(self.client.TEMPLATE_GET_LIST_URL, "https://api.hellosign.com/v3/reusable_form/list")
        self.assertEqual(self.client.TEMPLATE_ADD_USER_URL, "https://api.hellosign.com/v3/reusable_form/add_user/")
        self.assertEqual(self.client.TEMPLATE_REMOVE_USER_URL, "https://api.hellosign.com/v3/reusable_form/remove_user/")

        self.assertEqual(self.client.TEAM_INFO_URL, "https://api.hellosign.com/v3/team")
        self.assertEqual(self.client.TEAM_CREATE_URL, "https://api.hellosign.com/v3/team/create")
        self.assertEqual(self.client.TEAM_UPDATE_URL, "https://api.hellosign.com/v3/team")
        self.assertEqual(self.client.TEAM_DESTROY_URL, "https://api.hellosign.com/v3/team/destroy")
        self.assertEqual(self.client.TEAM_ADD_MEMBER_URL, "https://api.hellosign.com/v3/team/add_member")
        self.assertEqual(self.client.TEAM_REMOVE_MEMBER_URL, "https://api.hellosign.com/v3/team/remove_member")

    def test_bad_request(self):
        request = HSRequest(self.client.auth)
        try:
            request.post(url=self.client.ACCOUNT_UPDATE_URL,
                         data={"bad": "request"})
        except BadRequest:
            pass

    def test_not_authorized(self):
        request = HSRequest(HTTPBasicAuth("test", ''))
        try:
            request.get(self.client.ACCOUNT_INFO_URL)
        except Unauthorized:
            pass

    def test_not_found(self):
        request = HSRequest(self.client.auth)
        try:
            request.get(url=self.client.API_URL + "/not/found")
        except NotFound:
            pass
