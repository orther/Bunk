# action imports
from actions import http_test

# set this to true for debugging
print_routes = True

file_exts = ('cjson', 'json', 'xml')

bunk_routes = {
    "/http_test": ("", http_test.HttpTestAction, "(id:\d*)"),
}
