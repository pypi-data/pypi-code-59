import sched


class BatteryMonitor(sched.scheduler):
    def run(self, blocking=True):
        print("monitoring battery")
