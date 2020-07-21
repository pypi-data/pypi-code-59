import unittest

from entities.SessionInfo import SessionInfo
from monitor.clients.BuildsClient import BuildsClient
from monitor.clients.ScenariosClient import ScenariosClient
from monitor.services.BuildsServiceImpl import BuildsServiceImpl
from monitor.services.OptimusServiceImpl import OptimusServiceImpl
from remote.OptimusCloudManager import OptimusCloudManager

from Constants import Constants
from model.Attributes import Attributes

attributes = Attributes()


class SuiteListener(unittest.TestResult):
    builds_client = BuildsClient()
    builds_service = BuildsServiceImpl()
    optimus_cloud_manager = OptimusCloudManager()
    session_info = SessionInfo()

    def startTestRun(self):
        self.builds_service.notify_build_start()
        self.builds_service.update_build_run_mode("Distribution")

    def stopTest(self, test: unittest.case.TestCase) -> None:
        self.builds_service.notify_build_end()
        self.builds_service.update_build_with_unique_scenarios()
