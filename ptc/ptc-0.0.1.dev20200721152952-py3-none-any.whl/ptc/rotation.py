import math
import numpy as np


def matrix(roll: float, pitch: float, yaw: float) -> np.array:
    salpha, calpha = math.sin(roll), math.cos(roll)
    sbeta, cbeta = math.sin(pitch), math.cos(pitch)
    sgamma, cgamma = math.sin(yaw), math.cos(yaw)
    a11 = cgamma * cbeta
    a12 = -sgamma * cbeta
    a13 = sbeta
    a21 = cgamma * sbeta * salpha + sgamma * calpha
    a22 = -sgamma * sbeta * salpha + cgamma * calpha
    a23 = -cbeta * salpha
    a31 = -cgamma * sbeta * calpha + sgamma * salpha
    a32 = sgamma * sbeta * calpha + cgamma * salpha
    a33 = cbeta * calpha
    return np.array([[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]])
