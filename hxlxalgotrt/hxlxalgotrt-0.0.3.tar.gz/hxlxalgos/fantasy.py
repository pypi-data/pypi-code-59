# -*- coding: UTF-8 -*-
import threading
import time
from collections import OrderedDict

import math
import numpy as np
import cv2
from hxlxalgos.algos.face_align import align_face
from hxlxalgos.algos.blur_detect import blur_mult_detect
from hxlxalgos.algos.face_front_level import get_front_level
from hxlxalgos.cfg import PathCfg
from hxlxalgos.utils import merge_persons_props, HxlxPerson, Timer, Singleton
from hxlxalgos.algos import (CenterNet, BodyPoseTop5Cls, BodyPoseCls, SPPE,
                             YuFace, HeadAgeExp, InsightFace, ExpressInferCls,
                             EyeStateInferCls, PFLD, FaceOrganDetector)

__all__ = ["FaceRecg", ]


class BodyAlgolParts(object):
    def __init__(self):
        self.al_body_detector = CenterNet(PathCfg.CenterNet)
        self.al_body_top5 = BodyPoseTop5Cls(PathCfg.BodyTop5)
        self.al_body_pose = BodyPoseCls(PathCfg.BodyPose)
        self.al_body_kpts = SPPE(PathCfg.SPPE)

    def get_persons_prop(self, image, pic_name, *args, **kwargs):
        bboxes = self.al_body_detector(image)
        height, width, channels = image.shape
        has_body_objs = []
        has_head_objs = []
        for bbox in bboxes:
            x1, y1, x2, y2 = bbox.abs(height, width)
            if bbox.name == "body":
                body_crop = image[y1:y2, x1:x2, :]
                res_pose = self.al_body_pose(body_crop)
                pose_cls = res_pose.get("cls_name")
                res_top5 = self.al_body_top5(body_crop)
                top5_cls = res_top5.get("cls_name")
                landmarks = self.al_body_kpts(body_crop)
                person = HxlxPerson(pic_name=pic_name)
                person.body_status = {"box": [x1, y1, x2, y2],
                                      "pose": pose_cls,
                                      "top5": top5_cls,
                                      "landmarks": [[int(px), int(py), ps] for px, py, ps in landmarks.tolist()],
                                      "hasbody": 'true',
                                      "bodyid": self._get_body_id(pic_name, [x1, y1, x2, y2])
                                      }
                person.set_gt_id()
                has_body_objs.append(person)
            elif bbox.name == "head":
                person = HxlxPerson(pic_name=pic_name)
                person.facebox = [x1, y1, x2, y2]
                person.body_det_head = [x1, y1, x2, y2]
                person.set_gt_id()
                has_head_objs.append(person)
        return has_head_objs, has_body_objs

    __call__ = get_persons_prop

    @staticmethod
    def _get_body_id(picname, box):
        return '{}__body_x{}y{}'.format(picname, int(box[0]), int(box[1]))


class DetectStats:
    def __init__(self, name):
        self.name = name
        self.total_count = 0
        self.total_time = 0
        self.detect_time = 0
        self.wait_time = 0
        self.detect_avg = 0
        self.total_avg = 0
        self.wait_avg = 0

    def add_stats(self, before_lock, start_detect):
        detecttime = time.time() - start_detect
        totaltime = detecttime + (start_detect - before_lock)
        self.total_count += 1
        self.total_time += int(totaltime * 1000)
        self.detect_time += int(detecttime * 1000)
        self.wait_time += int((start_detect - before_lock) * 1000)
        self.detect_avg = int(self.detect_time / self.total_count)
        self.total_avg = int(self.total_time / self.total_count)
        self.wait_avg = int(self.wait_time / self.total_count)

    def get_stats(self):
        return OrderedDict(name=self.name, total_count=self.total_count, detect_time=self.detect_time,
                           wait_time=self.wait_time,
                           detect_avg=self.detect_avg, total_avg=self.total_avg, wait_avg=self.wait_avg)


class FaceRecg(Singleton):
    def __init__(self, path_dir, align_pnt=11, debug=False):
        PathCfg.BASE_DIR = path_dir
        self._al_face_detect = YuFace(PathCfg.YUFACE)
        self._al_face_pnt98 = PFLD(98, PathCfg.PFLD_98)
        self._al_face_pnt7 = PFLD(7, PathCfg.PFLD_7)
        self._al_face_props = HeadAgeExp(PathCfg.HEAD_AGE_EXP)
        self._al_eye_state = EyeStateInferCls(PathCfg.EYE_STATE)
        self._al_face_express = ExpressInferCls(PathCfg.EXPRESS)
        self._al_face_organ_detect = FaceOrganDetector(PathCfg.FACE_ORGANS)
        self._landmarks_mean7 = np.load(PathCfg.FACE_7KPTS_MEAN)
        self._landmarks_mean98 = np.load(PathCfg.FACE_98KPTS_MEAN)

        self.align_pnt = align_pnt
        if align_pnt == 11:
            self._al_face_recg = InsightFace(PathCfg.INSIGHTFACE_98)

        elif align_pnt == 7:
            self._al_face_recg = InsightFace(PathCfg.INSIGHTFACE_7)
        else:
            raise ValueError("Align points error!")

        self.debug = debug
        self.timer = Timer('Total')
        self._body_algol_parts = BodyAlgolParts()
        self._body_semaphore = threading.Semaphore(1)
        self._face_semaphore = threading.Semaphore(1)
        self.body_stats = DetectStats('bodystats')
        self.face_stats = DetectStats('facestats')

    def detect_persons_prob(self, image, picname):
        has_head_objs, has_body_objs = self.get_persons_prob(image, picname)
        heads = [person.get_props() for person in has_head_objs]
        bodys = [body.get_props() for body in has_body_objs]
        return dict(heads=heads, bodys=bodys)

    def get_persons_prob(self, image, picname, img_type='photo'):
        before_lock = time.time()
        with self._body_semaphore:
            start_detect = time.time()
            has_head_objs, has_body_objs = self._body_algol_parts(image, picname, img_type)
        self.body_stats.add_stats(before_lock, start_detect)
        return has_head_objs, has_body_objs

    @staticmethod
    def add_definite_info(cvimg, faceinfos):
        cvimg = cv2.cvtColor(cvimg, cv2.COLOR_BGR2GRAY)
        for face in faceinfos:
            facebox = face['facebox']
            x1 = facebox[0]
            y1 = facebox[1]
            x2 = facebox[2]
            y2 = facebox[3]
            img = cvimg[y1:y2, x1:x2]
            try:
                imageVar = cv2.Laplacian(img, cv2.CV_64F).var()
                face['definite'] = int(math.sqrt(imageVar) * 100) / 100.0
            except Exception as e:
                face['definite'] = 0
            body_status = face['body_status']
            if body_status is not None and body_status.get('box'):
                box = body_status['box']
                x1 = box[0]
                y1 = box[1]
                x2 = box[2]
                y2 = box[3]
                img = cvimg[y1:y2, x1:x2]
                try:
                    imageVar = cv2.Laplacian(img, cv2.CV_64F).var()
                    body_status['definite'] = int(math.sqrt(imageVar) * 100) / 100.0
                except Exception as e:
                    body_status['definite'] = 0

    def get_feature(self, img, picname):
        before_lock = time.time()
        with self._face_semaphore:
            start_detect = time.time()
            face_infos = self._get_feature_internal(img, picname)
        self.face_stats.add_stats(before_lock, start_detect)
        return face_infos

    def get_image_props(self, image, picname, img_type='photo', for_debug=False):
        # 首先,获得身体检测相关算法结果
        with self.timer:
            has_head_objs, has_body_objs = self.get_persons_prob(image, picname, img_type)
            # 获取人脸相关算法结果
            has_face_objs = self.get_feature(img=image, picname=picname)
            # 进行头身匹配,合并人脸和身体结果
            img_props = merge_persons_props(has_face_objs, has_head_objs, has_body_objs)
            if for_debug:
                return img_props
        faceinfos = list()
        unmatched_body = list()
        for face in img_props:
            if len(face.get('facebox')) == 4:
                faceinfos.append(face)
            else:
                unmatched_body.append(face['body_status'])
        self.add_definite_info(image, faceinfos)
        return faceinfos, unmatched_body

    def get_faceboxes(self, img):
        return self._get_faceboxes(img)

    @staticmethod
    def _get_body_id(picname, box):
        return '{}__body_x{}y{}'.format(picname, int(box[0]), int(box[1]))

    def _get_faceboxes(self, image):
        total_bboxes, best_bbox = self._al_face_detect(image)

        return total_bboxes

    def _get_faceprop(self, image):
        prediction = self._al_face_props(image)
        age_name = prediction['age']
        exp_name = prediction['exp']

        if age_name in ["backhead", "jiaren", "people_unknown", "adult_unsure", "child_unsure"]:
            return 0, age_name, exp_name
        else:
            return 1, age_name, exp_name

    def _get_landmarks(self, image, pnts):
        if pnts == 98:
            landmarks = self._al_face_pnt98(image)
        elif pnts == 7:
            landmarks = self._al_face_pnt7(image)
        else:
            raise ValueError("Align points error!")

        return landmarks[0]

    def _get_eye_state(self, image, landmarks98):
        crph, crpw = image.shape[:2]
        if np.max(landmarks98) > 1:
            points = np.array(landmarks98, np.int)
        else:
            points = np.array(landmarks98, dtype=np.float32) * [crpw, crph]
            points = points.astype(np.int)
        l_eye = image[
                np.clip(points[35][1] - 5, 0, points[53][1] - 1):points[53][1],
                np.clip(points[33][0] - 5, 0, points[53][0] - 1):points[53][0]
                ].copy()
        r_eye = image[
                np.clip(points[44][1] - 5, 0, points[53][1] - 1):points[53][1],
                points[53][0]:np.clip(points[46][0] + 5, points[53][0] + 1, crpw)
                ].copy()
        if np.min(l_eye.shape[:2]) >= 25 and np.min(r_eye.shape[:2]) >= 25:  # when eyes area is small, skip
            eye_states = list()
            eye_states.append(self._al_eye_state(image=l_eye))
            eye_states.append(self._al_eye_state(image=r_eye))
            return 1, eye_states
        else:
            return 0, None  # eyes area is too small, return None

    def _get_eye_state_by_detect(self, image, face_organs):
        organs = face_organs.get("organs")
        h, w, c = image.shape
        eye_crops = list()
        for organ in organs:
            cls_name = organ.get("cls_name")
            box = np.array(organ.get("box"))
            if cls_name != 'eye':
                continue
            box = box * np.array([w, h, w, h])
            box = box.astype(np.int)
            box_w, box_h = box[2] - box[0], box[3] - box[1]
            expand_w, expand_h = int(box_w / 4), int(box_h)
            eye_crop = image[
                       np.clip(box[1] - expand_h, 0, box[1]):np.clip(box[3] + expand_h, 0, h),
                       np.clip(box[0] - expand_w, 0, box[0]):np.clip(box[2] + expand_w, 0, w)
                       ].copy()
            eye_crops.append(eye_crop)
        if np.min(eye_crops[0].shape[:2]) >= 15 and np.min(eye_crops[1].shape[:2]) >= 15:
            eye_states = list()
            eye_states.append(self._al_eye_state(image=eye_crops[0]))
            eye_states.append(self._al_eye_state(image=eye_crops[1]))
            return 1, eye_states
        else:
            return 0, None

    def _get_express(self, image):
        if np.min(image.shape[:2]) >= 8:
            express_res = self._al_face_express(image=image)
            return 1, express_res
        else:
            return 0, None

    def _get_align_face(self, image, landmarks, align_pnt):
        if align_pnt == 11:
            landmarks_mean = self._landmarks_mean98
        elif align_pnt == 7:
            landmarks_mean = self._landmarks_mean7
        else:
            raise ValueError("invalid align_pnt: %s." % align_pnt)
        face_img, expr_img = align_face(image, landmarks, landmarks_mean, method=1, num=align_pnt)
        return face_img, expr_img

    def _get_face_feat(self, image):
        fv = self._al_face_recg(image)
        return fv

    def _get_feature_internal(self, img, picname):
        """
        从原始大图中提取人脸相关属性,并将该图检测到的人物返回
        :param img: 原始大图, cvMat
        :param picname: 图片名称
        :return: list of HxlxPersons
        """
        h, w = img.shape[:2]
        face_boxes = self._get_faceboxes(img)  # 获取facebox
        face_boxes = self._calibrate_bbox(face_boxes, img.shape)
        if len(face_boxes) == 0:
            return []
        # 过滤异常/过大/过小/face box框
        face_boxes = np.array(face_boxes)
        good_bbox_idxs, bad_bbox_idxs, bad_flags = self.filter_face(face_boxes)

        filter_bboxes = []

        for bid, badbox_idx in enumerate(bad_bbox_idxs):
            badbox = face_boxes[badbox_idx]
            face_object_ = HxlxPerson(picname)
            face_object_['facebox'] = [int(badbox[0]), int(badbox[1]), int(badbox[2]), int(badbox[3])]
            face_object_['gt_id'] = self.get_gt_id(picname, badbox)
            face_object_['bl_valid'] = 'false'

            if bad_flags[bid] == 0:
                face_object_['bad_reason'] = 'bad_area'
            else:
                face_object_['bad_reason'] = 'bad_hw_ratio'
            filter_bboxes.append(face_object_)

        if len(good_bbox_idxs) == 0:
            return filter_bboxes
        # 过滤模糊框
        good_bboxes = face_boxes[good_bbox_idxs]
        good_bbox_idxs, blur_face_idxs = self._filter_blur(good_bboxes, img.copy(), margin_ratio=0.25)
        for badbox_idx in blur_face_idxs:
            badbox = good_bboxes[badbox_idx]
            face_object_ = HxlxPerson(picname)
            face_object_['facebox'] = [int(badbox[0]), int(badbox[1]), int(badbox[2]), int(badbox[3])]
            face_object_['gt_id'] = self.get_gt_id(picname, badbox)
            face_object_['bl_valid'] = 'false'
            face_object_['bad_reason'] = 'blur'
            filter_bboxes.append(face_object_)

        if len(good_bbox_idxs) == 0:
            return filter_bboxes

        face_boxes = good_bboxes[good_bbox_idxs].tolist()
        face_boxes_prop = self._expand_bbox(face_boxes, (h, w), margin_ratio=0.2)  # 为人脸属性扩边0.2

        valid_boxes = []
        valid_agenms = []
        valid_expnms = []
        for bid, box in enumerate(face_boxes_prop):
            crop_img = img[box[1]:box[3] + 1, box[0]:box[2] + 1, :]  # 去除假阳
            # 人脸属性:年龄/表情识别
            b, age_name, exp_name = self._get_faceprop(crop_img)
            if b:
                box_ = face_boxes[bid]
                valid_boxes.append(box_)
                valid_agenms.append(age_name)
                valid_expnms.append(exp_name)
            else:
                # 过滤角度异常人脸
                badbox = face_boxes[bid]
                face_object_ = HxlxPerson(picname)
                face_object_['facebox'] = [int(badbox[0]), int(badbox[1]), int(badbox[2]), int(badbox[3])]
                face_object_['gt_id'] = self.get_gt_id(picname, badbox)
                face_object_['bl_valid'] = 'false'
                face_object_['bad_reason'] = age_name
                face_object_['face_age'] = age_name
                face_object_['face_exp'] = exp_name
                filter_bboxes.append(face_object_)

        if len(valid_boxes) == 0:
            return filter_bboxes
        face_boxes_pfld = self._expand_bbox(valid_boxes, (h, w), margin_ratio=0.1)  # 为人脸landmark扩边0.1

        face_infos = filter_bboxes

        # 对余下的合法脸进行关键点检测,依据关键点检测,做人脸对齐/睁闭眼/表情
        for fid, box in enumerate(face_boxes_pfld):

            ori_box = valid_boxes[fid]
            face_object_ = HxlxPerson(picname)
            face_object_['facebox'] = [int(ori_box[0]), int(ori_box[1]), int(ori_box[2]), int(ori_box[3])]
            face_object_['gt_id'] = self.get_gt_id(picname, ori_box)
            face_object_['face_age'] = valid_agenms[fid]
            face_object_['face_exp'] = valid_expnms[fid]
            crop_img = img[box[1]:box[3] + 1, box[0]:box[2] + 1, :]
            src_box = valid_boxes[fid]
            crop_img_no_expand = img[int(src_box[1]):int(src_box[3] + 1), int(src_box[0]):int(src_box[2] + 1), :]
            crph, crpw = crop_img.shape[:2]
            face_object_['forpos_h'] = crph
            face_object_['forpos_w'] = crpw
            face_object_['landmarks_box'] = [box[0], box[1], box[2], box[3]]

            # landmark-98
            landmarks_98 = self._get_landmarks(crop_img, 98)
            landmarks_98[:, 0] *= crpw
            landmarks_98[:, 1] *= crph
            align_img_98, expr_img_98 = self._get_align_face(crop_img, landmarks_98, 11)  # 获取对齐脸

            face_object_['landmark_98'] = landmarks_98.astype(np.int)  # 返回绝对值
            # check eye state by landmark98
            # res, eye_states = self.get_eye_state(crop_img, landmarks_98)
            # if res == 1:  # if too small, skip
            #     eye_labels = np.array([i.get("label") for i in eye_states])
            #     if np.all(eye_labels == 0):  # both eyes closing
            #         # face_object_['bl_valid'] = 'false'   # 取消若推断为闭眼样本,不参与分堆
            #         face_object_['bad_reason'] = 'closing_eyes'
            #     face_object_['eyes_open_degree'] = np.sum([i.get('scores')[1] for i in eye_states]) / 2
            fnt_lv = get_front_level(crph, crpw, landmarks_98)
            face_object_['front_level'] = fnt_lv

            # get align face and mat
            # landmark-7
            landmarks_7 = self._get_landmarks(crop_img, 7)
            landmarks_7[:, 0] *= crpw
            landmarks_7[:, 1] *= crph
            align_img_7, expr_img_7 = self._get_align_face(crop_img, landmarks_7, 7)  # 获取对齐脸
            face_object_['landmark_7'] = landmarks_7.astype(np.int)  # 返回绝对值

            if self.align_pnt == 11:
                align_img = align_img_98
            elif self.align_pnt == 7:
                align_img = align_img_7
            else:
                raise ValueError("algin points error!")

            fv = self._get_face_feat(align_img)
            face_object_['featvec'] = fv

            # detect express
            al_express_res, express = self._get_express(crop_img_no_expand)
            if al_express_res:
                face_object_.update(express=express.get("cls_name"))

            # face organs detect
            organs_detect_res = self._al_face_organ_detect(image=crop_img)
            face_object_.update(face_organs=organs_detect_res)
            detect_valid = organs_detect_res.get("valid")
            # check eye state
            if detect_valid:
                res, eye_states = self._get_eye_state_by_detect(crop_img, organs_detect_res)
                if res == 1:  # if too small, skip
                    eye_labels = np.array([i.get("label") for i in eye_states])
                    if np.all(eye_labels == 0):  # both eyes closing
                        face_object_['bad_reason'] = 'closing_eyes'
                    face_object_['eyes_open_degree'] = np.sum([i.get('scores')[1] for i in eye_states]) / 2
            else:
                face_object_['bad_reason'] = 'bad_facial_organs'
                # face_object_['bl_valid'] = 'false'

            face_infos.append(face_object_)

        return face_infos

    def _filter_blur(self, face_bboxes, src_img, margin_ratio=0.25):
        clear_face_idxs, blur_face_idxs = [], []
        face_bboxes_exp = self._expand_bbox(face_bboxes, src_img.shape, margin_ratio=margin_ratio)

        for idx, bbox in enumerate(face_bboxes_exp):
            face_image = self.crop_image(src_img, bbox)
            is_blur, clear_score = blur_mult_detect(face_image)
            if is_blur:
                blur_face_idxs.append(idx)
            else:
                clear_face_idxs.append(idx)
        return clear_face_idxs, blur_face_idxs

    def get_gt_id(self, picname, box):
        if self.debug:
            return '{}#{}#{}#{}#{}'.format(picname, int(box[0]), int(box[1]),
                                           int(box[2]), int(box[3]))
        else:
            return '{}__face_x{}y{}'.format(picname, int(box[0]), int(box[1]))

    @staticmethod
    def _calibrate_bbox(bboxes, img_shape):
        height, width = img_shape[:2]
        out_bboxes = []
        for bbox in bboxes:

            x1, y1, x2, y2 = bbox[:4]
            x1, x2 = [np.clip(i, 0, width - 1) for i in [x1, x2]]
            y1, y2 = [np.clip(i, 0, height - 1) for i in [y1, y2]]
            bbox_new = [int(i) for i in [x1, y1, x2, y2]]
            if len(bbox) == 5:
                bbox_new.append(bbox[4])
            out_bboxes.append(bbox_new)
        return np.array(out_bboxes)

    @staticmethod
    def _expand_bbox(bboxes, img_shape, hw_ratio=1.2, margin_ratio=0.1):
        height, width = img_shape[:2]
        bbox_outes = []
        for bbox in bboxes:
            x1, y1, x2, y2 = bbox[:4]
            score = -1
            if len(bbox) == 5:
                score = bbox[-1]
            bbox_w, bbox_h = x2 - x1 + 1, y2 - y1 + 1

            p1 = bbox_w * margin_ratio
            x1_new = np.maximum(x1 - p1 + 1, 0)
            x2_new = np.minimum(x2 + p1 - 1, width - 1)
            bbox_w_new = x2_new - x1_new + 1
            bbox_h_new = bbox_w_new * hw_ratio
            p2 = (bbox_h_new - bbox_h) / 2
            y1_new = np.maximum(y1 - p2 + 1, 0)
            y2_new = np.minimum(y2 + p2 - 1, height - 1)
            bbox_out = [int(x1_new), int(y1_new), int(x2_new), int(y2_new), score]
            bbox_outes.append(bbox_out)

        return bbox_outes

    @staticmethod
    def filter_face(face_bboxes, min_area=1296, min_ratio=0.8, max_ratio=1.7):
        good_bbox_idxs, bad_bbox_idxs = [], []
        area_flag, ratio_flag = 0, 1
        bad_flags = []
        ws = (face_bboxes[:, 2] - face_bboxes[:, 0] + 1)
        hs = (face_bboxes[:, 3] - face_bboxes[:, 1] + 1)
        areas = ws * hs

        nrof_face = len(face_bboxes)

        for idx in range(nrof_face):
            area_i = areas[idx]
            ratio_i = hs[idx] / float(ws[idx]) if ws[idx] > 0 else 0.0
            if area_i <= min_area:
                bad_bbox_idxs.append(idx)
                bad_flags.append(area_flag)
                continue

            if not (min_ratio <= ratio_i <= max_ratio):
                bad_bbox_idxs.append(idx)
                bad_flags.append(ratio_flag)
                continue
            good_bbox_idxs.append(idx)

        return good_bbox_idxs, bad_bbox_idxs, bad_flags

    @staticmethod
    def crop_image(img, bbox):
        x1, y1, x2, y2 = [int(i) for i in bbox[:4]]
        crop_img = img[y1:y2 + 1, x1:x2 + 1, :]
        return crop_img

    def get_time_consume(self):
        res = []
        for k, v in self._body_algol_parts.__dict__.items():
            if hasattr(v, 'helper'):
                res.append(getattr(v, 'helper').get_cost())
        for k, v in self.__dict__.items():
            if hasattr(v, 'helper'):
                res.append(getattr(v, 'helper').get_cost())
        res.append(self.timer.get_cost())
        res = sorted(res, key=lambda x: float(x['avg']), reverse=True)
        res = "\n".join([i.get("info") for i in res])
        return res
