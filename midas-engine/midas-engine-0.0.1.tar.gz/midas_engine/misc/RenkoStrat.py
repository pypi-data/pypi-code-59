import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyrenko
import scipy.optimize as opt
from scipy.stats import iqr
import talib
from datetime import datetime, timedelta
import winsound

from catalyst import run_algorithm
from catalyst.api import (record, symbol, order_target, order_target_percent, get_datetime)
from logbook import Logger
from catalyst import run_algorithm
from catalyst.api import order_target_percent, record, symbol
from catalyst.exchange.utils.stats_utils import extract_transactions

NAMESPACE = "RENKO"
log = Logger(NAMESPACE)

def initialize(context):
    context.start
    symbols = ['vet_usd']
    context.asset = []
    for sym in symbols:
        context.asset.append(symbol(sym))

    context.leverage = 1.0              # 1.0 - no leverage
    context.n_history = 60*24         # Number of lookback bars for modelling
    context.tf = '1T'                  # How many minutes in a timeframe
    context.model = pyrenko.renko()     # Renko object
    context.part_cover_ratio = 0.0    # Partially cover position ratio
    context.last_brick_size = 0.0       # Last optimal brick size (just for storing)
    context.set_commission(maker = 0.001, taker = 0.001)
    context.set_slippage(slippage = 0.0005)
#     context.consolidator = consolidate(15)

# def handle_consolidated_data:
#     def __init__(context,consoli)
# def consolidate(data=None):
    # def __init(self,minutes)
        # self.tf 

def unpack_data(context, data):
    temp = {}  
    temp['symbol']=[]
    temp['price']=[]
    temp['time']=[]

    for asset in context.asset:
        symbol = asset
        price = data.current(asset,'price')
        time = context.current_time

        
        temp['symbol'].append(asset)
        temp['price'].append(float(price))
        temp['time']=pd.to_datetime(time,unit='ms')

        
        df = pd.DataFrame(temp).set_index(['time','symbol'])

    
    return df

def evaluate_renko(brick, history, column_name):
    renko_obj = pyrenko.renko()
    renko_obj.set_brick_size(brick_size = brick, auto = False)
    renko_obj.build_history(prices = history)
    return renko_obj.evaluate()[column_name]

def renko_bars(context, data):
    for asset in context.asset:

        # When model is empty
        if len(context.model.get_renko_prices()) == 0:
            context.model = pyrenko.renko()
            history = data.history(asset,
                'price',
                bar_count = context.n_history, 
                frequency = context.tf
                )
            print(history)
            
            # Get daily absolute returns
            diffs = history.diff(30).abs()
            diffs = diffs[~np.isnan(diffs)]
            # Calculate IQR of daily returns
            iqr_diffs = np.percentile(diffs, [25, 75])

            # Find the optimal brick size
            opt_bs = opt.fminbound(lambda x: -evaluate_renko(brick = x,
                history = history, column_name = 'score'),
            iqr_diffs[0], iqr_diffs[1], disp=0)

            # Build the model
            print('REBUILDING RENKO: ' + str(opt_bs))
            context.last_brick_size = opt_bs
            context.model.set_brick_size(brick_size = opt_bs, auto = False)
            context.model.build_history(prices = history)
            

            # Store some information        
            record(
                rebuilding_status = 1,
                brick_size = context.last_brick_size,
                price = history[-1],
                renko_price = context.model.get_renko_prices()[-1],
                num_created_bars = 0,
                amount = context.portfolio.positions[asset].amount
            )

        else:
            last_price = data.history(asset,
                                'price',
                                bar_count = 1,
                                frequency = '1T',
                                )
            
            # Just for output and debug
            prev = context.model.get_renko_prices()[-1]
            prev_dir = context.model.get_renko_directions()[-1]
            num_created_bars = context.model.do_next(last_price)
            if num_created_bars != 0:
                print('New Renko bars created')
                print('last price: ' + str(last_price[-1]))
                print('previous Renko price: ' + str(prev))
                print('current Renko price: ' + str(context.model.get_renko_prices()[-1]))
                print('direction: ' + str(prev_dir))
                print('brick size: ' + str(context.model.brick_size))

            # Store some information
            
            record(
                rebuilding_status = 0,
                brick_size = context.last_brick_size,
                price = last_price[-1],
                renko_price = context.model.get_renko_prices()[-1],
                num_created_bars = num_created_bars,
                amount = context.portfolio.positions[asset].amount
            )

            print(   "last brick direction: " + str(prev_dir),
                    "\ncurrent brick direction: " + str(context.model.get_renko_directions()[-1]),
                    "\nlast Renko Price: " + str(context.model.get_renko_prices()[-2]),
                    "\ncurrent Renko Price: " + str(context.model.get_renko_prices()[-1]),
                    "\nnext renko price: " + str(context.model.get_renko_prices()[-1]+context.model.brick_size)
                )
            #open position if green bar forms
            if prev_dir > 0 and context.portfolio.positions[asset].amount < 1:
                order_target_percent(asset, 1)
                winsound.Beep(600, 200)
                print("BOUGHT",prev_dir, context.model.get_renko_directions()[-2])
            # If the last price moves in the backward direction we should rebuild the model
            if np.sign(context.portfolio.positions[asset].amount * context.model.get_renko_directions()[-1]) == -1:
                order_target_percent(asset, 0.0)
                print("SOLD")
                winsound.Beep(400, 200)
                context.model = pyrenko.renko()
    
def handle_data(context, data):
    #update slice time
    # if context.asset == list:
    #     asset = context.asset[0]
    # else:
    #     asset = context.asset
    # context.current_time = data.history(asset,'price',1,'1T').index[0]
    # context.current_time = pd.Timestamp(context.current_time)


    #reorganize data indexed to time and asset
    # repacked_data = unpack_data(context,data)
    # context.con
    renko_bars(context,data)
    

    # context.consolidator.Update(context.asset,data)

def consolidator_handler(context):
    pass
   
 
def analyze(context, perf):

    # Summary output
    print('Total return: ' + str(perf.algorithm_period_return[-1]))
    print('Sortino coef: ' + str(perf.sortino[-1]))
    print('Max drawdown: ' + str(np.min(perf.max_drawdown)))
    print('Alpha: ' + str(perf.alpha[-1]))
    print('Beta: ' + str(perf.beta[-1]))
    perf.to_csv('perf_' + str(context.asset) + '.csv')
    
    f = plt.figure(figsize = (7.2, 7.2))

    # Plot performance
    ax1 = f.add_subplot(611)
    ax1.plot(perf.algorithm_period_return, 'blue')
    ax1.plot(perf.benchmark_period_return, 'red')
    ax1.set_title('Performance')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Return')

    # Plot price and renko price
    ax2 = f.add_subplot(612, sharex = ax1)
    ax2.plot(perf.price, 'grey')
    ax2.plot(perf.renko_price, 'yellow')
    ax2.set_title(context.asset)
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Price')

    # Plot brick size
    ax3 = f.add_subplot(613, sharex = ax1)
    ax3.plot(perf.brick_size, 'blue')
    xcoords = perf.index[perf.rebuilding_status == 1]
    for xc in xcoords:
        ax3.axvline(x = xc, color = 'red')
    ax3.set_title('Brick size and rebuilding status')
    ax3.set_xlabel('Time')
    ax3.set_ylabel('Size and Status')

    # Plot renko_price
    ax4 = f.add_subplot(614, sharex = ax1)
    ax4.plot(perf.num_created_bars, 'green')
    ax4.set_title('Number of created Renko bars')
    ax4.set_xlabel('Time')
    ax4.set_ylabel('Amount')

    # Plot amount of asset in portfolio
    ax5 = f.add_subplot(615, sharex = ax1)
    ax5.plot(perf.amount, 'black')
    ax5.set_title('Asset amount in portfolio')
    ax5.set_xlabel('Time')
    ax5.set_ylabel('Amount')

    # Plot drawdown
    ax6 = f.add_subplot(616, sharex = ax1)
    ax6.plot(perf.max_drawdown, 'yellow')
    ax6.set_title('Max drawdown')
    ax6.set_xlabel('Time')
    ax6.set_ylabel('Drawdown')

    plt.show()

if __name__ == "__main__":
    run_algorithm(
                data_frequency = "minute",
                initialize = initialize,
                handle_data = handle_data,
                analyze = analyze,
                exchange_name = "binance",
                live = True,
                simulate_orders=False,
                algo_namespace = NAMESPACE,
                quote_currency = "usd",
                capital_base = 1900
        )