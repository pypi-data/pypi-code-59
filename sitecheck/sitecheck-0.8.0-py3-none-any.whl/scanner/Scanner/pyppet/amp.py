"""
    Amp navigation control for Pyppet
"""
# __author__ = DanEdens
# __status__  = "production"

import os

from dateutil.parser import parse

from sitecheck.scanner import logger
from sitecheck.scanner.Scanner import options, data
from . import sites, utlis, text


class Amp_Webpage:
    """
    Operator pool for Amp.
    """

    async def goto_plan_view(self):
        """
        Navigates to each planview listed in project.planarray and
        iterates through an array to check over sensor boxes

        :rtype: None

        """
        views = self.project.planarray.split(",")
        for view in views:
            logger.debug('Scanning Planview: ' + view)
            await self.page.goto(self.url + text.Amp_text.planview + view)
            await sites.scan_plan_view(self, Amp_Webpage)

    async def get_last_update(self):
        """


        Args: TODO trim methods
            self.page(obj): Page Context
            self.project.name(str): Project name
            self.target_child(str): Sensor to Scan

        :rtype: None
        """
        for type_of_sensor_box in text.Amp_text.label:
            name_sel = str(
                'body ' + text.Amp_text.csspath + type_of_sensor_box + ')' + text.Amp_text.csspath + os.environ[
                    'TARGET_CHILD'] +
                text.Amp_text.title)
            value_sel = str(
                'body ' + text.Amp_text.csspath + type_of_sensor_box + ')' + text.Amp_text.csspath + os.environ[
                    'TARGET_CHILD'] +
                text.Amp_text.sensor)
            name = await self.page.J(name_sel)
            link = await self.page.J(value_sel)
            if name is None:
                pass
            else:
                sensor = await self.page.evaluate('(name) => name.textContent', name)
                value = await self.page.evaluate('(link) => link.textContent', link)
                date = await self.page.evaluate('(link) => link.title', link)
                sensor_data = '\nSensor name: ' + sensor
                if options.getvalue:
                    sensor_data += '\nCurrent value: ' + value
                sensor_data += '\nLatest data on AMP: '
                diff_in_days = parse(text.nowdate) - parse(date)
                diff = int(diff_in_days.total_seconds())
                sensor_data += date
                await data.watchdog_processor(diff, sensor_data, self.project.name, sensor, date)
                if options.screenshot:
                    # todo fix screenshot selector hover
                    await utlis.screenshot(self, sensor, name_sel)
