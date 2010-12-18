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

        @param server        (HttpServer) The HttpServer instance.
        @param title         (str)        The title to display when this core action handles a request.
        @param response_code (str)        The response code to use when this core action handles a request.
        """

        HttpAction.__init__(self, **kwargs)

        if logging_on:
            # setup logging if turned on
            logging.basicConfig(filename=logging_file, level=logging_level)

    # ------------------------------------------------------------------------------------------------------------------

    def init_db (self):
        """
        Import database module.

        @return (module) elements.model.database
        """

        from elements.model import database

        return database
