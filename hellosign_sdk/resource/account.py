from resource import Resource
from hellosign_sdk.utils import HSAccessTokenAuth

class Account(Resource):

    ''' Contains information about an account and its settings.

    Attributes:
        account_id (str): The id of the Account

        email_address (str): The email address associated with the Account

        is_paid_hs (bool) : If the user has a paid HelloSign license will
        return true

        is_paid_hf (bool): If the user has a paid HelloFax license will return
        true

        quotas (dict) : An object detailing remaining monthly quotas, which has
        the following attributes:
        templates_left (int): API templates remaining
        api_signature_requests_left (int): API signature requests remaining

        callback_url (str): The URL that HelloSign events will be POSTed to

        role_code (str): The membership role for the team. O = Owner, M = Member

    Examples:
        To print the account_id

        >>> from hsclient import HSClient
        >>> client = HSClient()
        >>> account = client.get_account_info()
        >>> print account.account_id

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
        super(Account, self).__init__(jsonstr, key)
        if self.json_data and 'oauth' in self.json_data:
            oauth = HSAccessTokenAuth.from_response(self.json_data['oauth'])
            self.json_data['oauth'] = oauth

    def __str__(self):
        ''' Return a string representation of this Account '''
        return 'Account %s (%s)' % (self.account_id, self.email_address)
