import logging

from elements.http.action import HttpAction
from elements.http        import response_code

from settings import logging_file
from settings import logging_level
from settings import logging_on

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
        Import database module.

        @return (module) elements.model.database
        """


    # ------------------------------------------------------------------------------------------------------------------

    def init_db (self):
        """
        Import database module.

        @return (module) elements.model.database
        """

        from elements.model import database

        return database

    # ------------------------------------------------------------------------------------------------------------------

    def respond (self, response_data, block_formating=False):
        """
        Return a full response to the request including headers and body. Response data is formated using the set
        format.

        @param response_data   (*)    All data types are accepted. If response_data is of a type not supported by the
                                      response format a BunkAcception is raised.
        @param block_formating (bool) If set to True the respopnse data will not be formated by the forma
        """

        # TODO: add mechanism to format response according to request. For example return JSON for requests with .json
        formated_resp = str(response)

        client.compose_headers()
        client.write(formated_resp)
        client.flush()
