from monitor.entities.DeviceDetails import DeviceDetails
from monitor.requests.Device import Device


class DeviceToDeviceDetailsMapper(object):

    def get_devices_from_device_details(self, latest_build_id: str, device_details_list: list):
        device_list = []
        for device_details in device_details_list:
            device = self.get_device(latest_build_id, device_details)
            device_list.append(device)
        return device_list

    def get_device(self, latest_build_id, device_details: DeviceDetails):
        device = Device()
        device.platform = device_details.platform
        device.buildId = latest_build_id
        device.deviceName = device_details.deviceName
        device.runsOn = device_details.runsOn
        device.udid = device_details.udid
        device.platformVersion = device_details.platformVersion
        return device

    def get_device_details(self, device: Device()):
        device_details = DeviceDetails()
        device_details.runsOn = device.get("runsOn")
        device_details.status = device.get("status")
        device_details.platform = device.get("platform")
        device_details.platformVersion = device.get("platformVersion")
        device_details.deviceName = device.get("deviceName")
        device_details.udid = device.get("udid")
        return device_details

    def get_device_details_from_devices(self, device_list: []):
        device_details_list = []
        for device in device_list:
            device_details = self.get_device_details(device)
            device_details_list.append(device_details)
        return device_details_list
