from imonke import iMonkeRequest, iMonkeHandler

request = iMonkeRequest.requests()
url = iMonkeHandler.iMonkeUrl()
json = iMonkeHandler.json()

me_endpoint = url + "me/"
user_endpoint = url + "user/"
auth_endpoint = url + "auth/"


def create_user(email, password, nick, bio=None):

    # Creates a user profile

    headers = {"email": email,
                "nick": nick,
                "password": password}

    general_error = "Please include all params (email, nick, password)"
    bio_warning = "You may include a bio as well"

    if not bio:
        iMonkeHandler.raise_warning(bio_warning)
        pass
    else:
        headers['bio'] = bio

    try:
        data = request.post(user_endpoint, data=json.dumps(headers))
        return data.json()
    except Exception as Error:
        raise Error


def get_me(bearer):
    header = {"Authorization": "Bearer " + bearer}
    try:
        data = request.get(me_endpoint, headers=header)
        return data.json()
    except Exception as Error:
        raise Error


def auth(email, password=None, secret=None):

    general_error = "You must provide a secret or a password"
    gen_error_2 = "Only password OR secret please"

    if not secret and not password:
        iMonkeHandler.raise_warning(general_error)
    else:
        pass
    header = {"email": email, }
    if secret:
        header['secret'] = secret

    if password:
        header['password'] = password

    if password and secret:
        iMonkeHandler.raise_warning(gen_error_2)

    try:
        data = request.post(auth_endpoint, json.dumps(header))
        return data.json()
    except Exception as Error:
        raise Error
