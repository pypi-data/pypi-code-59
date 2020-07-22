"""
    Geo-Instruments
    Sitecheck scanner
    Data handler Package for scanner

"""
# __author__ = "Dan Edens"
# __url__= "https://github.com/DanEdens/Sitecheck_Scrapper"
# __status__  = "production"
from sitecheck.scanner import logger
from sitecheck.scanner.Scanner import options
from sitecheck.scanner.Scanner.card_generator import adaptivecards



def check_mode(self, sensor, name_sel):
    """
    --unfinished--
    Returns: Wait for input
    """
    print(sensor + ' is missing data')
    return input("Check Mode enabled. Pausing run for eval.\nPress Enter to continue...")


async def watchdog_processor(diff, sensor_data, project_name, sensor, date):
    """
    Handles sorting sensor watchdog status.

    Up-to-date, Behind, Old

    :param diff: Time since last reading
    :type diff: int

    :param sensor_data: Text block that is printed to console
    :type sensor_data: str

    :param project_name: Name of Project
    :type project_name: str

    :param sensor: Sensor ID
    :type sensor: str

    :param date: Formatted Date string
    :type date: str
    """
    if diff <= options.watchdog:
        data_list = [sensor, 'good', 'Up-to-date', date]
        # logger.debug(sensor_data + '\n' + text.uptoDate)
        logger.info(data_list)
        if options.PrintNew:
            adaptivecards.store(project_name, data_list)
    elif options.watchdog <= diff <= options.watchdog * 7:
        data_list = [sensor, 'warning', 'Older than 24 hours', date]
        # logger.debug(sensor_data + '\n' + text.behindDate)
        logger.info(data_list)
        adaptivecards.store(project_name, data_list)
        if options.Checkmode:
            check_mode(sensor)
    else:
        data_list = [sensor, 'attention', 'Older than a week', date]
        # logger.debug(sensor_data + '\n' + text.oldDate)
        logger.info(data_list)
        if options.PrintOld:
            adaptivecards.store(project_name, data_list)
            if options.Checkmode:
                check_mode(sensor)
