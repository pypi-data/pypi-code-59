from DError import ParamError
from chain.TransactionManager import TransactionManager
from chain.UtxoManager import UtxoManager
from rpcnet.RPCClient import RPCClient


class Dappley(object):

    def __init__(self, host, port):
        self._host = host
        self._port = port

    @staticmethod
    def get_total_utxo_cost(amount, tip, gas_limit, gas_price):
        if amount is None:
            return 0
        total = amount
        total = total + tip

        if (gas_limit is not None) and (gas_price is not None):
            total = total + gas_price * gas_limit

        return total

    def send_transaction(self, from_address, to_address, amount, private_key, tip, gas_limit, gas_price, contract):
        if (from_address is None) or (to_address is None):
            raise ParamError(ValueError, "fromAddress or toAddress is empty!")

        all_utxo = RPCClient(self._host, self._port).get_utxos(from_address)
        if all_utxo is None:
            raise ParamError(ValueError, "FromAddress has no balance!")

        total_cost = self.get_total_utxo_cost(amount, tip, gas_limit, gas_price)
        utxos = UtxoManager.get_suitable_utxos(all_utxo, total_cost)

        if utxos is None:
            raise ParamError(ValueError, "Balance of fromAddress is not enough!")

        transaction = TransactionManager().new_transaction(utxos, to_address, amount, private_key, tip, gas_limit,
                                                           gas_price, contract)
        request_data = transaction.to_proto()
        send_tx_result = RPCClient(self._host, self._port).send_transaction(request_data)
        return send_tx_result


if __name__ == '__main__':
    pass
