from resource import Resource


class Embedded(Resource):

    """An object that contains necessary information to set up embedded signing.

    Attributes:
        sign_url (str): URL of the signature page to display in the embedded
        iFrame

        expires_at (str): When the link expires

    """
