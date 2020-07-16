"""
Contains a class which describes the time period and interval of a simulation.
"""

import yfinance
import bisect

class PriceCache:
    """
    This class stores the price of a certain stock at a certain time.
    """
    def __init__(self):
        # Cache format: {Stock: {Interval: {Datetime: Stock data}}
        self.cache = {}

        # Stores the ranges of data that have already been downloaded
        # Format: {Stock: {Interval: {Start of range: End of range}}}
        self.downloaded_ranges = {}

    def _save_range(self, symbol, start_time, end_time, interval):
        if symbol not in self.cache[symbol]:
            self.cache[symbol] = {}

        symbol_cache = self.cache[symbol]
        
        if interval not in symbol_cache:
            symbol_cache[interval] = {}

        # This is a reference, so when we edit this, we are actually editing self.cache[symbol][interval] indirectly
        interval_cache = symbol_cache[interval]
        
        data = yfinance.Ticker(symbol).history(start=start_time, end=end_time, interval=interval)

        # Returns {datetime: stock_data, ...}
        rows = data.to_dict('index')

        # Interval_cache stores 
        interval_cache.update(rows)

    def cache_stock_data(self, symbol, start, end, interval):
        """
        Caches the stock data downloaded from the yfinance downloader.

        If the data was already cached, does not cache again.

        If there are "holes" in the data (eg you have up to April 10, and past April 12, but you want
        data from April 9 - April 15) then it will patch the holes, but not redownload the other data.

        Args:
            symbol (string): Stock symbol
            start (datetime): The beginning of the data you would like to download
            end (datetime): The end of the data you would like to download
            interval: The width of each bar (30min, 1hour, 1day, etc)
        """

        # Find which ranges of time have been downloaded
        ranges = self.downloaded_ranges.get(symbol, {}).get(interval, [])

        # If nothing has been downloaded yet
        if len(ranges) == 0:
            # Add the start/end markers
            ranges[start] = end

            self._save_range(symbol, start, end, interval)
            return

        # Here, we optimize!
        # Any ranges that are already downloaded within this range
        # we don't need to download again.

        for range_start, range_end in sorted(ranges.items()):
            if range_end > start:
                start = range_end

                # extend this range to the right from range_end to end
                ranges[range_start] = end

            if range_start < end:
                end = range_start

                # extend this range to the left from range_start to start
                del ranges[range_start]
                ranges[start] = range_end

            if range_start <= start <= end <= range_end:
                del ranges[range_start]
            
        self._save_range(symbol, start, end, interval)

    def get_price(self, symbol, interval, time):
        """
        This gets the value of a stock at self.current_time.
        If the stock is not loaded yet in the cache, it will
        load the data from current_time up to end_time.

        Args:
            symbol (string): The stock symbol to look up
        """
        
        self.cache_stock_data(symbol, time, time, interval)

        return self.cache[symbol][interval][time]