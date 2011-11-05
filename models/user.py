# This file is part of Bunk.
# Copyright (c) 2011 Brandon Orther. All rights reserved.
#
# The full license is available in the LICENSE file that was distributed with this source code.

from hashlib import md5

from elements.model.database import DatabaseModel
from elements.model.model    import Boolean
from elements.model.model    import Datetime
from elements.model.model    import Email
from elements.model.model    import Int
from elements.model.model    import Model
from elements.model.model    import Text

class UserModel (Model):

    # ids
    user_id = Int("ID", required=False)

    # details
    email         = Email("Email address", max=65, max_err="Too long! Max is %3")
    password      = Text("Password", min=8, min_err="Too short! Min is %3", read_only=True)
    password_hash = Text("Password Hash", required=False)
    username      = Text("Username", regex="^[a-zA-Z][a-zA-Z0-9]{3,23}$", regex_err="Invalid! Must be alphanumeric, can NOT begin with a number and between 4 and 24 characters long.")

    # statuses
    is_deleted = Boolean("Is Deleted", required=False)

    # dates
    date_created     = Datetime("Date Created", required=False)
    date_last_log_in = Datetime("Last Log In At", required=False)

# ----------------------------------------------------------------------------------------------------------------------

class UserDBModel (DatabaseModel):

    model = UserModel
    table = "user"

    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def hash_password (password):
        """
        Return the hash of a password.

        @param password (str)

        @return (str)
        """

        try:
            salt          = password[0] + password[7] + password[6] + password[0]
            password_hash = md5(salt + password).hexdigest()

        except:
            # failed to hash password
            return None

        return password_hash

    # ------------------------------------------------------------------------------------------------------------------

    def save (self, **kwargs):
        """
        Hash password before saving if set.

        @return (bool) True, upon success.
        """

        if self.password:
            self.password_hash = UserDBModel.hash_password(self.values()["password"])

        DatabaseModel.save(self, **kwargs)
