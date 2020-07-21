import requests

from monitor.entities.MongoService import MongoService
from monitor.requests.Scenario import Scenario
from monitor.requests.ScreenShot import ScreenShot


class ScenariosClient(object):
    pass

    SCENARIOS = MongoService.MONGO_SERVICE + "/scenarios"

    def create_new_scenario(self, scenario: Scenario(), lines: list):
        if len(lines) > 1:
            print("Scenario lines {}".format(lines))
            scenarios_count = self.get_number_of_existing_scenarios_by_name(scenario.buildId, scenario.scenarioName)
            scenario.dataRowNumber = ++scenarios_count
        scenario_id = requests.post(
            url=self.SCENARIOS,
            headers={"Content-Type": "application/json"},
            json=scenario.__dict__
        )
        return scenario_id.json()

    def get_number_of_existing_scenarios_by_name(self, build_id, scenario_name):
        scenario_id = requests.get(
            url=self.SCENARIOS + "/search/countByBuildIdAndScenarioName",
            params={"buildId": build_id, "scenarioName": scenario_name},
            headers={"Content-Type": "application/json"}
        )
        return int(scenario_id.json())

    def find_relevant_scenario(self, build_id, feature_name, scenario_name, location: int, device_id):
        response = requests.get(
            url=self.SCENARIOS + "/search/findByBuildIdAndFeatureFileNameAndScenarioNameAndLocationAndDeviceId",
            headers={"Content-Type": "application/json"},
            params={"deviceId": device_id, "location": location, "scenarioName": scenario_name,
                    "featureFileName": feature_name, "buildId": build_id}
        )
        return response.json()

    def update_scenario(self, build_id, scenario: Scenario()):
        response = requests.patch(
            url="{}/{}".format(self.SCENARIOS, scenario["id"]),
            headers={"Content-Type": "application/json"},
            json=scenario
        )
        return response.json()

    def load_screenshot(self, screenshot: ScreenShot):
        response = requests.post(
            url=MongoService.MONGO_SERVICE + "/screenshots",
            headers={"Content-Type": "application/json"},
            json=screenshot.__dict__
        )
        return response.json()

    def get_distinct_scenarios(self):
        response = requests.get(
            url=self.SCENARIOS + "/distinct",
            headers={"Content-Type": "application/json"},
        )
        return response.json()

    def get_build_scenario_count(self, build_id):
        response = requests.get(
            url=self.SCENARIOS + "/search/countByBuildId",
            params={"buildId": build_id}
        )
        return int(response.json())

    def get_build_scenario_count_by_status(self, build_id, status):
        response = requests.get(
            url=self.SCENARIOS + "/search/countByBuildIdAndStatus",
            headers={"Content-Type": "application/json"},
            params={"buildId": build_id, "status": status}
        )
        return int(response.json())

    def get_distinct_scenarios_by_device_id(self, build_id):
        response = requests.get(
            url=self.SCENARIOS + "/distinctDeviceId",
            headers={"Content-Type": "application/json"},
            params={"buildId": build_id}
        )
        return response.json()

    def get_scenarios_by_activity(self, build_id, device_id, activity):
        response = requests.get(
            url=self.SCENARIOS + "/search/findByBuildIdAndDeviceIdAndActivity",
            headers={"Content-Type": "application/json"},
            params={"buildId": build_id, "deviceId": device_id, "activity": activity}
        )
        return response.json().get("content")[0].get("content")

    def get_scenario_by_id(self, id):
        response = requests.get(
            url=self.SCENARIOS + "/search/",
            params={"scenarioId": id},
            headers={"Content-Type": "application/json"},
        )
        return response.json()
