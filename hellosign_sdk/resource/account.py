from resource import Resource


class Account(Resource):

    """Contains information about an account and its settings.

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

    """

    def __str__(self):
        ''' Return a string representation of this Account '''
        return 'Account %s (%s)' % (self.account_id, self.email_address)
