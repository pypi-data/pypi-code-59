import requests

from monitor.entities.Intellisense import Intellisense
from monitor.entities.MongoService import MongoService


class IntellisenseClient:
    pass


INTELLI_SENSE = MongoService.MONGO_SERVICE + "/intellisense"


def record_exception_sense(intellisense: Intellisense):
    response = requests.post(
        url=INTELLI_SENSE,
        headers={"Content-Type": "application/json"},
        json=intellisense
    )
    return response.json()
