import abc


class OptimusService(abc.ABC):

    @abc.abstractmethod
    def get_latest_id(self):
        pass
