from bunk.core.exception import ResponseFormatException
from bunk.core.exception import BunkException

class ResponseFormatter:

    @staticmethod
    def validate_response_data_type (response_data_type, supported_data_types):
        """
        Check if the reponse_data type is supported by the implemented response formatter and raise a
        ResponseFormatException if it is NOT.

        @param response_data_type   (type)
        @param supported_data_types (tuple) A tuple of all supported data types
        """

        if response_data_type not in supported_data_types:
            e_msg = "validate_response_data_type() recieved response_data of type `%s` but only supports: %s"

            raise ResponseFormatException(e_msg % (response_data_type, supported_data_types))

    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def format (response_data):
        """
        Format response data with to the set _format.

        @param response_data (*) All data types are accepted. If response_data is of a type not supported by the
                                 implemented response format then a ResponseFormatException is raised.

        @return (str)
        """

        raise BunkException("%s is required to provide a format() method and does not" % self.__class__.__name__)
