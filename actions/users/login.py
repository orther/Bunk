from datetime import datetime

from bunk.action                              import BunkAction
from bunk.response_formatters.json_formatter  import JsonFormatter

from models.user import UserDBModel

class UsersLoginAction (BunkAction):

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
        Authenticate a user and return user_id and set session cookie on success.
        """

        user            = UserDBModel()
        user.password   = "cocks4PASSES"
        user.username   = "dick"
        user.email      = "brandon.orther@gmail.com"

        print "Validated:", user.validate()
        print "Errors:", user.errors()

        # save the user
        user.save()

        print user.values()

        self.respond({"user_id": 1})
