"""Todos os indicadores de mercado são reunidos aqui, estendendo a classe
pandas.Dataframe

Indicadores baseados em um preço, devem tomar uma ou mais colunas, sendo:
"o"     = "Open"
"h"     = "High"
"l"     = "Low"
"c"     = "Close"
"oh2"   = ("Open" + "High")/2
"olc3"  = ("Open" + "Low" + "Close")/3
"ohlc4" = ("Open" + "High" + "Low" + "Close")/4
"""

import pandas as pd

_columns = {
    "o": ["Open"],
    "h": ["High"],
    "l": ["Low"],
    "c": ["Close"],
    "oh2": ["Open", "High"],
    "olc3": ["Open", "Low", "Close"],
    "ohlc4": ["Open", "High", "Low", "Close"],
}


class Indicator(object):
    __slots__ = ["name", "serie", "last"]

    def __init__(self):
        self.name: str = ""
        self.serie: pd.core.series.Series = 0
        self.last: float = 0


class Trend:
    """Indicadores de tendência
    """

    def __init__(self, candles_dataframe):

        self._candles_dataframe = candles_dataframe

    def simple_moving_average(
        self,
        number_of_candles: int,
        price_source: str = "ohlc4",
        create_indicator_column: bool = True,
    ) -> object:
        """Média móvel simples

        Args:
            number_of_candles (int): Número de candles que deve compor o 
            cálculo da média, devendo ser menor ou igual ao número de candles
            no dataframe

            price_source (str, optional): Como a série de preços deve ser
            interpretada?
            
            create_indicator_column (bool, optional): Cria no dataframe a
            coluna correspondente à série histórica do indicador. 
            Defaults to True.

        Returns:
            [object]: Indicador contendo o nome, série e último valor da série.
        """

        indicator = Indicator()
        _price_serie = 0
        indicator.name = "sma_{}_{}".format(price_source, str(number_of_candles))

        for column in _columns[price_source]:
            _price_serie += self._candles_dataframe[column]

        indicator.serie = (
            (_price_serie / len(_columns[price_source]))
            .rolling(window=number_of_candles)
            .mean()
        )
        indicator.last = indicator.serie.tail(1).item()
        if create_indicator_column:
            self._candles_dataframe[indicator.name] = indicator.serie

        return indicator


class Momentum:
    def __init__(self, candles_dataframe):

        self._candles_dataframe = candles_dataframe


class Volatility:
    def __init__(self, candles_dataframe):

        self._candles_dataframe = candles_dataframe


class Volume:
    def __init__(self, candles_dataframe):

        self._candles_dataframe = candles_dataframe
