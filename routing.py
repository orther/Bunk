# action imports
from actions import http_test

# set this to true for debugging
print_routes = True

file_exts = ('', 'html', 'json', 'xml')

bunk_routes = (
    ("/http_test", "(id:\d*)", http_test.HttpTestAction, {}),
)
