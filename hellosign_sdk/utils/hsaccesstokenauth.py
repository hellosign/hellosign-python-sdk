from requests.auth import AuthBase


class HSAccessTokenAuth(AuthBase):
    """Authentication object using HelloSign's access token

    """

    def __init__(self, access_token, access_token_type, refresh_token=None,
                 expires_in=None, state=None):
        """Initialziation of the object

        Args:
            access_token (str): Access token
            access_token_type (str): Access token type
            refresh_token (str):
            expires_in (int): Seconds after which the token will expire
            state (str):

        """

        self.access_token = access_token
        self.access_token_type = access_token_type
        self.refresh_token = refresh_token
        self.expires_in = expires_in
        self.state = state

    def __call__(self, r):
        r.headers['Authorization'] = self.access_token + \
            ' ' + self.access_token_type
        return r
