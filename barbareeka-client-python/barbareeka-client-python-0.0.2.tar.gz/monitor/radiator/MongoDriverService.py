from monitor.radiator.MongoPort import get_port


class MongoDriverService(object):

    def __init__(self) -> None:
        super().__init__()


def mongo_service():
    return MongoDriverService()


def mongo_command():
    strings = ["mongod", "--port", get_port()]
    return strings
