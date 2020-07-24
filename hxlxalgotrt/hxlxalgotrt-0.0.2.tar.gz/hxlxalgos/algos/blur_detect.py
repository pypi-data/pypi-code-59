# -*- coding: UTF-8 -*-
import glob
import os
import shutil

import cv2
import numpy as np

__all__ = ["blur_detect", "blur_mult_detect"]

_BASE_FIX_FACE_SIZE = 48
"""
 * @brief global blur detect
 * @param
 *
 * @return
 *     - score
"""


def blur_detect(src):
    shape = src.shape
    if len(shape) == 3:
        if shape[2] != 1:
            gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        else:
            gray = src
    else:
        gray = src
    gray = cv2.GaussianBlur(gray, (3, 3), 0, 0, borderType=cv2.BORDER_DEFAULT)  # REPLICATE  BORDER_DEFAULT

    Lgrad = cv2.Laplacian(gray, cv2.CV_64F, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
    # Lgrad = cv2.Laplacian(gray, cv2.CV_16S, ksize = 3)

    # print Lgrad
    Lgrad = cv2.convertScaleAbs(Lgrad)

    mean, stddv = cv2.meanStdDev(Lgrad)

    return stddv.reshape(1)[0] ** 2


"""
 * @brief local clear side face detect
 * @param
 *
 * @return
 *     - score
"""


def find_clear_sideface(src):
    shape = src.shape
    if shape[2] != 1:
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    else:
        gray = src

    shape = src.shape
    row = shape[0]
    col = shape[1]

    Vstep = col / 2
    Hstep = row / 2
    shift = row / 16

    start_x = 0
    start_y = int(3 * shift)
    end_x = int(Vstep - shift)
    end_y = int(3 * shift + row - 6 * shift)
    VLsrc = gray[start_y:end_y, start_x:end_x]

    start_x = int(Vstep + shift - 1)
    start_y = int(3 * shift)
    end_x = int(Vstep + shift - 1 + Vstep - shift)
    end_y = int(3 * shift + row - 6 * shift)
    VRsrc = gray[start_y:end_y, start_x:end_x]
    VLblurPer = blur_detect(VLsrc)
    VRblurPer = blur_detect(VRsrc)

    m_val_l, stddv = cv2.meanStdDev(VLsrc)
    m_val_r, stddv = cv2.meanStdDev(VRsrc)

    score = 0
    if m_val_l.reshape(1)[0] > m_val_r.reshape(1)[0]:
        score = VLblurPer
    else:
        score = VRblurPer
    return score


"""
 * @brief 计算图像的大小等级
 * @param
 *
 * @return
 *     - 0, 1, 2, 3
"""


def get_size_level(src):
    shape = src.shape
    row = shape[0]
    col = shape[1]
    ret = -1
    size = (row * col) ** 0.5
    if size > 4 * _BASE_FIX_FACE_SIZE - 8:
        ret = 0
    elif size > 3 * _BASE_FIX_FACE_SIZE - 8:
        ret = 1
    elif size > 2 * _BASE_FIX_FACE_SIZE - 16:
        ret = 2
    else:
        ret = 3

    return ret


def blur_mult_detect(cvimg):
    thrshBlur = [20, 50, 140, 390]
    thrshSideClear = [20, 32, 90, 360]
    ret = True  # blur
    index = get_size_level(cvimg)
    dst = cv2.resize(cvimg, (_BASE_FIX_FACE_SIZE * (4 - index), _BASE_FIX_FACE_SIZE * (4 - index)))
    blurPer = blur_detect(dst)
    if blurPer > thrshBlur[index]:
        clear_degree = blurPer - thrshBlur[index]
        ret = False  # clear
    else:  # find clear in detect-blur
        score = find_clear_sideface(dst)
        if (score > thrshSideClear[index]) and (blurPer > thrshBlur[index] * 4 / 5):
            ret = False
        clear_degree = score - thrshSideClear[index]
    return ret, clear_degree


def test():
    input_dir = '/data/dataset/chaos/remark/fr-real-test/pview-exp-0.25'
    output_dir = '/data/dataset/chaos/remark/fr-real-test/pview-exp-0.25-blur-out'

    clear_count = 0
    blur_count = 0
    image_paths = glob.glob(os.path.join(input_dir, '**', '*.jpg'), recursive=True)
    nrof_image = len(image_paths)
    for idx, img_path in enumerate(image_paths, start=1):
        src_img = cv2.imread(img_path, 1)
        if not isinstance(src_img, np.ndarray):
            print('Failed to read ', img_path)
            continue

        if blur_mult_detect(src_img):
            blur_count += 1
            name = 'blur'
        else:
            clear_count += 1
            name = 'clear'
        output_path = os.path.join(output_dir, name)
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        shutil.copy(img_path, output_path)
        print('No. %5d/%5d, blur_count=%5d, clear_count=%5d' % (idx, nrof_image, blur_count, clear_count))


if __name__ == "__main__":
    test()
