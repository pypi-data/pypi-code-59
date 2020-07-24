# -*- coding: UTF-8 -*-
from copy import deepcopy

import cv2
import numpy as np
from math import ceil
from itertools import product as product
from ..utils import get_affine_transform, transform_preds, Resize, sigmoid
from ..core import TRTInference
from ..external.nms import soft_nms
from ..utils import Bbox

__all__ = ["CenterNet", "YOLO", "YOLOV3DetectOut", "FaceOrganDetector", "YuFace"]


def top_k_2d(dim2array, k=100):
    """
    对二维数组flatten,再取top K.这里使用了np.argpartition方法，比直接使用np.argsort复杂度低/快
    :param dim2array: ndarray,dim=2
    :param k: int
    :return:
    """
    dim2array = dim2array.flatten()
    # 取前topK,topK未排序
    chaotic_top_k_inds = np.argpartition(dim2array, -k)[-k:]
    # 对前topK进行排序
    inds_ = np.argsort(dim2array[chaotic_top_k_inds])[::-1]
    topk_inds = chaotic_top_k_inds[inds_]
    topk_scores = dim2array[topk_inds]
    return topk_inds.reshape(1, -1), topk_scores.reshape(1, -1)


def top_k(m, k=100):
    """
    对每类取topK
    :param m: np.ndarray
        每一类为一个feature map
        shape= batch * class_num * out_height * out_width
    :param k: int
        取前top K
    :return: tuple
        inds,前topK的索引值,shape=batch * class_num * 100
        scores,前topK的分,shape=batch * class_num * 100
    """
    n, c, h, w = m.shape
    inds = []
    scores = []
    for n_ in range(n):
        for c_ in range(c):
            inds_, scores_ = top_k_2d(m[n_][c_], k)
            inds.append(inds_)
            scores.append(scores_)
    inds = np.vstack(inds)
    scores = np.vstack(scores)
    return np.expand_dims(inds, axis=0), np.expand_dims(scores, axis=0)


class CenterNet(TRTInference):
    model_name = "CenterNet"

    def __init__(self, *args, **kwargs):
        super(CenterNet, self).__init__(*args, **kwargs)
        self.input_res = (384, 384)
        self.input_w, self.input_h = self.input_res
        self.mean = np.tile([[[0.40789655, 0.44719303, 0.47026116]]], (self.input_h, self.input_w, 1))
        self.std = np.tile([[[0.2886383, 0.27408165, 0.27809834]]], (self.input_h, self.input_w, 1))
        self.num_classes = 2
        self.class_names = ('__background__', 'head', 'body')
        self.color = {"head": [0, 0, 255], "body": [255, 255, 0]}
        self.thresh = (1., 0.40, 0.37)
        self.out_height = 96
        self.out_width = 96
        self.K = 100
        self.output_shapes = [(1, 2, 96, 96), (1, 2, 96, 96), (1, 2, 96, 96), (1, 2, 96, 96)]

    def _pre_process(self, image):
        height, width = image.shape[0:2]
        inp_height, inp_width = self.input_h, self.input_w
        c = np.array([width / 2., height / 2.], dtype=np.float32)
        s = max(height, width) * 1.0
        trans_input = get_affine_transform(c, s, 0, [inp_width, inp_height])
        # resized_image = cv2.resize(image, (width, height))
        inp_image = cv2.warpAffine(
            image, trans_input, (inp_width, inp_height),
            flags=cv2.INTER_LINEAR)
        inp_image = ((inp_image / 255. - self.mean) / self.std).astype(np.float32)
        pre_image = inp_image.transpose([2, 0, 1])
        meta = {'s': s, 'c': c, 'out_height': self.out_height, 'out_width': self.out_width,
                "img_width": width, "img_height": height, "image": pre_image}
        return meta

    def _post_process(self, outputs: list(), meta: dict = None):
        wh, reg, hm_sigmoid, hm_maxpool = outputs
        keep = (hm_sigmoid == hm_maxpool)
        hm = hm_sigmoid * keep
        dets = self._decode(hm, reg, wh, self.K)
        dets = dets.reshape(1, -1, dets.shape[2])
        dets = self.ctdet_post_process(dets.copy(), [meta['c']], [meta['s']],
                                       meta["out_height"], meta["out_width"], self.num_classes)[0]
        detections = list()
        img_w, img_h = meta["img_width"], meta["img_height"]
        for j in range(1, self.num_classes + 1):
            dets[j] = np.array(dets[j], dtype=np.float32).reshape(-1, 5)
            mask = dets[j][..., 4] > 0.01
            dets[j] = dets[j][mask]
            keeps = soft_nms(dets[j], method=2)
            dets[j] = dets[j][keeps]
            ws = dets[j][:, 2] - dets[j][:, 0]
            hs = dets[j][:, 3] - dets[j][:, 1]
            ss = dets[j][:, -1]
            mask1 = (ws > 12) & (hs > 12)
            mask2 = np.logical_not((ws < 24) & (hs / ws > 5))
            mask3 = ss > self.thresh[j]
            keeps = (mask1 & mask2 & mask3)
            cur_class_dets = dets[j][keeps]
            for det in cur_class_dets:
                det[[0, 2]] = det[[0, 2]] / meta["img_width"]
                det[[1, 3]] = det[[1, 3]] / meta["img_height"]
                detections.append(Bbox(self.class_names[j], det))
        return detections

    @staticmethod
    def topK(hm, K):
        topk_inds, topk_scores = top_k(hm, K)
        n, c, height, width = hm.shape
        topk_inds = topk_inds % (width * height)
        topk_ys = (topk_inds / width).astype(np.int).astype(np.float)
        topk_xs = (topk_inds % width).astype(np.int).astype(np.float)
        topk_ind, topk_score = top_k_2d(topk_scores.reshape(n, -1), K)
        topk_clses = (topk_ind / K).astype(np.int)

        topk_inds = topk_inds.flatten()[topk_ind].reshape(n, K)
        topk_ys = topk_ys.flatten()[topk_ind].reshape(n, K)
        topk_xs = topk_xs.flatten()[topk_ind].reshape(n, K)
        return topk_score, topk_inds, topk_clses, topk_ys, topk_xs

    def _decode(self, hm, reg, wh, K):
        """
        :param hm: np.ndarray
            前景中心点及分值,shape=batch * class_num * out_height * out_widht
        :param reg: np.ndarray
            中心点offset,shape=batch * class_num * out_height * out_width
        :param wh: np.ndarray
            前景物体的宽高,shape=batch * class_num * out_height * out_width
        :param K: int
            topK
        :return:
        """
        n, c, height, width = reg.shape
        scores, inds, clses, ys, xs = self.topK(hm, K=K)

        reg = np.transpose(reg, [0, 2, 3, 1]).reshape((n, height * width, c))
        reg = reg[:, inds, :].reshape((n, K, 2))
        xs = xs.reshape(n, K, 1) + reg[:, :, 0:1]
        ys = ys.reshape(n, K, 1) + reg[:, :, 1:2]

        wh = np.transpose(wh, [0, 2, 3, 1]).reshape((n, height * width, c))
        wh = wh[:, inds, :].reshape((n, K, 2))

        clses = clses.reshape(n, K, 1).astype(np.float)
        scores = scores.reshape(n, K, 1)
        bboxes = np.concatenate([xs - wh[..., 0:1] / 2,
                                 ys - wh[..., 1:2] / 2,
                                 xs + wh[..., 0:1] / 2,
                                 ys + wh[..., 1:2] / 2], axis=2)
        detections = np.concatenate([bboxes, scores, clses], axis=2)
        return detections

    @staticmethod
    def ctdet_post_process(dets, c, s, h, w, num_classes):
        # dets: batch x max_dets x dim
        # return 1-based class det dict
        ret = []
        for i in range(dets.shape[0]):
            top_preds = {}
            dets[i, :, :2] = transform_preds(
                dets[i, :, 0:2], c[i], s[i], (w, h))
            dets[i, :, 2:4] = transform_preds(
                dets[i, :, 2:4], c[i], s[i], (w, h))
            classes = dets[i, :, -1]
            for j in range(num_classes):
                inds = (classes == j)
                top_preds[j + 1] = np.concatenate([
                    dets[i, inds, :4].astype(np.float32),
                    dets[i, inds, 4:5].astype(np.float32)], axis=1).tolist()
            ret.append(top_preds)
        return ret

    def draw_img(self, image, res):
        img = image.copy()
        height, width, c = img.shape
        for item in res:
            tl, br = item.tl, item.br
            x1 = np.clip(int(tl[0] * width), 0, width)
            y1 = np.clip(int(tl[1] * height), 0, height)
            x2 = np.clip(int(br[0] * width), 0, width)
            y2 = np.clip(int(br[1] * height), 0, height)
            cv2.rectangle(img, (x1, y1), (x2, y2), self.color[item.name], 1)
            cv2.putText(img, item.name, (x1, y1 + 15), cv2.FONT_HERSHEY_COMPLEX, 0.5, self.color[item.name])
            cv2.putText(img, "{:.2f}".format(item.score), (x1, y1 + 30), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                        self.color[item.name])
        return img


class YOLOV3DetectOut(object):
    def __init__(self, nc=80, stride=(), anchors=(), thresh=0.01, nms_thresh=0.40):  # detection layer
        assert len(stride) > 0 and len(stride) == len(anchors), \
            "Unvalid Stride:{} or anchors:{}!".format(stride, anchors)
        self.stride = stride  # strides
        self.nc = nc  # number of classes
        self.no = nc + 5  # number of outputs per anchor
        self.nl = len(anchors)  # number of detection layers
        self.na = len(anchors[0]) // 2  # number of anchors
        self.grid = [np.zeros(1)] * self.nl  # init grid
        a = np.array(anchors, np.float32).reshape((self.nl, -1, 2))
        self.anchors = a  # shape(nl,na,2)
        self.anchor_grid = a.reshape((self.nl, 1, -1, 1, 1, 2))  # shape(nl,1,na,1,1,2)
        self.thresh = thresh
        self.nms_thresh = nms_thresh

    def forward(self, x):
        z = []  # inference output
        for i in range(self.nl):
            bs, _, ny, nx = x[i].shape  # x(bs,255,20,20) to x(bs,3,20,20,85)
            x[i] = x[i].reshape((bs, self.na, self.no, ny, nx)).transpose((0, 1, 3, 4, 2))

            if self.grid[i].shape[2:4] != x[i].shape[2:4]:
                self.grid[i] = self._make_grid(nx, ny)
            y = np.empty_like(x[i])
            xy = (sigmoid(x[i][..., 0:2]) + self.grid[i]) * self.stride[i]
            wh = np.exp(x[i][..., 2:4]) * self.anchor_grid[i]
            y[..., 0:2] = xy - wh / 2
            y[..., 2:4] = xy + wh / 2
            y[..., 4:] = sigmoid(x[i][..., 4:])
            z.append(y.reshape((bs, -1, self.no)))

        z = np.concatenate(z, axis=1)
        return self._extract_bboxes(z)

    def _extract_bboxes(self, output):
        # do nms for each image
        batch_size = output.shape[0]
        detections = []
        for b in range(batch_size):
            mask = output[b][..., 4] > self.thresh
            detouts = output[b][mask]
            positions = detouts[..., :4]
            classes = np.argmax(detouts[..., 5:], axis=1)
            scores = detouts[..., 4] * detouts[np.arange(detouts.shape[0]), 5 + classes]
            bboxes = np.concatenate([positions, scores[..., np.newaxis]], axis=1)
            image_dets = list()
            for c in range(self.nc):
                c_indies = classes == c
                c_bboxes = bboxes[c_indies]
                keeps = soft_nms(c_bboxes, Nt=self.nms_thresh, threshold=self.thresh)
                c_bboxes = c_bboxes[keeps]
                image_dets.append(np.concatenate([c_bboxes, np.full((len(keeps), 1), c)], axis=1))
            detections.append(np.concatenate(image_dets, axis=0))
        return np.stack(detections)

    __call__ = forward

    @staticmethod
    def _make_grid(nx=20, ny=20):
        xv, yv = np.meshgrid(np.arange(nx), np.arange(ny))
        return np.stack((xv, yv)).transpose((1, 2, 0)).reshape((1, 1, ny, nx, 2)).astype(np.float32)


class YOLO(TRTInference):
    model_name = "yolo"

    def __init__(self, *args, **kwargs):
        super(YOLO, self).__init__(*args, **kwargs)
        self.input_res = (352, 352)
        self.input_w, self.input_h = self.input_res
        self.mean = np.array([0., 0., 0.])
        self.scale = np.array([0.003921, 0.003921, 0.003921])
        self.num_classes = 2
        self.class_names = ('head', 'body')
        self.color = {"head": [0, 0, 255], "body": [255, 255, 0]}
        self.output_shapes = [(1, 21, 11, 11), (1, 21, 22, 22)]
        self.thresh = (0.50, 0.40)
        self.stride = (32, 16)
        self.anchors = [(64, 238, 96, 148, 140, 269), (20, 35, 36, 65, 52, 121)]
        self.detect = YOLOV3DetectOut(
            nc=self.num_classes,
            stride=self.stride,
            anchors=self.anchors,
        )
        self.transform = Resize(self.input_res, False, self.mean, self.scale, cv2.COLOR_BGR2RGB)

    def _post_process(self, outputs: list, meta: dict = None):
        detections = self.detect(outputs)[0]
        detections = self.transform.bbs_transback(detections, meta)
        detection_outs = list()
        for i in range(detections.shape[0]):
            d = detections[i]
            xyxys, label = d[:5], int(d[5])
            score = xyxys[-1]
            if score > self.thresh[label]:
                detection_outs.append(Bbox(self.class_names[label], xyxys))
        return detection_outs

    def draw_img(self, image, res):
        img = image.copy()
        height, width, c = img.shape
        for item in res:
            tl, br = item.tl, item.br
            x1 = np.clip(int(tl[0] * width), 0, width)
            y1 = np.clip(int(tl[1] * height), 0, height)
            x2 = np.clip(int(br[0] * width), 0, width)
            y2 = np.clip(int(br[1] * height), 0, height)
            cv2.rectangle(img, (x1, y1), (x2, y2), self.color[item.name], 1)
            cv2.putText(img, item.name, (x1, y1 + 15), cv2.FONT_HERSHEY_COMPLEX, 0.5, self.color[item.name])
            cv2.putText(img, "{:.2f}".format(item.score), (x1, y1 + 30), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                        self.color[item.name])
        return img


class FaceOrganDetector(TRTInference):
    model_name = "FaceOrgan"

    def __init__(self, *args, **kwargs):
        super(FaceOrganDetector, self).__init__(*args, **kwargs)
        self.input_res = (160, 160)
        self.input_w, self.input_h = self.input_res
        self.scale = np.array([0.017, 0.017, 0.017])
        self.mean = np.array([103.94, 116.78, 123.68])
        self.num_classes = 3
        self.class_names = ('__background__', 'eye', 'nose', 'mouth', 'expanded_eye',
                            'expanded_mouth', 'discard_eye', 'discard_nose', 'discard_mouth')
        self.color = {"eye": [0, 0, 255], "nose": [255, 255, 0], 'mouth': [255, 0, 0]}
        self.output_shapes = [(1, 24, 10, 10), (1, 24, 20, 20)]
        self.thresh = (1.0, 0.2, 0.2, 0.2)
        self.stride = (16, 8)
        self.anchors = [(25, 13, 25, 24, 16, 20), (17, 8, 10, 6, 8, 15)]
        self.detect = YOLOV3DetectOut(
            nc=self.num_classes,
            stride=self.stride,
            anchors=self.anchors,
            nms_thresh=0.3,
        )
        self.transform = Resize(self.input_res, False, self.mean, self.scale)

        self.classes_label_map = {name: ix for ix, name in enumerate(self.class_names)}
        self.obj_template = {"organs": [], "valid": True, "yaw": 'unknown', "proposal_score": 0}

    # def _post_process(self, outputs: list, meta: dict = None):
    #     detections = self.detect(outputs)[0]
    #     detections = self.transform.bbs_transback(detections, meta)
    #     detection_outs = list()
    #     for i in range(detections.shape[0]):
    #         d = detections[i]
    #         xyxys, label = d[:5], int(d[5]) + 1
    #         score = xyxys[-1]
    #         if score > self.thresh[label]:
    #             detection_outs.append(Bbox(self.class_names[label], xyxys))
    #     return detection_outs

    @staticmethod
    def cal_cos_dis(vector1, vector2):
        cos_dis = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
        if cos_dis == cos_dis:
            angle = int(np.arccos(cos_dis) / np.pi * 180)
        else:
            angle = None
        return cos_dis, angle

    def check_detect_out(self, detect_out, center):
        cand_nose_idxs = np.where((detect_out[:, 1] == 2) & (detect_out[:, 2] >= self.thresh[2]))[0]
        # 没有鼻子,不处理
        if cand_nose_idxs.shape[0] == 0:
            cand_eye_idxs = np.where((detect_out[:, 1] == 1) & (detect_out[:, 2] >= self.thresh[1]))[0]
            cand_mouth_idxs = np.where((detect_out[:, 1] == 3) & (detect_out[:, 2] >= self.thresh[3]))[0]
            if cand_eye_idxs.shape[0] > 0:
                detect_out[cand_eye_idxs[2:], 1] = self.classes_label_map['discard_eye']
            if cand_mouth_idxs.shape[0] > 0:
                detect_out[cand_mouth_idxs[1:], 1] = self.classes_label_map['discard_mouth']
            return 'unknown'
        # nose exists, try predict head angle
        distance_from_nose_factor = 1.3
        nose = detect_out[cand_nose_idxs[0]]
        nose_center = center[cand_nose_idxs[0]]
        nose_diag_len = np.sqrt(np.square(nose[5] - nose[3]) + np.square(nose[6] - nose[4]))

        # filter out some item far away nose.
        for ix in range(detect_out.shape[0]):
            if ix == cand_nose_idxs[0]:
                continue
            item_center = center[ix]
            distance_from_nose = np.linalg.norm(nose_center - item_center)
            src_label = detect_out[ix, 1]
            if distance_from_nose > distance_from_nose_factor * nose_diag_len:
                if src_label == 1:
                    detect_out[ix, 1] = self.classes_label_map['discard_eye']
                elif src_label == 2:
                    detect_out[ix, 1] = self.classes_label_map['discard_nose']
                else:
                    detect_out[ix, 1] = self.classes_label_map['discard_mouth']

        # 重新检索五官
        cand_nose_idxs = np.where(detect_out[:, 1] == 2)[0]
        cand_eye_idxs = np.where(detect_out[:, 1] == 1)[0]
        cand_mouth_idxs = np.where(detect_out[:, 1] == 3)[0]
        valid_cand_nose_idxs = list(cand_nose_idxs[1:])

        # nose-top1 肯定>thresh,排除多余nose
        if cand_nose_idxs.shape[0] > 1:
            detect_out[cand_nose_idxs[1:], 1] = self.classes_label_map['discard_nose']

        head_roll = 'unknown'
        base_line = np.array([1, 0], np.float32)
        vector = np.array([0, 0], np.float32)
        roll = None

        valid_mouth_idx = -1
        valid_eye_idxs = list()
        valid_cand_mouth_idxs = list()
        valid_cand_eye_idxs = list()
        if cand_mouth_idxs.shape[0] > 0:
            # 嘴巴存在
            for i in range(cand_mouth_idxs.shape[0]):
                mouth_idx = cand_mouth_idxs[i]
                mouth_conf = detect_out[mouth_idx, 2]
                if valid_mouth_idx == -1 and mouth_conf >= self.thresh[3]:
                    # 符合条件,刚好还未找到合适的嘴巴
                    valid_mouth_idx = mouth_idx
                    continue
                # 符合条件,但是已找到合适的嘴巴/不符合条件,抛弃
                valid_cand_mouth_idxs.append(mouth_idx)
                detect_out[mouth_idx, 1] = self.classes_label_map['discard_mouth']

            mouth_center = center[valid_mouth_idx]
            vector1 = nose_center - mouth_center
            vector = vector + vector1
            cos_dis, roll = self.cal_cos_dis(base_line, vector)

        if cand_eye_idxs.shape[0] >= 2:
            # 至少有两只备选眼睛
            for i in range(cand_eye_idxs.shape[0]):
                eye_idx = cand_eye_idxs[i]
                eye_conf = detect_out[eye_idx, 2]
                if len(valid_eye_idxs) < 2 and eye_conf >= self.thresh[1]:
                    # 符合条件,刚好还未找全合适的眼睛
                    valid_eye_idxs.append(eye_idx)
                    continue

                # 符合条件,已找全合适的眼睛/不符合条件,抛弃
                valid_cand_eye_idxs.append(eye_idx)
                detect_out[eye_idx, 1] = self.classes_label_map['discard_eye']

            if cand_mouth_idxs.shape[0] == 0 and len(valid_eye_idxs) == 2:
                # 嘴巴不存在时,使用眼睛预测头的状态
                eye1_center = center[valid_eye_idxs[0]]
                eye2_center = center[valid_eye_idxs[1]]
                eye_center = (eye1_center + eye2_center) / 2
                vector2 = eye_center - nose_center
                vector = vector + vector2
                cos_dis, roll = self.cal_cos_dis(base_line, vector)
        if roll is not None:
            if roll < 45:
                head_roll = 'rightSideLying'
            elif roll > 135:
                head_roll = 'leftSideLying'
            else:
                head_roll = 'normal'
        if head_roll == 'unknown':
            return 'unknown'

        # 下面尝试提高召回
        if valid_mouth_idx == -1:
            # 缺少嘴巴, 已经有两只眼睛.(没有嘴巴，只有一只眼睛上面直接返回了,head_status='unknown')
            cand_idxs_pool = valid_cand_nose_idxs + valid_cand_eye_idxs
            expand_mouth_idxs = list()
            for idx in cand_idxs_pool:
                item = detect_out[idx]
                if head_roll == 'normal':
                    check_mouth_code = item[3] - nose[5] < 0.1 and nose[3] - item[5] < 0.1 \
                                       and item[6] > nose[6] and item[4] > nose[4]
                elif head_roll == 'rightSideLying':
                    check_mouth_code = item[3] < nose[3] and item[5] < nose[5] \
                                       and item[4] - nose[6] < 0.1 and nose[4] - item[6] < 0.1
                else:
                    # rightSideLying
                    check_mouth_code = item[3] > nose[3] and item[5] > nose[5] \
                                       and item[4] - nose[6] < 0.1 and nose[4] - item[6] < 0.1
                if check_mouth_code:
                    expand_mouth_idxs.append(idx)
            if len(expand_mouth_idxs) > 0:
                expand_mouth_idx = expand_mouth_idxs[int(np.argmax(detect_out[expand_mouth_idxs, 2]))]
                detect_out[expand_mouth_idx, 1] = self.classes_label_map['expanded_mouth']

        # 有嘴巴,缺少1只或者2只眼睛
        if len(valid_eye_idxs) < 2:
            cand_idxs_pool = valid_cand_nose_idxs + valid_cand_eye_idxs
            select_out_eye_pool = list()
            for idx in cand_idxs_pool:
                # 先选出备用item
                item = detect_out[idx]
                if head_roll == 'normal':
                    check_eye_code = item[4] < nose[4] and item[6] < nose[6]
                elif head_roll == 'rightSideLying':
                    check_eye_code = item[3] > nose[3] and item[5] > nose[5]
                else:
                    # head_status == 'leftSideLying':
                    check_eye_code = item[3] < nose[3] and item[5] < nose[5]
                if check_eye_code:
                    select_out_eye_pool.append(idx)

            if len(select_out_eye_pool) > 0:
                if len(valid_eye_idxs) == 1:
                    # 已经有一只眼睛
                    cur_eye_idx = valid_eye_idxs[0]
                else:
                    # 没有眼睛
                    cur_eye_idx = select_out_eye_pool[int(np.argmax(detect_out[select_out_eye_pool, 2]))]
                    detect_out[cur_eye_idx, 1] = self.classes_label_map['expanded_eye']
                # 下面找另一只眼睛
                cur_eye_center = center[cur_eye_idx]
                expand_eye_idxs = list()
                for idx in cand_idxs_pool:
                    if idx == cur_eye_idx:
                        continue
                    item_center = center[idx]
                    if head_roll == 'normal' and cur_eye_center[0] < nose_center[0]:
                        # 有左眼,找右眼
                        check_eye_code = item_center[0] > nose_center[0]
                    elif head_roll == 'normal' and cur_eye_center[0] > nose_center[0]:
                        # 有右眼,找左眼
                        check_eye_code = item_center[0] < nose_center[0]
                    elif head_roll == 'rightSideLying' and cur_eye_center[1] < nose_center[1]:
                        # 有左眼,找右眼
                        check_eye_code = item_center[1] > nose_center[1]
                    elif head_roll == 'rightSideLying' and cur_eye_center[1] > nose_center[1]:
                        # 有右眼,找左眼
                        check_eye_code = item_center[1] < nose_center[1]
                    elif head_roll == 'leftSideLying' and cur_eye_center[1] > nose_center[1]:
                        # 有左眼,找右眼
                        check_eye_code = item_center[1] < nose_center[1]
                    else:
                        # head_status == 'leftSideLying' and cur_eye_center[1] < nose_center[1]
                        # 有右眼,找左眼
                        check_eye_code = item_center[1] > nose_center[1]
                    if check_eye_code:
                        expand_eye_idxs.append(idx)
                if len(expand_eye_idxs) > 0:
                    expand_eye_idx = expand_eye_idxs[int(np.argmax(detect_out[expand_eye_idxs, 2]))]
                    detect_out[expand_eye_idx, 1] = self.classes_label_map['expanded_eye']

        return head_roll

    def analize_head_yaw(self, detect_out, center, head_roll):
        eye_idxs = np.where(detect_out[:, 1] == 1)[0]
        nose_idxs = np.where(detect_out[:, 1] == 2)[0]
        mouth_idxs = np.where(detect_out[:, 1] == 3)[0]
        expanded_mouth_idxs = np.where(detect_out[:, 1] == self.classes_label_map['expanded_mouth'])[0]
        expanded_eye_idxs = np.where(detect_out[:, 1] == self.classes_label_map['expanded_eye'])[0]
        mouth_idxs = np.concatenate([mouth_idxs, expanded_mouth_idxs])
        eye_idxs = np.concatenate([eye_idxs, expanded_eye_idxs])

        # 没有鼻子，或者没有眼睛
        if nose_idxs.shape[0] == 0:
            return False, 'no nose', 0
        if eye_idxs.shape[0] == 0:
            return False, 'no eyes', 0
        nose_center = center[nose_idxs[0]]
        nose = detect_out[nose_idxs[0]]

        # 有鼻子，有两眼，正面至90度之间
        if eye_idxs.shape[0] == 2:
            if mouth_idxs.shape[0] == 1:
                mouth = detect_out[mouth_idxs[0]]
                right_eye_idx_ = np.argmax(detect_out[eye_idxs, 3])
                if right_eye_idx_ == 0:
                    right_eye_idx = eye_idxs[0]
                    left_eye_idx = eye_idxs[1]
                else:
                    right_eye_idx = eye_idxs[1]
                    left_eye_idx = eye_idxs[0]
                left_eye = detect_out[left_eye_idx]
                right_eye = detect_out[right_eye_idx]
                left_eye_width = left_eye[5] - left_eye[3]
                right_eye_width = right_eye[5] - right_eye[3]
                ratio = left_eye_width / right_eye_width
                #
                left_eye_c = center[left_eye_idx]
                right_eye_c = center[right_eye_idx]
                if head_roll == 'normal':
                    m1 = left_eye_c[0] + right_eye_c[0] - 1
                    m2 = ratio - 1
                    m3 = nose_center[0] + center[mouth_idxs[0]][0] - 1
                else:
                    m1 = left_eye_c[1] + right_eye_c[1] - 1
                    m2 = ratio - 1
                    m3 = nose_center[1] + center[mouth_idxs[0]][1] - 1
                m = m1 / 2 + m2 / 3 + m3 / 5  # 五官离图像中心程度
                m_ = 1 - min(abs(m), 1)  # 反转换
                mean_score = 3 / 20 * mouth[2] + 1 / 4 * nose[2] + 3 / 10 * left_eye[2] + 3 / 10 * right_eye[
                    2]  # 五官scores
                proposal_score = 2 / 3 * mean_score + 1 / 3 * m_  # 合并
                #
                if -0.25 <= m <= 0.25:
                    return True, 'front', proposal_score
                elif m < -0.25:
                    return True, 'left', proposal_score
                else:
                    return True, 'right', proposal_score
            else:
                return False, 'onlyNoMouth', 0

        # 90度左右, 有鼻子/一只眼睛/嘴巴
        base_line = np.array([1, 0], np.float32)
        if mouth_idxs.shape[0] == 1 and eye_idxs.shape[0] == 1:
            eye_center = center[eye_idxs[0]]
            mouth_center = center[mouth_idxs[0]]
            vector1 = eye_center - nose_center
            vector2 = mouth_center - nose_center
            vector = vector1 + vector2
            cos_dis, cos_theta = self.cal_cos_dis(vector, base_line)
            if cos_theta <= 90 and nose_center[0] < 0.25:
                # 90right
                return False, '90left', 0
            elif cos_theta > 90 and nose_center[0] > 0.75:
                # 90left
                return False, '90right', 0
            else:
                return False, 'unknown', 0
        # 余下为一只鼻子,一只眼睛
        return False, 'unknown', 0

    def _post_process(self, outputs: list, meta: dict = None):
        detections = self.detect(outputs)[0]
        detections = detections[np.argsort(detections[:, 4])[::-1]]
        detections = self.transform.bbs_transback(detections, meta)
        detect_out = np.ones((detections.shape[0], 7), dtype=np.float32)
        detect_out[:, 3:7] = detections[:, 0: 4]
        detect_out[:, 1] = detections[:, -1] + 1
        detect_out[:, 2] = detections[:, 4]

        center_x = (detect_out[:, 5] + detect_out[:, 3]) / 2
        center_y = (detect_out[:, 6] + detect_out[:, 4]) / 2
        center = np.hstack([center_x.reshape(-1, 1), center_y.reshape((-1, 1))])
        head_roll = self.check_detect_out(detect_out, center)
        head_yaw = self.analize_head_yaw(detect_out, center, head_roll)
        face_obj = deepcopy(self.obj_template)
        face_obj.update(valid=head_yaw[0])
        face_obj.update(yaw=head_yaw[1])
        face_obj.update(proposal_score=head_yaw[2])
        organs = list()
        for i in range(detect_out.shape[0]):
            label_ix = int(detect_out[i, 1])
            if label_ix == 0 or label_ix > 5:
                continue
            if label_ix == 4:  # expanded_eye
                label_ix = 1
            elif label_ix == 5:  # expanded_mouth
                label_ix = 3
            cls_name = self.class_names[label_ix]
            score = detect_out[i, 2]
            box = detect_out[i, 3:7]
            organs.append({"cls_name": cls_name, "score": score, "box": box.tolist()})
        face_obj.update(organs=organs)
        return face_obj


class YuFace(TRTInference):
    model_name = "YuFace"

    def __init__(self, *args, **kwargs):
        super(YuFace, self).__init__(*args, **kwargs)
        self._input_width = 960
        self._input_height = 640
        # self._input_width = 640
        # self._input_height = 480
        self.output_shapes = ((-1, 14), (-1, 2))
        self.top_k = 200
        self.keep_top_k = 50
        self.confidence_threshold = 0.5
        self.nms_threshold = 0.3
        self.scale = np.array(
            7 * [self._input_width, self._input_height]).reshape(1, 14)
        self.min_sizes = ((10, 16, 24), (32, 48), (64, 96), (128, 192, 256))
        self.steps = (8, 16, 32, 64)
        self.variances = (0.1, 0.2)
        self.clip = True
        # for ii in range(4):
        #     if(self.steps[ii] != pow(2,(ii+3))):
        #         raise ValueError("steps must be [8,16,32,64]")
        self.priorboxes = self.cal_priorbox()
        self.transform = Resize((self._input_width, self._input_height), True)

    def _post_process(self, outputs: list, meta: dict = None):
        loc, conf = outputs
        scores = conf[:, 1]
        # filter with thresh
        inds = scores > self.confidence_threshold
        loc = loc[inds, :]
        priors = self.priorboxes[inds, :]
        scores = scores[inds]
        # sort by score with descending order
        inds = np.argsort(scores)[::-1][:self.top_k]
        scores = scores[inds]
        loc = loc[inds, :]
        priors = priors[inds, :]
        bboxes = self.decode(loc, priors, self.variances)
        bboxes *= self.scale
        # do NMS
        dets = np.hstack((bboxes, scores[:, np.newaxis])).astype(np.float32, copy=False)
        keep = self.nms(dets[:, [0, 1, 2, 3, 14]], self.nms_threshold)
        dets = dets[keep, :]
        # keep top-K faster NMS
        ### x1,y1,x2,y2,px1,py1,px2,py2,px3,py3,px4,py4,px5,py5,score
        dets = dets[:self.keep_top_k, :]
        dets[:, list(range(0, 14, 2))] = np.clip(0, meta["src_w"],
                                                 (dets[:, list(range(0, 14, 2))] - meta["pad"][0]) / meta["scale"][0])
        dets[:, list(range(1, 14, 2))] = np.clip(0, meta["src_h"],
                                                 (dets[:, list(range(1, 14, 2))] - meta["pad"][1]) / meta["scale"][1])
        bboxes = dets[:, [0, 1, 2, 3, 14]]
        bboxes[:, :4] = np.int32(bboxes[:, :4])
        points = np.int32(dets[:, list(range(4, 14))])
        return bboxes, points

    @staticmethod
    def decode(loc, priors, variances):
        """Decode locations from predictions using priors to undo
        the encoding we did for offset regression at train time.
        Args:
            loc (tensor): location predictions for loc layers,
                Shape: [num_priors,4]
            priors (tensor): Prior boxes in center-offset form.
                Shape: [num_priors,4].
            variances: (list[float]) Variances of priorboxes
        Return:
            decoded bounding box predictions
        """
        pcxy = priors[:, 0:2]
        pwh = variances[0] * priors[:, 2:4]
        bbcxy = pcxy + loc[:, 0:2] * pwh
        bbwh = priors[:, 2:4] * np.exp(loc[:, 2:4] * variances[1])
        ptsxy = np.tile(pcxy, 5) + loc[:, 4:14] * np.tile(pwh, 5)  # 5 points
        boxes = np.hstack([bbcxy, bbwh, ptsxy])
        boxes[:, 0:2] -= boxes[:, 2:4] / 2
        boxes[:, 2:4] += boxes[:, 0:2]
        return boxes

    @staticmethod
    def nms(dets, thresh):
        """Pure Python NMS baseline."""
        x1 = dets[:, 0]
        y1 = dets[:, 1]
        x2 = dets[:, 2]
        y2 = dets[:, 3]
        scores = dets[:, 4]

        areas = (x2 - x1 + 1) * (y2 - y1 + 1)
        order = scores.argsort()[::-1]

        keep = []
        while order.size > 0:
            i = order[0]
            keep.append(i)
            xx1 = np.maximum(x1[i], x1[order[1:]])
            yy1 = np.maximum(y1[i], y1[order[1:]])
            xx2 = np.minimum(x2[i], x2[order[1:]])
            yy2 = np.minimum(y2[i], y2[order[1:]])

            w = np.maximum(0.0, xx2 - xx1 + 1)
            h = np.maximum(0.0, yy2 - yy1 + 1)
            inter = w * h
            ovr = inter / (areas[i] + areas[order[1:]] - inter)

            inds = np.where(ovr <= thresh)[0]
            order = order[inds + 1]

        return keep

    def cal_priorbox(self):
        feature_maps = [[ceil(self._input_height / step), ceil(self._input_width / step)] for step in self.steps]
        anchors = []
        for k, f in enumerate(feature_maps):
            min_sizes = self.min_sizes[k]
            for i, j in product(range(f[0]), range(f[1])):
                for min_size in min_sizes:
                    s_kx = min_size / self._input_width
                    s_ky = min_size / self._input_height
                    cx = (j + 0.5) * self.steps[k] / self._input_width
                    cy = (i + 0.5) * self.steps[k] / self._input_height
                    anchors += [cx, cy, s_kx, s_ky]
        anchors = np.array(anchors).reshape(-1, 4)
        if self.clip:
            anchors = np.clip(0, 1, anchors)
        return anchors
