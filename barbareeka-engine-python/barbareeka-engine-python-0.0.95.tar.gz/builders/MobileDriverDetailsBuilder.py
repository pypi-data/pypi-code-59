import unittest

from entities.MobileDriverDetails import MobileDriverDetails
from monitor.entities.Device.DeviceType import DeviceType
from monitor.entities.Device.Platform import Platform


class MobileDriverDetailsBuilder(unittest.TestRunner):
    mobile_driver_details: MobileDriverDetails()
    desired_capabilities: {}

    def __init__(self):
        self.mobile_driver_details = MobileDriverDetails()
        self.desired_capabilities = dict()
        self.set_defaults()

    def with_device_name(self, device_name):
        self.desired_capabilities["deviceName"] = device_name
        return self

    def with_platform(self, platform):
        self.desired_capabilities["platform"] = platform
        self.desired_capabilities["platformName"] = platform
        return self

    def with_device_type(self, device_type):
        self.desired_capabilities["deviceType"] = device_type
        return self

    def with_platform_version(self, version):
        self.desired_capabilities["platformVersion"] = version
        return self

    def with_udid(self, udid):
        self.desired_capabilities["udid"] = udid
        self.mobile_driver_details.udid = udid
        return self

    def set_defaults(self):
        self.default_device_name()
        self.default_udid()
        self.default_platform()
        self.default_platform_version()
        self.default_device_type()

    def default_device_name(self):
        if self.desired_capabilities["deviceName"]:
            self.with_device_name("Optimus_Device")

    def default_platform(self):
        if self.desired_capabilities["platform"] or self.desired_capabilities["platformName"] is None:
            self.with_platform(Platform.ANDROID.value)
        if self.desired_capabilities["platformName"] is not None:
            self.with_platform("platformName")

    def default_udid(self):
        if self.desired_capabilities["udid"] is None:
            self.with_device_name("NSM3Y18213011358")

    def default_platform_version(self):
        if self.desired_capabilities["platformVersion"] is None:
            self.with_platform_version("9")

    def default_device_type(self):
        if self.desired_capabilities["deviceType"] is None:
            self.with_device_type(DeviceType.DEVICE.value)

    def build(self):
        if self.mobile_driver_details is None:
            raise Exception("Cannot build mobile driver details without mobile driver")
        self.mobile_driver_details.desiredCapabilities = self.desired_capabilities
        return self.mobile_driver_details
