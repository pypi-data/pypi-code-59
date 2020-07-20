from .radix import Radix


class Octal(Radix):
    """
    Class Octal, implements functions to manipulate octal values.
    """
    def __init__(self, value):
        Radix.__init__(self, value)

    def convert_to(self, other_radix: int) -> int:
        if other_radix == 10:
            converted = self.convert_to_decimal(8)
        elif other_radix == 16:
            converted = self.convert_to_hex(8)
        elif other_radix == 2:
            converted = self.convert_to_octal(8)
        else:
            print("conversion to radix {} not available!".format(other_radix))
            converted = self._numerical_value
        return converted
