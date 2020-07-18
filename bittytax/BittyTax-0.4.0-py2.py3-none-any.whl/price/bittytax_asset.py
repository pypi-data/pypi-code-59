# -*- coding: utf-8 -*-
# (c) Nano Nano Ltd 2019

import sys
import logging
import argparse

from ..version import __version__
from ..config import config
from .datasource import DataSourceBase
from .asset import AssetSymbols

if sys.version_info[0] >= 3:
    sys.stdout.reconfigure(encoding='utf-8')

logging.basicConfig(stream=sys.stdout,
                    level=logging.INFO,
                    format='[%(asctime)s.%(msecs)03d] %(levelname)s -- : %(message)s',
                    datefmt='%Y-%m-%dT%H:%M:%S')
log = logging.getLogger()

def main():
    choices = sorted([ds.__name__ for ds in DataSourceBase.__subclasses__()])
    parser = argparse.ArgumentParser()
    parser.add_argument("asset",
                        type=str,
                        nargs='?',
                        help="symbol of cryptoasset or fiat currency (i.e. BTC/LTC/ETH or EUR/USD)")
    parser.add_argument("-v",
                        "--version",
                        action='version',
                        version='%(prog)s {version}'.format(version=__version__))
    parser.add_argument("-d",
                        "--debug",
                        action='store_true',
                        help="enabled debug logging")
    parser.add_argument("-ds",
                        choices=sorted([ds.__name__ for ds in DataSourceBase.__subclasses__()]),
                        type = str.lower, 
                        dest='data_source',
                        help="specify the data source to use")

    config.args = parser.parse_args()

    if config.args.debug:
        log.setLevel(logging.DEBUG)
        config.output_config(parser.prog)

    asset = config.args.asset

    if asset == config.CCY:
        return

    if config.args.data_source:
        asset_manager = AssetSymbols(config.args.data_source)
    else:
        asset_manager = AssetSymbols()

    if asset:
        asset_manager.get_asset_name(asset)
    else:
        asset_manager.list_assets()
