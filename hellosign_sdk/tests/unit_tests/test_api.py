from unittest import TestCase
from hellosign_sdk.tests import test_helper
from hellosign_sdk import HSClient
from hellosign_sdk.utils import HSRequest, BadRequest, NotFound, Unauthorized


class Api(TestCase):

    def setUp(self):
        try:
            self.env = test_helper.env
        except AttributeError:
            self.env = 'production'
        self.client = HSClient(api_key=test_helper.api_key, env=self.env)

    def test_endpoint(self):

        # Base
        base_url = self.client.API_URL
        if self.env == 'dev':
            self.assertEqual(base_url, "https://www.my.hellosign.com/apiapp_dev.php/v3")
        elif self.env == 'staging':
            self.assertEqual(base_url, "https://staging.hellosign.com/apiapp_dev.php/v3")
        else:
            self.assertEqual(base_url,"https://api.hellosign.com/v3")

        # Account
        self.assertEqual(self.client.ACCOUNT_CREATE_URL, base_url + "/account/create")
        self.assertEqual(self.client.ACCOUNT_INFO_URL, base_url + "/account")
        self.assertEqual(self.client.ACCOUNT_UPDATE_URL, base_url + "/account")

        # Signature request
        self.assertEqual(self.client.SIGNATURE_REQUEST_INFO_URL, base_url + "/signature_request/")
        self.assertEqual(self.client.SIGNATURE_REQUEST_LIST_URL, base_url + "/signature_request/list")
        self.assertEqual(self.client.SIGNATURE_REQUEST_DOWNLOAD_PDF_URL, base_url + "/signature_request/files/")
        self.assertEqual(self.client.SIGNATURE_REQUEST_CREATE_URL, base_url + "/signature_request/send")
        self.assertEqual(self.client.SIGNATURE_REQUEST_CREATE_WITH_TEMPLATE_URL, base_url + "/signature_request/send_with_reusable_form")
        self.assertEqual(self.client.SIGNATURE_REQUEST_REMIND_URL, base_url + "/signature_request/remind/")
        self.assertEqual(self.client.SIGNATURE_REQUEST_CANCEL_URL, base_url + "/signature_request/cancel/")
        self.assertEqual(self.client.SIGNATURE_REQUEST_CREATE_EMBEDDED_URL, base_url + "/signature_request/create_embedded")
        self.assertEqual(self.client.SIGNATURE_REQUEST_CREATE_EMBEDDED_WITH_TEMPLATE_URL, base_url + "/signature_request/create_embedded_with_reusable_form")

        # Embedded
        self.assertEqual(self.client.EMBEDDED_OBJECT_GET_URL, base_url + "/embedded/sign_url/")

        # Unclaimed draft
        self.assertEqual(self.client.UNCLAIMED_DRAFT_CREATE_URL, base_url + "/unclaimed_draft/create")

        # Template
        self.assertEqual(self.client.TEMPLATE_GET_URL, base_url + "/reusable_form/")
        self.assertEqual(self.client.TEMPLATE_GET_LIST_URL, base_url + "/reusable_form/list")
        self.assertEqual(self.client.TEMPLATE_ADD_USER_URL, base_url + "/reusable_form/add_user/")
        self.assertEqual(self.client.TEMPLATE_REMOVE_USER_URL, base_url + "/reusable_form/remove_user/")

        # Team
        self.assertEqual(self.client.TEAM_INFO_URL, base_url + "/team")
        self.assertEqual(self.client.TEAM_CREATE_URL, base_url + "/team/create")
        self.assertEqual(self.client.TEAM_UPDATE_URL, base_url + "/team")
        self.assertEqual(self.client.TEAM_DESTROY_URL, base_url + "/team/destroy")
        self.assertEqual(self.client.TEAM_ADD_MEMBER_URL, base_url + "/team/add_member")
        self.assertEqual(self.client.TEAM_REMOVE_MEMBER_URL, base_url + "/team/remove_member")

    def test_bad_request(self):
        request = HSRequest(self.client.auth, self.env)
        try:
            request.post(url=self.client.ACCOUNT_UPDATE_URL, data={"bad": "request"})
            self.fail("BadRequest was expected")
        except BadRequest:
            pass
        except BaseException, e:
            self.fail("BadRequest was expected but got %s instead" % e.__class__.__name__)

    def test_not_authorized(self):
        request = HSRequest(("test", ''), self.env)
        try:
            request.get(self.client.ACCOUNT_INFO_URL)
            self.fail("Unauthorized was expected")
        except Unauthorized:
            pass
        except BaseException, e:
            self.fail("BadRequest was expected but got %s instead" % e.__class__.__name__)

    def test_not_found(self):
        request = HSRequest(self.client.auth, self.env)
        try:
            request.get(url=self.client.API_URL + "/not/found")
            self.fail("NotFound was expected")
        except NotFound:
            pass
        except BaseException, e:
            self.fail("BadRequest was expected but got %s instead" % e.__class__.__name__)
