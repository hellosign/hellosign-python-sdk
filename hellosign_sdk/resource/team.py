from resource import Resource


class Team(Resource):
    """Contains information about your team and its members

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

    """
