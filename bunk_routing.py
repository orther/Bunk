# actions
from actions import http_test

from actions.users import login  as users_login
from actions.users import create as users_create


# file extensions
file_exts = ('json',)

# Bunk routes
bunk_routes = (

    # Bunk routes format: (path, action, [validation, action_args])
    # Blog WS Example: ("/login",          blog.AuthAction),
    #                  ("/posts",          blog.PostsAction, {"list_all": True}),
    #                  ("/posts/",         blog.PostsAction, "(post_id:\d+)"),
    #                  ("/posts/spanish/", blog.PostsAction, "(post_id:\d+)", {"translate": True, "lang": "spanish"}),

    # http test routes
    ("/http_test", http_test.HttpTestAction),
    ("/http_test", http_test.HttpTestAction, "(id:\d*)"),

    # users routes
    ("/users/create", users_create.UsersCreateAction),
    ("/users/login",  users_login.UsersLoginAction),

)
