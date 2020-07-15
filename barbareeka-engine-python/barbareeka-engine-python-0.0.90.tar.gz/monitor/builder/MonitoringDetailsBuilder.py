from monitor.entities.MonitoringDetails import MonitoringDetails


class MonitoringDetailsBuilder:
    monitoring_details = MonitoringDetails()

    def scenario_name(self, scenario_name):
        self.monitoring_details.scenario_name = scenario_name
        return self.monitoring_details

    def device_udid(self, device_udid):
        self.monitoring_details.device_udid = device_udid
        return self.monitoring_details

    def app_package(self, app_package):
        self.monitoring_details.app_package = app_package
        return self.monitoring_details
