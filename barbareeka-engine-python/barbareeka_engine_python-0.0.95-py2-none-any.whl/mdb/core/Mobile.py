import abc
import os

from mdb.utils.Commands import Commands
from monitor.entities.Device import Platform


class Mobile(metaclass=abc.ABCMeta):
    pass

    def collect_devices_output(self, platform: Platform):
        command = str
        if platform is platform.ANDROID:
            command = Commands.AndroidCommands.LIST_ALL_DEVICES.value
        elif platform is platform.IOS:
            command = Commands.Instruments.LIST_ALL_DEVICES.value
        devices = [os.popen(command).read()]
        return devices

    @abc.abstractmethod
    def collect_device_details(self):
        pass
