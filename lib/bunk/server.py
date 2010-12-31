import os
import sys

sys.path.append(os.path.abspath("./lib/Elements/lib/"))

from elements.http.server import RoutingHttpServer

from bunk.core    import bunk
from bunk.routing import build_routes

class BunkServer (RoutingHttpServer):

    def __init__ (self, bunk_routes, file_exts, print_routes, **kwargs):
        """
        Create a new RoutingHttpServer instance.

        @param routes (dict) A path->(action, [validation, action_args]) mapping.
        """

        routes = build_routes(bunk_routes, file_exts, print_routes)

        RoutingHttpServer.__init__(self, routes=routes, **kwargs)
