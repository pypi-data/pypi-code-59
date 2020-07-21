import sched

from mdb.android.Android import Android
from monitor.entities.SmartBOT import SmartBOT


class ActivityMonitor(sched.scheduler):
    counter = int()
    interval = int()
    smartBOT = SmartBOT()
    activities = list()

    def __init__(self, activities: list, smartBOT: SmartBOT, interval: int) -> None:
        super().__init__()
        self.interval = interval
        self.smartBOT = smartBOT
        self.activities = activities

    def run(self, blocking=True):
        activity = Android().get_activity(self.smartBOT)
        sched.scheduler(++self.counter * self.interval)
        self.activities.append(activity)
