class Utxo(object):
    def __init__(self, amount, public_key_hash, tx_id, vout_index):
        self.amount = amount
        self.public_key_hash = public_key_hash
        self.tx_id = tx_id
        self.vout_index = vout_index
