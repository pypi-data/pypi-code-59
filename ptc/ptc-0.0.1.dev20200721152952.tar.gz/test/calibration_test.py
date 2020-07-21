import numpy as np
from hamcrest import *
import ptc

def test_valid_calibration(valid_data_point):
    inp = valid_data_point["input"]
    expected = valid_data_point["tcp_offset"]
    got = ptc.calibrate(inp)
    solution_is_close = np.allclose(got.x, np.array(expected), atol=1e-3)
    assert_that(solution_is_close, is_(True))


def test_valid_output_length(valid_data_point):
    inp = valid_data_point["input"]
    got = ptc.calibrate(inp)
    assert_that(got.x, has_length(3))


