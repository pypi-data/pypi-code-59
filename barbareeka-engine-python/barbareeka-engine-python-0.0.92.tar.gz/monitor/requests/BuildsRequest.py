from monitor.requests.Build import Build
from monitor.utils.Utils import Utils


class BuildRequest(object):
    builds = Build()

    def __init__(self):
        self.builds.buildStartTime = Utils().get_current_time()
        self.builds.buildEndTime = Utils().get_current_time()
        self.builds.scenariosCount = 0
        self.builds.scenarioSuccessRate = "0.0"
        self.builds.id = None
        self.builds.crashlytics = None
        self.builds.buildScenario = None
        self.builds.runMode = None
        self.builds.buildSuccessRate = None

    def with_build_id(self, build_id=None):
        self.builds.id = build_id
        return self

    def with_build_start_time(self, build_start_time):
        self.builds.buildStartTime = build_start_time
        return self

    def with_run_mode(self, run_mode):
        self.builds.runMode = run_mode
        return self

    def with_build_end_time(self, build_end_time):
        self.builds.buildEndTime = build_end_time
        return self

    def with_scenario_count(self, scenario_count):
        self.builds.scenariosCount = scenario_count
        return self

    def with_scenario_success_rate(self, success_rate):
        self.builds.scenarioSuccessRate = success_rate
        return self

    def build(self):
        return self.builds
