from bunk.action import BunkAction

class HttpTestAction (BunkAction):

    # ------------------------------------------------------------------------------------------------------------------
    # SQL
    # ------------------------------------------------------------------------------------------------------------------

    sql_get_http_test_record = """
    SELECT
        id, route_id, request_ip, created_at
    FROM
        http_test
    WHERE
        id = %s
    LIMIT 1
    """

    # ------------------------------------------------------------------------------------------------------------------

    sql_insert_http_test_record = """
    INSERT INTO http_test
        (id, route_id, request_ip, created_at)
    VALUES
        (%(id)i, %(route_id)s, %(request_ip)s, NOW())
    """

    # ------------------------------------------------------------------------------------------------------------------
    # METHODS
    # ------------------------------------------------------------------------------------------------------------------

    def __init__ (self, route_id, **kwargs):
        """
        Create a new ExampleArgsAction instance.

        @param route_id (str) Route identifier set as an argument in the route.
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

        # pull record
        dbcurs.execute(HttpTestAction.sql_get_http_test_record % client.params["id"])
        record = db.fetch_one(dbcurs)

        # close db connection
        dbcurs.close()
        dbconn.close()

        client.compose_headers()
        client.write("GET Parameters: " + str(client.params) + "\n")
        #client.write("DB Result: " + str(record))
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

        # initialize and connect to database
        db     = self.init_db()
        dbconn = db.get_connection()
        dbcurs = dbconn.cursor()

        # pull record
        sql_params = {"id":         clients.params["id"],
                      "route_id":   self._route_id,
                      "request_ip": "Fake For Now"}

        sql = HttpTestAction.sql_insert_http_test_record % client.params["id"]

        dbcurs.execute(sql)

        # close db connection
        dbcurs.close()
        dbconn.close()

        client.compose_headers()
        client.write("PUT Parameters: " + str(client.params) + "\n")
        #client.write("DB Result: " + str(record))
        client.flush()
