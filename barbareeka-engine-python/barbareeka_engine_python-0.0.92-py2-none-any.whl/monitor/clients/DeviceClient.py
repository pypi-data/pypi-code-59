import requests

from monitor.entities.MongoService import MongoService
from monitor.exceptions.DeviceEngagedException import DeviceEngagedException
from monitor.exceptions.DeviceReleaseException import DeviceReleaseException
from monitor.requests import Device
from monitor.utils.DeviceToDeviceDetailsMapper import DeviceToDeviceDetailsMapper
from monitor.utils.DictToClass import DictToClass


class DeviceClient:
    DEVICE = MongoService.MONGO_SERVICE + "/devices"

    def store_devices(self, devices: list):
        response = dict
        for device in devices:
            device.status = "Available"
            response = requests.post(
                url=self.DEVICE,
                headers={"Content-Type": "application/json"},
                json=device.__dict__
            )
        return DictToClass(response.json())

    def get_all_devices(self, build_id):
        response = requests.get(
            url="{}{}".format(self.DEVICE, "/search/findAllByBuildId"),
            headers={"Content-Type": "application/json"},
            params={"buildId": build_id}
        )
        device_response = DictToClass(response.json()).content
        return DeviceToDeviceDetailsMapper().get_device_details_from_devices(device_response)

    def get_device(self, build_id, device: Device):
        response = requests.get(
            url=self.DEVICE + "/findMatchingDevice",
            headers={"Content-Type": "application/json"},
            params={"buildId": build_id},
            json=device.__dict__
        )
        return response.json()

    def get_device_by_udid(self, build_id, udid):
        device_response = requests.get(
            url="{}{}".format(self.DEVICE, "/search/findByBuildIdAndUdid"),
            params={"buildId": build_id, "udid": udid},
            headers={"Content-Type": "application/json"},
        )
        return device_response.json()

    def store_screenshot(self, build_id, device: Device):
        device_to_update = self.get_device_by_udid(build_id, device.udid)
        return requests.put(
            url=self.DEVICE + device_to_update,
            headers={"Content-Type": "application/json"},
            data=device_to_update.json.get("udid")
        )

    def update_device(self, device: Device):
        engaged_device_response = requests.put(
            url=self.DEVICE + device.udid,
            headers={"Content-Type": "application/json"},
            json=device.__dict__
        )
        print(engaged_device_response.text)
        try:
            device1 = engaged_device_response.json()
            return DeviceToDeviceDetailsMapper().get_device_details(device1)
        except Exception as error:
            print(error)
            raise DeviceEngagedException()

    def release_device(self, device: Device):
        release_device_response = requests.put(
            url=self.DEVICE + "/" + device.id,
            headers={"Content-Type": "application/json"},
            json=device.__dict__
        )
        try:
            device1 = release_device_response.json()
            return DeviceToDeviceDetailsMapper().get_device_details(device1)
        except Exception as error:
            print(error)
            raise DeviceReleaseException(device.udid)

    def get_device_by_id(self, device_id: str):
        response = requests.get(
            url=self.DEVICE + device_id,
            headers={"Content-Type": "application/json"}
        )
        return response.json()
