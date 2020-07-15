import abc


class DevicesService(abc.ABC):

    @abc.abstractmethod
    def get_device_by_udid(self, udid):
        pass

    @abc.abstractmethod
    def get_all_devices(self):
        pass

    @abc.abstractmethod
    def insert_device_list(self, device_details_list: list):
        pass

    @abc.abstractmethod
    def update_first_available_device_to_engaged(self, udid):
        pass

    @abc.abstractmethod
    def update_device_screenshot(self, udid: str, screenshot: []):
        pass

    @abc.abstractmethod
    def update_status_to_available_for_device(self, udid):
        pass
