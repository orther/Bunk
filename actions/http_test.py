from bunk.action import BunkAction

class HttpTestAction (BunkAction):

    def __init__ (self, test, **kwargs):
        """
        Create a new ExampleArgsAction instance.

        @param sentence (str) The sentence to repeat to the client.
        """

        BunkAction.__init__(self, **kwargs)

        self._test = test

    # ------------------------------------------------------------------------------------------------------------------

    def get (self, client):
        """
        Handle a GET request

        @param client (HttpClient) The HttpClient instance.
        """

        self.init_db()

        # create test table
        self.dbcursor.execute("CREATE TABLE test_table (test_table_id INT NOT NULL PRIMARY KEY, value VARCHAR(50) NOT NULL)")

        client.compose_headers()
        client.write("GET Parameters: " + str(client.params))
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
