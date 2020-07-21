from datetime import datetime

from monitor.clients.ScenariosClient import ScenariosClient
from monitor.entities.ScenarioTimeline import ScenarioTimeline
from monitor.entities.SmartBOT import SmartBOT
from monitor.entities.reportParser import ExecutedScenario
from monitor.requests.Scenario import Scenario
from monitor.requests.ScreenShot import ScreenShot
from monitor.services.OptimusServiceImpl import OptimusServiceImpl
from monitor.services.ScenariosService import ScenariosService


class ScenariosServiceImpl(ScenariosService):
    latest_id = OptimusServiceImpl().get_latest_id()
    date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    time_now = datetime.strftime(datetime.now(), date_format)

    def notify_BOT_registration(self, smartBOT: SmartBOT):
        scenario = Scenario()

        scenario.scenarioName = smartBOT.testCase.name
        scenario.startTime = self.time_now
        scenario.featureName = smartBOT.testCase.featureFileName
        scenario.deviceId = smartBOT.deviceId
        scenario.tags = smartBOT.testCase.sourceTagNames
        scenario.buildId = self.latest_id
        scenario.location = self.get_location(smartBOT)
        ScenariosClient().create_new_scenario(scenario, smartBOT.testCase.lines)

    def notify_scenario_completion(self, smartBOT: SmartBOT):
        scenario: Scenario()
        scenario = ScenariosClient().find_relevant_scenario(self.latest_id, smartBOT.testCase.featureFileName,
                                                            smartBOT.testCase.name,
                                                            self.get_location(smartBOT), smartBOT.deviceId)
        end_time = int(datetime.now().strftime("%s"))
        scenario.startTime = datetime.strptime(scenario.startTime, "%Y-%m-%dT%H:%M:%S%z")
        time_taken = end_time - scenario.startTime.timestamp()
        scenario.status = smartBOT.testCase.status.lower()
        scenario.completed = True
        scenario.endTime = self.time_now
        scenario.timeTaken = time_taken
        scenario.location = self.get_location(smartBOT)
        print("making scenario update call on completion")
        ScenariosClient().update_scenario(self.latest_id, scenario)

    def get_latest_record_for(self, scenario: ExecutedScenario):
        executed_scenario = self.get_scenario_by_name_and_location(scenario)

    def update_scenario_time_line(self, scenario, smartBOT, scenario_time_lines):
        scenario_client = ScenariosClient()
        if scenario is None:
            scenario = self.get_scenario(smartBOT)
        scenario_time_line = ScenarioTimeline()
        for scenario_time_line in scenario_time_lines:
            if scenario_time_line.screenshotData is not None:
                file_name = "{} {} {}".format(scenario.id, "_", scenario_time_line.interval)
                scenario_time_line.screenshotFileName = file_name
                screen_shot = ScreenShot()
                screen_shot.file_name = file_name
                screen_shot.data = scenario_time_line.screenshotData
                scenario_client.load_screenshot(screen_shot)
                scenario_time_line.screenshotData = None
        scenario["scenarioTimeline"] = scenario_time_line.__dict__
        scenario_client.update_scenario(self.latest_id, scenario)

    def update_crashes(self, smartBOT: SmartBOT, exceptions, activity):
        scenario = self.get_scenario(smartBOT)
        scenario.stacktrace = exceptions
        scenario.activity = activity
        ScenariosClient().update_scenario(self.latest_id, scenario)

    def get_location(self, smartBOT):
        return smartBOT.testCase.lines[0]

    def get_scenario_by_name_and_location(self, executed_scenario: ExecutedScenario):
        scenario_id = executed_scenario.id
        location = scenario_id[scenario_id.rfind("-") + 1:]
        scenario_name = scenario_id[0:scenario_id.rfind("-")]
        print("scenario name is {}".format(scenario_name))
        print("scenario location is {}".format(location))
        print("Device id is {}".format(executed_scenario.deviceName))
        print("Latest build is {}".format(self.latest_id))
        return ScenariosClient().find_relevant_scenario(self.latest_id, executed_scenario.featureName, scenario_name,
                                                        int(location), executed_scenario.deviceName)

    def get_scenario(self, smartBOT: SmartBOT):
        return ScenariosClient().find_relevant_scenario(self.latest_id, smartBOT.testCase.featureFileName,
                                                        smartBOT.testCase.name, self.get_location(smartBOT),
                                                        smartBOT.deviceId)

    def is_scenario_outline(self, smartBOT: SmartBOT):
        print(smartBOT.testCase.lines)
        return len(smartBOT.testCase.lines) > 1
