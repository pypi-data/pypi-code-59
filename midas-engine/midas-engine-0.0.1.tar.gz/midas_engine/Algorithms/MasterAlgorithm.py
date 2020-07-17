from Data.Asset import*
import pandas as pd
from unicorn_binance_websocket_api.unicorn_binance_websocket_api_manager import BinanceWebSocketApiManager
import logging
import time
import threading
import os
from Start_Stream import*
import sys

print(sys.path)

class MasterAlgorithm(object):
    def __init__(context):
        context.Assets = []
        context.Resolution = 'ticker'
        context.Initialize()
        print('done INIT')

        #connect to market
        Start_Stream(context)
        
    def AddAsset(self,value,market=None,type=None):
        value = Asset(value)
        self.Assets.append(value)
    def SetMarket(self,value):
        self.Market=value  
    def SetResolution(self,value):
        self.Resolution=value