from datetime import datetime

from elements.core.exception import DatabaseModelException
from elements.http           import response_code

from bunk.action                              import BunkAction
from bunk.response_formatters.json_formatter  import JsonFormatter

from models.user import UserDBModel

from settings import app_url_base

# ----------------------------------------------------------------------------------------------------------------------
# RESPONSE ERROR CODES
# ----------------------------------------------------------------------------------------------------------------------

RESP_ERR_CODE_USER_DETAILS_INVALID    = 1
RESP_ERR_CODE_USER_CREATION_FAILED    = 2
RESP_ERR_CODE_USERNAME_ALREADY_IN_USE = 3

# ----------------------------------------------------------------------------------------------------------------------

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
        Create a user and return user_id.

        @request_param username (str)
        @request_param password (str)
        @request_param email    (str)

        @response user_id (int)
        """

        user = UserDBModel()

        user.email    = self._client.params.get("email")
        user.password = str(self._client.params.get("password"))
        user.username = self._client.params.get("username")

        if user.validate():
            try:
                # get db connection and cursor
                db     = self.get_db()
                dbconn = db.get_connection()
                dbcurs = dbconn.cursor()

                # check if user exists
                existing_user = UserDBModel.filter([["username", "=", user.username]])()

                if existing_user:
                    # user exists
                    err_code   = RESP_ERR_CODE_USERNAME_ALREADY_IN_USE
                    err_msg    = "Username already in use."
                    field_errs = [('username', 'Username already in use. Please select another one.')]

                    return self.respond_error(err_code, err_msg, response_code.HTTP_409, field_errors=field_errs)

                # create user
                user.save(connection=dbconn)

                # retrieve newely created user_id
                dbcurs.execute("SELECT CURRVAL('user_user_id_seq') AS value")

                user.user_id = db.fetch_all(dbcurs)[0]["value"]

            except Exception, e:
                # failed to create user for unknown reason
                err_code = RESP_ERR_CODE_USER_CREATION_FAILED
                err_msg  = "User failed to create for unknown reason."

                return self.respond_error(err_code, err_msg, response_code.HTTP_500)

        else:
            # validation errors
            err_code   = RESP_ERR_CODE_USER_DETAILS_INVALID
            err_msg    = "One of more user detail(s) are invalid and must be fixed."
            field_errs = user.errors().items()

            return self.respond_error(err_code, err_msg, response_code.HTTP_400, field_errors=field_errs)

        # user successfully created
        self._client.out_headers["Location"] = "%s/users/%s.json" % (app_url_base, user.user_id)

        return self.respond({"user_id": user.user_id}, response_code.HTTP_201)
