import unittest
from datetime import datetime

from entities.MobileDriverDetails import MobileDriverDetails
from remote.OptimusCloudManager import OptimusCloudManager

from Constants import Constants
from TestStatus import TestStatus
from builders.ScenarioBuilder import ScenarioBuilder
from builders.SmartBotBuilder import SmartBotBuilder
from listeners.SuiteListener import SuiteListener
from model.Attributes import Attributes
from monitor.clients.DeviceClient import DeviceClient
from monitor.clients.ScenariosClient import ScenariosClient
from monitor.entities.Device.Status import Status
from monitor.entities.DeviceDetails import DeviceDetails
from monitor.entities.SmartBOT import SmartBOT
from monitor.entities.reportParser.Step import Step
from monitor.performance.ScenarioMonitor import ScenarioMonitor
from monitor.requests.Device import Device
from monitor.services.BuildsServiceImpl import BuildsServiceImpl
from monitor.services.DevicesServiceImpl import DevicesServiceImpl

attributes = Attributes()


class TestListener(unittest.TestResult):
    devices_client = DeviceClient()
    builds_service = BuildsServiceImpl()
    devices_service = DevicesServiceImpl()
    smartBOT = SmartBOT()
    device = Device()
    mobile_driver_details = MobileDriverDetails()
    build_id = str()
    scenario_monitor = ScenarioMonitor

    def listen_to_service(self, attributes: Attributes):
        # def startTest(self, test: unittest.case.TestCase) -> None:
        SuiteListener().startTestRun()
        TestListener.attributes = attributes
        TestListener.build_id = self.builds_service.get_latest_id()

        self.mobile_driver_details = TestListener.attributes.attributes.get(Constants.MOBILE_DRIVER.value)
        self.device = self.create_device_collection(self.mobile_driver_details)
        TestListener.smartBOT = SmartBotBuilder(mobile_driver_details=self.mobile_driver_details,
                                                smartBOT=None).with_device_id(
            self.device["id"]).build()
        # TODO: implement performance in barbareeka
        self.scenario_monitor = ScenarioMonitor(TestListener.smartBOT)
        self.scenario_monitor.start()
        new_scenario = self.create_scenario()
        scenario = ScenariosClient().create_new_scenario(new_scenario, lines=[])
        self.set_attributes(TestListener.smartBOT, self.mobile_driver_details, scenario)

    def create_scenario(self):
        scenario_builder = ScenarioBuilder(scenario=None, test_case=TestListener.smartBOT.testCase)
        scenario_builder.with_build_id(self.builds_service.get_latest_id()).with_device_id(self.device["id"])
        return scenario_builder.build()

    def addSuccess(self, test: unittest.case.TestCase) -> None:
        self.update_scenario_with_status(test, TestStatus.PASSED.value, False)

    def addFailure(self, test: unittest.case.TestCase, err) -> None:
        self.update_scenario_with_status(test, TestStatus.FAILED.value, False)

    def addSkip(self, test: unittest.case.TestCase, reason: str) -> None:
        self.update_scenario_with_status(test, TestStatus.SKIPPED.value, False)

    def update_scenario_with_status(self, test, status, failed_on_screen):
        # self.release_device()
        scenario = attributes.attributes.get(Constants.SCENARIO.value)
        if scenario is None:
            scenario = ScenarioBuilder(scenario=None, test_case=None).build()
        mobile_driver_details = attributes.attributes.get(Constants.MOBILE_DRIVER.value)
        scenario_builder = ScenarioBuilder(scenario=scenario, test_case=None)

        end_time = int(datetime.now().strftime("%s"))
        start_time = int(datetime.strptime(scenario.get("startTime"), "%Y-%m-%dT%H:%M:%S.%f+0000").timestamp())

        scenario_builder_updated = scenario_builder \
            .with_status(status) \
            .with_step(self.get_steps(test)) \
            .with_end_time(scenario.get("endTime")) \
            .with_time_taken(self.get_time_taken(end_time, start_time))

        scenario["status"] = scenario_builder_updated.scenario["status"]
        scenario["steps"] = scenario_builder_updated.scenario["steps"]
        scenario["endTime"] = scenario_builder_updated.scenario["endTime"]
        scenario["timeTaken"] = scenario_builder_updated.scenario["timeTaken"]

        if failed_on_screen:
            if mobile_driver_details is not None:
                scenario_builder_updated.with_failed_on_screen(self.take_screenshot(mobile_driver_details))
        # TODO: scenario = scenario_builder_updated.build()
        ScenariosClient().update_scenario(self.build_id, scenario)
        ScenarioMonitor(self).stop(scenario, TestListener.smartBOT)
        SuiteListener().stopTest(test)

    def release_device(self):
        try:
            OptimusCloudManager().releaseSession(self.mobile_driver_details)
        except Exception:
            raise Exception

    def get_steps(self, test: unittest.TestCase):
        steps = []
        step = Step()
        step.keyword = "Description: "
        try:
            if test.failureException.__str__(BaseException()) is not None:
                step.error_message = test.failureException.__str__(BaseException())
        except Exception as error:
            print(error)
        if int(unittest.TestResult.wasSuccessful(self)) == 0:
            step.status = "failed"
        else:
            step.status = "passed"
        # TODO: step.duration =
        self.add_description(step, test)
        steps.append(step)
        return steps

    def add_description(self, step: Step, test: unittest.TestCase):
        description = test.shortDescription()
        if not description:
            step.name = "No Description found!!"
        else:
            step.name = description

    def create_device_collection(self, mobile_driver_details: MobileDriverDetails):
        desired_capabilities = mobile_driver_details.desiredCapabilities
        device_details = DeviceDetails()
        device_details.status = Status.Available
        device_details.udid = desired_capabilities.get("udid")
        device_details.platform = desired_capabilities.get("platformName")
        device_details.runsOn = desired_capabilities.get("deviceType")
        device_details.deviceName = desired_capabilities.get("deviceName")
        device_details.platformVersion = desired_capabilities.get("platformVersion")
        is_device_present = False
        try:
            all_devices = self.devices_client.get_all_devices(self.builds_service.get_latest_id())
            b = False
            for all_device in all_devices:
                if all_device.udid == device_details.udid:
                    # TODO: check this one out to insert the device.
                    b = True
                    break
            is_device_present = b
        except Exception as error:
            print(error)
        if not is_device_present:
            self.devices_service.insert_device_list([device_details])
        device_by_udid = DeviceClient().get_device_by_udid(self.builds_service.get_latest_id(), device_details.udid)
        return device_by_udid

    def get_time_taken(self, end_time, start_time):
        time_taken = end_time - start_time
        return int(time_taken)

    def take_screenshot(self, mobile_driver_details):
        return mobile_driver_details.mobileDriver.get_screenshot_as_base64()

    def set_attributes(self, smart_bot, mobile_driver_details, scenario):
        name = "name"
        # smart_bot_key = "{} {}".format(name, Constants.SMART_BOT.value)
        # mobile_driver_details_key = "{} {}".format(name, Constants.MOBILE_DRIVER.value)
        # scenario_key = "{} {}".format(name, Constants.SCENARIO.value)
        attributes.attributes.update({Constants.SMART_BOT.value: smart_bot})
        attributes.attributes.update({Constants.MOBILE_DRIVER.value: mobile_driver_details})
        attributes.attributes.update({Constants.SCENARIO.value: scenario})
