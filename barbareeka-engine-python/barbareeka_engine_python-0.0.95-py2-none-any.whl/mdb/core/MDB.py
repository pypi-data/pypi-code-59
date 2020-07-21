import abc


class MDB(abc.ABC):

    @abc.abstractmethod
    def get_devices(self):
        pass
