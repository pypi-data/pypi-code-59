import time
from json import JSONDecodeError
from typing import Callable
from loguru import logger

import requests


class LazyResponse:

    def __init__(self, method_call: Callable[..., requests.Response], url: str, method: str, data=None, headers=None):
        self._response: requests.Response = None
        self._response_loaded = False
        self._get_response = method_call
        self.url = url
        self.method = method
        self.request_data = data
        self.response_time = None
        self.request_headers = headers

    def _load_response(self):
        if not self._response_loaded:
            logger.info(f"REQUEST: {self.url} | method: {self.method} | data: {self.request_data} | headers: {self.request_headers}")
            start = time.time()
            self._response = self._get_response()
            self.response_time = time.time() - start
            self._response_loaded = True
            logger.info(f"RESPONSE: {self.url} | {self.status} | {self.response_time:.4f} seconds")

    @property
    def data(self):
        self._load_response()
        try:
            response_data = self._response.json()
        except JSONDecodeError:
            logger.warning(f"{self.url} did not respond with valid JSON, falling back to raw content (probably HTML).")
            response_data = self._response.content
        return response_data

    @property
    def status(self):
        self._load_response()
        return self._response.status_code

    @property
    def headers(self):
        self._load_response()
        return self._response.headers

    def __repr__(self):
        return f"LazyResponse(request_data={self.request_data}, url={self.url}, method={self.method})"

    def __str__(self):
        return str(self.data)
