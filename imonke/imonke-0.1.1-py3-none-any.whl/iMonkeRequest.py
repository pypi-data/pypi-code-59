import requests as REQUESTS

def get_post_points(self):
    # Returns a list of post_points
    post_points = ["POST/auth/", "POST/content/", "POST/user/"]
    return post_points

def get_get_points():
    # Returns a list of get_points

    get_points = ["GET/check/email/<email>/", "GET/check/nick/<nick>/",
                      "GET/content/<id>/", "GET/feed/all", "GET/me/",
                      "GET/user/id/<id>/", "GET/user/nick/<nick>/"]
    return get_points

def get_put_points():
    # Returns a list of put_points
    put_points = ["PUT/user/id/<id>/reports", ]
    return put_points

def requests():
    # Returns a requests object
    return REQUESTS