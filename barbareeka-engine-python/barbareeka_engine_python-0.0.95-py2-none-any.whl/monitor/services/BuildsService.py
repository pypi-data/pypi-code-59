import abc


class BuildsService(abc.ABC):
    pass

    @abc.abstractmethod
    def notify_build_start(self):
        pass

    @abc.abstractmethod
    def notify_build_end(self):
        pass

    @abc.abstractmethod
    def update_build_with_unique_scenarios(self):
        pass

    @abc.abstractmethod
    def create_crash_collection(self):
        pass
