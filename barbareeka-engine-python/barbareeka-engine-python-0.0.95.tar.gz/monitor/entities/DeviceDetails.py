from monitor.entities.Device.DeviceType import DeviceType
from monitor.entities.Device.Platform import Platform
from monitor.entities.Device.Status import Status


class DeviceDetails(object):
    udid = str()
    deviceName = str()
    platform = Platform
    platformVersion = str()
    runsOn = DeviceType
    status = Status

    def __str__(self):
        return "DeviceDetails { " + \
               "deviceName={}" + format(self.deviceName) + \
               ", udid={}" + format(self.udid) + \
               ", status={}" + format(self.status.name) + \
               ", platform={}" + format(self.platform) + \
               ", platformVersion={}" + format(self.platformVersion) + \
               ", runsOn={}" + format(self.runsOn) + \
               '}'

    # def __init__(self):
    #     self.udid = str()
    #     self.deviceName = str()
    #     self.platform =
    #     self.platformVersion = str()
    #     self.runsOn = DeviceType
    #     self.status = Status.value
