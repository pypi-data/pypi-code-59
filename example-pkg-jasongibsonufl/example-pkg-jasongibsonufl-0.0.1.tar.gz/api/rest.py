from urllib.request import urlopen 



class MWRester(object):
    def __init__(self, api_key=None,
                 endpoint="http://2dmaterialsweb.org/rest/calculation"):
        if api_key is not None:
            self.api_key = api_key
        else:
            self.api_key = ""
        self.preamble = endpoint
        import requests
        self.session = requests.Session()
        self.session.headers = {"x-api-key": self.api_key}

    def _make_request(self, sub_url, payload=None, method="GET",
                      mp_decode=True):
        url = self.preamble + sub_url + "/" + self.api_key
        x = urlopen(url)
        return x.read()