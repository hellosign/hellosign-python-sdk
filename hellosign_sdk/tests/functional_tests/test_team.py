from unittest import TestCase
from hellosign_sdk.tests.test_helper import api_key
from hellosign_sdk.hsclient import HSClient
from hellosign_sdk.resource.team import Team
from hellosign_sdk.utils.exception import NotFound, HSException, BadRequest, Forbidden


class TestTeam(TestCase):

    def setUp(self):
        self.client = HSClient(api_key=api_key)

    def test_add_team_member_with_invalid_info(self):
        try:
            self.client.add_team_member(email_address="in valid email")
        except BadRequest:
            pass

        try:
            self.client.add_team_member(account_id="in valid account_id")
        except NotFound:
            pass

    def test_team_functions(self):
        try:
            # You already in a team
            # save your old team name -> update new team name -> add member ->
            # remove member -> restore your old team name
            team = self.client.get_team_info()
            old_team_name = team.name

            try:
                result = self.client.destroy_team()
                self.assertTrue(result)
            except NotFound:
                pass

            team = self.client.create_team(old_team_name)
            self.assertEquals(team.name, old_team_name)

            team = self.client.update_team_name("New team name")
            self.assertEquals(isinstance(team, Team), True)

            try:
                team = self.client.add_team_member(
                    email_address="not_existed_user@example.com")
                self.assertEquals(isinstance(team, Team), True)
            except Forbidden:
                    pass
            try:
                self.client.add_team_member()
            except HSException:
                pass

            team = self.client.remove_team_member(
                email_address="not_existed_user@example.com")
            self.assertEquals(isinstance(team, Team), True)

            team = self.client.update_team_name(old_team_name)
            self.assertEquals(isinstance(team, Team), True)
        except NotFound:
            # You do not belong to any teams
            # create team -> add member, remove member, destroy team
            team = self.client.create_team("New team")
            self.assertEquals(team.name, "New team")

            team = self.client.add_team_member(
                email_address="not_existed_user@example.com")
            self.assertEquals(isinstance(team, Team), True)

            team = self.client.remove_team_member(
                email_address="not_existed_user@example.com")
            self.assertEquals(isinstance(team, Team), True)

            result = self.client.destroy_team()
            self.assertEquals(result, True)
