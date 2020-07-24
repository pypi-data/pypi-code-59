# -*- coding: UTF-8 -*-
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

import threading
import time

import numpy as np
from copy import deepcopy
from threading import Semaphore


class HxlxPerson(object):
    def __init__(self, pic_name):
        self.pic_name = pic_name
        self.gt_id = None
        self.featvec = None
        self.landmark_7 = None
        self.landmark_98 = None
        self.forpos_w = None
        self.forpos_h = None
        self.pred_id = -1
        self.facebox = []
        self.landmarks_box = []
        self.front_level = None
        self.bl_valid = 'true'
        self.bad_reason = 'N'
        self.express = None
        self.body_status = {"box": [], 'top5': None, 'pose': None, "hasbody": 'false', 'landmarks': [], "bodyid": None}
        self.eyes_open_degree = None
        self.face_age = None
        self.face_exp = None
        self.face_organs = {}
        self.body_det_head = []

    def get_gt_id(self):
        if self.gt_id is not None:
            return self.gt_id
        if len(self.facebox) > 0:
            box = self.facebox
        elif len(self.body_status['box']) > 0:
            box = self.body_status['box']
        else:
            raise ValueError("face box and body box don't exists!")
        return '{}__face_x{}y{}'.format(self.pic_name, int(box[0]), int(box[1]))

    def set_gt_id(self):
        self.gt_id = self.get_gt_id()

    def get_props(self):
        if self.gt_id is None:
            self.gt_id = self.get_gt_id()
        person_props = deepcopy(self.__dict__)
        return person_props

    def to_dict(self):
        return self.get_props()

    def update(self, e=None, **f):
        d = e or dict()
        d.update(f)
        for k in d:
            setattr(self, k, d[k])

    def get(self, k, default=None):
        if k not in self.__dict__.keys():
            return default
        return self.__dict__.get(k)

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key] = value


class Bbox(object):
    def __init__(self, name: str, xyxys: np.ndarray):
        self.name = name
        self.xyxys = np.clip(np.array(xyxys), 0., 0.999999)
        self.xyxy = self.xyxys[:4]
        self.score = self.xyxys[-1]
        self.tl = self.xyxy[:2]
        self.br = self.xyxy[2:]

    def xywh(self):
        wh = self.xyxy[[2, 3]] - self.xyxy[[0, 1]]
        return np.array([self.tl[0], self.tl[1], wh[0], wh[1]], np.float32)

    def abs(self, height, width):
        x1 = int(np.clip(self.tl[0] * width, 0, width - 1))
        y1 = int(np.clip(self.tl[1] * height, 0, height - 1))
        x2 = int(np.clip(self.br[0] * width, 0, width - 1))
        y2 = int(np.clip(self.br[1] * height, 0, height - 1))
        return [x1, y1, x2, y2]

    def __repr__(self):
        return "<BBox object, tl: {}, br: {}, name: {} , score: {}>".format(
            tuple(self.tl), tuple(self.br), self.name, self.score)

    __str__ = __repr__


def compute_intersect(body_box, face_box):
    x_a = max(body_box[0], face_box[0])
    y_a = max(body_box[1], face_box[1])
    x_b = min(body_box[2], face_box[2])
    y_b = min(body_box[3], face_box[3])

    wid = x_b - x_a
    hei = y_b - y_a
    if wid <= 0 or hei <= 0:
        return -1
    inter_area = wid * hei
    obj_area = (face_box[2] - face_box[0]) * (face_box[3] - face_box[1])
    if obj_area == 0:
        return -1
    return float(inter_area) / float(obj_area)


def compute_iou_mou(box1, box2):
    x_a = max(box1[0], box2[0])
    y_a = max(box1[1], box2[1])
    x_b = min(box1[2], box2[2])
    y_b = min(box1[3], box2[3])

    wid = x_b - x_a
    hei = y_b - y_a
    if wid <= 0 or hei <= 0:
        return -1, -1
    inter_area = wid * hei
    box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
    box2_area = (box2[2] - box2[0]) * (box2[3] - box2[1])
    # computer iou
    if inter_area == 0 or (box1_area + box2_area - inter_area) == 0:
        iou = -1
    else:
        iou = inter_area / (box1_area + box2_area - inter_area)
    # computer mou
    min_area = min(box1_area, box2_area)
    if min_area == 0:
        mou = -1
    else:
        mou = inter_area / min_area
    return iou, mou


def merge_face_head(has_face_objs, has_head_objs):
    matched_head_ixs = []
    for face_ix, face_obj in enumerate(has_face_objs):
        face_box = face_obj['facebox']
        match_head_ix = -1
        max_iou = -1
        for head_ix, head_obj in enumerate(has_head_objs):
            head_box = head_obj['facebox']
            cur_iou, cur_mou = compute_iou_mou(head_box, face_box)
            if cur_iou > max_iou:
                max_iou = cur_iou
                match_head_ix = head_ix
        if match_head_ix != -1:
            matched_head_ixs.append(match_head_ix)
    unmatched_head_ixs = [ix for ix in range(len(has_head_objs)) if ix not in matched_head_ixs]
    for head_ix in unmatched_head_ixs:
        has_head_objs[head_ix]['bl_valid'] = "false"
        has_head_objs[head_ix]['bad_reason'] = "only_has_head"
        has_face_objs.append(has_head_objs[head_ix])
    return has_face_objs


def merge_persons_props(has_face_objs, has_head_objs, has_body_objs):
    # 合并身体检测的脸
    has_face_objs = merge_face_head(has_face_objs=has_face_objs, has_head_objs=has_head_objs)

    # 开始头身匹配
    matched_body_ix = []
    if len(has_face_objs) > 0 and len(has_body_objs) > 0:
        face_boxes = []
        for ix, obj in enumerate(has_face_objs):
            face_box = obj.get("facebox")
            face_boxes.append(np.array(face_box, np.float32))
        body_boxes = []
        for ix, obj in enumerate(has_body_objs):
            box = obj.body_status.get("box")[:4]
            body_boxes.append(box)
        face_body_intersects = [[] for i in range(len(face_boxes))]
        for face_ix, face_box in enumerate(face_boxes):
            for body_ix, body_box in enumerate(body_boxes):
                face_body_intersects[face_ix].append(compute_intersect(body_box, face_box))

        # 同一张脸匹配上多个身体
        for face_ix, inters in enumerate(face_body_intersects):
            inters = np.array(inters, np.float32)
            if np.any(inters == 1.0):
                face_box = face_boxes[face_ix]
                face_box_center = np.array([(face_box[2] + face_box[0]) / 2, (face_box[3] + face_box[1]) / 2])
                matched_body_ixs_for_cur_face = np.where(inters == 1.0)[0]
                best_body_ix = -1
                min_distance = float('inf')
                for body_ix in matched_body_ixs_for_cur_face:
                    body_box = body_boxes[body_ix]
                    body_landmarks = np.array(has_body_objs[body_ix].body_status.get("landmarks")[:3])
                    body_landmarks = body_landmarks[:, :2] + np.array([body_box[0], body_box[1]])
                    distance = np.sum(np.square(body_landmarks - face_box_center))
                    if distance < min_distance:
                        min_distance = distance
                        best_body_ix = body_ix
                matched_body_ix.append(best_body_ix)
            else:
                best_body_ix = np.argmax(inters)
                if inters[best_body_ix] != -1:
                    matched_body_ix.append(best_body_ix)
                else:
                    matched_body_ix.append(-1)

        #  同一身体匹配上多个脸
        matched_face_ixs_for_body = [[] for i in range(len(body_boxes))]
        for face_ix, body_ix in enumerate(matched_body_ix):
            if body_ix != -1:
                matched_face_ixs_for_body[body_ix].append(face_ix)
        for body_ix, face_ixs in enumerate(matched_face_ixs_for_body):
            if len(face_ixs) > 1:
                # 该身体匹配上了多个脸
                body_box = body_boxes[body_ix]
                body_landmarks = np.array(has_body_objs[body_ix].body_status.get("landmarks")[:3])
                body_landmarks = body_landmarks[:, :2] + np.array([body_box[0], body_box[1]])
                best_face_ix = -1
                min_distance = float('inf')
                for face_ix in face_ixs:
                    face_box = face_boxes[face_ix]
                    face_box_center = np.array([(face_box[2] + face_box[0]) / 2, (face_box[3] + face_box[1]) / 2])
                    distance = np.sum(np.square(body_landmarks - face_box_center))
                    if distance < min_distance:
                        min_distance = distance
                        best_face_ix = face_ix
                for face_ix in face_ixs:
                    if face_ix != best_face_ix:
                        matched_body_ix[face_ix] = -1

        for face_ix, body_ix in enumerate(matched_body_ix):
            if body_ix != -1:
                has_face_objs[face_ix]['body_status'] = has_body_objs[body_ix].body_status

    # 加上未匹配到的身体
    unmatched_body_ixs = [body_ix for body_ix in range(len(has_body_objs)) if body_ix not in matched_body_ix]
    extend_body_objs = []
    for body_ix in unmatched_body_ixs:
        extend_body_objs.append(has_body_objs[body_ix])

    # 最后合并所有结果
    has_face_objs.extend(extend_body_objs)
    persons_props = []
    for obj in has_face_objs:
        # 更新gt_id
        obj.set_gt_id()
        persons_props.append(obj.get_props())
    return persons_props


class AverageMeter(object):
    def __init__(self, name=''):
        self.name = name
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count if self.count != 0 else 0

    def __str__(self):
        return "[%s] sum=%.2f, avg=%.2f, count=%d" % (self.name, self.sum, self.avg, self.count)

    __repr__ = __str__


class FakeLock(object):
    def acquire(self, *args, **kwargs):
        pass

    def release(self):
        pass


class Timer(AverageMeter):
    def __init__(self, name, with_lock=True):
        super(Timer, self).__init__(name)
        self._start = 0
        self._end = 0
        self._lock = FakeLock()
        if with_lock:
            self._lock = Semaphore(1)

    def __enter__(self):
        self.start()

    def __exit__(self, *args):
        self.pause(n=1)
        return False

    def start(self):
        self._lock.acquire()
        self._start = time.time()

    def pause(self, n=1):
        self._end = time.time()
        self.update((self._end - self._start) * 1000, n)
        self._lock.release()

    def update(self, val, n=1):
        self.val = val
        self.sum += val
        self.count += n
        self.avg = self.sum / self.count if self.count != 0 else 0

    def __str__(self):
        desc = "count=%d, sum=%.2f s, avg=%.2f ms" % (self.count, self.sum / 1000, self.avg)
        return "[%15s] | %s" % (self.name.center(15, ' '), desc)

    __repr__ = __str__

    def get_cost(self):
        return {"name": self.name, "count": self.count, "sum": self.sum, "avg": self.avg, "info": str(self)}


class AlgorithmHelper(object):
    def __init__(self, name, with_lock=True):
        self.name = name
        self.pre_stage = Timer("%s-pre" % name, False)
        self.exec_stage = Timer("%s-exec" % name, with_lock)
        self.post_stage = Timer("%s-post" % name, False)

    def __str__(self):
        desc = "count=%d, sum=%.2f s, avg=%.2f ms, pre-avg=%.2f ms, exec-avg=%.2f ms, post-avg=%.2f ms" % \
               (self.count, self.sum / 1000, self.avg, self.pre_stage.avg, self.exec_stage.avg, self.post_stage.avg)
        return "[%15s] | %s" % (self.name.center(15, ' '), desc)

    __repr__ = __str__

    @property
    def avg(self):
        pipeline_avg = self.sum / self.count if self.count != 0 else 0
        return pipeline_avg

    @property
    def count(self):
        return self.exec_stage.count

    @property
    def sum(self):
        return self.pre_stage.sum + self.exec_stage.sum + self.post_stage.sum

    def get_cost(self):
        return {"name": self.name, "count": self.count, "sum": self.sum, "avg": self.avg, "pre-avg": self.pre_stage.avg,
                "exec-avg": self.exec_stage.avg, "post-avg": self.post_stage.avg, "info": str(self)}


def synchronized(func):
    func.__lock__ = threading.Lock()

    def lock_func(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)

    return lock_func


class Singleton(object):
    _instance = None

    @synchronized
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class Const(object):
    def __setattr__(self, name, value):
        if getattr(self, name, None) is None:
            self.__dict__[name] = value
        else:
            raise ConstReassignError(name, value)


class ConstReassignError(Exception):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return "Constant {} reassigns to {} error!".format(self.name, self.value)


def xyxy2xywh(bbox):
    bbox[2] = bbox[2] - bbox[0]
    bbox[3] = bbox[3] - bbox[1]
    return bbox


def xywh2xyxy(bbox):
    bbox[2] = bbox[0] + bbox[2]
    bbox[3] = bbox[1] + bbox[3]
    return bbox
