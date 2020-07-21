from DappleySdk.lib.protobuf import transactionBase_pb2


class TxInput(object):
    def __init__(self, tx_id, vout, signature, pub_key):
        self.tx_id = tx_id
        self.vout = vout
        self.signature = signature
        self.pub_key = pub_key

    def to_proto(self):
        tx_input = transactionBase_pb2.TXInput()
        tx_input.txid = self.tx_id
        tx_input.vout = self.vout
        tx_input.signature = self.signature
        tx_input.public_key = self.pub_key
        return tx_input
