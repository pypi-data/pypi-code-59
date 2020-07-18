from imonke import iMonkeRequest, iMonkeHandler

request = iMonkeRequest.requests()
imonke_url = iMonkeHandler.iMonkeUrl()

url = imonke_url
check_email_endpoint = url + "/check/email/"
check_nick_endpoint = url + "/check/nick/"

def check_email(email):
    # Checks if an email is available
    try:
        data = request.get(check_email_endpoint + email)
        return data.json()
    except Exception as Error:
        raise Error

def check_nick(nick):
    # Checks if an nick is available

    try:
        data = request.get(check_nick_endpoint + nick)
        return data.json()
    except Exception as Error:
        raise Error