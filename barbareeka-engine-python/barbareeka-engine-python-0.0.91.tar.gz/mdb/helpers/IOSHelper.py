import re

from mdb.builder.DeviceDetailBuilder import DeviceDetailBuilder
from mdb.utils.Commands import Commands
from monitor.entities.Device import DeviceType
from monitor.entities.Device import Platform
from monitor.entities.Device import Status


class IOSHelper(object):
    device_details = list()

    def __init__(self, device_details: list):
        self.device_details = device_details

    def init_simulators(self, process_log: []):
        for process in process_log:
            if self.is_simulator(process):
                simulator = self.get_simulator(process)
                self.device_details.append(simulator)

    def is_simulator(self, process: str):
        if "[" not in process:
            return False
        pattern_from_process = self.get_pattern_from_process(process)
        return re.match(Commands.Instruments.SIMULATOR_UDID_PATTERN.value, pattern_from_process) and process.startswith(
            "iPhone") and "+" not in process

    def get_simulator(self, process):
        udid = self.get_udid(process)
        device_name = self.get_device_name(process)
        ios_version = self.get_ios_version(process)
        simulator = DeviceDetailBuilder()
        simulator.with_device_type(DeviceType.DeviceType.SIMULATOR)
        simulator.with_status(Status.Status.Available)
        simulator.with_platform(Platform.Platform.IOS)
        simulator.with_device_udid(udid)
        simulator.with_device_name(device_name)
        simulator.with_os_version(ios_version)
        return simulator

    def get_udid(self, process: str):
        start_index = process.index("[") + 1
        end_index = process.index("]")
        return process[start_index:end_index]

    def get_device_name(self, process: str):
        index = process.index("(")
        return process[0:index].strip()

    def get_ios_version(self, process: str):
        ios_version_str = process.replace("(Simulator)", "").strip()
        ios_start_value = ios_version_str.index("(")
        ios_last_value = ios_version_str.index(")")
        return ios_version_str[ios_start_value + 1:ios_last_value]

    def get_pattern_from_process(self, process: str):
        start = process.index("[") + 1
        end = process.index("]")
        return process[start:end]
