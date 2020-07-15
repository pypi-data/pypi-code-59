from monitor.utils.Utils import Utils


class Build(object):
    id = str()
    runMode = str()
    buildStartTime = Utils().get_current_time()
    buildEndTime = Utils().get_current_time()
    buildScenario = int()
    buildSuccessRate = int()
    scenariosCount = int()
    scenarioSuccessRate = str()
    crashlytics = str()
