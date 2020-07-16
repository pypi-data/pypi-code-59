import multiprocessing
import threading
import time
from threading import Thread

from pyOptional import Optional

from monitor.entities.ScenarioTimeline import ScenarioTimeline
from monitor.entities.ScreenshotStatistics import ScreenshotStatistics
from monitor.entities.SmartBOT import SmartBOT
from monitor.entities.performance.Activity import Activity
from monitor.performance.CpuMonitor import CpuMonitor
from monitor.performance.ScreenShotGenerator import ScreenShotGenerator, screenshots
from monitor.services.ScenariosServiceImpl import ScenariosServiceImpl
from monitor.utils.Commons import Commons

thread_list = list()


class ScenarioMonitor(object):
    screen_shot_generator: ScreenShotGenerator
    PERIOD = 1000
    cpu_stats = list()
    memory_stats = list()
    activities = list()
    smartBOT = SmartBOT
    countdown: Thread()
    timer = threading.Timer
    take_screenshots = True
    threads = []

    def __init__(self, smartBOT):
        self.smartBOT = smartBOT
        # self.countdown = Thread(target=self.thread_start())
        # define countdown if required

    def thread_start(self):
        try:
            # while 1:
            time.sleep(.003 * self.PERIOD)

        except ValueError as error:
            print(error)

    def start(self):
        interval = int(self.PERIOD / 1000)
        Commons().create_temp_folder(self.smartBOT)

        cpu_details = CpuMonitor(self.cpu_stats, self.smartBOT, interval)
        monitor_cpu_thread = multiprocessing.Process(target=cpu_details.monitor_cpu_details)

        ScenarioMonitor.screen_shot_generator = ScreenShotGenerator(self.smartBOT)
        screen_shot_thread = multiprocessing.Process(target=ScenarioMonitor.screen_shot_generator.generate_screenshot)

        thread_list.append(monitor_cpu_thread)
        thread_list.append(screen_shot_thread)
        for thread in thread_list:
            thread.start()
        # ScenarioMonitor.screenshot_thread.start()

    def stop(self, scenario, smartBOT):
        for thread in thread_list:
            thread.kill()
        scenario_time_lines = list()
        activity = get_base_activity()
        screenshot_statistics = [ScreenshotStatistics()]
        ScenarioMonitor.screen_shot_generator.import_screenshots()
        ScenarioMonitor.screen_shot_generator.update_screenshot_statistics(screenshots)

        for cpu_stats in self.cpu_stats:
            screenshot_statistics_optional = Optional.empty()
            screenshot_statistics_optional.if_present(screenshot_statistics[0])
            self.set_screenshot_statistics_for_monitoring_off(screenshot_statistics[0])
            scenario_time_line = self.get_scenario_timeline(None, None, cpu_stats.interval, None,
                                                            screenshot_statistics[0])
            scenario_time_lines.append(scenario_time_line)
        self.screen_shot_generator.delete_image_folder()
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


def get_base_activity():
    activity = Activity()
    activity.focussedActivity = "undefinedActivity"
    return activity
