# This file is part of Bunk.
# Copyright (c) 2011 Brandon Orther. All rights reserved.
#
# The full license is available in the LICENSE file that was distributed with this source code.

# actions
from actions import http_test

from actions.users import create  as users_create
from actions.users import details as users_details
from actions.users import login   as users_login
from actions.users import logout  as users_logout

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
    ("/users/logout", users_logout.UsersLogoutAction),
    ("/users",        users_details.UsersDetailsAction, "(username:\w+)"),
)

element_routes = [
    # http test routes
    ["/http_test",         None,       http_test.HttpTestAction],
    ["/http_test_pattern", "(id:\d*)", http_test.HttpTestAction],

    # users routes
    ["/users/create", None,             users_create.UsersCreateAction],
    ["/users/login",  None,             users_login.UsersLoginAction],
    ["/users/logout", None,             users_logout.UsersLogoutAction],
    ["/users",        "(username:\w+)", users_details.UsersDetailsAction]
]
