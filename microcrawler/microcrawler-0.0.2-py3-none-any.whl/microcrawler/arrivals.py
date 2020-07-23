# Utilities for predicting the next time of arrival

from statistics import mode, StatisticsError

def approx_mode(xs):
    xr = [round(x) for x in xs]
    try:
        return mode(xr)
    except StatisticsError:
        return None
