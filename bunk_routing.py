# set this to true for debugging
print_routes = True

# file extensions
file_exts = ('json', 'xml')

# actions
from actions import http_test
from actions import fb_tag_images_creator

# Bunk routes
bunk_routes = (
    # Bunk routes format: (path, action, [validation, action_args])
    # Blog WS Example: ("/login",          blog.AuthAction),
    #                  ("/posts",          blog.PostsAction, {"list_all": True}),
    #                  ("/posts/",         blog.PostsAction, "(post_id:\d+)"),
    #                  ("/posts/spanish/", blog.PostsAction, "(post_id:\d+)", {"translate": True, "lang": "spanish"}),

    # http test routes
    ("/http_test", http_test.HttpTestAction, "(id:\d*)"),

    # facebook image creator routes
    ("/facebook/5_recent_images_creator", fb_tag_images_creator.FbTagImageCreatorAction),
)
