from elements.http.action import HttpAction

class BunkAction (HttpAction):
    """
    Base Action for all classes to inherit.
    """

    def init_db (self):
        """
        Initialize the Database connection.
        """

        import settings
        from elements.model import database

        database.init()

        dbconn = None

        # get a database connection and cursor
        self.dbconn   = database.get_connection()
        self.dbcursor = dbconn.cursor()
