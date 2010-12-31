# set this to true for debugging
print_routes = True

# file extensions
file_exts = ('cjson', 'json', 'xml')

# actions
from actions import http_test

# Bunk routes
bunk_routes = (
    # Bunk routes format: (path, action, [validation, action_args])
    ("/http_test", http_test.HttpTestAction, "(id:\d*)"),
    ("/http_test", http_test.HttpTestAction),
)
