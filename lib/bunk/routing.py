from core.exception import BunkRoutesException
from action         import BunkAction


def build_routes (bunk_routes, file_exts, print_routes=True):
    """
    Build Elements routes dict. This is a convience function to make it easier to accept multiple file extensions per
    route.

    NOTE: `validation` is a regex pattern str and `route_args` is an object containg any arguments to pass into
          HttpAction. The order does NOT matter. When the bunk route is being parse the type is checked to determine
          the route detail.

    @param bunk_routes  (dict)  route_path->(action, [validation, route_args])
    @param file_exts    (tuple) List of file extensions to great routes for.
    @param print_routes (bool)  If set to True the routes are printed while they are being built for debugging.

    @return (dict)
    """

    element_routes = {}

    if type(file_exts) != tuple or len(file_exts) < 1:
        raise BunkRoutesException("Bunk file_exts must be an instance of tuple with at least 1 item")

    if type(bunk_routes) != dict:
        raise BunkRoutesException("Bunk routes must be an instance of dict")

    if print_routes:
        print "Elements routes created:"

    # remove empty routes
    file_exts = [".%s" % ext for ext in file_exts if not ext == ""]

    # build file extension regex validator
    file_exts_regex = "(_file_ext:%s)$" % "|".join(file_exts)

    # compile routes
    for route_path, route_details in bunk_routes.iteritems():
        if type(route_path) != str:
            raise BunkRoutesException("Invalid route path")

        if len(route_details) < 1:
            raise BunkRoutesException("Bunk routes must containt an action as the first item of the tuple")

        try:
            if not issubclass(route_details[0], BunkAction):
                raise Exception()

        except Exception:
            raise BunkRoutesException("Action for route '%s' must be a sub-class of BunkAction" % route_path)

        # retrieve route arguments
        route_action     = route_details[0]
        route_args       = None
        route_validation = None

        # parse route details
        for detail in route_details[1:3]:
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
            element_routes[route_path] = build_elements_route(route_action, route_validation, route_args)

        else:
            # static path based route
            for file_ext in file_exts:
                route_path += file_ext

                #add route
                element_routes[route_path] = build_elements_route(route_action, route_validation, route_args)

    if print_routes:
        # print route for debugging
        print element_routes

    return element_routes

# ----------------------------------------------------------------------------------------------------------------------

def build_elements_route (action, validation, route_args):
    """
    Build an Elements route.

    @param action     (HttpAction)
    @param validation (str/None)
    @param route_args (dict/None)

    @return (tuple)
    """

    route = []

    if not validation == None:
        route.append(validation)

    route.append(action)

    if not route_args == None and not len(route_args) < 1:
        route.append(route_args)

    return tuple(route)
