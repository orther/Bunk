from response_formatter import ResponseFormatter

from cjson import encode

class CjsonFormatter (ResponseFormatter):

    @staticmethod
    def format (response_data):
        """
        Format response data into JSON using the cjson modules encode() function.

        @param response_data (*) All data types are accepted. If response_data is of a type not supported by the
                                 implemented response format then a ResponseFormatException is raised.

        @return (str)
        """

        supported_data_types = (type(None), str, int, long, float, list, tuple, dict, bool)

        # validate response_data type
        ResponseFormatter.validate_response_data_type(type(response_data), supported_data_types)

        return encode(response_data)
