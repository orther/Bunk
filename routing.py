# action imports
from actions import http_test

# routes
routes = {
    "/http_test": ("(controller:\w+)", http_test.HttpTestAction, {"test": "http_test"})
}

