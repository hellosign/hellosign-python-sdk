from resource import Resource
from account import Account

class Team(Resource):
    ''' Contains information about your team and its members

    Comprises the following attributes:

        name (str): The name of your Team

        accounts (list of dict): A list of all Accounts belonging to your Team.
            Note that this response is a subset of the response parameters
            found in GET /account.

            account_id (str): The id of the Account
            email_address (str): The email address associated with the Account
            role_code (str): The membership role for the team. O = Owner,
                M = Member

        invited_accounts (str): A list of all Accounts that have an outstanding
            invitation to join your Team. Note that this response is a subset
            of the response parameters found in GET /account.

            account_id (str): The id of the Account
            email_address (str): The email address associated with the Account

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
        super(Team, self).__init__(jsonstr, key)
        if 'accounts' in self.json_data:
            acct_list = []
            for acct in self.accounts:
                acct_list.append(Account(acct))
            self.accounts = acct_list
        if 'invited_accounts' in self.json_data:
            acct_list = []
            for acct in self.invited_accounts:
                acct_list.append(Account(acct))
            self.invited_accounts = acct_list

    def __str__(self):
        ''' Return a string representation of this Team '''
        return 'Team %s' % self.name
