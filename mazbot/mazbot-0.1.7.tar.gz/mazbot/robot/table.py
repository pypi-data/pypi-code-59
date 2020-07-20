from typing import Tuple


class Table:
    """
    Stores table state and responds to within bounds of table queries
    """

    def __init__(self, width=5, length=5):
        """
        Constructor of Table class
        """
        self._width = width
        self._length = length

    def is_position_valid(self, coords: Tuple) -> bool:
        """
        Check if the coordinates passed in are outside the table

        Args:
            coords (Tuple): Coordinates to check whether within table

        Returns:
            bool: Returns True if coordinates are outside the table
        """

        (x, y) = coords
        return (x >= 0 and x <= self._width - 1) and (y >= 0 and y <= self._length - 1)
