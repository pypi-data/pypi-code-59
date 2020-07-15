from httpx import Response

from ..exceptions import FailedRequest


def validate_200(r: Response):
    if r.status_code != 200:
        raise FailedRequest(r.text)


def validate_201(r: Response):
    if r.status_code != 201:
        raise FailedRequest(r.text)


def validate_204(r: Response):
    if r.status_code != 204:
        raise FailedRequest(r.text)
