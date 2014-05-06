from hellosign_sdk.tests.functional_tests import BaseTestCase
from hellosign_sdk.resource import Team, ResourceList, Template
from hellosign_sdk.utils import Forbidden, NotFound
from time import time


class TestTemplate(BaseTestCase):

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

    def _get_one_template(self):
        ''' Return one template from the current account '''

        templates = self.client.get_template_list()
        self.assertTrue(isinstance(templates, ResourceList))
        self.assertTrue(len(templates) > 0, "CREATE A TEMPLATE BEFORE RUNNING THIS TEST")

        for template in templates:
            self.assertTrue(isinstance(template, Template))

        return template

    def test_template_list_and_get(self):
        ''' Test listing and retrieve templates '''
        template = self._get_one_template()
        result = self.client.get_template(template.template_id)
        self.assertTrue(isinstance(result, Template))
        self.assertEquals(result.template_id, template.template_id)

    def test_add_remove_template_users(self):
        ''' Test adding and removing users from a template '''

        team = self._get_team()
        template = self._get_one_template()
        template_id = template.template_id
        email = team.accounts[-1].email_address

        try:
            t = self.client.add_user_to_template(template_id, None, email)
            self.assertTrue(isinstance(t, Template))

            t = self.client.remove_user_from_template(template_id, None, email)
            self.assertTrue(isinstance(t, Template))
        except Forbidden:
            pass
