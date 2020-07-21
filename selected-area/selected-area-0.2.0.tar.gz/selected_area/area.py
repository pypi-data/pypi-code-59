from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Tuple, Union


@dataclass
class Point:
    x: [float, int]
    y: [float, int]


def convert_to_point(*args):
    args = list(args)
    for index, arg in enumerate(args):
        if type(arg) not in [Point, tuple]:
            raise TypeError('point must be of type Point or tuple')
        if type(arg) == tuple:
            if len(arg) != 2:
                raise ValueError('point must have exactly 2 values (x and y)')
            args[index] = Point(*arg)
    return args


class Segment:
    def __init__(self, p1, p2):
        """
        :type p1: Union[Point, Tuple[Union[float, int], Union[float, int]]
        :type p2: Union[Point, Tuple[Union[float, int], Union[float, int]]
        """
        self.p1, self.p2 = convert_to_point(p1, p2)

    def line(self):
        """
        :rtype: Tuple[float, float, float]
        """
        a = self.p1.y - self.p2.y
        b = self.p2.x - self.p1.x
        c = self.p1.x * self.p2.y - self.p2.x * self.p1.y
        return a, b, -c

    def intersection_point(self, segment2):
        """
        :type segment2: Segment
        :rtype: Optional[Point]
        """
        line1 = self.line()
        line2 = segment2.line()
        d = line1[0] * line2[1] - line1[1] * line2[0]
        dx = line1[2] * line2[1] - line1[1] * line2[2]
        dy = line1[0] * line2[2] - line1[2] * line2[0]
        if d != 0:
            x = dx / d
            y = dy / d
            return Point(x, y)

    def __repr__(self):
        return f'Segment(p1={self.p1!r}, p2={self.p2!r})'


class SelectedArea:
    def __init__(self, p1, p2):
        """
        :type p1: Union[Point, Tuple[Union[float, int], Union[float, int]]
        :type p2: Union[Point, Tuple[Union[float, int], Union[float, int]]
        """
        self.p1, self.p2 = convert_to_point(p1, p2)

    def point_inside(self, point):
        """
        :type point: Point
        :rtype: bool
        """
        return self.p1.x <= point.x <= self.p2.x and self.p1.y <= point.y <= self.p2.y

    def crossing_line(self, segment):
        """
        :type segment: Segment
        :rtype: bool
        """
        plot1 = Segment(self.p1, Point(self.p2.x, self.p1.y))
        plot2 = Segment(Point(self.p1.x, self.p2.y), self.p2)
        intersections = [plot1.intersection_point(segment), plot2.intersection_point(segment)]
        for intersection in intersections:
            if intersection and self.point_inside(intersection):
                return True
        return False

    def contains(self, segment):
        """
        :type segment: Segment
        :rtype: bool
        """
        points = [segment.p1, segment.p2]
        for point in points:
            if self.point_inside(point):
                return True
        return self.crossing_line(segment)
