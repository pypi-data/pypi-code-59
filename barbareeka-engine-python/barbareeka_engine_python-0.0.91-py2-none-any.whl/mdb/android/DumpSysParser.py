import re

from mdb.core.CommandExecutor import CommandExecutor
from mdb.utils.Commands import Commands
from monitor.entities.SmartBOT import SmartBOT
from monitor.entities.performance import CpuStatistics


class DumpSysParser(object):
    smartBOT = SmartBOT()
    previousActivity = str()

    def __init__(self, smartBOT: SmartBOT()):
        self.smartBOT = smartBOT
        self.previousActivity = "OptimusActivity"

    def get_cpu_usage(self):
        user_kernel_info = dict()
        cpu_info_command = Commands.AndroidCommands.GET_CPU_INFO.value.format(self.smartBOT.deviceUdid,
                                                                              self.smartBOT.appPackageName)
        cpu_info = CommandExecutor().exec_as_list(cpu_info_command)
        for s in cpu_info:
            if "TOTAL" in s:
                cpu_usage_output = s.split(":")[1].strip()
                cpu_regex = re.search(Commands.AndroidCommands.CPU_REGEX.value, cpu_usage_output)
                user_kernel_info = {cpu_regex.group(3): cpu_regex.group(1),
                                    cpu_regex.group(7): cpu_regex.group(5)}

        cpu_statistics = CpuStatistics.CpuStatistics()
        cpu_statistics.user = user_kernel_info.get("user")
        cpu_statistics.kernel = user_kernel_info.get("kernel")
        return cpu_statistics

    # TODO: Implement these
    # def get_memory_info(self):
    #     pass
    #
    # def get_current_activity(self):
    #     pass
    #
    # def get_exception(self):
    #     pass
    #
    # def get_activity(self):
    #     pass
    # def get_exception(self):
    #     pass
