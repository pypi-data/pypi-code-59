#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math

import cv2
import numpy as np

__all__ = ["get_front_level"]

# coordinates of ROS (robotic operative system) (z, x, y)
_P3D_RIGHT_SIDE = np.float32([-100.0, -77.5, -5.0])  # 0
_P3D_GONION_RIGHT = np.float32([-110.0, -77.5, -85.0])  # 4
_P3D_MENTON = np.float32([0.0, 0.0, -122.7])  # 8
_P3D_GONION_LEFT = np.float32([-110.0, 77.5, -85.0])  # 12
_P3D_LEFT_SIDE = np.float32([-100.0, 77.5, -5.0])  # 16
_P3D_FRONTAL_BREADTH_RIGHT = np.float32([-20.0, -56.1, 10.0])  # 17
_P3D_FRONTAL_BREADTH_LEFT = np.float32([-20.0, 56.1, 10.0])  # 26
_P3D_SELLION = np.float32([0.0, 0.0, 0.0])  # 27
_P3D_NOSE = np.float32([21.1, 0.0, -48.0])  # 30
_P3D_SUB_NOSE = np.float32([5.0, 0.0, -52.0])  # 33
_P3D_RIGHT_EYE = np.float32([-20.0, -65.5, -5.0])  # 36
_P3D_RIGHT_TEAR = np.float32([-10.0, -40.5, -5.0])  # 39
_P3D_LEFT_TEAR = np.float32([-10.0, 40.5, -5.0])  # 42
_P3D_LEFT_EYE = np.float32([-20.0, 65.5, -5.0])  # 45
_P3D_STOMION = np.float32([10.0, 0.0, -75.0])  # 62

_LANDMARKS_3D_MODEL = np.float32([_P3D_RIGHT_SIDE,
                                  _P3D_GONION_RIGHT,
                                  _P3D_MENTON,
                                  _P3D_GONION_LEFT,
                                  _P3D_LEFT_SIDE,
                                  _P3D_FRONTAL_BREADTH_RIGHT,
                                  _P3D_FRONTAL_BREADTH_LEFT,
                                  _P3D_SELLION,
                                  _P3D_NOSE,
                                  _P3D_SUB_NOSE,
                                  _P3D_RIGHT_EYE,
                                  _P3D_RIGHT_TEAR,
                                  _P3D_LEFT_TEAR,
                                  _P3D_LEFT_EYE,
                                  _P3D_STOMION])

_LANDMARKS_3D_MODEL = _LANDMARKS_3D_MODEL[:, [1, 2, 0]]

# The points to track
# These points are the ones used by PnP
# to estimate the 3D pose of the face
_TRACKED_POINTS = [0, 9, 16, 23, 32, 33, 46, 51, 54, 57, 60, 64, 68, 72, 90]


def get_camera_matrix(img_shape):
    focal_length = img_shape[1]
    center = (img_shape[1] / 2.0, img_shape[0] / 2.0)
    camera_matrix = np.array([
        [focal_length, 0, center[0]],
        [0, focal_length, center[1]],
        [0, 0, 1],
    ], dtype=np.float64)
    return camera_matrix


def get_rotation_vector(landmarks_image, landmarks_model, camera_matrix, dist_coeffs=None):
    if dist_coeffs is None:
        dist_coeffs = np.zeros((4, 1), dtype=np.float64)  # assuming no lens distortion
    success, rotation_vector, translation_vector = cv2.solvePnP(landmarks_model, landmarks_image, camera_matrix,
                                                                dist_coeffs, flags=cv2.SOLVEPNP_ITERATIVE)
    # print('success=', success)
    return rotation_vector, translation_vector


class Quaterniond(object):

    def __init__(self, rotation_vector):
        super(Quaterniond, self).__init__()
        self.rotation_vector = rotation_vector

        theta = np.linalg.norm(rotation_vector)
        self.theta = theta
        self.w = math.cos(theta / 2.0)
        self.x = math.sin(theta / 2.0) * rotation_vector[0, 0] / theta
        self.y = math.sin(theta / 2.0) * rotation_vector[1, 0] / theta
        self.z = math.sin(theta / 2.0) * rotation_vector[2, 0] / theta


def norm180(x):
    return x if x <= 180 else x - 360


def norm_angle(deg):
    # if deg >= -90 and deg <= 90:
    #     return deg
    # norm360 = lambda x: x % 360
    deg = norm180(norm180(deg))
    if 135 < deg <= 180:
        deg = -180 + deg
    if -180 < deg <= - 135:
        deg = 180 + deg
    return deg


def get_euler_angle(q):
    # pitch (x-axis rotation)
    t0 = 2.0 * (q.w * q.x + q.y * q.z)
    t1 = 1.0 - 2.0 * (q.x ** 2 + q.y ** 2)
    pitch = math.atan2(t0, t1)

    # yaw (y-axis rotation)
    t2 = 2.0 * (q.w * q.y - q.z * q.x)
    if np.fabs(t2) >= 1:
        yaw = np.copysign(np.pi / 2, t2)  # use 90 degrees if out of range
    else:
        yaw = math.asin(t2)

    # roll (z-axis rotation)
    t3 = 2.0 * (q.w * q.z + q.x * q.y)
    t4 = 1.0 - 2.0 * (q.y ** 2 + q.z ** 2)
    roll = math.atan2(t3, t4)

    # yaw, pitch, roll = [norm_angle(np.rad2deg(i)) for i in [yaw, pitch, roll]]
    yaw, pitch, roll = [np.rad2deg(i) for i in [yaw, pitch, roll]]
    return yaw, pitch, roll


def isRotationMatrix(R):
    Rt = np.transpose(R)
    shouldBeIdentity = np.dot(Rt, R)
    eye = np.identity(3, dtype=R.dtype)
    n = np.linalg.norm(eye - shouldBeIdentity)
    return n < 1e-6


def rotationMatrixToEulerAngles(R):
    assert (isRotationMatrix(R))

    sy = math.sqrt(R[0, 0] * R[0, 0] + R[1, 0] * R[1, 0])

    singular = sy < 1e-6

    if not singular:
        x = math.atan2(R[2, 1], R[2, 2])
        y = math.atan2(-R[2, 0], sy)
        z = math.atan2(R[1, 0], R[0, 0])
    else:
        x = math.atan2(-R[1, 2], R[1, 1])
        y = math.atan2(-R[2, 0], sy)
        z = 0

    return np.array([x, y, z])


def get_head_pose(img_shape, landmarks_2d_image, landmarks_3d_model):
    camera_matrix = get_camera_matrix(img_shape)
    rotation_vector, translation_vector = get_rotation_vector(landmarks_2d_image, landmarks_3d_model, camera_matrix)

    q = Quaterniond(rotation_vector)
    yaw, pitch, roll = get_euler_angle(q)
    return np.array([yaw, pitch, roll], dtype=np.float32)


def get_yaw_pitch_roll(h, w, landmarks):
    assert landmarks.shape == (98, 2)
    landmarks = landmarks.astype(np.float32)
    if np.max(landmarks) <= 1:
        landmarks[:, 0] = landmarks[:, 0] * w + 0.5
        landmarks[:, 1] = landmarks[:, 1] * h + 0.5

    landmarks_2d_image = landmarks[_TRACKED_POINTS]
    pose_deg = get_head_pose((h, w), landmarks_2d_image, _LANDMARKS_3D_MODEL)
    pose_rad = np.deg2rad(pose_deg)
    return pose_rad


def get_front_level(face_h, face_w, landmarks):
    """
    输出正脸程度（0-100), 越接近0越是正脸
    :param face_h: 原始脸图像块的高
    :param face_w: 原始脸图像块的宽
    :param landmarks: pfld的输出, np.array, shape(98, 2)
    :return: 正脸程度（0-100）
    """

    pose = get_yaw_pitch_roll(face_h, face_w, landmarks)
    pose = pose / math.pi * 180.0

    front_level = int(abs(pose[0]) / 90.0 * 100)

    return front_level
