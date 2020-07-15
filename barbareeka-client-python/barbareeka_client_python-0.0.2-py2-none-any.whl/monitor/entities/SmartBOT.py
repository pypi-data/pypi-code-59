from appium import webdriver
from appium.webdriver.appium_service import AppiumService

from monitor.entities.TestCase import TestCase


class SmartBOT(object):
    belongsTo: str
    capabilities: {}
    deviceUdid: str
    appiumService: AppiumService()
    driver: webdriver
    runsOn: str
    appPackageName: str
    deviceId: str
    testName: str
    testCase: TestCase

    def __init__(self):
        self.belongsTo = str()
        self.capabilities = {}
        self.deviceUdid = str()
        self.appiumService = AppiumService()
        self.driver = webdriver
        self.runsOn = str()
        self.appPackageName = str()
        self.deviceId = str()
        self.testName = str()
        self.testCase = TestCase()
