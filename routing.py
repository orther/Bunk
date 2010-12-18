# action imports
from actions import http_test

# routes
routes = {
    "/http_test": ("(test_id:\w+)", http_test.HttpTestAction, {"route_id": "http_test_1"})
}
