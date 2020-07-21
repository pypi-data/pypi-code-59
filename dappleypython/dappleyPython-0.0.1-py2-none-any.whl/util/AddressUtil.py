import binascii

import base58
from DappleySdk.util.Constant import ADDRESS_CHECKSUM_LENGTH
from DappleySdk.util.HashUtil import HashUtil


class AddressUtil:
    def __init__(self):
        pass

    @staticmethod
    def validate_address(address):
        if address is None:
            return False
        full_payload = base58.b58decode(address)

        if (full_payload is None) or (len(full_payload) < ADDRESS_CHECKSUM_LENGTH):
            return False
        actual_check_sum = full_payload[len(full_payload)-ADDRESS_CHECKSUM_LENGTH:]

        pub_key_hash = full_payload[:len(full_payload)-ADDRESS_CHECKSUM_LENGTH]
        check_sum = HashUtil.get_pub_key_hash_check_sum(pub_key_hash, ADDRESS_CHECKSUM_LENGTH)
        return actual_check_sum == check_sum
