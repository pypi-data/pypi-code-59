#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
sys.path.append("/home/renatomz/Documents/Projects/Dal-io")

import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')


# ## Import Base Packages

# In[2]:


import numpy as np
import pandas as pd
import matplotlib as plt

from scipy.stats import skew, kurtosis


# ### Import Dal-io Pieces

# In[3]:


from dalio.external import (
    YahooDR, 
    PyPlotGraph, 
    PandasInFile,
)

from dalio.translator import (
    YahooStockTranslator,
    StockStreamFileTranslator,
)
    
from dalio.pipe import (
    ColSelect, 
    Change,
    DateSelect,
    StockReturns, 
    Period, 
    Custom, 
    Rolling,
    CovShrink, 
    PandasLinearModel,
    ExpectedReturns,
    OptimumWeights,
    MakeARCH,
    ValueAtRisk,
    ExpectedShortfall,
    PipeLine
)

from dalio.model import (
    MakeEfficientFrontier, 
    OptimumPortfolio,
)

from dalio.application import (
    Grapher,
    PandasXYGrapher,
)

from dalio.ops import risk_metrics


# ### Basic Setup

# In[4]:


yahoo_in = YahooStockTranslator()(YahooDR())
price = ColSelect(cols="adj_close")(yahoo_in)


# In[5]:


forex_in = StockStreamFileTranslator()(PandasInFile("tests/sample_forex.xls"))
funds_in = StockStreamFileTranslator()(PandasInFile("tests/sample_funds.xls"))


# In[6]:


time = DateSelect()
price = time.set_input(forex_in)


# In[7]:


simple_rets = Change(strategy="pct_change")(price)

one_tick = "JPY-USD"
ticker = ["DJI", "GSPC" , "IXIC"]


# In[8]:


simple_rets.run()


# ### VaR

# In[9]:


time.set_start("2011-01")
time.set_end("2017-12")


# In[10]:


time.set_start(None)
time.set_end(None)


# In[11]:


rets_avg = Custom(np.mean)(simple_rets)
rets_std = Custom(np.std)(simple_rets)


# In[12]:


rets_std.run(ticker=one_tick)


# In[13]:


am = MakeARCH()(simple_rets)    .set_piece("mean", "ConstantMean")    .set_piece("volatility", "RiskMetrics", lam=None)    .set_piece("distribution", "Normal")


# In[14]:


res = am.run(ticker=one_tick).fit()


# In[15]:


res.params


# In[16]:


am2 = am.with_piece("volatility", "GARCH", p=1, q=1)


# In[ ]:


res2 = am2.run(ticker=one_tick).fit()


# In[ ]:


res2.params


# In[ ]:


VaR025 = am.pipeline(ValueAtRisk(quantiles=[0.025]))


# In[ ]:


var = VaR025.run(ticker=one_tick)


# In[ ]:


ES025 = am.pipeline(ExpectedShortfall(quantiles=[0.025]))


# In[ ]:


ES025.run(ticker=one_tick)


# ### Switch input

# In[ ]:


price.set_input(funds_in)


# In[ ]:


simple_rets.run()


# In[ ]:


S = CovShrink()(price)    .set_piece("shrinkage", "ledoit_wolf")

mu = ExpectedReturns()(price)    .set_piece("return_model", "mean_historical_return")


# In[ ]:


annual_rets = Period("Y", agg_func= lambda x: x[-1]).pipeline(
    Change(strategy="pct_change", rm_first=True)
)(price)

ann_agg = Custom(np.mean)(annual_rets)


# In[ ]:


cov_rets = Custom(lambda x: x.cov())(annual_rets)


# In[ ]:


cov_rets = Custom(lambda x: x.cov())(simple_rets)


# In[ ]:


ef = MakeEfficientFrontier(weight_bounds=(0, 1))    .set_input("sample_covariance", cov_rets)    .set_input("expected_returns", ann_agg)

opt_weights = OptimumWeights()(ef)    .set_piece("strategy", "max_sharpe", risk_free_rate=0.0)


# In[ ]:


cov_rets.run(ticker=ticker)


# In[ ]:


opt_weights.run(ticker=ticker)


# In[ ]:


opt_port = OptimumPortfolio()    .set_input("data_in", price)    .set_input("weights_in", opt_weights)


# In[ ]:


opt_port.run(ticker=ticker)


# In[ ]:


opt_rets = simple_rets.with_input(opt_port)
opt_avg = rets_avg.with_input(opt_rets)
opt_std = rets_std.with_input(opt_rets)


# In[ ]:


simple_rets._source._connection


# In[ ]:


simple_rets.run(ticker=ticker)


# In[ ]:


# set input of ARCH Model, as that is in turn the value at risk input
VaR025.set_input(opt_rets) # same as am.set_input(opt_port)


# In[ ]:


VaR025.run(ticker=ticker)


# In[ ]:


ES025.set_input(opt_rets)


# In[ ]:


ES025.run(ticker=ticker)


# ### Back Testing

# In[ ]:


time.set_start("2018-01")
time.set_end("2019-12")


# In[ ]:


annual_rets.run(ticker=ticker)


# In[ ]:


var = VaR025.run(ticker=ticker)
var


# In[ ]:


np.sum(var["max_exedence"] <= 0.025)


# ### RiskMetrics

# In[ ]:


daily_var = Custom(risk_metrics, 0.94)(opt_rets)


# In[ ]:


daily_var.run(ticker=ticker)


# In[ ]:


VaR01 = am.pipeline(ValueAtRisk(quantiles=[0.01]))


# In[ ]:


var = VaR01.run(ticker=ticker)
var


# In[ ]:


np.sum(var["max_exedence"] <= 0.01)


# In[ ]:




