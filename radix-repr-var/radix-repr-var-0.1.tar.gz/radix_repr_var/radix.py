from abc import ABC, abstractmethod
from math import pow


class Radix(ABC):
    """
    Radix class.
    This abstract base class gives a general definition on
    how to implement a subclass that allows to represent a
    numerical value into a specific (subclass defined) numerical base (radix).
    The class also provides an abstract method to convert to a specific radix
    """

    def __init__(self, value):
        self._numerical_value = value
        self._numerical_value_str = str(self._numerical_value)
        super().__init__()

    @abstractmethod
    def convert_to(self, other_radix):
        pass

    def convert_to_decimal(self, src_radix: int) -> int:
        n = len(self._numerical_value_str)
        s = 0
        for i in range(n):
            n -= 1
            s += int(self._numerical_value_str[i]) * pow(src_radix, n)
        return s

    def convert_to_binary(self, src_radix: int) -> int:
        if src_radix == 8:
            pass
        elif src_radix == 10:
            return self._convert_from_decimal()
        elif src_radix == 16:
            pass

    def _convert_from_decimal(self, dst_radix: int) -> int:
        n = self._numerical_value
        converted_val_str = ''
        while n > 0:
            r = n % dst_radix
            n = n / dst_radix
            converted_val_str = r + converted_val_str
        return int(converted_val_str)
