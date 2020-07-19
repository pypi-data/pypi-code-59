import sys
sys.path.append("/home/renatomz/Documents/Projects/Dal-io")

import numpy as np
import pandas as pd
import matplotlib as plt

from scipy.stats import skew, kurtosis

from dalio.external import (
    YahooDR, 
    PyPlotGraph, 
    PyPfOptGraph,
    PySubplotGraph,
    PandasInFile,
)

from dalio.translator import (
    YahooStockTranslator,
    StockStreamFileTranslator,
)
    
from dalio.pipe import (
    ColSelect, 
    StockReturns,
    Change, 
    Period, 
    Custom, 
    Rolling,
    CovShrink, 
    ExpectedReturns,
    LinearModel,
    OptimumWeights,
)

from dalio.model import (
    Join,
    MakeCriticalLine, 
    MakeEfficientFrontier, 
    OptimumPortfolio,
    XYLinearModel
)

from dalio.application import (
    Grapher,
    PandasTSGrapher,
    PandasMultiGrapher,
    LMGrapher,
)

from dalio.ops import risk_metrics

ticker = ["WMT", "MSFT", "AMZN", "HD"]

file_in = StockStreamFileTranslator()(PandasInFile("tests/sample_stocks.xlsx"))
yahoo_in = YahooStockTranslator()(YahooDR())

res = file_in.run()

price = ColSelect(cols="price")(file_in)
# res = price.run(ticker="NVDA")
# simple_rets = StockReturns()(price)
simple_rets = Change(strategy="pct_change")(price)
# res = simple_rets.run(ticker="NVDA")

###### goes to infinity very fast
daily_var = Custom(risk_metrics, 0.94)(simple_rets)
# res = daily_var.run(ticker=ticker)

ret_avg = Custom(np.mean)(simple_rets)
ret_sd = Custom(np.std)(simple_rets)
ret_skew = Custom(skew)(simple_rets)
ret_kurt = Custom(kurtosis)(simple_rets)

price_graph = PandasTSGrapher(legend="upper left")\
    .set_input("data_in", price)\
    .set_output("data_out", PyPlotGraph())
# fig = price_graph.run(ticker=ticker)
rets_graph = PandasTSGrapher()\
    .set_input("data_in", simple_rets)\
    .set_output("data_out", PyPlotGraph())
vol_graph = PandasTSGrapher()\
    .set_input("data_in", daily_var)\
    .set_output("data_out", PyPlotGraph())

summary_grapher = PandasMultiGrapher(2, 2)\
    .set_input((0, 0), price)\
        .set_piece((0, 0), "line", x_index=True, y="price")\
    .set_input((0, 1), simple_rets)\
        .set_piece((0, 1), "line", x_index=True, y="price")\
    .set_input((1, 0), daily_var)\
        .set_piece((1, 0), "line", x_index=True, y="price")\
    .set_input((1, 1), simple_rets)\
        .set_piece((1, 1), "histogram", x="price", bins=30)\
    .set_output("data_out", PySubplotGraph(2, 2))

# fig = summary_grapher.run(ticker=["AMZN", "NVDA"])

annual_rets = Period("Y", agg_func=np.sum)(simple_rets)
avg_rets = Period("Y", agg_func=np.mean)(simple_rets)
var_rets = Period("Y", agg_func=np.var)(simple_rets)
std_rets = Period("Y", agg_func=np.std)(simple_rets)

cov_rets = Custom(lambda x: x.cov())(annual_rets)
corr_rets = Custom(lambda x: x.corr())(annual_rets)

S = CovShrink(frequency=252)(price)\
    .set_piece("shrinkage", "ledoit_wolf")
mu = ExpectedReturns()(price)\
    .set_piece("return_model", "mean_historical_return")

CLA = MakeCriticalLine()\
    .set_input("sample_covariance", S)\
    .set_input("expected_returns", mu)
   
cla_graph = Grapher()\
    .set_input("data_in", CLA)\
    .set_output("data_out", PyPfOptGraph())

opt = OptimumWeights(weight_bounds=(-0.5, 1))\
    .set_input(CLA)\
    .set_piece("strategy", "max_sharpe")

opt_long = OptimumWeights(weight_bounds=(0.05, 1))\
    .set_input(CLA)\
    .set_piece("strategy", "max_sharpe")

min_vol_opt = opt.with_piece("strategy", "min_volatility")
min_vol_opt_long = opt_long.with_piece("strategy", "min_volatility")

max_sharpe_opt = opt.with_piece("strategy", "max_sharpe")
max_sharpe_opt_long = opt_long.with_piece("strategy", "max_sharpe")

lm = PandasLinearModel()\
    .set_input(price)\
    .set_piece("strategy", "LinearRegression")

lm2 = XYLinearModel()\
    .set_input("x", price)\
    .set_input("y", daily_var)\
    .set_piece("strategy", "LinearRegression")

res = lm2.run(ticker="NVDA")

all_lm_graph = LMGrapher(legend="upper left")\
    .set_input("data_in", price)\
    .set_input("linear_model", lm)\
    .set_output("data_out", PyPlotGraph())
# fig = all_lm_graph.run(ticker=ticker)

lm_graph = LMGrapher(x="price", y="price_right", legend="upper left")\
    .set_input(
        "data_in", 
        Join(rsuffix="_right")\
            .set_input("left", price)\
            .set_input("right", daily_var))\
    .set_input("linear_model", lm2)\
    .set_output("data_out", PyPlotGraph())

sp500_lm = XYLinearModel()\
    .set_input("x", ColSelect(("price", "SPY"))(simple_rets))\
    .set_input("y", ColSelect(("price", "WMT"))(simple_rets))\
    .set_piece("strategy", "LinearRegression")

sp500_lm_graph = LMGrapher(x=("price", "SPY"), y=("price", "WMT"))\
    .set_input("data_in", simple_rets)\
    .set_input("linear_model", sp500_lm)\
    .set_output("data_out", PyPlotGraph())

fig = sp500_lm_graph.run(ticker=["WMT", "SPY"])

opt_port = OptimumPortfolio()\
    .set_input("data_in", simple_rets)\
    .set_input("weights_in", min_vol_opt)

sp_opt_weights = max_sharpe_opt_long.copy()\
    .add_stock_weight_constraint(ticker="SPY", comparisson="==", weight=0.6)

sp_opt_port = opt_port\
    .with_input("weights_in", sp_opt_weights)