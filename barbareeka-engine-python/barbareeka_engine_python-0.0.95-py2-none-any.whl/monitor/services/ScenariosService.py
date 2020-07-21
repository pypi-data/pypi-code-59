import abc

from monitor.entities.SmartBOT import SmartBOT
from monitor.entities.reportParser import ExecutedScenario
from monitor.requests.Scenario import Scenario


class ScenariosService(abc.ABC):
    pass

    @abc.abstractmethod
    def notify_BOT_registration(self, smartBOT: SmartBOT):
        pass

    @abc.abstractmethod
    def notify_scenario_completion(self, smartBOT: SmartBOT):
        pass

    @abc.abstractmethod
    def get_latest_record_for(self, scenario: ExecutedScenario):
        pass

    @abc.abstractmethod
    def update_scenario_time_line(self, scenario: Scenario, smartBOT: SmartBOT, scenario_time_lines: list):
        pass

    @abc.abstractmethod
    def update_crashes(self, smartBOT: SmartBOT, exceptions, activity):
        pass
