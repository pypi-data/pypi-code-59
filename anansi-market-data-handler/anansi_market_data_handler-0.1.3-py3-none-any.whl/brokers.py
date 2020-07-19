""" A finalidade deste módulo é prover comunicação (de baixo nível para o
referencial do usuário utilizador do sistema) com as corretoras suportadas.

Neste sentido, deve ser capaz de abstrair protocolos de rede, como HTTP, AMPQ,
FTP e similares, servindo como uma API python para que o restante do sistema 
se comunique com as corretoras em questão.

Esta comunicação pode se dar tanto no sentido de obtenção de dados de mercado
(candlesticks/klines, book de ordens, market depth, etc) como disparamento de
ordens de compra/venda/stop ou mesmo obtenção dos dados de trades.

Toda simplicidade aqui é importante, a fim de reduzir a superfície de erros.
Por exemplo: se a corretora possui um limite de requests, dada uma janela de
tempo, não é função deste módulo interromper o fluxo de requests caso este
limite esteja próximo de ser atingido; um pedido só pode passar para esta API
depois de tratado por uma fila, ou gerenciador de pedidos.
"""

import requests
import pendulum
from . import settings, my_tools

doc_inherit = my_tools.DocInherit


def get_response(endpoint: str) -> requests.models.Response:
    with requests.get(endpoint) as response:
        if response.status_code == 200:
            return response


class Broker:
    """Encapsula as funções essenciais de comunicação com a corretora, como 
    pedido de dados e disparamento de ordens.
    """

    def __init__(self):
        pass

    def server_time(self) -> int:
        """Data e horário do servidor da corretora

        Returns:
            int: Timestamp em segundos
        """
        raise NotImplementedError

    def was_request_limit_reached(self) -> bool:
        """Teste booleano para verificar se o limite de requests, no minuto
        corrente e um IP, foi atingido; utilizando a informação
        'x-mbx-used-weight-1m' (ou similar) do header do response da corretora,
        retorna o número de requests feitos no minuto corrente.

        Returns: 
            bool: Limite atingido?
        """
        raise NotImplementedError

    def klines(
        self, symbol: str, interval: str, ignore_opened_candle: bool = True, **kwargs
    ) -> list:
        """Candlesticks históricos, também conhecidos como "klines".

        Args:
        =====
        
        symbol (str)   -- Símbolo do ativo
        interval (str) -- Intervalo (escala) dos candlesticks
        
        **kwargs:
        =========

        number_of_candles (int) -- Número de candelesticks desejados por série;
        observar limite de cada corretora ao implementar o método.

        Também é possível passar os timestamps, medidos em segundos:
        since (int) -- Open_time do primeiro candlestick da série 
        until (int) -- Open_time do último candlestick da série
        
        Returns: 
        
        list -- Lista formada por N sub-listas, em que:

        - N é o número de candles da série, retornada no response, podendo ser
          menor ou igual à _LIMIT_PER_REQUEST

        - As sub-listas contém as informações (open_time, open, high, low, ...,
          volume, ...) de cada candlestick da série buscada
        """
        raise NotImplementedError

    def _oldest_open_time(self, symbol: str, interval: str) -> int:
        """Data e horário do open time do primeiro candle deste tipo (symbol 
        e interval) armazenado no servidor da corretora

        Returns:
            int: Timestamp em segundos
        """
        raise NotImplementedError


class BinanceApiWrapper(Broker, settings.Binance_):
    @doc_inherit
    def __init__(self):
        super(BinanceApiWrapper, self).__init__()
        self._api_key = (
            self.api_key
        )  # TODO: Testar importação da API, mockando direto no módulo settings
        self._api_secret = self.api_secret

    @doc_inherit
    def server_time(self) -> int:
        return int(
            float((get_response(self._time_endpoint)).json()["serverTime"]) / 1000
        )

    @doc_inherit
    def was_request_limit_reached(self) -> bool:
        requests_on_current_minute = int(
            (get_response(self._ping_endpoint)).headers["x-mbx-used-weight-1m"]
        )
        if requests_on_current_minute >= self._request_weight_per_minute:
            return True

        return False

    @doc_inherit
    def klines(
        self, symbol: str, interval: str, ignore_opened_candle: bool = True, **kwargs
    ) -> list:

        since: int = kwargs.get("since")
        until: int = kwargs.get("until")
        number_of_candles: int = kwargs.get("number_of_candles")
        endpoint = self._klines_endpoint.format(symbol, interval)

        if since:
            endpoint += "&startTime={}".format(str(since * 1000))
        if until:
            endpoint += "&endTime={}".format(str(until * 1000))
        if number_of_candles:
            endpoint += "&limit={}".format(str(number_of_candles))
        _klines = (get_response(endpoint)).json()
        if ignore_opened_candle:
            now = (pendulum.now(tz="UTC")).int_timestamp
            last_open_time = int((float(_klines[-1][0])) / 1000)
            if (now - last_open_time) < settings.seconds_in[interval]:
                _klines = _klines[:-1]
        return _klines

    @doc_inherit
    def _oldest_open_time(self, symbol: str, interval: str) -> int:
        return int(
            (
                self.klines(
                    symbol=symbol, interval=interval, since=1, number_of_candles=1
                )[0][0]
            )
            / 1000
        )
