from elements.http.action import HttpAction
from elements.http        import response_code

from bunk.response_formatters.response_formatter import ResponseFormatter

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

        # unhandle request method defaults
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

    def bunk_connect (self):
        """
        Handle a CONNECT request.
        """

        self._client.response_code = self.__response_code

        self.respond(self.__title)

    # ------------------------------------------------------------------------------------------------------------------

    def bunk_delete (self):
        """
        Handle a DELETE request.
        """

        self._client.response_code = self.__response_code

        self.respond(self.__title)

    # ------------------------------------------------------------------------------------------------------------------

    def bunk_get (self):
        """
        Handle a GET request.
        """

        self._client.response_code = self.__response_code

        self.respond(self.__title)

    # ------------------------------------------------------------------------------------------------------------------

    def bunk_head (self):
        """
        Handle a HEAD request.
        """

        self._client.response_code = self.__response_code

        self.respond(self.__title)

    # ------------------------------------------------------------------------------------------------------------------

    def bunk_options (self):
        """
        Handle a OPTIONS request.
        """

        self._client.response_code = self.__response_code

        self.respond(self.__title)

    # ------------------------------------------------------------------------------------------------------------------

    def bunk_post (self, **kwargs):
        """
        Handle a POST request.
        """

        self._client.response_code = self.__response_code

        self.respond(self.__title)

    # ------------------------------------------------------------------------------------------------------------------

    def bunk_put (self):
        """
        Handle a PUT request.
        """

        self._client.response_code = self.__response_code

        self.respond(self.__title)

    # ------------------------------------------------------------------------------------------------------------------

    def bunk_trace (self):
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

        self.bunk_connect()

    # ------------------------------------------------------------------------------------------------------------------

    def delete (self, client):
        """
        Handle a DELETE request and pass it to bunk_delete.

        @param client (HttpClient) The HttpClient instance.
        """

        self._client = client

        self.bunk_delete()

    # ------------------------------------------------------------------------------------------------------------------

    def get (self, client):
        """
        Handle a GET request and pass it to bunk_get.

        @param client (HttpClient) The HttpClient instance.
        """

        self._client = client

        self.bunk_get()

    # ------------------------------------------------------------------------------------------------------------------

    def head (self, client):
        """
        Handle a HEAD request and pass it to bunk_head.

        @param client (HttpClient) The HttpClient instance.
        """

        self._client = client

        self.bunk_head()

    # ------------------------------------------------------------------------------------------------------------------

    def init_db (self):
        """
        Import database module.

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

        self.bunk_options()

    # ------------------------------------------------------------------------------------------------------------------

    def post (self, client):
        """
        Handle a POST request and pass it to bunk_post.

        @param client (HttpClient) The HttpClient instance.
        """

        self._client = client

        self.bunk_post()

    # ------------------------------------------------------------------------------------------------------------------

    def put (self, client):
        """
        Handle a PUT request pass it to bunk_put.

        @param client (HttpClient) The HttpClient instance.
        """

        self._client = client

        self.bunk_put()

    # ------------------------------------------------------------------------------------------------------------------

    def respond (self, response_data, format_response=True):
        """
        Return a full response to the request including headers and body. Response data is formated using the set
        response formatter.

        @param response_data
        @param format_response (bool) If set to True the respopnse data will be formated by ResponseFormatter
        """

        # apply response format
        response = self._response_formatter.format(response_data)

        self._client.compose_headers()

        if type(response) == str:
            self._client.write(response)

        self._client.flush()

    # ------------------------------------------------------------------------------------------------------------------

    def respond_error (self, error_code, error_message="", error_data=None, format_response=True):
        """
        Return an error response to the request including headers and body. Response data is formated using the set
        format.

        @param error_code      (int)
        @param error_code      (int)
        @param error_data      (*)          All data types are accepted. If response_data is of a type not supported by
                                            the response format ResponseFormatException is raised.
        @param format_response (bool)       If set to False the respopnse data will NOT be formated by ResponseFormatter
        """

        response_data = {"error_data": {"code":    error_code,
                                        "message": error_message,
                                        "data":    error_data}}

        # apply response format
        response = self._response_formatter.format(response_data)

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

        self.bunk_trace()
