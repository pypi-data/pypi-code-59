from unittest.result import TestResult

from entities.MobileDriverDetails import MobileDriverDetails
from monitor.entities.SmartBOT import SmartBOT

from Constants import Constants
from builders.TestCaseBuilder import TestCaseBuilder


class SmartBotBuilder(object):
    test_result: TestResult()
    smartBOT: SmartBOT()
    test_case_builder: TestCaseBuilder
    mobile_driver_details: MobileDriverDetails()

    def __init__(self, mobile_driver_details, smartBOT):
        if smartBOT is None:
            self.smartBOT = SmartBOT()
        else:
            self.smartBOT = smartBOT
        self.test_case_builder = TestCaseBuilder(test_case=None)
        self.mobile_driver_details = mobile_driver_details
        desired_capabilities = mobile_driver_details.desiredCapabilities
        self.with_app_package(desired_capabilities["appPackage"])
        self.with_desired_capabilities(desired_capabilities)
        self.with_test_case(self.test_case_builder.build())
        self.with_udid(mobile_driver_details.udid)

    def with_desired_capabilities(self, desired_capabilities):
        self.smartBOT.capabilities = desired_capabilities
        return self

    def with_app_package(self, package):
        self.smartBOT.appPackageName = package

    def get_app_package(self):
        return self.mobile_driver_details.desiredCapabilities.get(Constants.APP_PACKAGE.value)

    def with_test_case(self, test_case):
        self.smartBOT.testCase = test_case
        return self

    def with_udid(self, udid):
        self.smartBOT.deviceUdid = udid
        return self

    def with_device_id(self, id):
        self.smartBOT.deviceId = id
        return self

    def build(self):
        return self.smartBOT
