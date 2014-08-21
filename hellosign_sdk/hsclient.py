from hellosign_sdk.utils import HSRequest, HSException, NoAuthMethod, HSAccessTokenAuth
from hellosign_sdk.resource import Account, ResourceList, SignatureRequest, Template, Team, Embedded, UnclaimedDraft
from requests.auth import HTTPBasicAuth


class HSClient(object):

    ''' Client object to interact with the API urls

    Most of the operations of the SDK is made through this object. Please refer
    to the README.rst file for more details on how to use the client object.

    '''

    version = '3.2'     # SDK version
    API_VERSION = 'v3'  # API version
    API_URL = ''

    ACCOUNT_CREATE_URL = ''
    ACCOUNT_INFO_URL = ''
    ACCOUNT_UPDATE_URL = ''
    ACCOUNT_VERIFY_URL = ''

    SIGNATURE_REQUEST_INFO_URL = ''
    SIGNATURE_REQUEST_LIST_URL = ''
    SIGNATURE_REQUEST_DOWNLOAD_PDF_URL = ''
    SIGNATURE_REQUEST_CREATE_URL = ''
    SIGNATURE_REQUEST_CREATE_WITH_TEMPLATE_URL = ''
    SIGNATURE_REQUEST_REMIND_URL = ''
    SIGNATURE_REQUEST_CANCEL_URL = ''
    SIGNATURE_REQUEST_CREATE_EMBEDDED_URL = ''
    SIGNATURE_REQUEST_CREATE_EMBEDDED_WITH_TEMPLATE_URL = ''

    EMBEDDED_OBJECT_GET_URL = ''

    UNCLAIMED_DRAFT_CREATE_URL = ''
    UNCLAIMED_DRAFT_CREATE_EMBEDDED_URL = ''

    TEMPLATE_GET_URL = ''
    TEMPLATE_GET_LIST_URL = ''
    TEMPLATE_ADD_USER_URL = ''
    TEMPLATE_REMOVE_USER_URL = ''

    TEAM_INFO_URL = ''
    TEAM_UPDATE_URL = ''
    TEAM_CREATE_URL = ''
    TEAM_DESTROY_URL = ''
    TEAM_ADD_MEMBER_URL = ''
    TEAM_REMOVE_MEMBER_URL = ''

    OAUTH_TOKEN_URL = ''

    def __init__(self, email_address=None, password=None, api_key=None, access_token=None, access_token_type="Bearer", env='production'):
        '''Initialize the client object with authentication information to send requests

        Args:
            email_address (str): E-mail of the account to make the requests
            password (str): Password of the account used with email address
            api_key (str): API Key. You can find your API key in https://www.hellosign.com/home/myAccount/current_tab/integrations
            access_token (str): OAuth access token to use
            access_token_type (str): Type of OAuth token (defaults to Bearer, which is the only value supported for now)

        '''

        super(HSClient, self).__init__()
        self.auth = self._authenticate(email_address, password, api_key, access_token, access_token_type)
        self.account = Account()
        self.env = env
        self._init_endpoints()

    def __str__(self):
        ''' Return a string description of this object '''
        return "HelloSign Client %s" % self.version

    def _init_endpoints(self):

        API_PRODUCTION_URL = "https://api.hellosign.com"
        API_DEV_URL = "https://www.my.hellosign.com/apiapp_dev.php"
        API_STAGING_URL = "https://staging.hellosign.com/apiapp_dev.php"

        WEB_PRODUCTION_URL = "https://www.hellosign.com"
        WEB_DEV_URL = "https://www.my.hellosign.com/webapp_dev.php"
        WEB_STAGING_URL = "https://staging.hellosign.com/webapp_dev.php"

        if self.env == "production":
            self.API_URL = API_PRODUCTION_URL + '/' + self.API_VERSION
            self.OAUTH_TOKEN_URL = WEB_PRODUCTION_URL + '/oauth/token'
        elif self.env == "dev":
            self.API_URL = API_DEV_URL + '/' + self.API_VERSION
            self.OAUTH_TOKEN_URL = WEB_DEV_URL + '/oauth/token'
            print "WARNING: Using dev api endpoint %s" % self.API_URL
        elif self.env == "staging":
            self.API_URL = API_STAGING_URL + '/' + self.API_VERSION
            self.OAUTH_TOKEN_URL = WEB_STAGING_URL + '/oauth/token'
            print "WARNING: Using staging api endpoint %s" % self.API_URL

        self.ACCOUNT_CREATE_URL = self.API_URL + '/account/create'
        self.ACCOUNT_INFO_URL = self.API_URL + '/account'
        self.ACCOUNT_UPDATE_URL = self.API_URL + '/account'
        self.ACCOUNT_VERIFY_URL = self.API_URL + '/account/verify'

        self.SIGNATURE_REQUEST_INFO_URL = self.API_URL + '/signature_request/'
        self.SIGNATURE_REQUEST_LIST_URL = self.API_URL + '/signature_request/list'
        self.SIGNATURE_REQUEST_DOWNLOAD_PDF_URL = self.API_URL + '/signature_request/files/'
        self.SIGNATURE_REQUEST_CREATE_URL = self.API_URL + '/signature_request/send'
        self.SIGNATURE_REQUEST_CREATE_WITH_TEMPLATE_URL = self.API_URL + '/signature_request/send_with_template'
        self.SIGNATURE_REQUEST_REMIND_URL = self.API_URL + '/signature_request/remind/'
        self.SIGNATURE_REQUEST_CANCEL_URL = self.API_URL + '/signature_request/cancel/'
        self.SIGNATURE_REQUEST_CREATE_EMBEDDED_URL = self.API_URL + '/signature_request/create_embedded'
        self.SIGNATURE_REQUEST_CREATE_EMBEDDED_WITH_TEMPLATE_URL = self.API_URL + '/signature_request/create_embedded_with_template'

        self.EMBEDDED_OBJECT_GET_URL = self.API_URL + '/embedded/sign_url/'

        self.UNCLAIMED_DRAFT_CREATE_URL = self.API_URL + '/unclaimed_draft/create'
        self.UNCLAIMED_DRAFT_CREATE_EMBEDDED_URL = self.API_URL + '/unclaimed_draft/create_embedded'

        self.TEMPLATE_GET_URL = self.API_URL + '/template/'
        self.TEMPLATE_GET_LIST_URL = self.API_URL + '/template/list'
        self.TEMPLATE_ADD_USER_URL = self.API_URL + '/template/add_user/'
        self.TEMPLATE_REMOVE_USER_URL = self.API_URL + '/template/remove_user/'

        self.TEAM_INFO_URL = self.API_URL + '/team'
        self.TEAM_UPDATE_URL = self.TEAM_INFO_URL
        self.TEAM_CREATE_URL = self.API_URL + '/team/create'
        self.TEAM_DESTROY_URL = self.API_URL + '/team/destroy'
        self.TEAM_ADD_MEMBER_URL = self.API_URL + '/team/add_member'
        self.TEAM_REMOVE_MEMBER_URL = self.API_URL + '/team/remove_member'


    #####  ACCOUNT METHODS  ###############################

    def create_account(self, email_address, password, client_id=None, client_secret=None):
        ''' Create a new account.

        If the account is created via an app, then Account.oauth will contain the 
        OAuth data that can be used to execute actions on behalf of the newly created account.

        Args:
            email_address (str): Email address of the new account to create
            password (str): Password of the new account
            client_id (str, optional): Client id of the app to use to create this account
            client_secret (str, optional): Secret of the app to use to create this account

        Returns:
            The new Account object

        '''
        request = self._get_request()
        
        params = {
            'email_address': email_address, 
            'password': password
        }
        if client_id:
            params['client_id'] = client_id
            params['client_secret'] = client_secret

        response = request.post(self.ACCOUNT_CREATE_URL, params)

        if 'oauth_data' in response:
            response["account"]["oauth"] = response['oauth_data']

        return Account(response["account"])

    # Get account info and put in self.account so that further access to the
    # info can be made by using self.account.attribute
    def get_account_info(self):
        ''' Get current account information

        The information then will be saved in `self.account` so that you can
        access the information like this:

        >>> hsclient = HSClient()
        >>> acct = hsclient.get_account_info()
        >>> print acct.email_address

        Returns:
            An Account object

        '''
        request = self._get_request()
        response = request.get(self.ACCOUNT_INFO_URL)
        self.account.json_data = response["account"]
        return self.account

    # At the moment you can only update your callback_url only
    def update_account_info(self):
        ''' Update current account information

        At the moment you can only update your callback_url.

        Returns:
            An Account object

        '''
        request = self._get_request()
        resp = request.post(self.ACCOUNT_UPDATE_URL, { 'callback_url': self.account.callback_url })
        return Account(resp['account'])

    def verify_account(self, email_address):
        ''' Verify whether a HelloSign Account exists 

            email_address (str): Email address for the account to verify

            Returns:
                True or False
        '''
        request = self._get_request()
        resp = request.post(self.ACCOUNT_VERIFY_URL, {
            'email_address': email_address
        })
        return ('account' in resp)


    #####  SIGNATURE REQUEST METHODS  #####################

    def get_signature_request(self, signature_request_id):
        ''' Get a signature request by its ID

        Args:
            signature_request_id (str): The id of the SignatureRequest to retrieve

        Returns:
            A SignatureRequest object

        '''
        request = self._get_request()
        response = request.get(self.SIGNATURE_REQUEST_INFO_URL + signature_request_id)
        return SignatureRequest(response["signature_request"])

    def get_signature_request_list(self, page=1):
        ''' Get a list of SignatureRequest that you can access

        This includes SignatureRequests you have sent as well as received, but
        not ones that you have been CCed on.

        Args:
            page (int, optional): Which page number of the SignatureRequest list to
                return. Defaults to 1.

        Returns:
            A ResourceList object

        '''
        request = self._get_request()
        response = request.get(self.SIGNATURE_REQUEST_LIST_URL, parameters={ "page": page })
        return ResourceList(SignatureRequest, response)

    def get_signature_request_file(self, signature_request_id, filename, file_type=None):
        ''' Download the PDF copy of the current documents

        Args:
            signature_request_id (str): Id of the signature request

            filename (str): Filename to save the PDF file to. This should be a full path.

            file_type (str): Type of file to return. Either "pdf" for a single merged document 
                             or "zip" for a collection of individual documents. Defaults to "pdf" 
                             if not specified.

        Returns:
            True if file is downloaded and successfully written, False otherwise.

        '''
        request = self._get_request()
        url = self.SIGNATURE_REQUEST_DOWNLOAD_PDF_URL + signature_request_id
        if file_type:
            url += '?file_type=%s' % file_type
        return request.get_file(url, filename)

    def send_signature_request(self, test_mode=False, files=None, file_urls=None, title=None, subject=None, message=None, signing_redirect_url=None, signers=None, cc_email_addresses=None, form_fields_per_document=None, use_text_tags=False, hide_text_tags=False):
        ''' Creates and sends a new SignatureRequest with the submitted documents

        Creates and sends a new SignatureRequest with the submitted documents.
        If form_fields_per_document is not specified, a signature page will be
        affixed where all signers will be required to add their signature,
        signifying their agreement to all contained documents.

        Args:
            test_mode (bool, optional): Whether this is a test, the signature request will not be legally binding if set to True. Defaults to False.
            
            files (list of str): the uploaded file(s) to send for signature
            
            file_urls (list of str): urls of the file for HelloSign to download to send for signature. Use either `files` or `file_urls`
            
            title (str, optional): The title you want to assign to the SignatureRequest
            
            subject (str, optional): The subject in the email that will be sent to the signers
            
            message (str, optional): The custom message in the email that will be sent to the signers
            
            signing_redirect_url (str, optional): The URL you want the signer redirected to after they successfully sign.

            signers (list of dict): A list of signers, which each has the following attributes:

                name (str): The name of the signer
                email_address (str): email address of the signer
                order (str, optional): The order the signer is required to sign in
                pin (str, optional): The 4- to 12-character access code that will secure this signer's signature page

            cc_email_addresses (list of str, optional): A list of email addresses that should be CC'd

            form_fields_per_document (str): The fields that should appear on the document, expressed as a serialized JSON data structure which is
                a list of lists of the form fields. Please refer to the API reference of HelloSign for more details (https://www.hellosign.com/api/reference#SignatureRequest)

            use_text_tags (bool, optional): Use text tags in the provided file(s) to create form fields

            hide_text_tags (bool, optional): Hide text tag areas

        Returns:
            A SignatureRequest object

        '''

        self._check_required_fields({ "signers": signers }, [{ "files": files, "file_urls": file_urls }])
        
        params = {
            'test_mode': self._boolean(test_mode), 
            'files': files, 
            'file_urls':file_urls, 
            'title': title,
            'subject': subject, 
            'message': message,
            'signing_redirect_url': signing_redirect_url, 
            'signers': signers,
            'cc_email_addresses': cc_email_addresses,
            'form_fields_per_document': form_fields_per_document,
            'use_text_tags': self._boolean(use_text_tags),
            'hide_text_tags': self._boolean(hide_text_tags)
        }

        return self._send_signature_request(**params)

    def send_signature_request_with_template(self, test_mode=False, template_id=None, title=None, subject=None, message=None, signing_redirect_url=None, signers=None, ccs=None, custom_fields=None):
        ''' Creates and sends a new SignatureRequest based off of a Template

        Creates and sends a new SignatureRequest based off of the Template
        specified with the template_id parameter.

        Args:
            test_mode (bool, optional): Whether this is a test, the signature
                request will not be legally binding if set to True. Defaults to False.
            
            template_id (str): The id of the Template  to use when creating the SignatureRequest.
            
            title (str, optional): The title you want to assign to the SignatureRequest
            
            subject (str, optional): The subject in the email that will be sent to the signers
            
            message (str, optional): The custom message in the email that will be sent to the signers
            
            signing_redirect_url (str, optional): The URL you want the signer redirected to after they successfully sign.
            
            signers (list of dict): A list of signers, which each has the following attributes:

                role_name (str): Signer role
                name (str): The name of the signer
                email_address (str): email address of the signer
                pin (str, optional): The 4- to 12-character access code that will secure this signer's signature page

            ccs (list of str, optional): The email address of the CC filling the role of RoleName. Required when a CC role exists for the
                Template. Each dict has the following attributes:

                role_name (str):        CC role name
                email_address (str):    CC email address

            custom_fields (list of dict, optional): A list of custom fields. Required when a CustomField exists in the Template. An item
                of the list should look like this: `{'name: value'}`

        Returns:
            A SignatureRequest object

        '''

        self._check_required_fields({ "signers": signers, "template_id": template_id })

        params = {
            'test_mode': self._boolean(test_mode), 
            'template_id': template_id,
            'title': title, 
            'subject': subject, 
            'message': message,
            'signing_redirect_url': signing_redirect_url, 
            'signers': signers,
            'ccs': ccs, 
            'custom_fields': custom_fields
        }

        return self._send_signature_request_with_template(**params)

    def remind_signature_request(self, signature_request_id, email_address):
        ''' Sends an email to the signer reminding them to sign the signature request

        Sends an email to the signer reminding them to sign the signature
        request. You cannot send a reminder within 1 hours of the last reminder
        that was sent. This includes manual AND automatic reminders.

        Args:
            signature_request_id (str): The id of the SignatureRequest to send a reminder for

            email_address (str): The email address of the signer to send a reminder to

        Returns:
            A SignatureRequest object

        '''
        request = self._get_request()
        response = request.post(self.SIGNATURE_REQUEST_REMIND_URL + signature_request_id, data={ "email_address": email_address })
        return SignatureRequest(response["signature_request"])

    def cancel_signature_request(self, signature_request_id):
        ''' Cancels a SignatureRequest

        Cancels a SignatureRequest. After canceling, no one will be able to sign
        or access the SignatureRequest or its documents. Only the requester can
        cancel and only before everyone has signed.

        Args:
            signing_request_id (str): The id of the signature request to cancel

        Returns:
            None

        '''
        request = self._get_request()
        request.post(url=self.SIGNATURE_REQUEST_CANCEL_URL + signature_request_id, get_json=False)

    def send_signature_request_embedded(self, test_mode=False, client_id=None, files=None, file_urls=None, title=None, subject=None, message=None, signing_redirect_url=None, signers=None, cc_email_addresses=None, form_fields_per_document=None):
        ''' Creates and sends a new SignatureRequest with the submitted documents

        Creates a new SignatureRequest with the submitted documents to be signed
        in an embedded iFrame . If form_fields_per_document is not specified, a
        signature page will be affixed where all signers will be required to add
        their signature, signifying their agreement to all contained documents.
        Note that embedded signature requests can only be signed in embedded
        iFrames whereas normal signature requests can only be signed on
        HelloSign.

        Args:
            test_mode (bool, optional): Whether this is a test, the signature
                request will not be legally binding if set to True. Defaults to False.

            client_id (str): Client id of the app you're using to create this
                embedded signature request. Visit the embedded page to learn
                more about this parameter
                (https://www.hellosign.com/api/embedded)

            files (list of str): the uploaded file(s) to send for signature

            file_urls (list of str): urls of the file for HelloSign to download to send for signature. Use either `files` or `file_urls`

            title (str, optional): The title you want to assign to the SignatureRequest

            subject (str, optional): The subject in the email that will be sent to the signers

            message (str, optional): The custom message in the email that will be sent to the signers

            signing_redirect_url (str, optional): The URL you want the signer redirected to after they successfully sign.

            signers (list of dict): A list of signers, which each has the following attributes:

                name (str): The name of the signer
                email_address (str): email address of the signer
                order (str, optional): The order the signer is required to sign in
                pin (str, optional): The 4- to 12-character access code that will secure this signer's signature page

            cc_email_addresses (list of str, optional): A list of email addresses that should be CCed

            form_fields_per_document (str): The fields that should appear on the document, expressed as a serialized JSON data structure which is
                a list of lists of the form fields. Please refer to the API reference of HelloSign for more details (https://www.hellosign.com/api/reference#SignatureRequest)

        Returns:
            A SignatureRequest object

        '''

        self._check_required_fields({ "signers": signers, "client_id": client_id }, [{ "files": files, "file_urls": file_urls }])

        params = {
            'test_mode': self._boolean(test_mode), 
            'client_id': client_id, 
            'files': files,
            'file_urls': file_urls, 
            'title': title, 
            'subject': subject, 
            'message': message,
            'signing_redirect_url': signing_redirect_url, 
            'signers': signers,
            'cc_email_addresses': cc_email_addresses,
            'form_fields_per_document': form_fields_per_document
        }

        return self._send_signature_request(**params)

    def send_signature_request_embedded_with_template(self, test_mode=False, client_id=None, template_id=None, title=None, subject=None, message=None, signing_redirect_url=None, signers=None, ccs=None, custom_fields=None):
        ''' Creates and sends a new SignatureRequest based off of a Template

        Creates a new SignatureRequest based on the given Template to be
        signed in an embedded iFrame. Note that embedded signature requests can
        only be signed in embedded iFrames whereas normal signature requests can
        only be signed on HelloSign.

        Args:
            test_mode (bool, optional): Whether this is a test, the signature
                request will not be legally binding if set to True. Defaults to False.

            client_id (str): Client id of the app you're using to create this embedded signature request. 
                Visit the embedded page to learn more about this parameter (https://www.hellosign.com/api/embedded)

            template_id (str): The id of the Template to use when creating the SignatureRequest.

            title (str, optional): The title you want to assign to the SignatureRequest

            subject (str, optional): The subject in the email that will be sent to the signers

            message (str, optional): The custom message in the email that will be sent to the signers

            signing_redirect_url (str, optional): The URL you want the signer redirected to after they successfully sign.

            signers (list of dict): A list of signers, which each has the following attributes:

                name (str): The name of the signer
                email_address (str): email address of the signer
                pin (str, optional): The 4- to 12-character access code that will secure this signer's signature page

            ccs (list of str, optional): The email address of the CC filling the
                role of RoleName. Required when a CC role exists for the
                Template. Each dict has the following attributes:

                role_name (str):        CC role name
                email_address (str):    CC email address

            custom_fields (list of dict, optional): A list of custom fields. Required when a CustomField exists in the Template. An item
                of the list should look like this: `{'name: value'}`

        Returns:
            A SignatureRequest object of the newly created Signature Request

        '''

        self._check_required_fields({
            "signers": signers, 
            "template_id": template_id, 
            "client_id": client_id
        })

        params = {
            'test_mode': self._boolean(test_mode), 
            'client_id': client_id,
            'template_id': template_id, 
            'title': title, 
            'subject': subject,
            'message': message, 
            'signing_redirect_url': signing_redirect_url,
            'signers': signers, 
            'ccs': ccs, 
            'custom_fields': custom_fields
        }

        return self._send_signature_request_with_template(**params)


    #####  REUSABLE FORM METHODS  #########################

    def get_template(self, template_id):
        ''' Gets a Template which includes a list of Accounts that can access it

        Args:
            template_id (str): The id of the template to retrieve

        Returns:
            A Template object

        '''
        request = self._get_request()
        response = request.get(self.TEMPLATE_GET_URL + template_id)
        return Template(response["template"])

    def get_template_list(self, page=1):
        ''' Lists your Templates

        Args:
            page (int, optional): Page number of the template List to return. Defaults to 1.

        Returns:
            A ResourceList object

        '''
        request = self._get_request()
        response = request.get(self.TEMPLATE_GET_LIST_URL, parameters={ "page": page })
        return ResourceList(Template, response)

    # RECOMMEND: this api does not fail if the user has been added...
    def add_user_to_template(self, template_id, account_id=None, email_address=None):
        ''' Gives the specified Account access to the specified Template

        Args:
            template_id (str): The id of the template to give the account access to

            account_id (str): The id of the account to give access to the template. 
                The account id prevails if both account_id and email_address are provided.

            email_address (str): The email address of the account to give access to.

        Returns:
            A Template object

        '''
        return self._add_remove_user_template(self.TEMPLATE_ADD_USER_URL, template_id, account_id, email_address)

    def remove_user_from_template(self, template_id, account_id=None, email_address=None):
        ''' Removes the specified Account's access to the specified Template

        Args:
            template_id (str): The id of the template to remove the account's access from.

            account_id (str): The id of the account to remove access from the template. 
                The account id prevails if both account_id and email_address are provided.

            email_address (str): The email address of the account to remove access from.

        Returns:
            An Template object

        '''
        return self._add_remove_user_template(self.TEMPLATE_REMOVE_USER_URL, template_id, account_id, email_address)


    #####  TEAM METHODS  ##################################

    def get_team_info(self):
        ''' Gets your Team and a list of its members

        Returns information about your team as well as a list of its members.
        If you do not belong to a team, a 404 error with an error_name of
        "not_found" will be returned.

        Returns:
            A Team object

        '''
        request = self._get_request()
        response = request.get(self.TEAM_INFO_URL)
        return Team(response["team"])

    def create_team(self, name):
        ''' Creates a new Team

        Creates a new Team and makes you a member. You must not currently belong to a team to invoke.

        Args:
            name (str): The name of your team

        Returns:
            A Team object

        '''
        request = self._get_request()
        response = request.post(self.TEAM_CREATE_URL, { "name": name })
        return Team(response["team"])

    # RECOMMEND: The api event create a new team if you do not belong to any team
    def update_team_name(self, name):
        ''' Updates a Team's name

        Args:
            name (str): The new name of your team

        Returns:
            A Team object

        '''
        request = self._get_request()
        response = request.post(self.TEAM_UPDATE_URL, { "name": name })
        return Team(response["team"])

    def destroy_team(self):
        ''' Delete your Team

        Deletes your Team. Can only be invoked when you have a team with only one member left (yourself).

        Returns:
            None

        '''
        request = self._get_request()
        request.post(url=self.TEAM_DESTROY_URL, get_json=False)

    def add_team_member(self, account_id=None, email_address=None):
        ''' Add or invite a user to your Team

        Args:
            account_id (str): The id of the account of the user to invite to your team.

            email_address (str): The email address of the account to invite to your team. 
                The account id prevails if both account_id and email_address are provided.

        Returns:
            A Team object

        '''
        return self._add_remove_team_member(self.TEAM_ADD_MEMBER_URL, email_address, account_id)

    # RECOMMEND: Does not fail if user has been removed
    def remove_team_member(self, account_id=None, email_address=None):
        ''' Remove a user from your Team

        Args:
            account_id (str): The id of the account of the user to remove from your team.

            email_address (str): The email address of the account to remove from your team. 
                The account id prevails if both account_id and email_address are provided.

        Returns:
            A Team object

        '''
        return self._add_remove_team_member(self.TEAM_REMOVE_MEMBER_URL, email_address, account_id)


    #####  EMBEDDED METHODS  ##############################

    def get_embedded_object(self, signature_id):
        ''' Retrieves a embedded signing object

        Retrieves an embedded object containing a signature url that can be opened in an iFrame.

        Args:
            signature_id (str): The id of the signature to get a signature url for

        Returns:
            An Embedded object

        '''
        request = self._get_request()
        response = request.get(self.EMBEDDED_OBJECT_GET_URL + signature_id)
        return Embedded(response["embedded"])


    #####  UNCLAIMED DRAFT METHODS  #######################

    def create_unclaimed_draft(self, test_mode=False, files=None, file_urls=None, draft_type=None, subject=None, message=None, signers=None, cc_email_addresses=None, signing_redirect_url=None, form_fields_per_document=None):
        ''' Creates a new Draft that can be claimed using the claim URL

        Creates a new Draft that can be claimed using the claim URL. The first
        authenticated user to access the URL will claim the Draft and will be
        shown either the "Sign and send" or the "Request signature" page with
        the Draft loaded. Subsequent access to the claim URL will result in a
        404. If the type is "send_document" then only the file parameter is
        required. If the type is "request_signature", then the identities of the
        signers and optionally the location of signing elements on the page are
        also required.

        Args:
            test_mode (bool, optional): Whether this is a test, the signature
                request created from this draft will not be legally binding if
                set to True. Defaults to False.

            files (list of str): the uploaded file(s) to send for signature

            file_urls (list of str): urls of the file for HelloSign to download to send for signature. Use either `files` or `file_urls`

            draft_type (str): The type of unclaimed draft to create. Use "send_document" to create a claimable file, and
                "request_signature" for a claimable signature request. If the type is "request_signature" then signers name and email_address are not optional.

            subject (str, optional): The subject in the email that will be sent to the signers

            message (str, optional): The custom message in the email that will be sent to the signers

            signers (list of dict): A list of signers, which each has the following attributes:

                name (str): The name of the signer
                email_address (str): email address of the signer
                order (str, optional): The order the signer is required to sign in

            cc_email_addresses (list of str, optional): A list of email addresses that should be CC'd

            signing_redirect_url (str, optional): The URL you want the signer redirected to after they successfully sign.

            form_fields_per_document (str, optional): The fields that should appear on the document, expressed as a serialized JSON data structure which is
                a list of lists of the form fields. Please refer to the API reference of HelloSign for more details (https://www.hellosign.com/api/reference#SignatureRequest)

        Returns:
            An UnclaimedDraft object

        '''

        self._check_required_fields({ 'draft_type': draft_type }, [{ "files": files, "file_urls": file_urls }])

        params = {
            'test_mode': self._boolean(test_mode), 
            'files': files,
            'file_urls': file_urls, 
            'draft_type': draft_type,
            'subject': subject, 
            'message': message,
            'signing_redirect_url': signing_redirect_url, 
            'signers': signers,
            'cc_email_addresses': cc_email_addresses,
            'form_fields_per_document': form_fields_per_document
        }

        return self._create_unclaimed_draft(**params)

    def create_embedded_unclaimed_draft(self, test_mode=False, client_id=None, is_for_embedded_signing=False, requester_email_address=None, files=None, file_urls=None, draft_type=None, subject=None, message=None, signers=None, cc_email_addresses=None, signing_redirect_url=None, requesting_redirect_url=None, form_fields_per_document=None):
        ''' Creates a new Draft to be used for embedded requesting

        Args:
            test_mode (bool, optional): Whether this is a test, the signature
                request created from this draft will not be legally binding if
                set to True. Defaults to False.

            client_id (str): Client id of the app used to create the embedded draft.

            is_for_embedded_signing (bool, optional): Whether this is also for embedded signing. Defaults to False.

            requester_email_address (str): Email address of the requester.

            files (list of str): the uploaded file(s) to send for signature.

            file_urls (list of str): urls of the file for HelloSign to download to send for signature. Use either `files` or `file_urls`

            draft_type (str): The type of unclaimed draft to create. Use
                "send_document" to create a claimable file, and
                "request_signature" for a claimable signature request. If the
                type is "request_signature" then signers name and email_address
                are not optional.

            subject (str, optional): The subject in the email that will be sent to the signers

            message (str, optional): The custom message in the email that will be sent to the signers

            signers (list of dict): A list of signers, which each has the following attributes:

                name (str): The name of the signer
                email_address (str): email address of the signer
                order (str, optional): The order the signer is required to sign in

            cc_email_addresses (list of str, optional): A list of email addresses that should be CC'd

            signing_redirect_url (str, optional): The URL you want the signer redirected to after they successfully sign.

            requesting_redirect_url (str, optional): The URL you want the signer to be redirected to after the request has been sent.

            form_fields_per_document (str, optional): The fields that should appear on the document, expressed as a serialized JSON data structure which is
                a list of lists of the form fields. Please refer to the API reference of HelloSign for more details (https://www.hellosign.com/api/reference#SignatureRequest)

        Returns:
            An UnclaimedDraft object

        '''

        self._check_required_fields({ 
            'client_id': client_id, 
            'requester_email_address': requester_email_address, 
            'draft_type': draft_type
        }, [{ 
            "files": files, 
            "file_urls": file_urls 
        }])

        params = {
            'test_mode': self._boolean(test_mode), 
            'client_id': client_id, 
            'requester_email_address': requester_email_address,
            'is_for_embedded_signing': self._boolean(is_for_embedded_signing),
            'files': files,
            'file_urls': file_urls, 
            'draft_type': draft_type,
            'subject': subject, 
            'message': message,
            'signing_redirect_url': signing_redirect_url, 
            'requesting_redirect_url': requesting_redirect_url, 
            'signers': signers,
            'cc_email_addresses': cc_email_addresses,
            'form_fields_per_document': form_fields_per_document
        }

        return self._create_unclaimed_draft(**params)


    #####  OAUTH METHODS  #################################

    def get_oauth_data(self, code, client_id, client_secret, state):
        ''' Get Oauth data from HelloSign

        Args:
            code (str): Code returned by HelloSign for our callback url
            client_id (str): Client id of the associated app
            client_secret (str): Secret token of the associated app

        Returns:
            A HSAccessTokenAuth object

        '''
        request = self._get_request()
        response = request.post(self.OAUTH_TOKEN_URL, {
            "state": state,
            "code": code,
            "grant_type": "authorization_code",
            "client_id": client_id, 
            "client_secret": client_secret
        })
        return HSAccessTokenAuth.from_response(response)

    def refresh_access_token(self, refresh_token):
        ''' Refreshes the current access token.

            Gets a new access token, updates client auth and returns it.

        Args:
            refresh_token (str): Refresh token to use

        Returns:
            The new access token
        '''
        request = self._get_request()
        response = request.post(self.OAUTH_TOKEN_URL, {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token
        })
        self.auth = HSAccessTokenAuth.from_response(response)
        return self.auth.access_token


    #####  HELPERS  #######################################

    def _boolean(self, v):
        ''' Convert a value to a boolean '''
        return '1' if (v in (True, 'true', 'True', '1', 1)) else '0'

    def _get_request(self, auth=None):
        ''' Return an http request object 

            auth: Auth data to use

            Returns:
                A HSRequest object
        '''
        return HSRequest(auth or self.auth, self.env)

    def _authenticate(self, email_address=None, password=None, api_key=None, access_token=None, access_token_type=None):
        ''' Create authentication object to send requests

        Args:
            email_address (str): Email address of the account to make the requests

            password (str): Password of the account used with email address

            api_key (str): API Key. You can find your API key in https://www.hellosign.com/home/myAccount/current_tab/integrations
            access_token (str): OAuth access token
            access_token_type (str): Type of OAuth access token

        Raises:
            NoAuthMethod: If no authentication information found

        Returns:
            A HTTPBasicAuth or HSAccessTokenAuth object

        '''

        if access_token_type and access_token:
            return HSAccessTokenAuth(access_token, access_token_type)
        elif api_key:
            return HTTPBasicAuth(api_key, '')
        elif email_address and password:
            return HTTPBasicAuth(email_address, password)
        else:
            raise NoAuthMethod("No authentication information found!")

    def _check_required_fields(self, fields=None, either_fields=None):
        ''' Check the values of the fields

        If no value found in `fields`, an exception will be raised.
        `either_fields` are the fields that one of them must have a value

        Raises:
            HSException: If no value found in at least one item of`fields`, or
                no value found in one of the items of `either_fields`

        Returns:
            None

        '''

        for (key, value) in fields.iteritems():
            # If value is a dict, one of the fields in the dict is required ->
            # exception if all are None
            if not value:
                raise HSException("Field '%s' is required." % key)
        if either_fields is not None:
            for field in either_fields:
                if not any(field.values()):
                    raise HSException("One of the following fields is required: %s" % ", ".join(field.keys()))

    def _send_signature_request(self, test_mode=False, client_id=None, files=None, file_urls=None, title=None, subject=None, message=None, signing_redirect_url=None, signers=None, cc_email_addresses=None, form_fields_per_document=None, use_text_tags=False, hide_text_tags=False):
        ''' To share the same logic between send_signature_request &
            send_signature_request_embedded functions

        Args:
            test_mode (bool, optional): Whether this is a test, the signature
                request will not be legally binding if set to True. Defaults to False.

            client_id (str): Client id of the app you're using to create this embedded signature request. 
                Visit the embedded page to learn more about this parameter (https://www.hellosign.com/api/embedded)

            files (list of str): the uploaded file(s) to send for signature

            file_urls (list of str): urls of the file for HelloSign to download to send for signature. Use either `files` or `file_urls`

            title (str, optional): The title you want to assign to the SignatureRequest

            subject (str, optional): The subject in the email that will be sent to the signers

            message (str, optional): The custom message in the email that will be sent to the signers

            signing_redirect_url (str, optional): The URL you want the signer redirected to after they successfully sign

            signers (list of dict): A list of signers, which each has the following attributes:

                name (str): The name of the signer
                email_address (str): email address of the signer
                order (str, optional): The order the signer is required to sign in
                pin (str, optional): The 4- to 12-character access code that will secure this signer's signature page

            cc_email_addresses (list of str, optional): A list of email
                addresses that should be CCed

            form_fields_per_document (str): The fields that should appear on the
                document, expressed as a serialized JSON data structure which is
                a list of lists of the form fields. Please refer to the API
                reference of HelloSign for more details
                (https://www.hellosign.com/api/reference#SignatureRequest)

            use_text_tags (bool, optional): Use text tags in the provided file(s) to create form fields

            hide_text_tags (bool, optional): Hide text tag areas

        Returns:
            A SignatureRequest object

        '''

        # Files
        files_payload = {}
        if files:
            for idx, filename in enumerate(files):
                files_payload["file[" + str(idx) + "]"] = open(filename, 'rb')

        # File URLs
        file_urls_payload = {}
        if file_urls:
            for idx, fileurl in enumerate(file_urls):
                file_urls_payload["file_url[" + str(idx) + "]"] = fileurl

        # Signers
        signers_payload = {}
        for idx, signer in enumerate(signers):
            signers_payload["signers[" + str(idx) + "][name]"] = signer["name"]
            signers_payload["signers[" + str(idx) + "][email_address]"] = signer[
                "email_address"]
            if "order" in signer:
                signers_payload[
                    "signers[" + str(idx) + "][order]"] = signer["order"]
            if "pin" in signer:
                signers_payload[
                    "signers[" + str(idx) + "][pin]"] = signer["pin"]

        # CCs
        cc_email_addresses_payload = {}
        if cc_email_addresses:
            for idx, cc_email_address in enumerate(cc_email_addresses):
                cc_email_addresses_payload[
                    "cc_email_addresses[" + str(idx) + "]"] = cc_email_address
        
        payload = {
            "test_mode": self._boolean(test_mode), 
            "client_id": client_id, 
            "title": title,
            "subject": subject, 
            "message": message,
            "signing_redirect_url": signing_redirect_url,
            "form_fields_per_document": form_fields_per_document,
            "use_text_tags": self._boolean(use_text_tags),
            "hide_text_tags": self._boolean(hide_text_tags)
        }

        # remove attributes with none value
        payload = dict((key, value) for key, value in payload.iteritems() if value)

        url = self.SIGNATURE_REQUEST_CREATE_URL
        if client_id:
            url = self.SIGNATURE_REQUEST_CREATE_EMBEDDED_URL
        
        data = dict(payload.items() + signers_payload.items() + cc_email_addresses_payload.items() + file_urls_payload.items())

        request = self._get_request()
        response = request.post(url, data=data, files=files_payload)

        return SignatureRequest(response["signature_request"])

    def _send_signature_request_with_template(self, test_mode=False, client_id=None, template_id=None, title=None, subject=None, message=None, signing_redirect_url=None, signers=None, ccs=None, custom_fields=None):
        ''' To share the same logic between send_signature_request_with_template 
            and send_signature_request_embedded_with_template

        Args:
            test_mode (bool, optional): Whether this is a test, the signature
                request will not be legally binding if set to True. Defaults to False.

            client_id (str): Client id of the app you're using to create this embedded signature request. 
                Visit the embedded page to learn more about this parameter (https://www.hellosign.com/api/embedded)

            template_id (str): The id of the Template to use when creating the SignatureRequest.

            title (str, optional): The title you want to assign to the SignatureRequest

            subject (str, optional): The subject in the email that will be sent to the signers

            message (str, optional): The custom message in the email that will be sent to the signers

            signing_redirect_url (str, optional): The URL you want the signer redirected to after they successfully sign.

            signers (list of dict): A list of signers, which each has the
                following attributes:

                role_name (str): Role the signer is assigned to
                name (str): The name of the signer
                email_address (str): email address of the signer
                pin (str, optional): The 4- to 12-character access code that will secure this signer's signature page

            ccs (list of str, optional): The email address of the CC filling the role of RoleName. Required when a CC role exists for the Template. 
                Each dict has the following attributes:

                role_name (str):        CC role name
                email_address (str):    CC email address

            custom_fields (list of dict, optional): A list of custom fields. Required when a CustomField exists in the Template. An item
                of the list should look like this: `{'name: value'}`

        Returns:
            A SignatureRequest object

        '''

        # Signers
        signers_payload = {}
        for signer in signers:
            signers_payload["signers[" + signer["role_name"] + "][name]"] = signer["name"]
            signers_payload["signers[" + signer["role_name"] + "][email_address]"] = signer["email_address"]
            if "pin" in signer:
                signers_payload[
                    "signers[" + signer["role_name"] + "][pin]"] = signer["pin"]

        # CCs
        ccs_payload = {}
        if ccs:
            for cc in ccs:
                # cc_emaiL_address: {"email_address": "email@email.email",
                # "role_name": "Role Name"}
                ccs_payload[
                    "ccs[" + cc["role_name"] + "][email_address]"] = cc["email_address"]

        # Custom fields
        custom_fields_payload = {}
        if custom_fields:
            # custom_field: {"name": value}
            for custom_field in custom_fields:
                for key, value in custom_field.iteritems():
                    custom_fields_payload["custom_fields[" + key + "]"] = value

        payload = {
            "test_mode": self._boolean(test_mode), 
            "client_id": client_id,
            "template_id": template_id, 
            "title": title,
            "subject": subject, 
            "message": message,
            "signing_redirect_url": signing_redirect_url
        }

        # remove attributes with empty value
        payload = dict((key, value) for key, value in payload.iteritems() if value)

        url = self.SIGNATURE_REQUEST_CREATE_WITH_TEMPLATE_URL
        if client_id:
            url = self.SIGNATURE_REQUEST_CREATE_EMBEDDED_WITH_TEMPLATE_URL

        data = dict(payload.items() + signers_payload.items() + ccs_payload.items() + custom_fields_payload.items())

        request = self._get_request()
        response = request.post(url, data=data)

        return SignatureRequest(response["signature_request"])

    def _create_unclaimed_draft(self, test_mode=False, client_id=None, is_for_embedded_signing=False, requester_email_address=None, files=None, file_urls=None, draft_type=None, subject=None, message=None, signers=None, cc_email_addresses=None, signing_redirect_url=None, requesting_redirect_url=None, form_fields_per_document=None):
        ''' Creates a new Draft that can be claimed using the claim URL

        Args:
            test_mode (bool, optional): Whether this is a test, the signature
                request created from this draft will not be legally binding if
                set to True. Defaults to False.

            client_id (str): Client id of the app used to create the embedded draft.

            is_for_embedded_signing (bool): Whether this is for embedded signing on top of being for embedded requesting.

            requester_email_address (str): Email address of the requester when creating a draft for embedded requesting.

            files (list of str): the uploaded file(s) to send for signature.

            file_urls (list of str): urls of the file for HelloSign to download to send for signature. Use either `files` or `file_urls`

            draft_type (str): The type of unclaimed draft to create. Use
                "send_document" to create a claimable file, and
                "request_signature" for a claimable signature request. If the
                type is "request_signature" then signers name and email_address
                are not optional.

            subject (str, optional): The subject in the email that will be sent to the signers

            message (str, optional): The custom message in the email that will be sent to the signers

            signers (list of dict): A list of signers, which each has the following attributes:

                name (str): The name of the signer
                email_address (str): email address of the signer
                order (str, optional): The order the signer is required to sign in

            cc_email_addresses (list of str, optional): A list of email addresses that should be CC'd

            signing_redirect_url (str, optional): The URL you want the signer redirected to after they successfully sign.

            requesting_redirect_url (str, optional): The URL you want the signer to be redirected to after the request has been sent.

            form_fields_per_document (str): The fields that should appear on the
                document, expressed as a serialized JSON data structure which is
                a list of lists of the form fields. Please refer to the API
                reference of HelloSign for more details
                (https://www.hellosign.com/api/reference#SignatureRequest)

        Returns:
            An UnclaimedDraft object

        '''

        # Files
        files_payload = {}
        if files:
            for (idx, filename) in enumerate(files):
                files_payload["file[%s]" % idx] = open(filename, 'rb')

        # Files URLs
        file_urls_payload = {}
        if file_urls:
            for (idx, fileurl) in enumerate(file_urls):
                file_urls_payload["file_url[%s]" % idx] = fileurl
        
        # Signers
        signers_payload = {}
        if signers:
            for (idx, signer) in enumerate(signers):
                if draft_type == UnclaimedDraft.UNCLAIMED_DRAFT_REQUEST_SIGNATURE_TYPE:
                    if "name" not in signer and "email_address" not in signer:
                        raise HSException("Signer's name and email are required")
                    else:
                        signers_payload["signers[%s][name]" % idx] = signer["name"]
                        signers_payload["signers[%s][email_address]" % idx] = signer["email_address"]
                if "order" in signer:
                    signers_payload["signers[%s][order]" % idx] = signer["order"]

        # CCs
        cc_email_addresses_payload = {}
        if cc_email_addresses:
            for (idx, cc_email_address) in enumerate(cc_email_addresses):
                cc_email_addresses_payload["cc_email_addresses[%s]" % idx] = cc_email_address
        
        payload = {
            "test_mode": self._boolean(test_mode), 
            "type": draft_type,
            "subject": subject, 
            "message": message,
            "signing_redirect_url": signing_redirect_url,
            "form_fields_per_document": form_fields_per_document
        }

        url = self.UNCLAIMED_DRAFT_CREATE_URL

        if client_id is not None:
            payload.update({
                'client_id': client_id,
                'is_for_embedded_signing': '1' if is_for_embedded_signing else '0',
                'requester_email_address': requester_email_address,
                'requesting_redirect_url': requesting_redirect_url
            })
            url = self.UNCLAIMED_DRAFT_CREATE_EMBEDDED_URL

        # remove attributes with none value
        payload = dict((key, value) for key, value in payload.iteritems() if value)

        data = dict(payload.items() + signers_payload.items() + cc_email_addresses_payload.items() + file_urls_payload.items())

        request = self._get_request()
        response = request.post(url, data=data, files=files_payload)

        return UnclaimedDraft(response["unclaimed_draft"])

    def _add_remove_user_template(self, url, template_id, account_id=None, email_address=None):
        ''' Add or Remove user from a Template

        We use this function for two tasks because they have the same API call

        Args:
            template_id (str): The id of the template

            account_id (str): ID of the account to add/remove access to/from

            email_address (str): The email_address of the account to add/remove access to/from

        Raises:
            HSException: If no email address or account_id specified

        Returns:
            A Template object

        '''

        if not email_address and not account_id:
            raise HSException("No email address or account_id specified")

        data = {}
        if account_id is not None:
            data = { "account_id": account_id }
        else:
            data = { "email_address": email_address }

        request = self._get_request()
        response = request.post(url + template_id, data)

        return Template(response["template"])

    def _add_remove_team_member(self, url, email_address=None, account_id=None):
        ''' Add or Remove a team member

        We use this function for two different tasks because they have the same
        API call

        Args:
            email_address (str): Email address of the Account to add/remove

            account_id (str): ID of the Account to add/remove

        Returns:
            A Team object

        '''

        if not email_address and not account_id:
            raise HSException("No email address or account_id specified")

        data = {}
        if account_id is not None:
            data = { "account_id": account_id }
        else:
            data = { "email_address": email_address }

        request = self._get_request()
        response = request.post(url, data)

        return Team(response["team"])
