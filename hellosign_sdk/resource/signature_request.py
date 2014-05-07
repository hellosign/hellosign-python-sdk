from resource import Resource
from signature import Signature


class SignatureRequest(Resource):
    ''' Contains information regarding documents that need to be signed

    Comprises the following attributes:

        test_mode (bool): Whether this is a test signature request. Test requests have no legal value. Defaults to False.

        signature_request_id (str): The id of the SignatureRequest

        requester_email_address (str): The email address of the initiator of the SignatureRequest

        title (str): The title the specified Account uses for the SignatureRequest

        subject (str): The subject in the email that was initially sent to the signers

        message (str): The custom message in the email that was initially sent to the signers

        is_complete (bool): Whether or not the SignatureRequest has been fully executed by all signers

        has_error (bool): Whether or not an error occurred (either during the creation of the SignatureRequest or during one of the signings)

        files_url (str): The URL where a copy of the request's documents can be downloaded

        signing_url (str): The URL where a signer, after authenticating, can sign the documents

        details_url (str): The URL where the requester and the signers can view the current status of the SignatureRequest

        cc_email_addresses (list): A list of email addresses that were CCed on
            the SignatureRequest. They will receive a copy of the final PDF
            once all the signers have signed

        signing_redirect_url (str): The URL you want the signer redirected to after they successfully sign

        custom_fields (list of dict): An array of Custom Field objects
            containing the name and type of each custom field

            name (str): The name of the Custom Field
            type (str): The type of this Custom Field. Currently, `text` and `checkmark` are the only valid values

        response_data (list of dict): An array of form field objects containing
            the name, value, and type of each textbox or checkmark field filled
            in by the signers

            api_id (str): The unique ID for this field signature_id (str): The ID of the signature to which this response is linked
            name (str): The name of the form field
            value (str): The value of the form field
            type (str): The type of this form field

        signatures (list of dict): An array of signature objects, 1 for each signer

            signature_id (str): Signature identifier
            signer_email_address (str): The email address of the signer
            signer_name (str): The name of the signer
            order (str): If signer order is assigned this is the 0-based index for this signer
            status_code (str): The current status of the signature. eg: `awaiting_signature`, `signed`, `on_hold`
            signed_at (str): Time that the document was signed or null
            last_viewed_at (str): The time that the document was last viewed by this signer or null
            last_reminded_at (str): The time the last reminder email was sent to the signer or null
            has_pin (bool): Boolean to indicate whether this signature requires a PIN to access

    '''

    def __init__(self, jsonstr=None, key=None):
        ''' Initialization of the object

        Args:
            jsonstr (str): a raw JSON string that is returned by a request.
                We store all the data in `self.json_data` and use `__getattr__`
                and `__setattr__` to make the data accessible like attributes
                of the object
            key (str): Optional key to use with jsonstr. If `key` exists, we'll
                load the data of `jsonstr[key]` instead of the whole `jsonstr`
        '''
        super(SignatureRequest, self).__init__(jsonstr, key)
        if 'signatures' in self.json_data:
            signature_list = []
            for signature in self.signatures:
                signature_list.append(Signature(signature))
            self.signatures = signature_list

    def __str__(self):
        ''' Return a string representation of this Account '''
        return 'SignatureRequest %s' % self.signature_request_id

    def find_response_component(self, api_id=None, signature_id=None):
        ''' Find one or many repsonse components.

            Args:

                api_id (str):           Api id associated with the component(s) to be retrieved.

                signature_id (str):     Signature id associated with the component(s) to be retrieved.

            Returns:
                A list of dictionaries containing component data

        '''
        if not api_id and not signature_id:
            raise ValueError('At least one of api_id and signature_id is required')

        components = list()
        
        if self.response_data:
            for component in self.response_data:
                if (api_id and component['api_id']) == api_id or (signature_id and component['signature_id'] == signature_id):
                    components.append(component)

        return components

    def find_signature(self, signature_id=None, signer_email_address=None):
        ''' Return a signature for the given parameters

            Args:

                signature_id (str):             Id of the signature to retrieve.
                signer_email_address (str):     Email address of the associated signer for the signature to retrieve.

            Returns:
                A Signature object or None

        '''
        if self.signatures:
            for signature in self.signatures:
                if signature.signature_id == signature_id or signature.signer_email_address == signer_email_address: 
                    return signature
