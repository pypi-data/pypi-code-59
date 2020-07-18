from imonke import iMonkeRequest, iMonkeHandler

request = iMonkeRequest.requests()
json = iMonkeHandler.json()
url = iMonkeHandler.iMonkeUrl()
content_endpoint = url + "content/"
feed_all_endpoint = url + "feed/all/"


def post_by_id(post_id, bearer=None, basic=None):
    # Get a posts information by its id

    general_error = "Please include either a Basic Auth or a Bearer"

    header = iMonkeHandler.headers(bearer, basic)
    if not header:
        iMonkeHandler.raise_warning(general_error)

    try:
        data = request.get(content_endpoint + post_id, headers=header)
        return data.json()
    except Exception as Error:
        raise Error

def post(bearer, mime, content, nsfw=False, featureable=False, tags=list):

    data = {"mime": mime,
            "nsfw": nsfw,
            "featurable": featureable,
            "tags": tags}

    payload = {'json': json.dumps(data)}

    files = [('file', content)]

    headers_ = {
        'Authorization': 'Bearer ' + bearer
    }

    try:
        data = request.post(content_endpoint, headers=headers_, data=payload, files=files)
        return data.json()
    except Exception as Error:
        raise Error


def feed_all(bearer=None, basic=None, query=None):
    # Get a posts information by its id

    url = feed_all_endpoint

    if not query:
        query = ""
    else:
        query = query

    general_error = "Please include either a Basic Auth or a Bearer"

    header = iMonkeHandler.headers(bearer, basic)
    if not header:
        iMonkeHandler.raise_warning(general_error)

    try:
        data = request.get(url + query, headers=header)
        return data.json()
    except Exception as Error:
        raise Error
