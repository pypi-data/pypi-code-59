class ConvertUtil:
    def __init__(self):
        pass

    @staticmethod
    def int_to_bytes(value):
        data = "{0:b}".format(value)
        return ConvertUtil.bitstring_to_bytes(data)

    @staticmethod
    def bitstring_to_bytes(s):
        v = int(s, 2)
        b = bytearray()
        while v:
            b.append(v & 0xff)
            v >>= 8
        return bytes(b[::-1])