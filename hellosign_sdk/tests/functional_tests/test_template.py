from hellosign_sdk.tests.functional_tests import BaseTestCase
from hellosign_sdk.resource import Team, ResourceList, Template
from hellosign_sdk.utils import Forbidden, NotFound
from time import time

import os

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
                team = self.client.add_team_member(email_address="demo+%s@example.com" % time())
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

    def test_create_embedded_template_draft(self):
        ''' Test creating an embedded Template draft '''

        files = [os.path.dirname(os.path.realpath(__file__)) + "/docs/nda.pdf"]
        signer_roles = [
            {'name': 'Baltar', 'order': 1},
            {'name': 'Madame President', 'order': 2},
            {'name': 'Lee Adama', 'order': 3},
        ]
        cc_roles = ['Deck Chief','Admiral','Starbuck']
        merge_fields = [{'name':'mymerge', 'type':'text'}]

        response = self.client.create_embedded_template_draft(
            client_id=self.client_id, 
            signer_roles=signer_roles, 
            test_mode=True, 
            files=files, 
            title='Battlestar Test Draft', 
            subject='There are cylons onboard', 
            message='Halp', 
            cc_roles=cc_roles, 
            merge_fields=merge_fields)

        self.assertTrue(isinstance(response, Template))

    def test_delete_template(self):
        '''Tests proper status code for template deletion'''

        # Note that we won't be actually deleting a template, but rather checking to make sure we get a 404 - Template not found error

        template_id = 'ax5d921d0d3ccfcd594d2b8c897ba774d89c9234' #random

        try:
            self.client.delete_template(template_id)
            self.fail('Expected failure, but got success')
        except NotFound:
            pass
        except BaseException as e:
            self.fail('Expected Not Found, but got %s' % e)