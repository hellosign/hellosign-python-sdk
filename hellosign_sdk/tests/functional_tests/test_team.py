from unittest import TestCase
from hellosign_sdk.tests.test_helper import api_key
from hellosign_sdk.hsclient import HSClient
from hellosign_sdk.resource.team import Team
from hellosign_sdk.utils.exception import NotFound, HSException, BadRequest
from time import time

class TestTeam(TestCase):

    def setUp(self):
        self.client = HSClient(api_key=api_key)
        try:
            self.client.get_team_info()
        except NotFound:
            self.client.create_team("Test Team - Py SDK")

    def _destroy_team(self):
        ''' Destroy the current team '''
        team = self.client.get_team_info()

        # Remove non-admins
        for acct in team.accounts:
            if acct.role_code.lower() != 'a':
                try:
                    self.client.remove_team_member(email_address=acct.email_address)
                except HSException, e:
                    self.fail('Could not remove team member: %s' % e.message)

        # Destroy team
        try:
            self.client.destroy_team()
        except HSException, e:
            self.fail(e.message)

    def test_add_team_member(self):
        ''' Test adding a new team member '''

        team = self.client.get_team_info()
        num_members = len(team.accounts)

        # Invalid
        try:
            self.client.add_team_member(email_address="invalid email")
            self.fail("NotFound was expected")
        except BadRequest:
            pass
        try:
            self.client.add_team_member(account_id="invalid account_id")
            self.fail("NotFound was expected")
        except NotFound:
            pass

        # Valid
        result = self.client.add_team_member(email_address="py-sdk-test-%s@example.com" % time())
        self.assertTrue(isinstance(result, Team))
        self.assertEquals(len(result.accounts), num_members + 1)

    def test_remove_team_member(self):
        ''' Test removing a team member '''
        try:
            self.client.remove_team_member(email_address="not_existed_user@example.com")
            self.fail('NotFound was expected')
        except NotFound:
            pass

        team = self.client.get_team_info()
        email_address = None
        for acct in team.accounts:
            if acct.role_code.lower() != 'a':
                email_address = acct.email_address
                break

        if email_address:
            try:
                self.client.remove_team_member(email_address=email_address)
            except HSException, e:
                self.fail(e.message)
        else:
            pass # Nothing to do, already tested as part of test_team_destroy

    def test_create_team(self):
        ''' Test creating a new team '''

        team_name = "Test team - Python SDK"
        
        try:
            self.client.get_team_info()
            try:
                self.client.create_team(team_name)
                self.fail('BadRequest was expected')
            except BadRequest, e:
                self.assertTrue(e.message.lower().find('already have a team') > 0, "'%s' does not contain 'already have a team" % e.message)
                self._destroy_team()
        except NotFound:
            pass

        try:
            result = self.client.create_team(team_name)
            self.assertTrue(isinstance(result, Team))
            self.assertEquals(result.name, team_name)
        except HSException, e:
            self.fail('Could not destroy team: %s' % e.message)

    def test_get_team(self):
        ''' Test getting team info '''
        result = self.client.get_team_info()
        self.assertTrue(isinstance(result, Team))

    def test_update_team(self):
        ''' Test updating the team name '''
        try:
            new_name = 'New team name'
            result = self.client.update_team_name(new_name)
            self.assertTrue(isinstance(result, Team))
            self.assertEquals(result.name, new_name)
        except HSException, e:
            self.fail(e.message)

    def test_team_destroy(self):
        ''' Test deleting the current team '''

        team = self.client.get_team_info()

        num_members = 0
        if team:
            for acct in team.accounts:
                if acct.role_code.lower() != 'a':
                    num_members += 1

        if num_members > 0:
            # Has members - can't destroy
            try:
                self.client.destroy_team()
                self.fail("BadRequest was expected")
            except BadRequest:
                pass

        self._destroy_team()
