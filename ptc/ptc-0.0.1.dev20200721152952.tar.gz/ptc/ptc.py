import numpy as np
import scipy.optimize
from typing import Callable

from ptc import sphere, rotation, types


def model(
    point_rotations: types.CalibrationInput, coeffs: np.array
) -> np.array:
    result = [
        np.array(pr[0]) + np.dot(rotation.matrix(*pr[1]), coeffs)
        for pr in point_rotations
    ]
    return np.array(result)


def residual_fn(
    optimization_target: np.array,
) -> Callable[[np.array, types.CalibrationInput], np.array]:
    def fn(
        coeffs: np.array, point_rotations: types.CalibrationInput
    ) -> np.array:
        model_result = model(point_rotations, coeffs)
        residuals = (optimization_target - model_result) ** 2
        return np.sum(residuals, axis=0)

    return fn


def calibrate(
    data_points: types.CalibrationInput,
    initial_guess: types.Point3f = (0.1, 0.1, 0.1),
) -> scipy.optimize.OptimizeResult:
    if len(data_points) < 4:
        raise ValueError("Not enough data points (less than 4)")

    points = [d[0] for d in data_points][:4]
    sphere_center = np.array(sphere.calculate_center(*points))
    initial_coeffs = np.array(initial_guess)
    optimization_target = np.array(
        [sphere_center for _ in range(len(data_points))]
    )
    optimization_result = scipy.optimize.least_squares(
        residual_fn(optimization_target),
        initial_coeffs,
        args=(data_points,),
        ftol=5e-9,
        xtol=5e-9,
        jac="3-point",
        loss="soft_l1",
    )
    return optimization_result
