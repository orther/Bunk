# This file is part of Bunk.
# Copyright (c) 2011 Brandon Orther. All rights reserved.
#
# The full license is available in the LICENSE file that was distributed with this source code.

from elements.http import response_code

from bunk.action                             import BunkAction
from bunk.response_formatters.json_formatter import JsonFormatter

# ----------------------------------------------------------------------------------------------------------------------

class UsersLogoutAction (BunkAction):

    # ------------------------------------------------------------------------------------------------------------------
    # METHODS
    # ------------------------------------------------------------------------------------------------------------------

    def _setup (self):
        """
        Setup action.
        """

        self._response_formatter = JsonFormatter

    # ------------------------------------------------------------------------------------------------------------------

    def bunk_get (self, client):
        """
        Log a user out.
        """

        # remove session auth roles
        self.auth_empty_roles()

        # remove user details
        if client.session.get("email", False):
            del client.session["email"]

        if client.session.get("user_id", False):
            del client.session["user_id"]

        if client.session.get("username", False):
            del client.session["username"]

        # user successfully logged out
        return self.respond(True)
