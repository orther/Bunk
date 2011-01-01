from bunk.action import BunkAction

class FbTagImageCreatorAction (BunkAction):

    # ------------------------------------------------------------------------------------------------------------------
    # METHODS
    # ------------------------------------------------------------------------------------------------------------------

    def get (self, client):
        """
        No action needed so we return empty response.
        """

        response = {}

        # return resource
        self.respond(client, response)
