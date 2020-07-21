import numpy as np
from hamcrest import *
from ptc import sphere


def test_sphere_center_close(valid_data_point):
    points = [p[0] for p in valid_data_point["input"]][:4]
    expected = valid_data_point["sphere_center"]
    got = sphere.calculate_center(*points)
    center_is_close = np.allclose(np.array(got), np.array(expected), atol=1e-3)
    assert_that(center_is_close, is_(True))
