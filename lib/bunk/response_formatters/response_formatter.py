from bunk.core.exception import ResponseFormatException
from bunk.core.exception import BunkException

class ResponseFormatter:

    def validate_response_data_type (self, response_data_type, supported_data_types):
        """
        Check if the reponse_data type is supported by the implemented response formatter and raise a
        ResponseFormatException if it is NOT.

        @param response_data_type   (type)
        @param supported_data_types (tuple) A tuple of all supported data types
        """

        if response_data_type not in supported_data_types:
            e_data = (response_data_type, supported_data_types, self.__class__.__name__)

            raise ResponseFormatException("%s recieved response_data of type `%s` but only supports: %s" % e_data)

    # ------------------------------------------------------------------------------------------------------------------

    def format (self, response_data):
        """
        Format response data with to the set _format.

        @param response_data (*) All data types are accepted. If response_data is of a type not supported by the
                                 implemented response format then a ResponseFormatException is raised.

        @return (str)
        """

        raise BunkException("%s is required to provide a format() method and does not" % self.__class__.__name__)
