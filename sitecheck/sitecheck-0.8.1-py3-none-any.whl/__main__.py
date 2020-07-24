"""
    Geo-Instruments
    Sitecheck scanner
"""
# __author__ = "Dan Edens"
# __version__= "0.8.19"
# __url__= "https://pypi.org/project/sitecheck/"

import asyncio
import os
import sys

from os import path

ROOT_DIR = os.path.dirname(path.abspath(sys.modules['__main__'].__file__))
os.environ['ROOT_DIR'] = ROOT_DIR
sys.path.insert(0, ROOT_DIR)

from sitecheck.scanner import Sitecheck


async def main():
    """
    Retrieves Sensor data from Project websites and produces
    an Adaptive card for Microsoft Teams to intake.
    """
    await Sitecheck()


if __name__ == "__main__":
    asyncio.run(main())
