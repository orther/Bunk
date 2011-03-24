import os
import sys

sys.path.append(os.path.abspath("./lib/Elements/lib/"))

from elements.http.server import RoutingHttpServer

from action         import BunkAction
from core           import bunk
from core.exception import BunkRoutesException

from settings import hosts
from settings import long_running
from settings import print_routes
from settings import worker_count

class BunkServer (RoutingHttpServer):

    def __init__ (self, bunk_routing, **kwargs):
        """
        Create a new RoutingHttpServer instance.

        @param bunk_routing (module)
        """

        #routes = self.build_elements_routes(bunk_routing.bunk_routes, bunk_routing.file_exts, print_routes)

        #RoutingHttpServer.__init__(self, routes=routes, **kwargs)

        self.print_routes(bunk_routing.element_routes)

        RoutingHttpServer.__init__(self, routes=bunk_routing.element_routes, **kwargs)

    # ------------------------------------------------------------------------------------------------------------------

    def build_elements_routes (self, bunk_routes, file_exts, print_routes=True):
        """
        Build Elements routes dict using Bunk routes.

        Single Bunk route format: (path, action, [validation, action_args])

        NOTE: `validation` is a regex pattern (str) and `action_args` is a (dict). The order of `validation` and
              `action_args` does NOT matter.

        @param bunk_routes  (tuple)
        @param file_exts    (tuple) List of file extensions to great routes for.
        @param print_routes (bool)  If set to True the routes are printed while they are being built for debugging.

        @return (dict)
        """

        elements_routes = []

        if type(file_exts) != tuple or len(file_exts) < 1:
            raise BunkRoutesException("`file_exts` must be an instance of (tuple) with at least 1 item")

        if type(bunk_routes) != tuple:
            raise BunkRoutesException("`bunk_routes` must be an instance of (tuple)")

        elif not len(bunk_routes):
            # no routes to build
            return elements_routes

        # remove empty routes
        file_exts = [".%s" % ext for ext in file_exts if not ext == ""]

        # build file extension regex validator
        file_exts_regex = "(_file_ext:%s)$" % "|".join(file_exts)

        # compile routes
        for route in bunk_routes:
            if type(route) != tuple:
                raise BunkRoutesException("Bunk route must be an instance of (tuple)")

            if len(route) < 2:
                raise BunkRoutesException("Bunk route must containt a `path` and `action` as the first to items")

            route_path       = route[0]
            route_action     = route[1]
            route_args       = dict()
            route_validation = None

            if type(route_path) != str:
                raise BunkRoutesException("Invalid route path")

            try:
                if not issubclass(route_action, BunkAction):
                    raise Exception()

            except Exception:
                raise BunkRoutesException("Action for route '%s' must be a sub-class of BunkAction" % route_path)

            # parse route details
            for detail in route[2:4]:
                if type(detail) == str:
                    route_validation = detail

                elif type(detail) == dict:
                    route_args = detail

                else:
                    raise BunkRoutesException("Detail for route '%s' must be an instace of a str or dict" % route_path)

            if route_validation:
                # validation based route
                route_validation += file_exts_regex

                # add route
                elements_routes.append(self.build_elements_route(route_path, route_action, route_validation,
                                                                 route_args))

            else:
                # static path based route
                for file_ext in file_exts:
                    static_path = route_path + file_ext

                    # add file_ext arg for static routes
                    static_route_args = dict(route_args, **{"file_ext": file_ext})

                    #add route
                    elements_routes.append(self.build_elements_route(route_path, route_action, route_validation,
                                                                     static_route_args))

        if print_routes:
            # print route for debugging
            self.print_routes(elements_routes)

        return elements_routes

    # ------------------------------------------------------------------------------------------------------------------

    def build_elements_route (self, route_path, action, validation, route_args):
        """
        Build an Elements route.

        @param route_path (str)
        @param action     (HttpAction)
        @param validation (str/None)
        @param route_args (dict/None)

        @return (tuple)
        """

        return [route_path, validation, action, route_args]

        route = []

        if not validation == None:
            route.append(validation)

        ["/validate", "(number:\d+)/(word:\w+)", ExampleValidatingAction, {"sentence": "Hello, world! This is ExampleArgsAction!"}]


        route.append(action)

        if not route_args == None and not len(route_args) < 1:
            route.append(route_args)

        return tuple(route)

    # ------------------------------------------------------------------------------------------------------------------

    def print_routes (self, elements_routes):
        """
        Print out Elements formated routes dict.

        @param elements_routes (dict)
        """

        print "Elements routes:"

        for route in elements_routes:
            print route
