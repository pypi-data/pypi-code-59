from DappleySdk.lib.protobuf import transactionBase_pb2


class TxOutput(object):
    def __init__(self, value, public_key_hash, contract):
        self.value = value
        self.public_key_hash = public_key_hash
        self.contract = contract

    def to_proto(self):
        proto_tx_out = transactionBase_pb2.TXOutput(value=self.value, contract=self.contract,
                                                    public_key_hash=self.public_key_hash)
        return proto_tx_out

    def parse_proto(self, proto_tx_out):
        self.value = proto_tx_out.value
        self.public_key_hash = proto_tx_out.public_key_hash
        self.contract = proto_tx_out.contract
