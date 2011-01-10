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

    def bunk_get (self):
        """
        Log a user out.
        """

        # remove session auth roles
        self.auth_empty_roles()

        # remove user details
        if self._client.session.get("user", False):
            del self._client.session["user"]

        # user successfully logged out
        return self.respond(True)
