from sys import platform

from mdb.core.Mobile import Mobile
from mdb.exceptions.ConnectedDevicesException import ConnectedDevicesException
from mdb.exceptions.UnsupportedPlatformException import UnsupportedPlatformException
from mdb.helpers.IOSHelper import IOSHelper
from mdb.ios.IDB import IDB
from mdb.utils.Commands import Commands
from monitor.entities.Device.Platform import Platform


class IOS(Mobile, IDB):
    device_details_list: []

    def __init__(self):
        if platform == "darwin":
            self.device_details_list = []
            self.collect_device_details()
        else:
            raise UnsupportedPlatformException("Your OS does not support IOS Commands")

    def collect_device_details(self):
        devices = Mobile.collect_devices_output(self, Platform.IOS)
        collected_devices = []
        for line in devices:
            if line is not Commands.AndroidCommands.ADB_HEADER.value:
                collected_devices.append(line)
        if len(collected_devices) == 0:
            raise ConnectedDevicesException("Could not find any devices, are any devices available?")
        else:
            ios_helper = IOSHelper(self.device_details_list)
            # ios_helper.init_a_device(collected_devices)
            ios_helper.init_simulators(collected_devices)
