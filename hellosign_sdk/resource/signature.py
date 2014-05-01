from resource import Resource


class Signature(Resource):

    """Contains information regarding signatures

    Comprises the following attributes:

    signed_at (str):
    last_viewed_at (str):
    status_code (str):
    has_pin (bool):
    signer_email_address (str):
    signer_name (str):
    last_reminded_at (str):
    signature_id (str):
    order (str):


    """

    def __str__(self):
        ''' Return a string representation of this Signature '''
        return 'Signature %s' % self.signature_id
