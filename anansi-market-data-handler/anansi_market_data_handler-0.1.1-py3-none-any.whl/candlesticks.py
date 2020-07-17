import time
import pendulum
import pandas as pd
from copy import deepcopy
from . import settings, brokers, indicators


@pd.api.extensions.register_dataframe_accessor("ParseTime")
class ParseTime:
    def __init__(self, candles_dataframe):
        self._candles = candles_dataframe

    def from_human_readable_to_timestamp(self):
        self._candles["Open_time"] = self._candles.apply(
            lambda date_time: ParseDateTime(
                date_time["Open_time"]
            ).from_human_readable_to_timestamp(),
            axis=1,
        )

        if "Close_time" in self._candles:
            self._candles["Close_time"] = self._candles.apply(
                lambda date_time: ParseDateTime(
                    date_time["Close_time"]
                ).from_human_readable_to_timestamp(),
                axis=1,
            )

    def from_timestamp_to_human_readable(self):
        self._candles["Open_time"] = self._candles.apply(
            lambda date_time: ParseDateTime(
                date_time["Open_time"]
            ).from_timestamp_to_human_readable(),
            axis=1,
        )

        if "Close_time" in self._candles:
            self._candles["Close_time"] = self._candles.apply(
                lambda date_time: ParseDateTime(
                    date_time["Close_time"]
                ).from_timestamp_to_human_readable(),
                axis=1,
            )


@pd.api.extensions.register_dataframe_accessor("save_to")
class SaveTo:
    def __init__(self, candles_dataframe):
        self._candles_dataframe = candles_dataframe

    def csv(self):
        pass

    def database(self):
        pass


@pd.api.extensions.register_dataframe_accessor("apply_indicator")
class ApplyIndicator:
    def __init__(self, candles_dataframe):
        self._candles_dataframe = candles_dataframe
        self.trend = indicators.Trend(self._candles_dataframe)
        self.momentum = indicators.Momentum(self._candles_dataframe)
        self.volatility = indicators.Volatility(self._candles_dataframe)
        self.volume = indicators.Volume(self._candles_dataframe)


class ParseDateTime:
    fmt = "YYYY-MM-DD HH:mm:ss"

    def __init__(self, date_time_in):
        self.date_time_in = date_time_in

    def from_human_readable_to_timestamp(self):
        return pendulum.from_format(self.date_time_in, self.fmt, "UTC").int_timestamp

    def from_timestamp_to_human_readable(self):
        return pendulum.from_timestamp(self.date_time_in).to_datetime_string()


class CandlesFromBroker:
    """Dispondo basicamente de 3 métodos (oldest, newest, range), tem por 
    finalidade servir de fila para a solicitação de candlesticks às corretoras,
    dividindo o número de requests a fim de respeitar os limites das mesmas e
    interrompendo os pedidos caso este limite esteja próximo de ser atingido,
    entregando ao cliente os candles sanitizados e formatados.
    """

    _brokers = {
        "binance": "BinanceApiWrapper",
    }

    def __init__(self, exchange: str, symbol: str, interval: str):

        self._symbol = symbol.upper()
        self._interval = interval

        self._broker = getattr(brokers, self._brokers[exchange.lower()])()

        self._oldest_open_time = self._broker._oldest_open_time(
            symbol=self._symbol, interval=self._interval
        )

        self._request_step = (
            self._broker.records_per_request * settings.seconds_in[self._interval]
        )
        self._key_map_of_raw_candles = self._broker.kline_information_map
        self.CandleInTime = self._broker.CandleTime

        self.CandleOutFormat = settings.CandleStickFormat
        self._desired_indexes = []
        self._since = 1
        self._until = 2
        self.candles = []

    def _format_each(self, candle_in: list) -> list:
        candle_out = []
        for i in range(len(candle_in)):
            info_is_open_time = bool(self.CandleOutFormat.info[i] == "Open_time")
            info_is_close_time = bool(self.CandleOutFormat.info[i] == "Close_time")

            if info_is_open_time or info_is_close_time:
                _date_time = candle_in[i]

                if self.CandleInTime.fmt == "timestamp":
                    _date_time = float(_date_time)

                    if self.CandleInTime.unit == "milliseconds":
                        _date_time = _date_time / 1000

                    _date_time = pendulum.from_timestamp(int(_date_time))

                if info_is_open_time:
                    if _date_time.second != 0:
                        _date_time = _date_time.subtract(seconds=_date_time.second)

                candle_out.append(_date_time.int_timestamp)

            else:
                candle_out.append(float(candle_in[i]))

        return candle_out

    def _format(self, candles):
        if not self._desired_indexes:
            self._desired_indexes = [
                self._key_map_of_raw_candles.index(info)
                for info in self.CandleOutFormat.info
            ]

        return [
            self._format_each([candle[i] for i in self._desired_indexes])
            for candle in candles
        ]

    def _append_missing_on(self, candles):
        len_info = len(candles[0][1:])
        step = settings.seconds_in[self._interval]
        candles_dict = {str(candle[0]): candle[1:] for candle in candles}
        sanitized_candles = []
        since = candles[0][0]
        for open_time in range(since, self._until + 1, step):
            candle = []
            candle.append(open_time)
            try:
                candle += candles_dict.pop(str(open_time))
            except Exception as e:
                print(e)
                candle += len_info * [0.0]
            sanitized_candles.append(candle)
        return sanitized_candles

    def _treat_candles(self):
        raw_candles = deepcopy(self.candles)
        formatted_candles = self._format(raw_candles)
        self.candles = self._append_missing_on(formatted_candles)

    def _candles_from_broker(self):
        self.candles = []
        for timestamp in range(self._since, self._until + 1, self._request_step):
            if self._broker.was_request_limit_reached():
                time.sleep(10)
                print("Sleeping cause request limit was hit.")
            self.candles += self._broker.klines(
                symbol=self._symbol, interval=self._interval, since=timestamp
            )
        self._treat_candles()

        candles_data_frame = pd.DataFrame(
            self.candles, columns=settings.CandleStickFormat.info
        )
        candles_data_frame.ParseTime.from_timestamp_to_human_readable()

        return candles_data_frame

    def period(self, since: str, until: str) -> list:
        now = (pendulum.now(tz="UTC")).int_timestamp
        self._since = ParseDateTime(since).from_human_readable_to_timestamp()
        self._until = ParseDateTime(until).from_human_readable_to_timestamp()

        if self._since < self._oldest_open_time:
            self._since = self._oldest_open_time
        if self._until > now:
            self._until = now

        return self._candles_from_broker()[:-1]

    def oldest(self, number_of_candles=1):
        now = (pendulum.now(tz="UTC")).int_timestamp
        self._since = self._oldest_open_time
        self._until = (number_of_candles + 1) * settings.seconds_in[
            self._interval
        ] + self._since
        if self._until > now:
            self._until = now

        return self._candles_from_broker()[:number_of_candles]

    def newest(self, number_of_candles=1):
        now = (pendulum.now(tz="UTC")).int_timestamp
        self._until = now
        self._since = (
            self._until - (number_of_candles + 1) * settings.seconds_in[self._interval]
        )
        if self._since < self._oldest_open_time:
            self._since = self._oldest_open_time

        return self._candles_from_broker()[:number_of_candles]


class CandlesFromDatabase:
    pass


class CandlesFromCsv:
    pass
