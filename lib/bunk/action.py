from elements.http.action import HttpAction
from elements.http        import response_code

from bunk.core.exception                         import BunkServerException
from bunk.response_formatters.response_formatter import ResponseFormatter


# ----------------------------------------------------------------------------------------------------------------------
# RESPONSE ERROR CODES
# ----------------------------------------------------------------------------------------------------------------------

RESP_ERR_CODE_ACCESS_DENIED = 70

# ----------------------------------------------------------------------------------------------------------------------

class BunkAction (HttpAction):

    def __init__ (self, server, file_ext=None, title="Method Not Allowed", response_code=response_code.HTTP_405):
        """
        Create a new BunkAction instance.

        @param server   (HttpServer) The HttpServer instance.
        @param file_ext (str)
        """

        self._client             = None
        self._file_ext           = file_ext
        self._response_formatter = ResponseFormatter
        self._server             = server
        self.__response_code     = response_code
        self.__title             = title

        self._setup()

    # ------------------------------------------------------------------------------------------------------------------

    def _setup (self):
        """
        This method can be overwritten in the inheriting action to allow for setup on a per action bases. I am currently
        using this to allow the response format to be set per action.
        """

        return

    # ------------------------------------------------------------------------------------------------------------------

    def auth_empty_roles (self):
        """
        Remove any authenticated roles.
        """

        self._client.session["__auth_roles__"] = None

        del self._client.session["__auth_roles__"]

    # ------------------------------------------------------------------------------------------------------------------

    @property
    def auth_roles (self):
        """
        Retrieve authenticated roles.

        @return (tuple)
        """

        return self._client.session.get("__auth_roles__", ())

    # ------------------------------------------------------------------------------------------------------------------

    def auth_set_roles (self, auth_roles):
        """
        Set the authenticated roles.

        @param auth_roles (tuple) A tuple of roles associated with this session.
        """

        if type(auth_roles) == tuple:
            self._client.session["__auth_roles__"] = auth_roles

            return

        raise BunkServerException("Invalid auth roles: %s" % auth_roles)

    # ------------------------------------------------------------------------------------------------------------------

    def bunk_connect (self, client):
        """
        Handle a CONNECT request.
        """

        self._client.response_code = self.__response_code

        self.respond(self.__title)

    # ------------------------------------------------------------------------------------------------------------------

    def bunk_delete (self, client):
        """
        Handle a DELETE request.
        """

        self._client.response_code = self.__response_code

        self.respond(self.__title)

    # ------------------------------------------------------------------------------------------------------------------

    def bunk_get (self, client):
        """
        Handle a GET request.
        """

        self._client.response_code = self.__response_code

        self.respond(self.__title)

    # ------------------------------------------------------------------------------------------------------------------

    def bunk_head (self, client):
        """
        Handle a HEAD request.
        """

        self._client.response_code = self.__response_code

        self.respond(self.__title)

    # ------------------------------------------------------------------------------------------------------------------

    def bunk_options (self, client):
        """
        Handle a OPTIONS request.
        """

        self._client.response_code = self.__response_code

        self.respond(self.__title)

    # ------------------------------------------------------------------------------------------------------------------

    def bunk_post (self, client):
        """
        Handle a POST request.
        """

        self._client.response_code = self.__response_code

        self.respond(self.__title)

    # ------------------------------------------------------------------------------------------------------------------

    def bunk_put (self, client):
        """
        Handle a PUT request.
        """

        self._client.response_code = self.__response_code

        self.respond(self.__title)

    # ------------------------------------------------------------------------------------------------------------------

    def bunk_trace (self, client):
        """
        Handle a TRACE request.
        """

        self._client.response_code = self.__response_code

        self.respond(self.__title)

    # ------------------------------------------------------------------------------------------------------------------

    def connect (self, client):
        """
        Handle a CONNECT request and pass it to bunk_connect.

        @param client (HttpClient) The HttpClient instance.
        """

        self._client = client

        self.bunk_connect(client)

    # ------------------------------------------------------------------------------------------------------------------

    def delete (self, client):
        """
        Handle a DELETE request and pass it to bunk_delete.

        @param client (HttpClient) The HttpClient instance.
        """

        self._client = client

        self.bunk_delete(client)

    # ------------------------------------------------------------------------------------------------------------------

    def get (self, client):
        """
        Handle a GET request and pass it to bunk_get.

        @param client (HttpClient) The HttpClient instance.
        """

        self._client = client

        self.bunk_get(client)

    # ------------------------------------------------------------------------------------------------------------------

    def head (self, client):
        """
        Handle a HEAD request and pass it to bunk_head.

        @param client (HttpClient) The HttpClient instance.
        """

        self._client = client

        self.bunk_head(client)

    # ------------------------------------------------------------------------------------------------------------------

    def get_db (self):
        """
        Import database module and return it.

        @return (module) elements.model.database
        """

        from elements.model import database

        return database

    # ------------------------------------------------------------------------------------------------------------------

    def options (self, client):
        """
        Handle a OPTIONS request and pass it to bunk_options.

        @param client (HttpClient) The HttpClient instance.
        """

        self._client = client

        self.bunk_options(client)

    # ------------------------------------------------------------------------------------------------------------------

    def post (self, client):
        """
        Handle a POST request and pass it to bunk_post.

        @param client (HttpClient) The HttpClient instance.
        """

        self._client = client

        self.bunk_post(client)

    # ------------------------------------------------------------------------------------------------------------------

    def put (self, client):
        """
        Handle a PUT request pass it to bunk_put.

        @param client (HttpClient) The HttpClient instance.
        """

        self._client = client

        self.bunk_put(client)

    # ------------------------------------------------------------------------------------------------------------------

    def respond (self, response_data, http_response_code=None, format_response=True):
        """
        Return a full response to the request including headers and body. Response data is formated using the set
        response formatter. If an http_response_code is provide it is set before the headers are composed.

        @param response_data
        @param http_response_code (str)
        @param format_response    (bool) If set to True the respopnse data will be formated by ResponseFormatter
        """

        # apply response format
        response = self._response_formatter.format(response_data)

        if not http_response_code == None:
            # set HTTP response code
            self._client.response_code = http_response_code

        self._client.compose_headers()

        if type(response) == str:
            self._client.write(response)

        self._client.flush()

    # ------------------------------------------------------------------------------------------------------------------

    def respond_access_denied (self):
        """
        Return an error response indicating that access has been denied.
        """

        err_code = RESP_ERR_CODE_ACCESS_DENIED
        err_msg  = "Access denied."

        return self.respond_error(err_code, err_msg, response_code.HTTP_403)

    # ------------------------------------------------------------------------------------------------------------------

    def respond_error (self, error_code, error_message, http_response_code, error_data=None, field_errors=None):
        """
        Return an error response to the request including headers and body. Response data is formated using the set
        formatter. The HTTP response code is set before the headers are composed.

        NOTE: This method is in place to assert a structure for all error data being returned by bunk web service.

        @param error_code         (int)
        @param error_message      (int)
        @param http_response_code (str)
        @param error_data         (dict)
        @param field_errors       (list) A list containing field specific errors. Each field error item is a tuple with
                                         the first item being the field name and the second item being field error data.
                                         Example: [('username', 'Already in use!'), ('password', 'Too short!')]
        """

        response_data = {"error_data": {"code":    error_code,
                                        "message": error_message}}

        if not error_data == None:
            response_data["error_data"]["data"] = error_data

        if not field_errors == None:
            response_data["error_data"]["field_errors"] = field_errors

        # apply response format
        response = self._response_formatter.format(response_data)

        # set HTTP response code
        self._client.response_code = http_response_code

        self._client.compose_headers()

        if type(response) == str:
            self._client.write(response)

        self._client.flush()

    # ------------------------------------------------------------------------------------------------------------------

    def trace (self, client):
        """
        Handle a TRACE request pass it to bunk_trace.

        @param client (HttpClient) The HttpClient instance.
        """

        self._client = client

        self.bunk_trace(client)

# ----------------------------------------------------------------------------------------------------------------------

class SecureBunkAction (HttpAction):

    def get (self, client):
        """
        Handle a GET request and pass it to bunk_get.

        @param client (HttpClient) The HttpClient instance.
        """

        self._client = client

        self.bunk_get()
