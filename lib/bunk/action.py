import logging

from elements.http.action import HttpAction
from elements.http        import response_code

from bunk.core.exception import ResponseFormatException

from settings import logging_file
from settings import logging_level
from settings import logging_on
from settings import response_formatters

# ----------------------------------------------------------------------------------------------------------------------

class BunkAction (HttpAction):

    def __init__ (self, **kwargs):
        """
        Create a new HttpAction instance and setup logging if logging is turned on in the settings.
        """

        HttpAction.__init__(self, **kwargs)

        if logging_on:
            # setup logging if turned on
            logging.basicConfig(filename=logging_file, level=logging_level)

        self._format = None

    # ------------------------------------------------------------------------------------------------------------------

    def format_response_data (self, response_data):
        """
        Format response data to the set format. If no format has been set then the response data is converted to a
        string.

        @param response_data           (*) All data types are accepted. If response_data is of a type not supported by
                                           the response format set then a ResponseFormatException is raised.

        @return (str)
        """

        if self._format == None:
            return str(response_data)

        if self._format not in response_formatters.keys():
            raise ResponseFormatException("A response formatter is not registered for the set format: %s" % self._format)

        return response_formatters[self._format].format(response_data)

    # ------------------------------------------------------------------------------------------------------------------

    def init_db (self):
        """
        Import database module.

        @return (module) elements.model.database
        """

        from elements.model import database

        return database

    # ------------------------------------------------------------------------------------------------------------------

    def respond (self, client, response_data, format_response=True):
        """
        Return a full response to the request including headers and body. Response data is formated using the set
        format.

        @param client (HttpClient)    The HttpClient instance.
        @param response_data   (*)    All data types are accepted. If response_data is of a type not supported by the
                                      response format ResponseFormatException is raised.
        @param format_response (bool) If set to True the respopnse data will be formated by the set ResponseFormatter
        """

        # set format based on filed extension
        # TODO: Remove this and make a more robust format setter with uptimization setting.
        self._format = client.params["_file_ext"][1:]

        if format_response:
            # apply response format
            response = self.format_response_data(response_data)

        else:
            # do not format
            response = response_data

        client.compose_headers()

        if type(response) == str:
            client.write(response)

        client.flush()
