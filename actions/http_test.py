from bunk.action import BunkAction

class HttpTestAction (BunkAction):

    # ------------------------------------------------------------------------------------------------------------------
    # SQL
    # ------------------------------------------------------------------------------------------------------------------

    sql_delete_http_test_record = """
    DELETE FROM http_test
    WHERE
        id = %s
    """

    # ------------------------------------------------------------------------------------------------------------------

    sql_get_all_http_test_records = """
    SELECT
        id, route_id, request_ip, DATE_FORMAT(created_at, '%H:%i:%s %W %M %Y') as created
    FROM
        http_test
    """

    # ------------------------------------------------------------------------------------------------------------------

    sql_get_http_test_record = """
    SELECT
        id, route_id, request_ip, DATE_FORMAT(created_at, '%%H:%%i:%%s %%W %%M %%Y') as created_at
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
        (%(id)s, "%(route_id)s", "%(request_ip)s", NOW())
    """

    # ------------------------------------------------------------------------------------------------------------------

    sql_update_http_test_record = """
    UPDATE http_test
    SET
        route_id   = "%(route_id)s",
        request_ip = "%(request_ip)s"
    WHERE
        id = %(id)s
    """

    # ------------------------------------------------------------------------------------------------------------------
    # METHODS
    # ------------------------------------------------------------------------------------------------------------------

    def __init__ (self, file_ext=None, **kwargs):
        """
        Create a new ExampleArgsAction instance.

        @param route_id (str) Route identifier set as an argument in the route.
        """

        BunkAction.__init__(self, **kwargs)

        self._file_ext = file_ext

        # TODO: set this static for now for testing
        self._format = "json"

    # ------------------------------------------------------------------------------------------------------------------

    def get (self, client):
        """
        Return http_test record(s)
        """
        response = {}

        # initialize and connect to database
        db     = self.init_db()
        dbconn = db.get_connection()
        dbcurs = dbconn.cursor()

        if "id" in client.params:
            # select a single record
            sql_query = HttpTestAction.sql_get_http_test_record % client.params["id"]

        else:
            # select all records
            sql_query = HttpTestAction.sql_get_all_http_test_records

        try:
            # pull record
            dbcurs.execute(sql_query)

            response["items"] = db.fetch_all(dbcurs)

        except Exception, e:
            # return sql error details
            self.respond(client, {"sql_error": e})

            return

        finally:
            # close db connection
            dbcurs.close()
            dbconn.close()

        # return resource
        self.respond(client, response)

    # ------------------------------------------------------------------------------------------------------------------

    def post (self, client):
        """
        Create a new http_test record and return the id.
        """

        # initialize and connect to database
        db     = self.init_db()
        dbconn = db.get_connection()
        dbcurs = dbconn.cursor()

        # insert record
        sql_params = {"id":         "NULL",
                      "route_id":   self._route_id,
                      "request_ip": "Fake For Now"}

        try:
            # attempt to insert new http_test record
            dbcurs.execute(HttpTestAction.sql_insert_http_test_record % sql_params)

            new_record_id = dbcurs.lastrowid

        except Exception, e:
            # return sql error details
            self.respond(client, {"sql_error": e})

            return

        # close db connection
        dbcurs.close()
        dbconn.close()

        # return created record's id
        self.respond(client, new_record_id)

    # ------------------------------------------------------------------------------------------------------------------

    def put (self, client):
        """
        Create or update an http_test record.
        """

        # initialize and connect to database
        db     = self.init_db()
        dbconn = db.get_connection()
        dbcurs = dbconn.cursor()

        # insert record
        sql_params = {"id":         int(client.params["id"]),
                      "route_id":   self._route_id,
                      "request_ip": "Fake For Now"}

        try:
            # attempt to insert new http_test record
            dbcurs.execute(HttpTestAction.sql_insert_http_test_record % sql_params)

        except Exception, e:
            try:
                # assume insert failed due to duplicate entry so we update the existing record
                dbcurs.execute(HttpTestAction.sql_update_http_test_record % sql_params)

            except Exception, e:
                # return sql error details
                self.respond(client, {"sql_error": e})

                return

        # close db connection
        dbcurs.close()
        dbconn.close()

        # return empty body on success
        self.respond(client, None, False)
