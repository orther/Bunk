# This file is part of Bunk.
# Copyright (c) 2011 Brandon Orther. All rights reserved.
#
# The full license is available in the LICENSE file that was distributed with this source code.

class ResponseFormatter:

    @staticmethod
    def format (response_data):
        """
        Format response data into a string. This is the default response formatter.

        @param response_data

        @return (str)
        """

        return str(response_data)
