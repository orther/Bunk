# This file is part of Bunk.
# Copyright (c) 2011 Brandon Orther. All rights reserved.
#
# The full license is available in the LICENSE file that was distributed with this source code.

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
