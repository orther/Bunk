from response_formatter import ResponseFormatter

import json

class JsonFormatter (ResponseFormatter):

    @staticmethod
    def format (response_data):
        """
        Format response data with to the set _format.

        @param response_data (*) All data types are accepted. If response_data is of a type not supported by the
                                 response format set then a ResponseFormatException is raised.

        @return (str)
        """

        supported_data_types = (type(None), str, int, long, float, list, dict, bool)

        # validate response_data type
        ResponseFormatter.validate_response_data_type(type(response_data), supported_data_types)

        return json.dumps(response_data)
