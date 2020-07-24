import enum
from functools import partialmethod
from urllib.parse import urljoin

import requests

from .exceptions import CardImportError
from .types import Expansion, Card


class Endpoint(enum.Enum):
    LOGIN = "/accounts/login/"
    ADD_CARD = "/cards/addcard"


class Client:
    base_url = "https://www.decksagainstsociety.com"

    def __init__(self, username: str, password: str):
        self.session = requests.Session()
        self.session.headers.update(
            {"Origin": self.base_url, "Referer": self.base_url,}
        )
        self.login(username, password)

    @classmethod
    def url(cls, endpoint: Endpoint) -> str:
        return urljoin(cls.base_url, endpoint.value)

    def request(self, method: str, endpoint: Endpoint, *args, **kwargs):
        url = self.url(endpoint)
        return self.session.request(method, url, *args, **kwargs)

    get = partialmethod(request, "get")

    def post(self, endpoint: Endpoint, data, **kwargs):
        data.setdefault("csrfmiddlewaretoken", self.session.cookies.get("csrftoken"))
        return self.request("post", endpoint, data=data, **kwargs)

    def login(self, username: str, password: str):
        self.get(Endpoint.LOGIN)
        response = self.post(
            Endpoint.LOGIN, data={"username": username, "password": password,}
        )
        response.raise_for_status()

    def add_card(self, expansion: Expansion, card: Card):
        response = self.post(
            Endpoint.ADD_CARD,
            data={
                "expansion": expansion.id,
                "type": card.type.value,
                "content": card.content,
            },
            allow_redirects=False,
        )
        if response.status_code != 302:
            # TODO perhaps one day I'll bother to retrieve the error message
            # from the response
            raise CardImportError()
