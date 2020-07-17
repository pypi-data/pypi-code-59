import pandas as pd


class Asset:
    #initialize the attributes
    def __init__(self, ticker, market=None, type=None):
        self.Ticker = ticker.lower()
        while market != None:
            market = market.lower()
        while type != None:
            type = type.lower()
        self.Market=market
        self.Type=type

    def __str__(self):
        return self.Ticker
    
    def __repr__(self):
        return self.Ticker

    def AddAsset(self,value,market=None,type=None):
        value = Asset(value)
        self.Assets.append(value)

    #setting the attributes
    @property
    def Market(self):
        return self._Market        
    @Market.setter
    def Market(self,value):
        self._Market=value
    @property
    def Type(self):
        return self._Market
    @Type.setter
    def Type(self,value):
        self._Type = value