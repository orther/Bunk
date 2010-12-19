from response_formatter import ResponseFormatter

class JsonFormatter (ResponseFormatter):

    def format (self, response_data):
        """
        Format response data with to the set _format.

        @param response_data (*) All data types are accepted. If response_data is of a type not supported by the
                                 response format set then a ResponseFormatException is raised.

        @return (str)
        """

        supported_data_types = (str, int, float, list, dict)

        # validate response_data type
        validate_response_data_type(type(response_data), supported_data_types)

        return str(response_data)
