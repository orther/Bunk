#!/usr/bin/env python

import os
import sys

sys.path.append(os.path.abspath("./lib/"))
sys.path.append(os.path.abspath("./lib/Elements/lib/"))

from elements.http.server import RoutingHttpServer

from routing import routes

# start the server
RoutingHttpServer(hosts=[("0.0.0.0", 8080)], routes=routes).start()
