# action imports
from actions import http_test

# routes
routes = {
    "/http_test.json": (http_test.HttpTestAction, {"route_id": "all_json"}),
    "/http_test":      ("(id:\d+).(format:\w+)", http_test.HttpTestAction, {"route_id": ""})
}
