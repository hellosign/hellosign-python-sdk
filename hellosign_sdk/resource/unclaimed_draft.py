from resource import Resource


class UnclaimedDraft(Resource):

    UNCLAIMED_DRAFT_SEND_DOCUMENT_TYPE = "send_document"
    UNCLAIMED_DRAFT_REQUEST_SIGNATURE_TYPE = "request_signature"

    """A group of documents that a user can take ownership of by going to the
    claim URL

    Comprises the following attributes:

        claim_url (str): The URL to be used to claim this UnclaimedDraft

        signing_redirect_url (str): The URL you want signers redirected to
            after they successfully sign.

        test_mode (bool): Whether this is a test draft. Signature requests
            made from test drafts have no legal value. Defaults to 0.

    """

    def __str__(self):
        ''' Return a string representation of this unclaimed draft '''
        return 'UnclaimedDraft %s' % self.claim_url
