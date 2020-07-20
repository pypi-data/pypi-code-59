from .radix import Radix


class Binary(Radix):
    """
    Class Binary, implements functions to manipulate binary values.
    """
    def __init__(self, value):
        Radix.__init__(self, value)

    def convert_to(self, other_radix: int) -> int:
        if other_radix == 10:
            converted = self.convert_to_decimal(2)
        elif other_radix == 16:
            converted = self.convert_to_hex(2)
        elif other_radix == 8:
            converted = self.convert_to_octal(2)
        else:
            print("conversion to radix {} not available!".format(other_radix))
            converted = self._numerical_value
        return converted
