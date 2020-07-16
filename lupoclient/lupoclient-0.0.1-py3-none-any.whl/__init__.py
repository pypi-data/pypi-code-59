"""

Zorro Client - provides easy access to indicators and strategies.

This is a wrapper for the REST API.

"""

# Contains API_URL and join_paths() methods
from .common import API_URL, join_paths

from .api.client import API
from .backtest.simulator import Simulator
from .models.strategy import Strategy
from .models.indicator import Indicator
from .stockdata import StockData

import json

with open("./presets.json") as presets_file:
    presets = json.load(presets_file)
