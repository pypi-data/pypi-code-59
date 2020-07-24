"""
    Init file for Pyppet
"""
# __author__ = DanEdens
# __status__  = "production"

import logging
import os

import sitecheck.scanner.Scanner

from . import sites, utlis

logger = logging.getLogger('root')
ROOT_DIR = sitecheck.scanner.Scanner.ROOT_DIR
os.environ['PREVIOUS_SENSOR'] = 'initstr'


async def __init__():
    utlis.disable_timeout_pyppeteer()


async def Launch():
    """
    Create Browser Object
    """
    return sites.make_browser
