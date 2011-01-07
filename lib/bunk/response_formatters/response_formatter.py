from bunk.core.exception import BunkException

class ResponseFormatter:

    @staticmethod
    def format (response_data):
        """
        Format response data with to the set _format.

        @param response_data           (*)    All data types are accepted. If response_data is of a type not supported
                                              by the implemented response format then a ResponseFormatException is raised.

        @return (str)
        """

        raise BunkException("%s is required to provide a format() method and does not" % self.__class__.__name__)
