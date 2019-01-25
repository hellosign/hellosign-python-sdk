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


class ApiApp(Resource):
    ''' Contains information about an API App.

    Attributes:
        client_id (str): The API App's Client ID

        created_at (int): Unix timestamp of when the API App was created

        name (str): The name of the API App

        domain (str): The domain name associated with the API App

        callback_url (str) : The URL that HelloSign events will be POSTed to

        is_approved (bool): Indicates if the API App is approved

        owner_account (dict): Information about the API App owner

            account_id (str): The id of the Account

            email_address (str): The email address associated with the Account

        options (dict): Options that override the Account settings

            can_insert_everywhere (bool): Denotes if signers can "Insert Everywhere" when
            signing a document

        oauth (dict): Information about the API App's OAuth properties. Null if OAuth is
        not configured for the API App.

            callback_url (str): The URL that HelloSign OAuth events will be POSTed to

            secret (str): The API App's OAuth secret

            scopes (list): List of the API App's OAuth scopes

            charges_users (bool): Indicates whether the API App or the authorized user
            is billed for OAuth requests.

        white_labeling_options (dict): Customization options for the API App's signer page

    Examples:
        To print the client_id

        >>> from hsclient import HSClient
        >>> client = HSClient()
        >>> app = client.get_api_app_info()
        >>> print app.client_id

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
        super(ApiApp, self).__init__(jsonstr, key, warnings)

    def __str__(self):
        ''' Return a string representation of this Account '''
        return 'ApiApp %s (%s)' % (self.name, self.client_id)
