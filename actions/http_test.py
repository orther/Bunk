from bunk.action                              import BunkAction
from bunk.response_formatters.json_formatter  import JsonFormatter

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

    def _setup (self):
        """
        Set response formatter.
        """

        self._response_formatter = JsonFormatter

    # ------------------------------------------------------------------------------------------------------------------

    def bunk_get (self, client):
        """
        Return http_test record(s)
        """
        response = {}

        # initialize and connect to database
        db     = self.init_db()
        dbconn = db.get_connection()
        dbcurs = dbconn.cursor()

        # ab benchmarking
        if "id" in client.params and not client.params["id"] == "":
            # select a single record
            sql_query = HttpTestAction.sql_get_http_test_record % client.params["id"]

        else:
            # select all records
            sql_query = HttpTestAction.sql_get_all_http_test_records

        try:
            # pull record
            dbcurs.execute(sql_query)

            # benchmark testing
            response["items"] = db.fetch_all(dbcurs)

        except Exception, e:
            # return sql error details
            self.respond({"sql_error": e})

            return

        finally:
            # close db connection
            dbcurs.close()
            dbconn.close()

        # return resource
        self.respond(response)

    # ------------------------------------------------------------------------------------------------------------------

    def bunk_post (self, client):
        """
        Create a new http_test record and return the id.
        """

        # initialize and connect to database
        db     = self.get_db()
        dbconn = db.get_connection()
        dbcurs = dbconn.cursor()

        # insert record
        sql_params = {"id":         "NULL",
                      "route_id":   self._file_ext,
                      "request_ip": client.in_headers["REMOTE_ADDR"]}

        try:
            # attempt to insert new http_test record
            dbcurs.execute(HttpTestAction.sql_insert_http_test_record % sql_params)

            new_record_id = dbcurs.lastrowid

        except Exception, e:
            # return sql error details
            self.respond({"sql_error": e})

            return

        # close db connection
        dbcurs.close()
        dbconn.close()

        # return created record's id
        self.respond(new_record_id)

    # ------------------------------------------------------------------------------------------------------------------

    def bunk_put (self, client):
        """
        Create or update an http_test record.
        """

        # initialize and connect to database
        db     = self.get_db()
        dbconn = db.get_connection()
        dbcurs = dbconn.cursor()

        # insert record
        sql_params = {"id":         int(client.params["id"]),
                      "route_id":   self._file_ext,
                      "request_ip": client.in_headers["REMOTE_ADDR"]}

        try:
            # attempt to insert new http_test record
            dbcurs.execute(HttpTestAction.sql_insert_http_test_record % sql_params)

        except Exception, e:
            try:
                # assume insert failed due to duplicate entry so we update the existing record
                dbcurs.execute(HttpTestAction.sql_update_http_test_record % sql_params)

            except Exception, e:
                # return sql error details
                self.respond({"sql_error": e})

                return

        # close db connection
        dbcurs.close()
        dbconn.close()

        # return empty body on success
        self.respond(None, False)
