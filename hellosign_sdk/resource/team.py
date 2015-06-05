from .resource import Resource
from .account import Account

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

class Team(Resource):
    ''' Contains information about your team and its members

    Comprises the following attributes:

        name (str): The name of your Team

        accounts (list of dict): A list of all Accounts belonging to your Team.
            Note that this response is a subset of the response parameters
            found in GET /account.

            account_id (str): The id of the Account
            email_address (str): The email address associated with the Account
            role_code (str): The membership role for the team. 
                a = Admin,
                m = Member
                d = Developer

        invited_accounts (str): A list of all Accounts that have an outstanding
            invitation to join your Team. Note that this response is a subset
            of the response parameters found in GET /account.

            account_id (str): The id of the Account
            email_address (str): The email address associated with the Account

    '''

    def __init__(self, jsonstr=None, key=None, warnings=None):
        ''' Initialization of the object

        Args:
            jsonstr (str): a raw JSON string that is returned by a request.
                We store all the data in `self.json_data` and use `__getattr__`
                and `__setattr__` to make the data accessible like attributes
                of the object
            key (str): Optional key to use with jsonstr. If `key` exists, we'll
                load the data of `jsonstr[key]` instead of the whole `jsonstr`
            warnings (list): List of associated warnings
        '''
        super(Team, self).__init__(jsonstr, key, warnings)
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
