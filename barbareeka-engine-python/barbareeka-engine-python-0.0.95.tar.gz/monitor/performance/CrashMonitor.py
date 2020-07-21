from pymongo import MongoClient

from mdb.android.Android import Android
from monitor.entities.SmartBOT import SmartBOT


class CrashMonitor(object):
    mongo_client: MongoClient
    smartBOT: SmartBOT

    def __init__(self, smartBOT):
        self.smartBOT = smartBOT

    # TODO: Implement
    def capture_crashes(self):
        exception = Android().get_exception(self.smartBOT)
