# -*- coding: UTF-8 -*-
import cv2
import math
import numpy as np
from ..core import TRTInference
from ..utils import get_affine_transform, transform_preds

__all__ = ["SPPE", ]

_CocoColors = [
    [255, 0, 0],  # "nose"
    [255, 0, 255],  # "left_eye"
    [170, 0, 255],  # "right_eye"
    [255, 0, 85],  # "left_ear"
    [255, 0, 170],  # "right_ear"
    [85, 255, 0],  # "left_shoulder"
    [255, 170, 0],  # "right_shoulder"
    [0, 255, 0],  # "left_elbow"
    [255, 255, 0],  # "right_elbow"
    [0, 255, 85],  # "left_wrist"
    [170, 255, 0],  # "right_wrist"
    [0, 85, 255],  # "left_hip"
    [0, 255, 170],  # "right_hip"
    [0, 0, 255],  # "left_knee"
    [0, 255, 255],  # "right_knee"
    [85, 0, 255],  # "left_ankle"
    [0, 170, 255],  # "right_ankle"
    [0, 170, 255],  # "right_ankle"
]

_CocoPairsRender = [
    [16, 14],
    [14, 12],
    [17, 15],
    [15, 13],
    [12, 13],
    [6, 12],
    [7, 13],
    [6, 7],
    [6, 8],
    [7, 9],
    [8, 10],
    [9, 11],
    [2, 3],
    [1, 2],
    [1, 3],
    [2, 4],
    [3, 5],
    [4, 6],
    [5, 7]
]


def get_max_preds(batch_heatmaps):
    '''
    get predictions from score maps
    heatmaps: numpy.ndarray([batch_size, num_joints, height, width])
    '''
    assert isinstance(batch_heatmaps, np.ndarray), \
        'batch_heatmaps should be numpy.ndarray'
    assert batch_heatmaps.ndim == 4, 'batch_images should be 4-ndim'

    batch_size = batch_heatmaps.shape[0]
    num_joints = batch_heatmaps.shape[1]
    width = batch_heatmaps.shape[3]
    heatmaps_reshaped = batch_heatmaps.reshape((batch_size, num_joints, -1))
    idx = np.argmax(heatmaps_reshaped, 2)
    maxvals = np.amax(heatmaps_reshaped, 2)

    maxvals = maxvals.reshape((batch_size, num_joints, 1))
    idx = idx.reshape((batch_size, num_joints, 1))

    preds = np.tile(idx, (1, 1, 2)).astype(np.float32)

    preds[:, :, 0] = (preds[:, :, 0]) % width
    preds[:, :, 1] = np.floor((preds[:, :, 1]) / width)

    pred_mask = np.tile(np.greater(maxvals, 0.0), (1, 1, 2))
    pred_mask = pred_mask.astype(np.float32)

    preds *= pred_mask
    return preds, maxvals


def get_final_preds(batch_heatmaps, center, scale, pix_std):
    coords, maxvals = get_max_preds(batch_heatmaps)

    heatmap_height = batch_heatmaps.shape[2]
    heatmap_width = batch_heatmaps.shape[3]

    # post-processing
    for n in range(coords.shape[0]):
        for p in range(coords.shape[1]):
            hm = batch_heatmaps[n][p]
            px = int(math.floor(coords[n][p][0] + 0.5))
            py = int(math.floor(coords[n][p][1] + 0.5))
            if 1 < px < heatmap_width - 1 and 1 < py < heatmap_height - 1:
                diff = np.array([hm[py][px + 1] - hm[py][px - 1],
                                 hm[py + 1][px] - hm[py - 1][px]])
                coords[n][p] += np.sign(diff) * .25

    preds = coords.copy()

    # Transform back
    for i in range(coords.shape[0]):
        preds[i] = transform_preds(coords[i], center[i], scale[i],
                                   [heatmap_width, heatmap_height], pix_std=pix_std)

    return preds, maxvals


def oks_iou(g, d, a_g, a_d, sigmas=None, in_vis_thre=None):
    if not isinstance(sigmas, np.ndarray):
        sigmas = np.array(
            [.26, .25, .25, .35, .35, .79, .79, .72, .72, .62, .62, 1.07, 1.07, .87, .87, .89, .89, 0.79]) / 10.0
    vars = (sigmas * 2) ** 2
    xg = g[0::3]
    yg = g[1::3]
    vg = g[2::3]
    ious = np.zeros((d.shape[0]))
    for n_d in range(0, d.shape[0]):
        xd = d[n_d, 0::3]
        yd = d[n_d, 1::3]
        vd = d[n_d, 2::3]
        dx = xd - xg
        dy = yd - yg
        e = (dx ** 2 + dy ** 2) / vars / ((a_g + a_d[n_d]) / 2 + np.spacing(1)) / 2
        if in_vis_thre is not None:
            ind = list(vg > in_vis_thre) and list(vd > in_vis_thre)
            e = e[ind]
        ious[n_d] = np.sum(np.exp(-e)) / e.shape[0] if e.shape[0] != 0 else 0.0
    return ious


def oks_nms(kpts_db, thresh, sigmas=None, in_vis_thre=None):
    """
    greedily select boxes with high confidence and overlap with current maximum <= thresh
    rule out overlap >= thresh, overlap = oks
    :param kpts_db
    :param thresh: retain overlap < thresh
    :return: indexes to keep
    """
    if len(kpts_db) == 0:
        return []

    scores = np.array([kpts_db[i]['score'] for i in range(len(kpts_db))])
    kpts = np.array([kpts_db[i]['keypoints'].flatten() for i in range(len(kpts_db))])
    areas = np.array([kpts_db[i]['area'] for i in range(len(kpts_db))])

    order = scores.argsort()[::-1]

    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)

        oks_ovr = oks_iou(kpts[i], kpts[order[1:]], areas[i], areas[order[1:]], sigmas, in_vis_thre)

        inds = np.where(oks_ovr <= thresh)[0]
        order = order[inds + 1]

    return keep


class SPPE(TRTInference):
    """Single person pose estimation.
    """
    model_name = "sppe"

    def __init__(self, *args, **kwargs):
        super(SPPE, self).__init__(*args, **kwargs)
        self.in_vis_thre = 0.2
        self.oks_thre = 0.9
        self.num_joints = 18
        self.input_res = (192, 256)
        self.input_w, self.input_h = self.input_res
        self.mean = np.array([[[104, 117, 124]]])
        self.std = np.array([[[0.017, 0.017, 0.017]]])
        self.aspect_ratio = self.input_res[0] / self.input_res[1]
        self.pixel_std = 200
        self.input_scale = 1.0
        self.output_shapes = [(1, 18, 64, 48), ]

    def _xywh2cs(self, x, y, w, h):
        center = np.zeros((2,), dtype=np.float32)
        center[0] = x + w * 0.5
        center[1] = y + h * 0.5
        # 补短边,使得w/h=3/4
        if w > self.aspect_ratio * h:
            h = w * 1.0 / self.aspect_ratio  # dst_w(192)/dst_h(256)
        elif w < self.aspect_ratio * h:
            w = h * self.aspect_ratio
        # scale = [w/200,h/200]
        scale = np.array(
            [w * 1.0 / self.pixel_std, h * 1.0 / self.pixel_std],
            dtype=np.float32)
        if center[0] != -1:
            scale = scale * self.input_scale
        return center, scale

    def _pre_process(self, image, box):
        x, y, w, h = box[0], box[1], box[2] - box[0] - 1, box[3] - box[1] - 1
        center, scale = self._xywh2cs(x, y, w, h)
        trans = get_affine_transform(center, scale, 0, self.input_res, pix_std=self.pixel_std)
        input_data = cv2.warpAffine(
            image,
            trans,
            (int(self.input_res[0]), int(self.input_res[1])),
            flags=cv2.INTER_LINEAR)
        input_data = (input_data - self.mean) * self.std
        input_data = np.transpose(input_data, (2, 0, 1)).astype(np.float32)
        meta = dict(image=input_data, center=center, scale=scale)
        return meta

    def predict_from_boxes(self, image, boxes=()):
        """
        使用整图和框来推断关键点,boxes格式必须是([x0, y0, x1, y1, score],...),若直接是框图,则boxes不传.
        Usage:
            get_img_kpts(image, img_name="demo", boxes=([12, 13, 56, 78, 0.9]))
        Parameters
            ----------
            image: np.array
                图像np.array对象
            boxes: list of list or tuple of list
                检测框列表或数组, 如boxes=[[x0, y0, x1, y1, score],...]
        """
        img_h, img_w, img_c = image.shape
        if len(boxes) == 0:
            boxes = [(0, 0, img_w, img_h, 1), ]
        img_kpts = []
        for i in range(len(boxes)):
            with self.helper.pre_stage:
                box = boxes[i]
                meta = self._pre_process(image, box)
            with self.helper.exec_stage:
                outputs = self._forward(meta["image"])
            with self.helper.post_stage:
                featvec = [i.reshape(self.output_shapes[index]) for index, i in enumerate(outputs)]
                preds, maxvals = get_final_preds(featvec[0], np.expand_dims(meta["center"], axis=0),
                                                 np.expand_dims(meta["scale"], axis=0), self.pixel_std)
                key_points = np.concatenate([preds, maxvals], axis=2)
                img_kpts.append(
                    {"keypoints": key_points,
                     "score": box[4],
                     "box": box[:4],
                     "area": np.prod(meta["scale"] * self.pixel_std),
                     }
                )
        return img_kpts

    def predict(self, image):
        """
        使用框图来推断关键点
        Usage:
            get_crop_kpts(image)
        Parameters
            ----------
            image: np.array
                图像np.array对象
        """
        img_kpts = self.predict_from_boxes(image)
        img_kpts = img_kpts[0]['keypoints'].squeeze()
        return img_kpts

    __call__ = predict

    def post_process(self, img_kpts):
        for n_p in img_kpts:
            score = n_p.get("score")
            key_points = n_p.get("keypoints")
            kpt_score = 0
            valid_num = 0
            for n_jt in range(self.num_joints):
                t_s = key_points[0][n_jt][2]
                if t_s > self.in_vis_thre:
                    kpt_score = kpt_score + t_s
                    valid_num = valid_num + 1
            if valid_num != 0:
                kpt_score = kpt_score / valid_num
            # rescoring
            n_p['score'] = kpt_score * score
        keep = oks_nms([img_kpts[i] for i in range(len(img_kpts))],
                       self.oks_thre)
        if len(keep) == 0:
            oks_nmsed_kpts = img_kpts
        else:
            oks_nmsed_kpts = [img_kpts[_keep] for _keep in keep]

        return oks_nmsed_kpts

    def draw_img(self, image, res):
        img = image.copy()
        positions, scores = res[:, :2], res[:, 2]
        centers = {}
        h, w, _ = img.shape
        # draw point
        for i, center in enumerate(positions):
            if scores[i] > self.in_vis_thre:
                center = int(center[0]), int(center[1])
                centers[i] = center
                cv2.circle(img, tuple(center), 3, _CocoColors[i], thickness=3, lineType=8, shift=0)
        # draw line
        for pair_order, pair in enumerate(_CocoPairsRender):
            if (pair[0] - 1) in centers and (pair[1] - 1) in centers:
                cv2.line(img, tuple(centers[pair[0] - 1]), tuple(centers[pair[1] - 1]),
                         (np.random.randint(256), np.random.randint(256), np.random.randint(256)), 2)
        return img
