from typing import Dict
from base64 import b64decode, b64encode
from r2dto import Serializer, ValidationError, InvalidTypeValidationError
from r2dto.fields import StringField, IntegerField, ObjectField, ListField, Field

from blatann.nrf.nrf_types import BLEGapAddr


class GattsCache(object):
    def __init__(self):
        self.entries: Dict[BLEGapAddr, bytes] = {}


class BLEGapAddrField(Field):
    def clean(self, data):
        return BLEGapAddr.from_string(data)

    def object_to_data(self, obj):
        if not isinstance(obj, BLEGapAddr):
            raise InvalidTypeValidationError(self.name, BLEGapAddr.__name__, type(obj))
        return str(obj)


class BytesField(Field):
    def __init__(self):
        super(BytesField, self).__init__()

    def clean(self, data):
        try:
            return b64decode(data)
        except Exception as e:
            raise ValidationError(str(e))

    def object_to_data(self, obj):
        if not isinstance(obj, bytes):
            raise InvalidTypeValidationError(self.name, bytes.__name__, type(obj))
        return b64encode(obj)


class DictField(Field):
    def __init__(self, key_field, value_field):
        super(DictField, self).__init__()
        self.key_field: Field = key_field
        self.value_field: Field = value_field

    def clean(self, data):
        if not isinstance(data, dict):
            return InvalidTypeValidationError(self.name, dict.__name__, type(data))
        typed_dict = {}
        for k, v in data.items():
            typed_dict[self.key_field.clean(k)] = self.value_field.clean(v)
        return typed_dict

    def object_to_data(self, obj):
        if not isinstance(obj, dict):
            return InvalidTypeValidationError(self.name, dict.__name__, type(obj))
        data_dict = {}
        for k, v in obj.items():
            k1 = self.key_field.object_to_data(k)
            v1 = self.value_field.object_to_data(v)
            data_dict[k1] = v1
        return data_dict


class GattsCacheSerializer(Serializer):
    entries = DictField(BLEGapAddrField(), BytesField())

    class Meta:
        model = GattsCache


def main():
    cache = GattsCache()
    addr1 = BLEGapAddr.from_string("00:01:02:03:04:05,s")
    addr2 = BLEGapAddr.from_string("00:01:02:03:04:06,s")
    addr3 = BLEGapAddr.from_string("00:01:02:03:04:07,s")
    d1 = b"1234567890"
    d2 = b"9876543210"
    d3 = b"5555555555"
    cache.entries[addr1] = d1
    cache.entries[addr2] = d2
    cache.entries[addr3] = d3
    print(cache.entries)
    print()

    s = GattsCacheSerializer(object=cache)
    s.validate()
    print(s.data)

    s1 = GattsCacheSerializer(data=s.data)
    s1.validate()
    print(s.object.entries)
    print()


if __name__ == '__main__':
    main()