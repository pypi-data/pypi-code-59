from DappleySdk.model.Utxo import Utxo


class UtxoManager:
    def __init__(self):
        pass

    @staticmethod
    def get_suitable_utxos(all_utxo, total_cost):
        if all_utxo is None:
            return None
        spendables = []
        accumulated = 0
        for utxo in all_utxo:
            if utxo is None:
                continue
            accumulated = accumulated + int(utxo.amount.encode('hex'), 16)
            temp_utxo = Utxo(utxo.amount, utxo.public_key_hash, utxo.txid, utxo.tx_index)
            spendables.append(temp_utxo)

            if accumulated - total_cost >= 0:
                break
        if accumulated - total_cost < 0:
            return None
        return spendables
