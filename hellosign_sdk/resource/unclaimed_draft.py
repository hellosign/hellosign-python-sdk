from .resource import Resource

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
