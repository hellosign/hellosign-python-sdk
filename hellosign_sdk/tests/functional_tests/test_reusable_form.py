from unittest import TestCase
from hellosign_sdk.tests.test_helper import api_key
from hellosign_sdk.hsclient import HSClient
from hellosign_sdk.resource.team import Team
from hellosign_sdk.resource.reusable_form import ReusableForm
from hellosign_sdk.utils.exception import Forbidden, NotFound


class TestReusableForm(TestCase):

    def setUp(self):
        self.client = HSClient(api_key=api_key)

    def test_reusable_form(self):
        ''' Test reusable form methods '''
        # Get reusable form list, if there's any:
        # Add a user to our team, get the first one
        # if no team exist, create team
        # then add and remove a user from/to this reusableform
        # remove user from our team
        # destroy team
        rfl = self.client.get_reusable_form_list()
        self.assertTrue(isinstance(rfl, list))
        create_team = False
        if len(rfl) > 0:
            self.assertTrue(isinstance(rfl[0], ReusableForm))

            try:
                team = self.client.get_team_info()
            except NotFound:
                team = self.client.create_team("Team Name")
                self.assertTrue(isinstance(team, Team))
                self.assertEquals(team.name, "Team Name")
                create_team = True
            try:
                new_team = self.client.add_team_member("demo@example.com")
                self.assertTrue(isinstance(new_team, Team))
                team = new_team
                # self.assertTrue("demo@example.com" in [account["email_address"].encode('UTF8') for account in team.accounts])
            except Forbidden:
                pass
            rf = self.client.get_reusable_form(rfl[0].reusable_form_id)
            self.assertTrue(isinstance(rf, ReusableForm))

            try:
                rf = self.client.add_user_to_reusable_form(
                    rfl[0].reusable_form_id, None, "demo@example.com")
                self.assertTrue(isinstance(rf, ReusableForm))

                rf = self.client.remove_user_from_reusable_form(
                    rfl[0].reusable_form_id, None, "demo@example.com")
                self.assertTrue(isinstance(rf, ReusableForm))
            except Forbidden:
                pass
            new_team = self.client.remove_team_member("demo@example.com")
            self.assertTrue(isinstance(team, Team))
            self.assertFalse("demo@example" in [account["email_address"].encode('UTF8') for account in team.accounts])

            if create_team is True:
                result = self.client.destroy_team()
                self.assertTrue(result)
