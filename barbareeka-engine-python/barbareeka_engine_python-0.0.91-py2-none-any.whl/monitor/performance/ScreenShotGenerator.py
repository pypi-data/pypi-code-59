import os
from time import sleep

from pyOptional import Optional

from monitor.entities.SmartBOT import SmartBOT
from monitor.entities.performance.ScreenshotStatistics import ScreenshotStatistics
from monitor.utils.ImageResizer import ImageResizer

screenshots: []


class ScreenShotGenerator(object):
    counter = 0
    smartBOT: SmartBOT
    interval = 1

    CAPTURE_SCREENSHOT = "adb -s {} shell screencap /sdcard/{}/{}.png"
    last_file: object

    def __init__(self, smartBOT: SmartBOT):
        super().__init__()
        self.smartBOT = smartBOT

    def generate_screenshot(self):
        while True:
            itr = self.counter = self.counter + 1 * self.interval
            try:
                self.capture_screenshots(itr)
            except IOError as error:
                print(error)
            screenshot = ScreenshotStatistics()
            screenshot.interval = itr
            screenshots.append(screenshot)
            sleep(0.3)

    def capture_screenshots(self, interval):
        self.create_folder(self.get_udid())
        screenshot_command = self.CAPTURE_SCREENSHOT.format(self.smartBOT.deviceUdid, self.get_scenario_id(), interval)
        os.popen(screenshot_command).read()

    def create_folder(self, udid: str):
        print("creating a folder for -- {}".format(udid.replace("\\.", "")))
        file_path = "build/screenshotstemp/{}".format(udid.replace("\\.", ""))
        try:
            file = open(file_path)
        except Exception as error:
            if not os.path.exists(file_path):
                os.makedirs(file_path)

    def get_udid(self):
        return self.smartBOT.deviceUdid.replace("\\.", "")

    def get_scenario_id(self):
        return self.smartBOT.testCase.test_case.id.replace("[^a-zA-Z0-9]", "")

    def import_screenshots(self):
        print("Importing screenshots from -- {}".format(self.smartBOT.deviceUdid))
        line = str()
        try:
            os.popen("adb -s {} pull /sdcard/{} build/screenshotstemp/{}".format(self.smartBOT.deviceUdid,
                                                                                 self.get_scenario_id(),
                                                                                 self.get_udid())).read()

        except Exception as error:
            print(error)

    def delete_image_folder(self):
        folder = "build/screenshotstemp/{}/{}".format(self.get_udid(), self.get_scenario_id())
        if os.path.isdir(folder):
            os.rmdir(folder)

    def update_screenshot_statistics(self, list_of_screenshots: []):
        file = "build/screenshotstemp/{}/{}".format(self.get_udid(), self.get_scenario_id())
        if os.path.exists(file):
            try:
                for screenshot in list_of_screenshots:
                    first = Optional.empty()
                    for file_name in os.listdir(file):
                        if file_name == screenshot.interval + '.png':
                            first = Optional(file_name)
                            break
                    if first.is_present():
                        try:
                            if self.last_file is not None:
                                pass
                                # image_diff = ImageComparator().get_image_difference(self.last_file, first)
                                # if image_diff >= 0.3:
                                #     screenshot.screenshot = ImageResizer(first.get()).resize()
                                #     screenshot.unique = True
                            else:
                                screenshot.screenshot = ImageResizer(first.get()).resize()
                                screenshot.unique = True
                            self.last_file = first.get()
                        except Exception as error:
                            print(error)
            except Exception as error:
                print(error)
