from bunk.action import BunkAction

class HttpTestAction (BunkAction):

    def __init__ (self, route_id, **kwargs):
        """
        Create a new ExampleArgsAction instance.

        @param sentence (str) The sentence to repeat to the client.
        """

        BunkAction.__init__(self, **kwargs)

        self._route_id = route_id

    # ------------------------------------------------------------------------------------------------------------------

    def get (self, client):
        """
        Handle a GET request

        @param client (HttpClient) The HttpClient instance.
        """

        # initialize and connect to database
        db     = self.init_db()
        dbconn = db.get_connection()
        dbcurs = dbconn.cursor()

        # grab records
        dbcurs.execute("SELECT * FROM test_tables LIMIT 1")

        record = db.fetch_one(dbcurs)

        # close db connection
        dbcurs.close()
        dbconn.close()

        client.compose_headers()
        client.write("GET Parameters: " + str(client.params) + "\n")
        client.write("DB Result: " + str(record))
        client.flush()

    # ------------------------------------------------------------------------------------------------------------------

    def post (self, client):
        """
        Handle a POST request
        """

        client.compose_headers()
        client.write("POST Parameters: " + str(client.params))
        client.flush()

    # ------------------------------------------------------------------------------------------------------------------

    def put (self, client):
        """
        Handle a PUT request
        """

        client.compose_headers()
        client.write("PUT Parameters: " + str(client.params))
        client.flush()
