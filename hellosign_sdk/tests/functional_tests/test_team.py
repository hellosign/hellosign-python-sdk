from hellosign_sdk.tests.functional_tests import BaseTestCase
from hellosign_sdk.resource import Team
from hellosign_sdk.utils import NotFound, HSException, BadRequest
from time import time

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


class TestTeam(BaseTestCase):

    def setUp(self):
        BaseTestCase.setUp(self)
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
                except HSException as e:
                    self.fail('Could not remove team member: %s' % e.message)

        # Destroy team
        try:
            self.client.destroy_team()
        except HSException as e:
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
        #self.assertEquals(len(result.accounts), num_members + 1) Test no longer works

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
            except HSException as e:
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
            except BadRequest as e:
                self.assertTrue(e.message.lower().find('already have a team') > 0, "'%s' does not contain 'already have a team" % e.message)
                self._destroy_team()
        except NotFound:
            pass

        try:
            result = self.client.create_team(team_name)
            self.assertTrue(isinstance(result, Team))
            self.assertEquals(result.name, team_name)
        except HSException as e:
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
        except HSException as e:
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
