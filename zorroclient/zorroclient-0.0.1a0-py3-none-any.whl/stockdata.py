"""
This is a general class that stores stock data for backtesting
"""

import yfinance

class StockData:
    def __init__(self, data, dates):
        self.dates = dates
        self.data = data
        
    def __getitem__(self, symbol):
        """ Gets a symbol's data """
        return self.data[symbol]

    @classmethod
    def create(cls, stock_list, start, end, interval):
        """
        Creates a stock dataframe, which stores data for a list of stocks,
        all within the same range of dates.
        """

        downloaded = yfinance.download(
            tickers=" ".join(stock_list),
            start=start,
            end=end,
            interval=interval
        )
        
        # Stores the list of dates to iterate over during backtesting
        unique_dates = set()

        # Create a dict of {Stock: Dataframe}
        separated_dataframes = {}
        
        for symbol in stock_list:
            symbol = symbol.upper()

            # access the stock-specific data.
            # the data is structured
            # Price          High         Low      ...
            # AMZN AAPL      AMZN AAPL    AMZN AAPL
            # To select Price    High    Low for just AMZN, we use 'cross sections'.
            # See more: https://stackoverflow.com/questions/45128523/pandas-multiindex-how-to-select-second-level-when-using-columns
            symbol_price_data = downloaded.xs(symbol, axis=1, level=1)
            separated_dataframes[symbol] = symbol_price_data

            unique_dates.update(symbol_price_data.index)

        dates = sorted(unique_dates)

        return cls(data=separated_dataframes, dates=dates)