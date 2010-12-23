from response_formatter import ResponseFormatter

from json import dumps

class JsonFormatter (ResponseFormatter):

    @staticmethod
    def format (response_data):
        """
        Format response data into JSON using the standard Python json.dumps() function.

        @param response_data (*) All data types are accepted. If response_data is of a type not supported by the
                                 implemented response format then a ResponseFormatException is raised.

        @return (str)
        """

        supported_data_types = (type(None), str, int, long, float, list, tuple, dict, bool)

        # validate response_data type
        ResponseFormatter.validate_response_data_type(type(response_data), supported_data_types)

        return dumps(response_data)
