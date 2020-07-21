import binascii

from secp256k1 import PrivateKey

from DappleySdk.model.Transaction import Transaction
from DappleySdk.model.TxInput import TxInput
from DappleySdk.model.TxOutput import TxOutput
from DappleySdk.util.ConvertUtil import ConvertUtil
from DappleySdk.util.HashUtil import HashUtil


class TransactionManager:
    def __init__(self):
        pass

    def new_transaction(self, utxos, to_address, amount, private_key, tip, gas_limit, gas_price, contract):

        sign_key = PrivateKey(bytes(bytearray.fromhex(private_key)), raw=True)
        return self.inner_new_transaction(utxos, to_address, amount, sign_key, tip, gas_limit, gas_price,
                                          contract)

    def inner_new_transaction(self, utxos, to_address, amount, sign_key, tip, gas_limit, gas_price, contract):
        transaction = Transaction(None, [], [], tip, gas_limit, gas_price)
        # add vin list and return the total amount of vin values
        total_amount = self.build_vin(transaction, utxos, sign_key)

        change = self.calculate_change(total_amount, amount, tip, gas_limit, gas_price)
        if change < 0:
            return None

        # add vout list. If there is change is this transaction, vout list wound have two elements, or have just one to
        # coin receiver.
        self.build_vout(transaction, to_address, amount, change, sign_key, contract)

        # generate Id
        transaction.set_id()

        self.sign(transaction, sign_key, utxos)
        return transaction

    def build_vin(self, transaction, utxos, singn_key):
        pub_key = singn_key.pubkey.serialize(False)
        total_amount = 0
        for utxo in utxos:
            if utxo is None:
                continue

            tx_input = TxInput(utxo.tx_id, utxo.vout_index, None, pub_key[1:])
            # add from publicKey value
            total_amount = total_amount + int(utxo.amount.encode('hex'), 16)
            transaction.tx_inputs.append(tx_input)
        return total_amount

    def calculate_change(self, total_amount, amount, tip, gas_limit, gas_price):
        change = total_amount - amount
        if change < 0:
            return None
        change = change - tip
        if change < 0:
            return None
        if gas_limit is not None and gas_price is not None:
            change = change - gas_limit * gas_price
            if change < 0:
                return None
        return change

    def build_vout(self, transaction, to_address, amount, change, sign_key, contract):
        if change is not None and change < 0:
            return
        tx_output = TxOutput(b'', b'', '')
        if contract is not None:
            if to_address is None:
                # here need to generate contract address,if contract is None
                pass

            tx_output.contract = contract

        tx_output.value = ConvertUtil.int_to_bytes(amount)
        tx_output.public_key_hash = HashUtil.get_public_key_hash_with_str(to_address)
        transaction.tx_outputs.append(tx_output)

        if change is not None and change > 0:
            tx_output = TxOutput(b'', b'', '')
            # set from address's pubKeyHash
            tx_output.public_key_hash = HashUtil.get_public_key_hash_with_bytes(
                sign_key.pubkey.serialize(False))
            tx_output.value = ConvertUtil.int_to_bytes(change)
            transaction.tx_outputs.append(tx_output)

    def sign(self, transaction, sign_key, utxos):
        tx_inputs = transaction.tx_inputs
        if tx_inputs is None or len(tx_inputs) == 0:
            return
        utxo_map = self.get_prev_utxos(utxos)
        transaction_copy = transaction.trimed_copy()
        self.build_sign_value(transaction, utxo_map, transaction_copy, sign_key)

    def get_prev_utxos(self, utxos):
        utxo_map = {}
        for utxo in utxos:
            utxo_map[binascii.hexlify(utxo.tx_id) + "-" + str(utxo.vout_index)] = utxo
        return utxo_map

    def build_sign_value(self, transaction, utxo_map, transaction_copy, sign_key):
        tx_copy_inputs = transaction_copy.tx_inputs
        for i in range(0, len(tx_copy_inputs)):
            transaction.tx_inputs[i].signature = ''
            tx_input = tx_copy_inputs[i]
            old_pub_key = tx_input.pub_key
            utxo = utxo_map[binascii.hexlify(tx_input.tx_id) + "-" + str(tx_input.vout)]
            tx_input.pub_key = utxo.public_key_hash
            tx_copy_hash = transaction_copy.hash()
            tx_input.pub_key = old_pub_key
            signature = HashUtil.secp256k1_sign(tx_copy_hash, sign_key)
            transaction.tx_inputs[i].signature = signature
