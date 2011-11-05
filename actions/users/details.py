# This file is part of Bunk.
# Copyright (c) 2011 Brandon Orther. All rights reserved.
#
# The full license is available in the LICENSE file that was distributed with this source code.

from elements.http import response_code

from bunk.action                             import SecureBunkAction
from bunk.response_formatters.json_formatter import JsonFormatter

from models.user import UserDBModel

from settings import AUTH_ROLE_USER
from settings import AUTH_ROLE_ADMIN

# ----------------------------------------------------------------------------------------------------------------------
# RESPONSE ERROR CODES
# ----------------------------------------------------------------------------------------------------------------------

RESP_ERR_CODE_ACCESS_DENIED = 1

RESP_ERR_CODE_USER_DETAILS_FAILED = 2
RESP_ERR_CODE_USER_DOES_NOT_EXIST = 3

# ----------------------------------------------------------------------------------------------------------------------

class UsersDetailsAction (SecureBunkAction):

    # ------------------------------------------------------------------------------------------------------------------
    # METHODS
    # ------------------------------------------------------------------------------------------------------------------

    def _setup (self):
        """
        Setup action.
        """

        self._response_formatter = JsonFormatter

        # set allowed auth roles
        self.set_allowed_auth_roles((AUTH_ROLE_USER, AUTH_ROLE_ADMIN))

    # ------------------------------------------------------------------------------------------------------------------

    def bunk_get (self, client):
        """
        Retrieve details for a user.

        @request_param username (str)

        @response user_id  (int)
        @response username (int)
        @response email    (int)
        """

        is_admin = AUTH_ROLE_ADMIN in self.auth_roles

        try:
            users_filters = [
                ["username",      "=", client.params.get("username")],
                ["is_deleted",    "=", False]
            ]

            users = UserDBModel.filter(users_filters).limit(1)()

            if users:
                user = users[0]

                if is_admin or user.user_id == client.session.get("user_id"):
                    # build reponse
                    response = {
                        "user_id":  user.user_id,
                        "username": user.username,
                        "email":    user.email
                    }

                    # return user details
                    return self.respond(response, response_code.HTTP_200)

            else:
                # failed to load user
                if is_admin:
                    err_code = RESP_ERR_CODE_USER_DOES_NOT_EXIST
                    err_msg  = "User does not exist."

                    return self.respond_error(err_code, err_msg, response_code.HTTP_404)

            # return access denied message
            return self.respond_access_denied()

        except Exception, e:
            # allow admin failed to log user in for unknown reason
            err_code = RESP_ERR_CODE_USER_DETAILS_FAILED
            err_msg  = "User failed to load for unknown reason."

            return self.respond_error(err_code, err_msg, response_code.HTTP_500)
