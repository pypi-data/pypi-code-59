from ..Algorithms import *

class Framework(MasterAlgorithm):
    def Initialize(context):
        symbols = ["VETUSD","ADAUSD","BTCUSD","ETHUSD"]
        for symbol in symbols:
            context.AddAsset(symbol)
        context.SetMarket('binance.us')
        print(context.Assets)
    
    def onData(context,data):
        print(data)

Framework()