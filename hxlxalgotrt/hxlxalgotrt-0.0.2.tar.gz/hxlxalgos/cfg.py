# -*- coding: UTF-8 -*-
"""
模型路径配置
"""
import os

from .utils import Singleton

_CUR_DIR = os.path.dirname(__file__)


class _PathCfg(Singleton):
    BASE_DIR = os.path.join(os.path.dirname(_CUR_DIR), "models/")

    # CenterNet-人头身体检测
    CenterNet = "body_det/CenterNetDla34_version0.2_20191021.trt"
    # SPPE-单人身体关键点评价
    SPPE = "body_pose/human_pose_resnet18_ap0.810_ar0.839.trt"
    # 舞蹈姿态top5分类
    BodyTop5 = "body_pose/bodytop5_version0.2_20190606.trt"
    # 身体姿态分类
    BodyPose = "body_pose/bodyPose_version0.2_20190605.trt"
    # yuface-人脸检测
    YUFACE = "yuface/hxlx-yuface-inplace_mergeBN.trt"
    # pfld-人脸关键点检测
    PFLD_98 = "pfld98/pfld-98pts-aug-20190618.trt"
    PFLD_7 = "pfld7/pfld-7pts-aug-20190618.trt"
    # 人脸年龄表情识别
    HEAD_AGE_EXP = "head_age_exp/pview_age_exp_20181211_mobilenet_v2.trt"
    # 睁闭眼识别
    EYE_STATE = "face_props/eyestate_20190419_mobilenet_v2.trt"
    # 表情识别
    EXPRESS = "face_exp/express_version0.2_20190627_haijun.trt"
    # 眼鼻口检测
    FACE_ORGANS = "face_props/wuguanDet_version0.2_20190615_yoloV3Lite.trt"
    # 标准人脸关键点均值
    FACE_98KPTS_MEAN = "mean_face_98pts_112x112.npy"
    FACE_7KPTS_MEAN = "mean_face_7pts_112x112.npy"
    # arcface-人脸识别
    INSIGHTFACE_7 = "r50-arcface-20191031-7pnts/model.trt"
    INSIGHTFACE_98 = "r50-arcface-20191031-98pnts/model.trt"

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if item.startswith("_"):
            return value
        if item == "BASE_DIR":
            return object.__getattribute__(self, item)
        if not os.path.isabs(value):
            value = os.path.join(self.BASE_DIR, value)
        if not os.path.exists(value):
            raise FileNotFoundError("File %s not found!" % value)
        return value


PathCfg = _PathCfg()
