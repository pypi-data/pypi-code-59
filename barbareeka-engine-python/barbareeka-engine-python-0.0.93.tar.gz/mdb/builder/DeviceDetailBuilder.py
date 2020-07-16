from monitor.entities.DeviceDetails import DeviceDetails


class DeviceDetailBuilder(object):
    device_detail = DeviceDetails()

    def with_device_udid(self, device_udid):
        self.device_detail.udid = device_udid
        return self.device_detail

    def with_platform(self, platform):
        self.device_detail.platform = platform
        return self.device_detail

    def with_os_version(self, os_version):
        self.device_detail.platformVersion = os_version
        return self.device_detail

    def with_device_type(self, device_type):
        self.device_detail.runsOn = device_type
        return self.device_detail

    def with_status(self, status):
        self.device_detail.status = status
        return self.device_detail

    def with_device_name(self, device_name):
        self.device_detail.deviceName = device_name
        return self.device_detail

    def build(self):
        return self.device_detail
