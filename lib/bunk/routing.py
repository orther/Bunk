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
    file_exts_regex_parts      = ["."+ext for ext in file_exts if not ext == ""]
    file_exts_regex_quantifier = "?" if "" in file_exts else ""
    file_exts_regex            = "(_file_ext:(%s)%s)$" % ("|".join(file_exts_regex_parts), file_exts_regex_quantifier)

    routes = {}

    for bunk_route in bunk_routes:
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
