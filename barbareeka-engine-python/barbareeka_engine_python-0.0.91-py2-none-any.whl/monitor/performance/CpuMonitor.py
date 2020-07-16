from time import sleep

from mdb.android.Android import Android
from monitor.entities.SmartBOT import SmartBOT
from monitor.helper.TestCaseHelper import TestCaseHelper


class CpuMonitor(object):
    counter = 0
    interval: float
    smartBOT: SmartBOT
    cpu_stats: list

    def __init__(self, cpu_stats, smartBOT, interval):
        super().__init__()
        self.cpu_stats = cpu_stats
        self.smartBOT = smartBOT
        self.interval = interval

    def monitor_cpu_details(self):
        while True:
            cpu_statistics = Android().get_cpu_info(self.smartBOT)
            print(
                "monitoring cpu for scenario - app {}".format(self.smartBOT.appPackageName))
            cpu_statistics.interval = ((++self.counter) * self.interval)
            self.cpu_stats = cpu_statistics
            sleep(1)

    def get_scenario_name(self):
        return TestCaseHelper(self.smartBOT.testCase).get_unique_scenario_name()
