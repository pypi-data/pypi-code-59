import logging
import requests
import sys
import json

import urllib3
urllib3.disable_warnings()

class TokenClient(object):
    def __init__(self, host, token, port=443):
        self.base_url = f'https://{host}:{port}'
        self.token = token

    def get(self, path, **options):
        url = self.base_url + path
        params=options.get("params", {}) 
        params['access_token'] = self.token

        try:
            res = requests.get(
                url,
                verify=False,
                params=params
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

        params=options.get("params", {}) 
        params['access_token'] = self.token

        try:
            res = requests.post(
                url,
                verify=False,
                params=params,
                data= json.dumps(options.get("data")) if isJson else options.get("data")
            )
        except requests.exceptions.RequestException as e:
            logging.error(e, exc_info=True)
            raise
        except:
            logging.error("Unexpected error:", exc_info=True)
            raise

        return res

    def put(self, path, isJson = True,**options):
        url = self.base_url + path

        params=options.get("params", {}) 
        params['access_token'] = self.token

        try:
            res = requests.put(
                url,
                verify=False,
                params=params,
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

        params=options.get("params", {}) 
        params['access_token'] = self.token

        try:
            res = requests.delete(
                url,
                verify=False,
                params=params
            )
        except requests.exceptions.RequestException as e:
            logging.error(e, exc_info=True)
            raise
        except:
            logging.error("Unexpected error:", exc_info=True)
            raise

        return res
