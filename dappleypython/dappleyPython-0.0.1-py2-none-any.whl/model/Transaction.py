import binascii
import hashlib

from DappleySdk.lib.protobuf import transaction_pb2
from DappleySdk.model.TxInput import TxInput
from DappleySdk.model.TxOutput import TxOutput
from DappleySdk.util.Constant import TxTypeContract
from DappleySdk.util.ConvertUtil import ConvertUtil


class Transaction(object):
    def __init__(self, tx_id=None, tx_inputs=None, tx_outputs=None, tip=None, gas_limit=None, gas_price=None,
                 tx_type=TxTypeContract):
        self.id = tx_id
        self.tx_inputs = tx_inputs
        self.tx_outputs = tx_outputs
        self.tip = tip
        self.gas_limit = gas_limit
        self.gas_price = gas_price
        self.type = tx_type

    def __repr__(self):
        return 'Transaction(id={0!r}, vin={1!r}, vout={2!r},tip={3!r},gas_limit={4!r},gas_price={5!r})'.format(
            self.id, self.tx_inputs, self.tx_outputs, self.tip, self.gas_limit, self.gas_price)

    def set_id(self):
        self.id = self.hash()

    def to_proto(self):
        ts = transaction_pb2.Transaction()
        ts.id = self.id
        ts.tip = ConvertUtil.int_to_bytes(self.tip)
        ts.gas_price = ConvertUtil.int_to_bytes(self.gas_price)
        ts.gas_limit = ConvertUtil.int_to_bytes(self.gas_limit)
        for tx_input in self.tx_inputs:
            ts.vin.append(tx_input.to_proto())
        for tx_output in self.tx_outputs:
            ts.vout.append(tx_output.to_proto())
        ts.type=self.type
        return ts

    def trimed_copy(self):
        inputs = []
        outputs = []

        for vin in self.tx_inputs:
            inputs.append(TxInput(vin.tx_id, vin.vout, None, None))

        for vout in self.tx_outputs:
            outputs.append(TxOutput(vout.value, vout.public_key_hash, vout.contract))

        return Transaction(self.id, inputs, outputs, self.tip, self.gas_limit, self.gas_price)

    def hash(self):
        need_hash_data = ''
        for tx_input in self.tx_inputs:
            tx_bs_bytes = ''
            if tx_input.tx_id:
                tx_bs_bytes += tx_input.tx_id
            if tx_input.vout >= 0:
                tem_data = bytes(tx_input.vout).zfill(8)
                tx_bs_bytes += binascii.a2b_hex(tem_data)
            if tx_input.pub_key:
                tx_bs_bytes += tx_input.pub_key
            if tx_input.signature:
                tx_bs_bytes += tx_input.signature
            need_hash_data = need_hash_data + tx_bs_bytes
        for tx_output in self.tx_outputs:
            tx_output_bytes = ''
            tx_output_bytes += (tx_output.value + tx_output.public_key_hash + bytes(tx_output.contract))
            need_hash_data = need_hash_data + tx_output_bytes

        need_hash_data += (ConvertUtil.int_to_bytes(self.tip) + ConvertUtil.int_to_bytes(self.gas_limit) + ConvertUtil.int_to_bytes(self.gas_price))
        need_hash_data += binascii.a2b_hex(bytes(self.type).zfill(8))
        m = hashlib.sha256()
        m.update(need_hash_data)
        _hash = m.digest()
        return _hash
