#!/usr/bin/env python3
#
# Copyright 2020 Graviti. All Rights Reserved.
#

"""This file defines class Shape, Box2D, Box3D, PointList, Polygon, Polyline, Keypoints"
"""

from copy import deepcopy
from typing import Any, Dict, List, Union


# pylint: disable=too-few-public-methods
class Shape:
    """A base class used to represent shapes.
    """

    NAME: str

    def __init__(self) -> None:
        self._data: Union[List[Any], Dict[str, Any]]

    def dumps(self) -> Union[List[Any], Dict[str, Any]]:
        """Returns all the information about this shape.

        :return: All the information of the shape, a list or a dictionary
        """
        return deepcopy(self._data)


class Box2D(Shape):
    """A class used to represent  2D rectangle extending the :class `Shape`

    :param x1: x coordinate of the bottom-left corner
    :param y1: y coordinate of the bottom-left corner
    :param x2: x coordinate of the top-right corner
    :param y2: y coordinate of the top-right corner
    """

    NAME = "box2D"

    def __init__(self, x1: float, y1: float, x2: float, y2: float) -> None:
        super().__init__()
        self._data: List[Dict[str, float]] = [
            {"x": x1, "y": y1},
            {"x": x2, "y": y2},
        ]


class Box3D(Shape):
    """A class used to represent a 3D box extending the :class `Shape`
    """

    NAME = "box3D"

    def __init__(self) -> None:
        super().__init__()
        self._data: Dict[str, Dict[str, float]] = {}

    # pylint: disable=invalid-name
    def set_translation(self, x: float, y: float, z: float) -> None:
        """Set the translation of the 3D box.

        :param x: Translation along the x-axis
        :param y: Translation along the y-axis
        :param z: Translation along the z-axis
        """
        self._data["translation"] = {"x": x, "y": y, "z": z}

    def set_rotation(self, w: float, x: float, y: float, z: float) -> None:
        """Set the rotation of the 3D box.
        Quaternion is used to describe rotation.

        :param w: w component of the quaternion
        :param x: x component of the quaternion
        :param y: y component of the quaternion
        :param z: z component of the quaternion
        """
        self._data["rotation"] = {"w": w, "x": x, "y": y, "z": z}

    def set_size(self, x: float, y: float, z: float) -> None:
        """Set the size of the 3D box

        :param x: length of the 3D box along the x-axis
        :param y: length of the 3D box along the y-axis
        :param z: length of the 3D box along the z-axis
        """
        self._data["size"] = {"x": x, "y": y, "z": z}


class PointList(Shape):
    """A class used to represent a list of points extending the :class `Shape`.
    """

    def __init__(self) -> None:
        super().__init__()
        self._data: List[Dict[str, float]] = []

    # pylint: disable=invalid-name
    def add_point(self, x: float, y: float) -> None:
        """Add a point to the point list according to the given x, y coordinates

        :param x: x coordinate of the point to be added
        :param y: y coordinate of the point to be added
        """
        self._data.append({"x": x, "y": y})


class Polygon(PointList):
    """A class used to represent a polygon extending the :class `PointList`.
    """

    NAME = "polygon"


class Polyline(PointList):
    """A class used to represent a polyline extending the :class `PointList`
    """

    NAME = "polyline"


class Keypoints(PointList):
    """A class used to represent a list of keypoints extending the :class `PointList`
    """

    NAME = "keypoints"
