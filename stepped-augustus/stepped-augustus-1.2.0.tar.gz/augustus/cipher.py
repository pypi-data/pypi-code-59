from typing import Collection, Iterable


class SteppedAugustus:
    """Represents a message to be encoded/decoded.

    Usage:
    >>> from augustus import SteppedAugustus as SA
    >>>
    >>> SA("Hello, World", 1).right_cipher
    'Igopt, Xqupi'
    >>>
    >>> SA("Igopt, Xqupi", 1).left_cipher
    'Hello, World'
    >>>
    >>> # Alternatively the _cipher method can be used for lazy
    >>> # evaluation and customizing the direction.
    >>>
    >>> for char in SA("Hello", 1)._cipher(1):
    ...     print(char)
    >>>
    >>> # Additionally, skip_chars and stop_chars can specified
    >>> # to semantically modify the behaviour of the algorithm.
    >>>
    >>> # Shifts with 10234
    >>> SA("Hello", skip_chars="H").right_cipher
    'Ienos'
    >>>
    >>> # Shifts with 11234
    >>> SA("Hello", stop_chars="e").right_cipher
    'Ifnos'
    >>>
    >>> # Shifts with 10123
    >>> SA("Hello", skip_chars="e", stop_chars="e").right_cipher
    'Iemnr'


    Parameters
    ----------
    message : str
        The message to be encoded.
    multiplier : int
        The multiplier to be applied when encoding.
    skip_chars : Container[str]
        Characters to be skipped when encoding.
    stop_chars : Container[str]
        Characters to be used to reset the algorithm.
    """

    def __init__(
        self,
        message: str,
        multiplier: int = 1,
        skip_chars: Collection[str] = "",
        stop_chars: Collection[str] = "",
    ) -> None:

        if not isinstance(message, str):
            raise TypeError("Cannot use {type(message)} as message.")

        if not isinstance(multiplier, int):
            raise TypeError("Cannot use {type(multiplier)} as multiplier.")

        if not isinstance(skip_chars, Collection):
            raise TypeError("Cannot use {type(skip_chars)} as skip_chars.")

        if not isinstance(stop_chars, Collection):
            raise TypeError("Cannot use {type(stop_chars)} as skip_chars.")

        self.message = message
        self.multiplier = multiplier

        self.skip_chars = skip_chars
        self.stop_chars = stop_chars

    def _do_skip(self, char: str) -> bool:
        """Checks if a given character must be skipped."""
        checks = (
            not char.isascii(),
            not char.isalpha(),
            char in self.skip_chars,
        )

        return any(checks)

    def _do_stop(self, char: str) -> bool:
        """Checks if a given character is a stop character."""
        checks = (
            char.isspace(),
            char in self.stop_chars,
        )

        return any(checks)

    def _cipher(self, direction: int) -> Iterable[str]:
        """Ciphers the message attribute given the direction
        and yields each character in a lazy manner."""

        position = 1

        for char in self.message:
            if self._do_stop(char):
                position = 1

            if self._do_skip(char):
                yield char
                continue

            case_start = 65 if char.isupper() else 97

            offset_mod = position * self.multiplier * direction
            true_offset = (ord(char) - case_start + offset_mod) % 26

            yield chr(case_start + true_offset)

            position += 1

    @property
    def right_cipher(self) -> str:
        """The message attribute ciphered to the right."""
        return "".join(self._cipher(1))

    @property
    def left_cipher(self) -> str:
        """The message attribute ciphered to the left."""
        return "".join(self._cipher(-1))
