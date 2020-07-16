class Trend:
    def __init__(self, candles_dataframe):

        self._candles_dataframe = candles_dataframe

    def simple_moving_average(self, price_source, number_of_samples):

        price = getattr(PriceSeriesFrom(self.klines), price_source + "_")()

        return price.rolling(number_of_samples).mean()


class Momentum:
    def __init__(self, candles_dataframe):

        self._candles_dataframe = candles_dataframe


class Volatility:
    def __init__(self, candles_dataframe):

        self._candles_dataframe = candles_dataframe


class Volume:
    def __init__(self, candles_dataframe):

        self._candles_dataframe = candles_dataframe
