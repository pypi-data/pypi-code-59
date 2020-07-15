from monitor.entities.CpuData import CpuData
from monitor.entities.MemoryData import MemoryData


class ScenarioTimeline(object):
    interval = int()
    cpuData = CpuData()
    memoryData = MemoryData()
    activity = str()
    screenshotFileName = str()
    screenshotData = []


