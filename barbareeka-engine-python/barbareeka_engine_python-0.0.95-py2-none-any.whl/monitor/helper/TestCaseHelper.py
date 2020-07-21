from sys import platform

from monitor.entities.TestCase import TestCase


class TestCaseHelper(object):
    testCase: TestCase

    def __init__(self, testCase) -> None:
        self.testCase = testCase

    def get_line_number(self):
        id = TestCaseHelper.testCase.id
        if ":" not in id:
            if platform == "win32":
                colon_index = id.rfind(":")
                return id[colon_index + 1:len(id)]
            else:
                uriArray = id.split(":")
                if len(uriArray) > 1:
                    return uriArray[1]
        return "0"

    def get_scenario_name(self):
        return self.testCase.name.replace(" ", "-")

    def get_unique_scenario_name(self):
        print("Scenario id {}".format(self.testCase.id))
        print("Scenario name {}".format(self.testCase.name))
        if self.testCase is None:
            raise TypeError
        return self.get_scenario_name() + " - " + self.get_line_number()
