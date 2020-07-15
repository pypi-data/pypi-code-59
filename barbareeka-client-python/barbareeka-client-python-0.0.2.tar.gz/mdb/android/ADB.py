import abc

from mdb.core.MDB import MDB
from monitor.entities.SmartBOT import SmartBOT


class ADB(MDB):

    @abc.abstractmethod
    def get_memory_info(self, smartBOT: SmartBOT):
        pass

    @abc.abstractmethod
    def get_cpu_info(self, smartBOT: SmartBOT):
        pass

    @abc.abstractmethod
    def get_activity(self, smartBOT: SmartBOT):
        pass

