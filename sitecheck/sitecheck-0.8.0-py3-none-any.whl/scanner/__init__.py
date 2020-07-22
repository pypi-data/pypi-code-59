"""
    Geo-Instruments
    Sitecheck scanner
"""
# __author__ = "Dan Edens"
# __url__= "https://github.com/DanEdens/Sitecheck_Scrapper"
# __status__  = "production"

import os

from sitecheck.scanner.Scanner import utlis
from sitecheck.scanner.Scanner import config

logger = utlis.make_logger('root')
ROOT_DIR = os.path.dirname(os.path.abspath("__main__.py"))
projects = config.load_projects()


async def Sitecheck():
    logger.debug("Available Projects:")
    logger.debug(projects.sections())
    from sitecheck.scanner.Scanner import projecthandler
    [await (projecthandler.run_controller(project)) for project in projects.sections()]
    logger.info('\nScan completed.')


def edit():
    config.edit_project()
