from response_formatter import ResponseFormatter

from json import dumps

class JsonFormatter (ResponseFormatter):

    @staticmethod
    def format (response_data):
        """
        Format response data into JSON using the standard Python json.dumps() function.

        @param response_data

        @return (str)
        """

        return dumps(response_data)
