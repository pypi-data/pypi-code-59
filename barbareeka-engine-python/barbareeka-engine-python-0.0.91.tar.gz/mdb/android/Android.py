from mdb.android.ADB import ADB
from mdb.android.DumpSysParser import DumpSysParser
from mdb.core.Mobile import Mobile
from mdb.exceptions.ConnectedDevicesException import ConnectedDevicesException
from mdb.helpers.AndroidHelper import AndroidHelper
from mdb.utils.Commands import Commands
from monitor.entities.Device.Platform import Platform
from monitor.entities.SmartBOT import SmartBOT


class Android(Mobile, ADB):
    device_details = list()

    def __init__(self):
        self.device_details = []

    def get_memory_info(self, smartBOT: SmartBOT):
        pass

    def get_cpu_info(self, smartBOT: SmartBOT):
        return DumpSysParser(smartBOT).get_cpu_usage()

    def get_activity(self, smartBOT: SmartBOT):
        pass

    def get_devices(self):
        pass

    def collect_device_details(self):
        devices = Mobile.collect_devices_output(self, Platform.Platform.ANDROID)
        collected_devices = []
        for line in devices:
            if line is not Commands.AndroidCommands.ADB_HEADER.value:
                collected_devices.append(line)
        if len(collected_devices) == 0:
            raise ConnectedDevicesException("Could not find any devices, are any devices available?")
        else:
            android_helper = AndroidHelper(self.device_details)
            android_helper.init_a_device(collected_devices)
            android_helper.init_a_emulator(collected_devices)

    def get_exception(self, smartBOT):
        return DumpSysParser(smartBOT).get_exception()
