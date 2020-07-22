"""
    Geo-Instruments
    Sitecheck scanner
"""
# __author__ = "Dan Edens"
# __version__= "0.8.0"
# __Repository__= "git@geodev.geo-instruments.com:DanEdens/scanner.git"
# __url__= "https://geodev.geo-instruments.com/DanEdens/Sitecheck_Scanner"


import asyncio

from sitecheck.scanner import Sitecheck



async def main():
    """
    Retrieves Sensor data from Project websites and produces
    an Adaptive card for Microsoft Teams to intake.
    """
    await Sitecheck()


if __name__ == "__main__":
    asyncio.run(main())
