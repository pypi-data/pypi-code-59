import numpy as np
from ptc.types import Point3f


def _calculate_coefficient_matrix(
    p1: Point3f, p2: Point3f, p3: Point3f, p4: Point3f
) -> np.array:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    x3, y3, z3 = p3
    x4, y4, z4 = p4
    return np.array(
        [
            [x1 - x2, y1 - y2, z1 - z2],
            [x2 - x3, y2 - y3, z2 - z3],
            [x3 - x4, y3 - y4, z3 - z4],
        ]
    )


def _calculate_ordinate_values(
    p1: Point3f, p2: Point3f, p3: Point3f, p4: Point3f
) -> np.array:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    x3, y3, z3 = p3
    x4, y4, z4 = p4
    return np.array(
        [
            ((x2 * x2 + y2 * y2 + z2 * z2) - (x1 * x1 + y1 * y1 + z1 * z1))
            / 2,
            ((x3 * x3 + y3 * y3 + z3 * z3) - (x2 * x2 + y2 * y2 + z2 * z2))
            / 2,
            ((x4 * x4 + y4 * y4 + z4 * z4) - (x3 * x3 + y3 * y3 + z3 * z3))
            / 2,
        ]
    )


def calculate_center(
    p1: Point3f, p2: Point3f, p3: Point3f, p4: Point3f
) -> Point3f:
    a = _calculate_coefficient_matrix(p1, p2, p3, p4)
    b = _calculate_ordinate_values(p1, p2, p3, p4)
    xs, ys, zs = np.linalg.solve(a, b)
    return (-xs, -ys, -zs)
