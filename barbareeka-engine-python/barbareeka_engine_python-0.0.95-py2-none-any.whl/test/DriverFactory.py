import unittest

from remote.OptimusCloudDriver import OptimusCloudDriver
from remote.OptimusCloudManager import OptimusCloudManager

from Constants import Constants
from listeners.TestListener import TestListener
from model.Attributes import Attributes


class DriverFactory(unittest.TestCase):
    def setUp(self) -> None:
        desired_caps = {
            'platformName': 'Android',
            'appPackage': 'com.cleartrip.android',
            'appActivity': 'com.cleartrip.android.activity.common.SplashActivity'
        }
        self.mobileDriverDetails = OptimusCloudDriver().createDriver(desiredCapabilities=desired_caps)
        self.driver = self.mobileDriverDetails.mobileDriver
        attribute = Attributes()
        attribute.attributes = {Constants.MOBILE_DRIVER.value.__str__(): self.mobileDriverDetails}
        TestListener().listen_to_service(attribute)

    def tearDown(self) -> None:
        OptimusCloudManager().releaseSession(self.mobileDriverDetails)
