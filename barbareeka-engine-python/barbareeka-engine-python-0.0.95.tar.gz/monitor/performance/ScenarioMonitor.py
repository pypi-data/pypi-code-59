import threading
from threading import Thread
from time import sleep

from pyOptional import Optional

from monitor.entities.ScenarioTimeline import ScenarioTimeline
from monitor.entities.ScreenshotStatistics import ScreenshotStatistics
from monitor.entities.SmartBOT import SmartBOT
from monitor.entities.performance.Activity import Activity
from monitor.performance.CpuMonitor import CpuMonitor
from monitor.performance.ScreenShotGenerator import ScreenShotGenerator
from monitor.services.ScenariosServiceImpl import ScenariosServiceImpl
from monitor.utils.Commons import Commons

thread_list = list()


class ScenarioMonitor(object):
    PERIOD = 1000
    cpu_monitor = list()
    memory_stats = list()
    activities = list()
    smartBOT = SmartBOT
    countdown: Thread()
    timer = threading.Timer
    take_screenshots = True
    threads = []
    screenshots = []

    def __init__(self, smartBOT):
        self.smartBOT = smartBOT

    def thread_start(self):
        try:
            sleep(.003 * self.PERIOD)

        except ValueError as error:
            print(error)

    def start(self):
        interval = int(self.PERIOD / 1000)
        Commons().create_temp_folder(self.smartBOT)

        cpu_details = CpuMonitor(self.smartBOT)

        # monitor_cpu_thread = multiprocessing.Process(target=cpu_details.monitor_cpu_details)
        # screen_shot_thread = multiprocessing.Process(target=self.method_name().generate_screenshot)
        self.screenshot_generator(self.smartBOT).generate_screenshot()
        self.cpu_monitor(self.smartBOT).monitor_cpu_details()
        # monitor_cpu_thread.daemon = True
        # screen_shot_thread.daemon = True

        # thread_list.append(monitor_cpu_thread)
        # thread_list.append(screen_shot_thread)
        # for thread in thread_list:
        #     thread.start()
        # sleep(10)
        # self.method_name().get_screenshots()

    def stop(self, scenario, smartBOT):
        # for thread in thread_list:
        #     thread.terminate()
        screenshots = self.screenshot_generator(smartBOT).get_screenshots()
        scenario_time_lines = list()
        activity = get_base_activity()
        screenshot_statistics = [ScreenshotStatistics()]
        self.screenshot_generator(smartBOT).import_screenshots()
        get_cpu_stats = self.cpu_monitor(smartBOT).get_cpu_stats()

        for cpu_stats in get_cpu_stats:
            screenshot_statistics_optional = Optional.empty()
            screenshot_statistics_optional.if_present(screenshot_statistics[0])
            self.set_screenshot_statistics_for_monitoring_off(screenshot_statistics[0])
            scenario_time_line = self.get_scenario_timeline(None, None, cpu_stats.interval, None,
                                                            screenshot_statistics[0])
            scenario_time_lines.append(scenario_time_line)
        self.screenshot_generator(smartBOT).delete_image_folder()
        ScenariosServiceImpl().update_scenario_time_line(scenario=scenario, smartBOT=smartBOT,
                                                         scenario_time_lines=scenario_time_lines)
        Commons().delete_temp_folder(smartBOT)

    def set_screenshot_statistics_for_monitoring_off(self, screenshot_stats: ScreenshotStatistics):
        if not self.take_screenshots:
            screenshot_statistics = ScreenshotStatistics()
            screenshot_statistics.unique = False
            screenshot_stats = screenshot_statistics
        return screenshot_stats

    def get_scenario_timeline(self, interval, activity, cpu_stats, memory_stats,
                              screenshot_stats: ScreenshotStatistics):
        scenario_timeline = ScenarioTimeline()
        scenario_timeline.interval = interval
        scenario_timeline.activity = get_base_activity()
        # scenario_timeline.cpuData = CpuData.user = cpu_stats.user = CpuData.kernel = cpu_stats.kernel
        if screenshot_stats.is_unique():
            scenario_timeline.screenshotData = screenshot_stats.screenshot
        return scenario_timeline

    def screenshot_generator(self, smartBOT):
        return ScreenShotGenerator(smartBOT)

    def cpu_monitor(self, smartBOT):
        return CpuMonitor(smartBOT)


def get_base_activity():
    activity = Activity()
    activity.focussedActivity = "undefinedActivity"
    return activity
