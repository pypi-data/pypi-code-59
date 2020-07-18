from imonke import iMonkeHandler, iMonkeRequest


url = iMonkeHandler.iMonkeUrl()
user_endpoint = url + "user/"
user_by_id_endpoint = user_endpoint + "id/"
user_by_nick_endpoint = user_endpoint + "nick/"
request = iMonkeRequest.requests()

def user_by_id(user_id, bearer=None, basic=None):

    # Gets a users information based on their id

    general_error = "Please include either a Basic Auth or a Bearer"

    header = iMonkeHandler.headers(bearer, basic)
    if not header:
        iMonkeHandler.raise_warning(general_error)

    try:
        data = request.get(user_by_id_endpoint + user_id, headers=header)
        return data.json()
    except Exception as Error:
        raise Error


def user_by_nick(nick, bearer=None, basic=None):

    # Gets a users information based on their nick

    general_error = "Please include either a Basic Auth or a Bearer"

    header = iMonkeHandler.headers(bearer, basic)
    if not header:
        iMonkeHandler.raise_warning(general_error)

    try:
        data = request.get(user_by_nick_endpoint + nick, headers=header)
        return data.json()
    except Exception as Error:
        raise Error


def report_user(user_id, reason, bearer=None, basic=None):

    # Reports a user

    general_error = "Please include either a Basic Auth or a Bearer"

    header = iMonkeHandler.headers(bearer, basic)
    if not header:
        iMonkeHandler.raise_warning(general_error)

    data = {"reason": reason}

    try:
        data = request.put(user_by_id_endpoint + user_id + "reports/", headers=header, data=data)
        return data.json()
    except Exception as Error:
        raise Error
