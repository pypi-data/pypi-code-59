from monitor.clients.DeviceClient import DeviceClient
from monitor.services.DevicesService import DevicesService
from monitor.services.OptimusServiceImpl import OptimusServiceImpl
from monitor.utils.DeviceToDeviceDetailsMapper import DeviceToDeviceDetailsMapper
from monitor.utils.DictToClass import DictToClass


class DevicesServiceImpl(OptimusServiceImpl, DevicesService):

    def get_device_by_udid(self, udid):
        latest_id = OptimusServiceImpl.get_latest_id(self)
        device_udid = DeviceClient().get_device_by_udid(latest_id, udid)
        return DeviceToDeviceDetailsMapper().get_device_details(device_udid)

    def get_all_devices(self):
        latest_id = OptimusServiceImpl.get_latest_id(self)
        return DeviceClient().get_all_devices(latest_id)

    def insert_device_list(self, device_details_list: list):
        latest_id = OptimusServiceImpl.get_latest_id(self)
        device_details = DeviceToDeviceDetailsMapper().get_devices_from_device_details(latest_id, device_details_list)
        return DeviceClient().store_devices(device_details)

    def update_first_available_device_to_engaged(self, udid):
        latest_id = OptimusServiceImpl.get_latest_id(self)
        return DeviceClient().get_device_by_udid(latest_id, udid)

    def update_device_screenshot(self, udid: str, screenshot: []):
        latest_id = OptimusServiceImpl.get_latest_id(self)
        device_to_update = DeviceClient().get_device_by_udid(latest_id, udid)
        attr_dict = DictToClass(device_to_update)
        device_to_update["screenshot"] = screenshot
        return DeviceClient().store_screenshot(latest_id, attr_dict)

    def update_status_to_available_for_device(self, udid):
        latest_id = OptimusServiceImpl.get_latest_id(self)
        device_to_update = DeviceClient().get_device_by_udid(latest_id, udid)
        attr_dict = DictToClass(device_to_update)
        attr_dict["status"] = "Available"
        DeviceClient().release_device(attr_dict)

