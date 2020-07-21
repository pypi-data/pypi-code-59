from pymongo import MongoClient

from monitor.clients.BuildsClient import BuildsClient


def get_latest_build_id():
    latest_build_id = BuildsClient().get_latest_build_id()
    return latest_build_id


class MongoIO(object):
    latest_build_id = None
    mongo_client: MongoClient()

    def __init__(self):
        self.mongo_client = MongoClient('mongodb://localhost:27017/')
        print("Mongo client: {}".format(self.mongo_client))
        if self.latest_build_id is None:
            get_latest_build_id()

