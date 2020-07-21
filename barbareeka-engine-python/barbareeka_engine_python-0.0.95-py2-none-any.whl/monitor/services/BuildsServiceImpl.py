from monitor.clients.BuildsClient import BuildsClient
from monitor.clients.ScenariosClient import ScenariosClient
from monitor.constants.MongoDB import STATUS_PASSED
from monitor.services.BuildsService import BuildsService
from monitor.services.OptimusServiceImpl import OptimusServiceImpl
from monitor.utils.Utils import Utils


class BuildsServiceImpl(BuildsService, OptimusServiceImpl):
    def notify_build_start(self):
        BuildsClient().create_new_build()

    def notify_build_end(self):
        build_to_update = BuildsClient().find_build_by_id(OptimusServiceImpl().get_latest_id())
        build_scenario_count = int(ScenariosClient().get_build_scenario_count(OptimusServiceImpl().get_latest_id()))
        build_scenario_count_by_status = ScenariosClient() \
            .get_build_scenario_count_by_status(OptimusServiceImpl()
                                                .get_latest_id(), "passed")
        build_to_update["buildEndTime"] = Utils().get_current_time()
        build_to_update["buildScenario"] = build_scenario_count
        build_to_update["scenarioSuccessRate"] = build_scenario_count_by_status
        BuildsClient().update_build_record(build_to_update)

    def update_build_with_unique_scenarios(self):
        distinct_scenarios = ScenariosClient().get_distinct_scenarios()
        number_of_unique_scenario = len(distinct_scenarios)
        print("Unique Scenarios {}".format(number_of_unique_scenario))
        distinct_scenarios = ScenariosClient().get_distinct_scenarios()
        number_of_unique_scenario = len(distinct_scenarios)
        print("Unique Scenarios {}".format(number_of_unique_scenario))
        scenario_passed = list()
        for scenarios in distinct_scenarios:
            if scenarios.get("status") == STATUS_PASSED:
                scenario_passed.append(scenarios)
        passed_scenarios = len(scenario_passed)
        pass_percent = float((passed_scenarios * 100) / number_of_unique_scenario)
        builds_by_id = BuildsClient().find_build_by_id(OptimusServiceImpl().get_latest_id())
        builds_by_id["scenarioCount"] = number_of_unique_scenario
        builds_by_id["scenarioSuccessRate"] = pass_percent
        BuildsClient().update_build_record(builds_by_id)

    def create_crash_collection(self):
        pass

    def update_build_run_mode(self, run_mode):
        build_id = BuildsClient().find_build_by_id(OptimusServiceImpl().get_latest_id())
        build_id["runMode"] = run_mode
        BuildsClient().update_build_record(build_id)
