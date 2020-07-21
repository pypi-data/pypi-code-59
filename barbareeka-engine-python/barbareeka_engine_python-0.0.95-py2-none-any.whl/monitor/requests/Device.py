class Device(object):
    id = str()
    status = str()
    platform = str()
    deviceName = str()
    runsOn = str()
    platformVersion = str()
    udid = str()
    buildId = str()
    screenshot = list()

    def __str__(self) -> str:
        return "{ id={}".format(self.id) + \
               ", status={}".format(self.status) + \
               ", device_name={}".format(self.deviceName) + \
               ", runs_on={}".format(self.runsOn) + \
               ", platform_version={}".format(self.platformVersion) + \
               ", udid={}".format(self.udid) + \
               ", platform={}".format(self.platform) + '}'

    def __init__(self, *args, **kwargs):
        super(Device, self).__init__(*args, **kwargs)
        self.__dict__ = self.__dict__
