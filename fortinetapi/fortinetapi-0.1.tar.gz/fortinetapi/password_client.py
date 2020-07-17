import logging
import requests
import sys
import json

import urllib3
urllib3.disable_warnings()

class PasswordClient(object):
    def __init__(self, host, port=443):
        self.base_url = f'https://{host}:{port}'

    def update_csrf(self):
        for cookie in self.session.cookies:
            if cookie.name == "ccsrftoken":
                csrftoken = cookie.value[1:-1]
                self.session.headers.update({"X-CSRFTOKEN": csrftoken})

    def login(self, user, password, csrf=True):
        self.logout()
        self.session = requests.session()
        self.session.verify = False

        res = self.post("/logincheck", params={'username': user, 'secretkey': password})

        if res.text.find("logindisclaimer") != -1:
            logging.info("logindisclaimer")
            if csrf:
                self.update_csrf()
            res = self.post("/logindisclaimer", False, data={"confirm": 1})

        if res.text.find("error") != -1:
            logging.error("LOGIN failed")
            return False

        if res.text.find("license") != -1:
            logging.error("LOGIN failed: license has probably expired")
            return False

        if csrf:
            self.update_csrf()

        return True

    def logout(self):
        if hasattr(self, "session"):
            self.post("/logout")

    def get(self, path, **options):
        url = self.base_url + path

        try:
            res = self.session.get(
                url,
                params=options.get("params")
            )
        except requests.exceptions.RequestException as e:
            logging.error(e, exc_info=True)
            raise
        except:
            logging.error("Unexpected error:", exc_info=True)
            raise

        return res

    def post(self, path, isJson = True, **options):
        url = self.base_url + path

        try:
            res = self.session.post(
                url,
                params=options.get("params"),
                data= json.dumps(options.get("data")) if isJson else options.get("data")
            )
        except requests.exceptions.RequestException as e:
            logging.error(e, exc_info=True)
            raise
        except:
            logging.error("Unexpected error:", exc_info=True)
            raise

        return res

    def put(self, path, isJson = True, **options):
        url = self.base_url + path

        try:
            res = self.session.put(
                url,
                params=options.get("params"),
                data= json.dumps(options.get("data")) if isJson else options.get("data")
            )
        except requests.exceptions.RequestException as e:
            logging.error(e, exc_info=True)
            raise
        except:
            logging.error("Unexpected error:", exc_info=True)
            raise

        return res

    def delete(self, path, **options):
        url = self.base_url + path

        try:
            res = self.session.delete(
                url,
                params=options.get("params")
            )
        except requests.exceptions.RequestException as e:
            logging.error(e, exc_info=True)
            raise
        except:
            logging.error("Unexpected error:", exc_info=True)
            raise

        return res
