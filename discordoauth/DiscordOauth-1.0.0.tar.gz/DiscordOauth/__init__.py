import requests

class Oauth(object):
    client_id = "0"
    client_secret = "0"
    scope = "0"
    redirect_uri = "0"
    discord_login_url = "0"
    discord_token_url = "https://discord.com/api/oauth2/token"
    discord_api_url = "https://discordapp.com/api"
    @staticmethod
    def get_acess_token(code):
        payload = {
            "client_id": Oauth.client_id,
            "client_secret": Oauth.client_secret,
            "grant_type": "authorization_code",
            "code":code,
            "redirect_uri":Oauth.redirect_uri,
            "scope":Oauth.scope
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        access_token = requests.post(url=Oauth.discord_token_url, data=payload,headers=headers)
        json = access_token.json()
        return json.get("access_token")

    @staticmethod
    def get_user_json(access_token):
        url = Oauth.discord_api_url+"/users/@me"

        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        user_json = requests.get(url=url, headers=headers)
        user_json = user_json.json()
        return user_json