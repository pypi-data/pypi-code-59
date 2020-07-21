import unittest

from monitor.entities.TestCase import TestCase


class TestCaseBuilder(object):
    test_case: TestCase()

    def __init__(self, test_case):
        if test_case is None:
            self.test_case = TestCase()
        else:
            self.test_case = test_case
        self.test_case.id = unittest.TestCase().id()
        lines = [0]
        self.test_case.lines = lines
        self.test_case.name = unittest.TestCase()._testMethodName
        self.test_case.status = "passed"
        self.test_case.featureFileName = unittest.TestCase().shortDescription()

    def build(self):
        return self

    def with_status(self, status):
        if unittest.TestResult().wasSuccessful() == 0:
            status = "failed"
        else:
            status = "passed"
        self.test_case.status = status
        return self

    def with_feature_name(self, feature_name):
        self.test_case = feature_name
        return self

    def get_tags(self):
        return list()

    def buils(self):
        return self.test_case
