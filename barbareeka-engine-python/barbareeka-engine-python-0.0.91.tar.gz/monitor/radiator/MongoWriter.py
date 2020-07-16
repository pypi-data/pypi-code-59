from monitor.constants.MongoDB import KEY_SCENARIOS_SCENARIO_NAME, DATABASE_NAME, COLLECTION_SCENARIOS, QUERY_AND, \
    KEY_SCENARIOS_START_TIME, ID
from monitor.entities.SmartBOT import SmartBOT
from monitor.helper.TestCaseHelper import TestCaseHelper
from monitor.radiator.MongoIO import MongoIO
from monitor.requests.Scenario import Scenario


class MongoWriter(MongoIO):

    def __init__(self) -> None:
        super().__init__()

    def set_scenario_location(self, smartBOT: SmartBOT, scenario: Scenario):
        lines = smartBOT.testCase.lines
        if self.is_scenario_outline(smartBOT):
            scenario.location = lines[1]
        else:
            scenario.location = lines[0]

    def is_scenario_outline(self, smartBOT: SmartBOT):
        return len(smartBOT.testCase.lines) > 1

    def get_location(self, smartBOT: SmartBOT):
        if self.is_scenario_outline(smartBOT):
            return smartBOT.testCase.lines[1]
        else:
            return smartBOT.testCase.lines[0]

    def get_latest_record_for(self, smartBOT: SmartBOT):
        unique_scenario_name = TestCaseHelper(smartBOT.testCase).get_unique_scenario_name()
        objects = {KEY_SCENARIOS_SCENARIO_NAME: unique_scenario_name}
        # objects = {KEY_SCENARIOS_SCENARIO_NAME: unique_scenario_name,
        #                  "status": "skipped"}
        and_query = {QUERY_AND: [objects]}
        collection = self.mongo_client[DATABASE_NAME][COLLECTION_SCENARIOS]
        for document in collection.find(and_query).sort(KEY_SCENARIOS_START_TIME, -1):
            return document.get(ID)

