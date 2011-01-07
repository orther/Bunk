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
    email     = Email("Email address", max=65, max_err="Too long! Max is %3")
    password  = Text("Password", min=8, min_err="Too short! Min is %3")
    username  = Text("Username", regex="^[a-zA-Z][a-zA-Z0-9]{3,23}$", regex_err="Invalid! Must be alphanumeric, can NOT begin with a number and between 4 and 24 characters long.")

    # statuses
    is_deleted = Boolean("Is Deleted")

    # dates
    date_created     = Datetime("Date Created", required=False)
    date_last_log_in = Datetime("Last Log In At", required=False)

class UserDBModel (DatabaseModel):

    model = UserModel
    table = "user"
