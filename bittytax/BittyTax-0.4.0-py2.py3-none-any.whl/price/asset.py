# -*- coding: utf-8 -*-
# (c) Nano Nano Ltd 2020

import logging

from .datasource import DataSourceBase
from .datasource import ExchangeRatesAPI, RatesAPI, CoinDesk, CryptoCompare, CoinGecko, CoinPaprika

log = logging.getLogger()

class AssetSymbols(object):
    def __init__(self, data_source=None):
        self.data_sources = {}

        if data_source:
            try:
                self.data_sources[data_source] = globals()[data_source]()
            except KeyError:
                raise ValueError("Data source: %s not recognised" % [data_source])
        else:
            for data_source in DataSourceBase.__subclasses__():
                self.data_sources[data_source.__name__.upper()] = data_source()

    def get_asset_name(self, asset):
        for data_source in sorted(self.data_sources):
            if asset in self.data_sources[data_source].assets:
                log.info("%s (%s) via %s", asset, self.data_sources[data_source].assets[asset], self.data_sources[data_source].name())

    def list_assets(self):
        assets = []

        for data_source in self.data_sources:
            for symbol in self.data_sources[data_source.upper()].assets:
                assets.append((symbol, self.data_sources[data_source.upper()].assets[symbol], self.data_sources[data_source].name()))

        for (symbol, name, data_source) in sorted(assets):
            log.info("%s (%s) via %s", symbol, name, data_source)

def old_list_assets():
    data_sources = {}
    symbols = {}
    assets = []

    for data_source in DataSourceBase.__subclasses__():
        data_sources[data_source().name()] = data_source()

    txt = ""
    for data_source in data_sources:
        for symbol in data_sources[data_source].assets:
            name = data_sources[data_source].assets[symbol]
            if symbol not in symbols:
                symbols[symbol] = [name]
            else:
                names = symbols[symbol]

                for stored_name in names:
                    #if similar(name.lower(), stored_name.lower()) < 0.9:
                    if name.lower() != stored_name.lower():
                    # Same symbol is different cryptoasset
                        log.info("Asset has different name: %s, %s, %s %s", symbol, name, stored_name, data_source)
                        assets.append((symbol, name, data_source))
                        symbols[symbol].append(name)

    symbol_len = 0
    for (symbol, name, data_source) in sorted(assets):
        log.info("%s, %s, %s", symbol, name, data_source)
        txt += u'{}, {}, {}\n'.format(symbol, name, data_source)
        if len(name) > symbol_len:
            symbol_len = len(name)

    txt += 'Total assets:' + str(len(assets))
    log.info("Max len: %s", symbol_len)
    return txt

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
