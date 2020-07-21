from time import sleep

from mdb.android.Android import Android
from monitor.entities.SmartBOT import SmartBOT
from monitor.helper.TestCaseHelper import TestCaseHelper


class CpuMonitor(object):
    counter = 0
    interval = 1
    smartBOT: SmartBOT
    cpu_stats = []

    def __init__(self, smartBOT):
        self.smartBOT = smartBOT

    def monitor_cpu_details(self):
        while True:
            itr = self.counter = self.counter + 1 * self.interval
            cpu_statistics = Android().get_cpu_info(self.smartBOT)
            print(
                "monitoring cpu for scenario - app {}".format(self.smartBOT.appPackageName))
            cpu_statistics.interval = itr
            self.cpu_stats.append(cpu_statistics)
            sleep(0.3)
            if itr == 1:
                break

    def get_scenario_name(self):
        return TestCaseHelper(self.smartBOT.testCase).get_unique_scenario_name()

    def get_cpu_stats(self):
        return self.cpu_stats
