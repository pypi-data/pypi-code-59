#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import cv2
import numpy as np
from skimage import transform as trans

__all__ = ["align_face", ]


def calibrate_norm_landmark(landmarks, img_shape, face_height=112, face_width=112, is_ratio=False):
    landmarks_out = landmarks.copy()

    height, width = img_shape[:2]
    if is_ratio:
        landmarks_out[:, 0] *= width
        landmarks_out[:, 1] *= height
    ratio_x = face_width / float(width)
    ratio_y = face_height / float(height)
    landmarks_out[:, 0] *= ratio_x
    landmarks_out[:, 1] *= ratio_y
    return landmarks_out


def select_landmark(landmarks, num=7):
    nrof_landmark = len(landmarks)
    nrof_landmark_choices = (7, 98)
    num_choices = (7, 11)
    if num not in num_choices:
        raise ValueError('Num=%s not in %s' % (num, num_choices))

    if nrof_landmark not in nrof_landmark_choices:
        raise ValueError('Number landmarks =%d, not in %s' % (nrof_landmark, nrof_landmark_choices))

    if nrof_landmark == 7:
        if num == 7:
            landmark_indices = [i for i in range(num)]
        else:
            raise ValueError('Input arg num is wrong.')
    elif nrof_landmark == 98:
        if num == 7:
            landmark_indices = (16, 51, 54, 76, 82, 96, 97)
        elif num == 11:
            landmark_indices = (16, 51, 54, 60, 64, 68, 72, 76, 82, 96, 97)
        else:
            raise ValueError('Input arg num is wrong.')

    out = np.asarray([landmarks[idx] for idx in landmark_indices], dtype=np.float32)
    return out


def align_face(img, landmarks, mean_landmarks, bbox=None, method=0, img_size=112, margin=44, num=11):
    # src = np.array([
    #              [30.2946, 51.6963],
    #              [65.5318, 51.5014],
    #              [48.0252, 71.7366],
    #              [33.5493, 92.3655],
    #              [62.7299, 92.2041] ], dtype=np.float32 )
    method_choices = (0, 1, 2)
    if method not in method_choices:
        raise ValueError('Input argument method(%s) must be in choices=%s ' % (method, method_choices))

    cropped_face, landmarks_new = expand_crop_face(img.copy(), landmarks.copy(), bbox, margin)
    src = select_landmark(mean_landmarks, num)
    dst = select_landmark(landmarks, num)
    ratio = cal_face_ratio(src, dst)
    # ### update src
    src[:, 0] *= ratio
    src[:, 1] *= ratio

    src[:, 0] += (dst[2, 0] - src[2, 0])
    src[:, 1] += (dst[2, 1] - src[2, 1])

    height, width, _ = cropped_face.shape

    if method == 0:
        tform = trans.SimilarityTransform()
        tform.estimate(dst, src)
        mat = tform.params[:2, :]
    elif method == 1:
        mat, _ = cv2.estimateAffinePartial2D(dst.reshape(1, -1, 2), src.reshape(1, -1, 2), False)
    else:
        mat, _ = cv2.estimateAffinePartial2D(dst.reshape(1, -1, 2), src.reshape(1, -1, 2), True)

    # if norm_affine is True:
    four_pts_boundary = np.array([[0, 0, 1],
                                  [width - 1, 0, 1],
                                  [width - 1, height - 1, 1],
                                  [0, height - 1, 1]]).T
    four_pts_affined = np.dot(mat, four_pts_boundary).T
    min_xy = np.min(four_pts_affined, axis=0)
    max_xy = np.max(four_pts_affined, axis=0)
    new_width, new_height = [int(i) for i in max_xy - min_xy]

    mat[1, 2] -= min_xy[1]
    mat[0, 2] -= min_xy[0]

    warped = cv2.warpAffine(cropped_face.copy(), mat, (new_width, new_height), borderValue=0.0, flags=cv2.INTER_LINEAR)

    # get express face
    remap_landmarks = np.ones((landmarks.shape[0], 3), dtype=np.float32)
    remap_landmarks[:, :2] = landmarks
    remap_landmarks = np.dot(mat, remap_landmarks.T).T
    alpha_1 = np.linalg.norm(np.array(remap_landmarks[6]) - np.array(remap_landmarks[1]))
    alpha_2 = np.linalg.norm(np.array(remap_landmarks[1]) - np.array(remap_landmarks[5]))
    tl_x = int(remap_landmarks[1][0] - 1.2 * max(alpha_1, alpha_2))
    tl_y = int(remap_landmarks[1][1] - 1.3 * alpha_1)
    br_x = int(remap_landmarks[1][0] + 1.2 * alpha_1)
    br_y = int(max(remap_landmarks[1][1] + 3.2 * alpha_1, remap_landmarks[0][1]))
    expr_img = warped[tl_y:br_y, tl_x:br_x, :]
    if img_size is None:
        return warped, expr_img
    else:
        resized = cv2.resize(warped, (img_size, img_size), interpolation=cv2.INTER_LINEAR)
        return resized, expr_img


def cal_face_ratio(src_landmarks, dest_landmarks):
    ratios = []
    num_points = src_landmarks.reshape(-1, 2).shape[0]
    for i in range(num_points - 1):
        for j in range(i + 1, num_points):
            ratio = np.linalg.norm(dest_landmarks[j, :] - dest_landmarks[i, :]) / \
                    np.linalg.norm(src_landmarks[j, :] - src_landmarks[i, :])
            ratios.append(ratio)
    ratio_mean = np.mean(ratios)
    return ratio_mean


def expand_crop_face(img, landmarks, bbox=None, margin=44):
    """
    Expand bounding box with margin and update landmarks, return cropped face image and landmarks.
    """
    img_shape = img.shape
    if bbox is None:  # use center crop
        bbox = np.zeros(4, dtype=np.int32)
        bbox[0] = int(img_shape[1] * 0.0625)
        bbox[1] = int(img_shape[0] * 0.0625)
        bbox[2] = img_shape[1] - bbox[0]
        bbox[3] = img_shape[0] - bbox[1]
    else:
        bbox = np.squeeze(bbox).astype(np.int32)

    bbox[0] = np.maximum(bbox[0] - margin / 2, 0)
    bbox[1] = np.maximum(bbox[1] - margin / 2, 0)
    bbox[2] = np.minimum(bbox[2] + margin / 2, img_shape[1])
    bbox[3] = np.minimum(bbox[3] + margin / 2, img_shape[0])
    cropped = img[bbox[1]:bbox[3], bbox[0]:bbox[2], :]
    landmarks_new = np.squeeze(landmarks)
    landmarks_new[:, 0] -= bbox[0]
    landmarks_new[:, 1] -= bbox[1]
    return cropped, landmarks_new
