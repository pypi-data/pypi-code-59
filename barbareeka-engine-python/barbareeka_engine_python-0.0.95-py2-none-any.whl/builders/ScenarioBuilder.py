import json

from monitor.entities.TestCase import TestCase
from monitor.requests.Scenario import Scenario
from monitor.utils.Utils import Utils

from builders.TestCaseBuilder import TestCaseBuilder


class ScenarioBuilder(object):
    scenario: Scenario()
    test_case: TestCase()

    def __init__(self, scenario, test_case):
        if scenario is None:
            self.scenario = Scenario()
        else:
            self.scenario = scenario
        if test_case is None:
            self.test_case = TestCaseBuilder(self)
        # self.with_feature_File_name(test_case)
        # self.with_tags(test_case.sourceTagNames)
        self.with_location(0)
        self.with_data_row(0)
        self.with_end_time(Utils().get_current_time())
        self.with_scenario_timeline("")
        self.with_failed_on_screen([])
        self.with_step([])
        self.with_status("skipped")

    def check_instance(self, key, value):
        if isinstance(self.scenario, dict):
            self.scenario[key] = value
        else:
            self.scenario.__dict__[key] = value

    def with_scenario_name(self, name):
        self.check_instance("scenarioName", name)
        return self

    def with_feature_name(self, featureFileName):
        self.check_instance("featureName", featureFileName)
        return self

    def with_feature_File_name(self, featureFileName):
        self.check_instance("featureFileName", featureFileName)
        return self

    def with_tags(self, sourceTagNames):
        self.check_instance("tags", sourceTagNames)
        return self

    def with_location(self, location):
        self.check_instance("location", location)
        return self

    def with_data_row(self, data_row):
        self.check_instance("dataRow", data_row)
        return self

    def with_scenario_timeline(self, time_line):
        self.check_instance("scenarioTimeline", time_line)
        return self

    def with_failed_on_screen(self, screen):
        self.check_instance("failedOn", screen)
        return self

    def with_status(self, status):
        self.check_instance("status", status)
        return self

    def with_step(self, steps):
        self.check_instance("steps", json.dumps(steps, default=str))
        return self

    def with_end_time(self, now):
        self.check_instance("endTime", now)
        return self

    def with_time_taken(self, time_taken):
        self.check_instance("timeTaken", time_taken)
        return self

    def with_start_time(self, now):
        self.check_instance("startTime", now)
        return self

    def build(self):
        return self.scenario

    def with_build_id(self, build_id):
        self.check_instance("buildId", build_id)
        return self

    def with_device_id(self, id):
        self.check_instance("deviceId", id)
        return self
