import os

from mdb.builder.DeviceDetailBuilder import DeviceDetailBuilder
from mdb.utils.Commands import Commands
from monitor.entities.Device.DeviceType import DeviceType
from monitor.entities.Device.Platform import Platform
from monitor.entities.Device.Status import Status


class AndroidHelper(object):
    device_details = list()

    def __init__(self, device_details: list):
        self.device_details = device_details

    def init_a_emulator(self, process_log):
        for process in process_log:
            if self.is_emulator(process):
                udid = self.get_udid(process)
                model = self.get_model(udid)
                os_version = self.get_os_version(udid)
                emulator = DeviceDetailBuilder()
                emulator.with_device_type(DeviceType.EMULATOR.value)
                emulator.with_status(Status.Available)
                emulator.with_platform(Platform.ANDROID)
                emulator.with_device_udid(udid)
                emulator.with_device_name(model)
                emulator.with_os_version(os_version)
                self.device_details.append(emulator)

    def init_a_device(self, process_log):
        for process in process_log:
            if self.is_device(process):
                udid = self.get_udid(process)
                model = self.get_model(udid)
                os_version = self.get_os_version(udid)
                device = DeviceDetailBuilder()
                device.with_device_type(DeviceType.DeviceType.DEVICE)
                device.with_status(Status.Status.Available)
                device.with_platform(Platform.Platform.ANDROID)
                device.with_device_udid(udid)
                device.with_device_name(model)
                device.with_os_version(os_version)
                self.device_details.append(device)

    def is_emulator(self, process: str):
        return "vbox" in process or process.startswith("emulator")

    def get_udid(self, process: str):
        uid_last_char = process.index(" ")
        return process[0: uid_last_char]

    def get_model(self, udid):
        command = Commands.AndroidCommands.GET_DEVICE_MODEL.value.format(udid)
        return os.popen(command).read().replace("\n", "")

    def get_os_version(self, udid):
        command = Commands.AndroidCommands.GET_DEVICE_OS.value.format(udid)
        return os.popen(command).read().replace("\n", "")

    def is_device(self, process):
        return "vbox" not in process and not process.startswith("emulator") and not process.startsWith("* daemon")
