import sys
sys.path.append("/home/renatomz/Documents/Projects/Dal-io")

import numpy as np
import pandas as pd
import matplotlib as plt

from scipy.stats import skew, kurtosis

from dalio.external import (
    YahooDR, 
    PyPlotGraph, 
    PandasInFile,
)

from dalio.translator import (
    YahooStockTranslator,
    StockStreamFileTranslator
)
    
from dalio.pipe import (
    ColSelect, 
    DateSelect,
    StockReturns, 
    Period, 
    Custom, 
    Rolling,
    CovShrink, 
    LinearModel,
    ExpectedReturns,
    MakeARCH,
    ValueAtRisk,
    ExpectedShortfall,
    PipeLine
)

from dalio.model import (
    MakeEfficientFrontier, 
    OptimumWeights,
    OptimumPortfolio,
)

from dalio.application import (
    Grapher,
    PandasXYGrapher,
)

from dalio.ops import risk_metrics

file_in = StockStreamFileTranslator()(PandasInFile("tests/ECO461.xls"))
price = file_in

yahoo_in = YahooStockTranslator()(YahooDR())
price = ColSelect(cols="adj_close")(yahoo_in)

simple_rets = StockReturns()(price)

ticker = ["WMT", "MSFT", "AMZN", "HD"]

rets_avg = Custom(np.mean)(simple_rets)
rets_std = Custom(np.std)(simple_rets)

am = MakeARCH()(simple_rets)\
    .set_piece("mean", "ConstantMean")\
    .set_piece("volatility", "RiskMetrics")\
    .set_piece("distribution", "Normal")

VaR025 = ValueAtRisk(quantiles=[0.025])(am)

var_rm = PipeLine(am, VaR025)

ES025 = ExpectedShortfall(quantiles=[0.025])(am)

S = CovShrink()(price)\
    .set_piece("shrinkage", "ledoit_wolf")

mu = ExpectedReturns()(price)\
    .set_piece("return_model", "mean_historical_return")

opt_weights = OptimumWeights(weight_bounds=(0, 1))\
    .set_input("sample_covariance", S)\
    .set_input("expected_returns", mu)\
    .set_piece("strategy", "max_sharpe")

opt_port = OptimumPortfolio()\
    .set_input("data_in", price)\
    .set_input("weights_in", opt_weights)

opt_rets = simple_rets.with_input(opt_port)
opt_avg = rets_avg.with_input(opt_rets)
opt_std = rets_std.with_input(opt_rets)

# set input of ARCH Model, as that is in turn the value at risk input
var_rm.set_input(opt_rets) # same as am.set_input(opt_port)

daily_var = Custom(risk_metrics, 0.94)(opt_rets)

VaR01 = ValueAtRisk(quantiles=[0.01])(am)
res = VaR01.run(ticker=ticker)