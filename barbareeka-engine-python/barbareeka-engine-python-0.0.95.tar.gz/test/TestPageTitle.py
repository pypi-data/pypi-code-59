import unittest
from time import sleep

from listeners.TestListener import TestListener
from test.DriverFactory import DriverFactory


class TestPageTitle(DriverFactory):
    def test_page_title(self):
        sleep(3)
        self.driver.find_element_by_id("classic_bottom_navigation_icon").click()
        assert self.driver.find_element_by_id("headerTxt").text == "Search Flights"


if __name__ == "__main__":
    # load the test from test class
    tests = unittest.defaultTestLoader.loadTestsFromTestCase(TestPageTitle)
    # create object for result class we created
    custom_result = TestListener()
    # load tests in to suite
    suite = unittest.TestSuite(tests)
    # run the suite
    final_result = suite.run(custom_result)
