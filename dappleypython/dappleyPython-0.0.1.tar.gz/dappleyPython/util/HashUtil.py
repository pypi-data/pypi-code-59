import binascii
import hashlib

import _pysha3
import base58

from DappleySdk.DError import ParamError
from DappleySdk.util.Constant import ADDRESS_CHECKSUM_LENGTH


class HashUtil:
    def __init__(self):
        pass

    @staticmethod
    def get_public_key_hash_with_bytes(public_key_bytes):
        v = _pysha3.sha3_256()
        v.update(public_key_bytes[1:])
        m = hashlib.new('ripemd160')
        m.update(v.digest())

        return b'\x5A'+m.digest()

    @staticmethod
    def get_public_key_hash_with_str(public_key_string):
        full_payload = base58.b58decode(public_key_string)
        return full_payload[:len(full_payload) - ADDRESS_CHECKSUM_LENGTH]

    @staticmethod
    def get_pub_key_hash_check_sum(pub_key_hash, length):
        m = hashlib.sha256()
        m2 = hashlib.sha256()
        m.update(pub_key_hash)
        first_sha = m.digest()
        m2.update(first_sha)
        second_sha = m2.digest()
        return second_sha[:length]

    @staticmethod
    def secp256k1_sign(data, sign_key):
        if len(data) != 32:
            raise ParamError(ValueError, "Expected 32 byte input to ECDSA signature, not {}".format(len(data)))
        sig_check = sign_key.ecdsa_sign_recoverable(msg=data, raw=True)
        sig_ser = sign_key.ecdsa_recoverable_serialize(sig_check)
        hex_str = "{}{}".format(binascii.hexlify(sig_ser[0]), binascii.hexlify(bytearray([sig_ser[1]])))
        return binascii.unhexlify(hex_str)
