from datetime import datetime

from bunk.action                              import BunkAction
from bunk.response_formatters.json_formatter  import JsonFormatter

from models.user import UserDBModel

class UsersCreateAction (BunkAction):

    # ------------------------------------------------------------------------------------------------------------------
    # METHODS
    # ------------------------------------------------------------------------------------------------------------------

    def _setup (self):
        """
        Setup action.
        """

        self._response_formatter = JsonFormatter

    # ------------------------------------------------------------------------------------------------------------------

    def bunk_post (self):
        """
        Create a user.
        """

        user = UserDBModel()

        user.password = self._client.params.get("password")
        user.username = self._client.params.get("username")
        user.email    = self._client.params.get("email")

        print user.validate()
        print "Errors:", user.errors()

        # save the user
        #user.save()

        #print user.values()

        #self.respond({"user_id": 1})
