from datetime import datetime

from elements.http import response_code

from bunk.action                             import BunkAction
from bunk.response_formatters.json_formatter import JsonFormatter

from models.user import UserDBModel

from settings import AUTH_ROLE_USER

# ----------------------------------------------------------------------------------------------------------------------
# RESPONSE ERROR CODES
# ----------------------------------------------------------------------------------------------------------------------

RESP_ERR_CODE_AUTHENTICATION_FAILED = 1
RESP_ERR_CODE_LOGIN_FAILED          = 2

# ----------------------------------------------------------------------------------------------------------------------

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
        Log a user in.

        @request_param username (str)
        @request_param password (str)

        @response user_id (int)
        """

        password_hash = UserDBModel.hash_password(self._client.params.get("password"))
        username      = self._client.params.get("username")

        try:
            users_filters = [
                ["username",      "=", username],
                ["password_hash", "=", password_hash],
                ["is_deleted",    "=", False]
            ]

            users = UserDBModel.filter(users_filters).limit(1)()

            if users:
                # user loaded
                user = users[0]

                # update last log in date
                user.date_last_log_in = "@NOW()"

                user.save()

                # store user details in session
                self._client.session["user_id"]  = user.user_id
                self._client.session["username"] = user.username
                self._client.session["email"]    = user.email

                # set session auth roles
                self.auth_set_roles((AUTH_ROLE_USER,))

            else:
                # failed to authenticate
                err_code = RESP_ERR_CODE_AUTHENTICATION_FAILED
                err_msg  = "Login credentials provided failed to authenticate."

                return self.respond_error(err_code, err_msg, response_code.HTTP_500)

        except Exception, e:
            print e
            # failed to log user in for unknown reason
            err_code = RESP_ERR_CODE_LOGIN_FAILED
            err_msg  = "User log in failed for unknown reason."

            return self.respond_error(err_code, err_msg, response_code.HTTP_500)

        # user successfully logged in
        return self.respond({"user_id": user.user_id}, response_code.HTTP_200)
