# -*- coding: UTF-8 -*-
import cv2
import numpy as np


def get_affine_transform(center,
                         scale,
                         rot,
                         output_size,
                         shift=np.array([0, 0], dtype=np.float32),
                         inv=0,
                         pix_std=1):
    if not isinstance(scale, np.ndarray) and not isinstance(scale, list):
        # print(scale)
        scale = np.array([scale, scale])

    scale_tmp = scale * pix_std  # scale = [w/200,h/200] * 1.0 -> scale_tmp = [w, h] * 1.0 | w/h=3/4
    src_w = scale_tmp[0]
    dst_w = output_size[0]  # 192
    dst_h = output_size[1]  # 256

    rot_rad = np.pi * rot / 180
    src_dir = get_dir([0, src_w * -0.5], rot_rad)  # [0, src_w*-0.5] -> [旋转后的坐标]
    dst_dir = np.array([0, dst_w * -0.5], np.float32)  # [0, -128]

    src = np.zeros((3, 2), dtype=np.float32)
    dst = np.zeros((3, 2), dtype=np.float32)
    src[0, :] = center + scale_tmp * shift
    src[1, :] = center + src_dir + scale_tmp * shift
    dst[0, :] = [dst_w * 0.5, dst_h * 0.5]
    dst[1, :] = np.array([dst_w * 0.5, dst_h * 0.5]) + dst_dir

    src[2:, :] = get_3rd_point(src[0, :], src[1, :])
    dst[2:, :] = get_3rd_point(dst[0, :], dst[1, :])

    if inv:
        trans = cv2.getAffineTransform(np.float32(dst), np.float32(src))
    else:
        trans = cv2.getAffineTransform(np.float32(src), np.float32(dst))

    return trans


def affine_transform(pt, t):
    new_pt = np.array([pt[0], pt[1], 1.]).T
    new_pt = np.dot(t, new_pt)
    return new_pt[:2]


def get_3rd_point(a, b):
    direct = a - b
    return b + np.array([-direct[1], direct[0]], dtype=np.float32)


def get_dir(src_point, rot_rad):
    """
    求旋转之后的坐标
    |x'|   |cos_theta, -sin_theta|   |x|
    |y'| = |sin_theta,  cos_theta| * |y|
    """

    sn, cs = np.sin(rot_rad), np.cos(rot_rad)

    src_result = [0, 0]
    src_result[0] = src_point[0] * cs - src_point[1] * sn
    src_result[1] = src_point[0] * sn + src_point[1] * cs

    return src_result


def transform_preds(coords, center, scale, output_size, pix_std=1):
    target_coords = np.zeros(coords.shape)
    trans = get_affine_transform(center, scale, 0, output_size, inv=1, pix_std=pix_std)
    for p in range(coords.shape[0]):
        target_coords[p, 0:2] = affine_transform(coords[p, 0:2], trans)
    return target_coords


def bbox_iou(box1, box2, x1y1x2y2=True):
    if x1y1x2y2:
        mx = min(box1[0], box2[0])
        Mx = max(box1[2], box2[2])
        my = min(box1[1], box2[1])
        My = max(box1[3], box2[3])
        w1 = box1[2] - box1[0]
        h1 = box1[3] - box1[1]
        w2 = box2[2] - box2[0]
        h2 = box2[3] - box2[1]
    else:
        mx = min(box1[0] - box1[2] / 2.0, box2[0] - box2[2] / 2.0)
        Mx = max(box1[0] + box1[2] / 2.0, box2[0] + box2[2] / 2.0)
        my = min(box1[1] - box1[3] / 2.0, box2[1] - box2[3] / 2.0)
        My = max(box1[1] + box1[3] / 2.0, box2[1] + box2[3] / 2.0)
        w1 = box1[2]
        h1 = box1[3]
        w2 = box2[2]
        h2 = box2[3]
    uw = Mx - mx
    uh = My - my
    cw = w1 + w2 - uw
    ch = h1 + h2 - uh
    carea = 0
    if cw <= 0 or ch <= 0:
        return 0.0

    area1 = w1 * h1
    area2 = w2 * h2
    carea = cw * ch
    uarea = area1 + area2 - carea
    return carea / uarea


def nms(boxes, nms_thresh=0.4, thresh=0.01):
    boxes = boxes[boxes[:, 4] > thresh]
    sort_ids = np.argsort(boxes[:, 4])[::-1]
    out_boxes = []
    for i in range(len(boxes)):
        box_i = boxes[sort_ids[i]]
        if box_i[4] > 0:
            out_boxes.append(box_i)
            for j in range(i + 1, len(boxes)):
                box_j = boxes[sort_ids[j]]
                if bbox_iou(box_i, box_j, x1y1x2y2=False) > nms_thresh:
                    box_j[4] = 0
    return out_boxes


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


class Resize(object):
    def __init__(self, dsize: (), keep_aspect=True, mean: np.ndarray = None,
                 scale: np.ndarray = None, color_mode: int = None):

        assert len(dsize) == 2 and isinstance(dsize[0], int) and isinstance(dsize[1], int)
        self.dsize = (int(i) for i in dsize[:2])
        self.dst_w, self.dst_h = self.dsize
        self.keep = keep_aspect

        self.mean = None if mean is None else np.tile(mean, (self.dst_h, self.dst_w, 1)).astype(np.float32)
        self.scale = None if scale is None else np.tile(scale, (self.dst_h, self.dst_w, 1)).astype(np.float32)
        self.color_mode = color_mode

    def process(self, image):
        if self.color_mode is not None:
            image = cv2.cvtColor(image, self.color_mode)
        img_h, img_w, _ = image.shape
        image_, scale, pad = self._resize(image, self.dst_w, self.dst_h, keep=self.keep)
        if self.mean is not None:
            image_ = image_ - self.mean
        if self.scale is not None:
            image_ = image_ * self.scale
        image_ = np.transpose(image_, (2, 0, 1))
        image_ = np.expand_dims(image_, 0).astype(np.float32)
        return {"image": image_, "src_h": img_h, "src_w": img_w, "scale": scale, "pad": pad}

    __call__ = process

    @staticmethod
    def _resize(image, dst_w, dst_h, keep=True):
        img_h, img_w, _ = image.shape
        if not keep:
            output = cv2.resize(image, (dst_w, dst_h))
            scale_x = float(dst_w) / img_w
            scale_y = float(dst_h) / img_h
            return output, (scale_x, scale_y), (0., 0.)
        if abs(float(img_h) / img_w - float(dst_h) / dst_w) < 1e-3:
            output = cv2.resize(image, (dst_w, dst_h))
            scale = float(dst_h) / img_h
            return output, (scale, scale), (0., 0.)
        output = np.zeros((dst_h, dst_w, 3), dtype=np.uint8)
        scale = float(dst_w) / img_w
        if int(scale * img_h) > dst_h:
            scale = float(dst_h) / img_h
        rz_w = int(scale * img_w)
        rz_h = int(scale * img_h)
        image = cv2.resize(image, (rz_w, rz_h))
        pad_x = int(max(0, (dst_w - rz_w) / 2))
        pad_y = int(max(0, (dst_h - rz_h) / 2))
        output[pad_y:(pad_y + rz_h), pad_x:(pad_x + rz_w), :] = image
        return output, (scale, scale), (pad_x, pad_y)

    @staticmethod
    def bbs_transback(bboxes, meta):
        bboxes[:, [0, 2]] = (bboxes[:, [0, 2]] - meta["pad"][0]) / meta["scale"][0] / meta["src_w"]
        bboxes[:, [1, 3]] = (bboxes[:, [1, 3]] - meta["pad"][1]) / meta["scale"][1] / meta["src_h"]
        return bboxes

    @staticmethod
    def pts_transback(pts, meta):
        pts[:, 0] = (pts[:, 0] - meta["pad"][0]) / meta["scale"][0] / meta["src_w"]
        pts[:, 1] = (pts[:, 1] - meta["pad"][1]) / meta["scale"][1] / meta["src_h"]
        return pts
