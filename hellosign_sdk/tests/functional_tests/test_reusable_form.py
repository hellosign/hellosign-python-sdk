from unittest import TestCase
from hellosign_sdk.tests.test_helper import api_key
from hellosign_sdk.hsclient import HSClient
from hellosign_sdk.resource.team import Team
from hellosign_sdk.resource.resource_list import ResourceList
from hellosign_sdk.resource.reusable_form import ReusableForm
from hellosign_sdk.utils.exception import Forbidden, NotFound
from time import time


class TestReusableForm(TestCase):

    def setUp(self):
        self.client = HSClient(api_key=api_key)

    def _get_team(self):
        ''' Get or create the current team '''

        try:
            team = self.client.get_team_info()
        except NotFound:
            team = self.client.create_team("Team Name")
            self.assertTrue(isinstance(team, Team))
            self.assertEquals(team.name, "Team Name")

        if len(team.accounts) < 2:
            try:
                team = self.client.add_team_member("demo+%s@example.com" % time())
                self.assertTrue(isinstance(team, Team))
            except Forbidden:
                pass

        return team

    def _get_one_reusable_form(self):
        ''' Return one reusable form '''

        reusable_forms = self.client.get_reusable_form_list()
        self.assertTrue(isinstance(reusable_forms, ResourceList))
        self.assertTrue(len(reusable_forms) > 0, "CREATE A TEMPLATE BEFORE RUNNING THIS TEST")

        for reusable_form in reusable_forms:
            self.assertTrue(isinstance(reusable_form, ReusableForm))

        return reusable_form

    def test_reusable_form_list_and_get(self):
        ''' Test listing and retrieve reusable forms '''
        reusable_form = self._get_one_reusable_form()
        result = self.client.get_reusable_form(reusable_form.reusable_form_id)
        self.assertTrue(isinstance(result, ReusableForm))
        self.assertEquals(result.reusable_form_id, reusable_form.reusable_form_id)

    def test_add_remove_reusable_form_users(self):
        ''' Test adding and removing users from the reusable form '''

        team = self._get_team()
        reusable_form = self._get_one_reusable_form()
        rf_id = reusable_form.reusable_form_id
        email = team.accounts[-1].email_address

        try:
            r = self.client.add_user_to_reusable_form(rf_id, None, email)
            self.assertTrue(isinstance(r, ReusableForm))

            r = self.client.remove_user_from_reusable_form(rf_id, None, email)
            self.assertTrue(isinstance(r, ReusableForm))
        except Forbidden:
            pass
