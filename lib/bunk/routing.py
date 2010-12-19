def build_routes (bunk_routes, file_exts, print_routes=True):
    """
    Build Elements routes dict. This is a convience function to make it easier to accept multiple file extensions per
    route.

    @param bunk_routes  (tuple)
    @param file_exts    (tuple)
    @param print_routes (bool)  If set to True the routes are printed while they are being built for debugging.

    @return (dict)
    """

    if print_routes:
        print "Routes:"

    # build file ext path validator
    file_exts_regex_parts      = "|".join(["."+ext for ext in file_exts if not ext == ""])
    file_exts_regex_quantifier = "?" if "" in file_exts else ""
    file_exts_regex            = "(_file_ext:(%s)%s)$" % (file_exts_regex_parts, file_exts_regex_quantifier)

    routes = {}

    for bunk_route in bunk_routes:
        if type(bunk_route[1]) == str:
            # url params route
            route_path_validation = bunk_route[1] + file_exts_regex
            route_action          = bunk_route[2]
            route_args            = bunk_route[3]

            route = build_single_route(route_path_validation, route_action, route_args)

            if print_routes:
                # print route for debugging
                print_single_route(bunk_route[0], route)

            # add route
            routes[bunk_route[0]] = route

        else:
            # static url route
            route_action = bunk_route[2]

            for file_ext in file_exts:
                if file_ext == "":
                    # add route without file extension
                    route_static_path = bunk_route[0]

                else:
                    # add route with file extension
                    route_static_path = "%s.%s" % (bunk_route[0], file_ext)

                route_args        = {"file_ext": file_ext}

                if type(bunk_route[3]) == dict and len(bunk_route[3]) > 0:
                    # merge existing route args
                    route_args = dict(route_args, **bunk_route[3])

                route = build_single_route(None, route_action, route_args)

                if print_routes:
                    # print route for debugging
                    print_single_route(route_static_path, route)

                # add route
                routes[route_static_path] = route

    return routes

# ----------------------------------------------------------------------------------------------------------------------

def build_single_route (path_validation, action, route_args):
    """
    Build a single Elements route.

    @param path_validation (str/None)
    @param action          (HttpAction)
    @param route_args      (dict/None)

    @return (tuple)
    """

    route = []

    if not path_validation == None:
        route.append(path_validation)

    route.append(action)

    if not route_args == None or not len(route_args) < 1:
        route.append(route_args)

    return tuple(route)

# ----------------------------------------------------------------------------------------------------------------------

def print_single_route (static_path, route):
    """
    Print a single route.

    @param static_path (str)
    @param route       (tuple)
    """

    print static_path, route
