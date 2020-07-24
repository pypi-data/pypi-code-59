# -*- coding: UTF-8 -*-
import numpy as np
from ..core import TRTInference, TRTClassifier
from ..utils import Resize

__all__ = ["HeadAgeExp", "FaceAge", "BodyPoseCls", "BodyPoseTop5Cls", "EyeStateInferCls", "ExpressInferCls"]


class HeadAgeExp(TRTInference):
    model_name = "HeadAgeExp"

    def __init__(self, *args, **kwargs):
        super(HeadAgeExp, self).__init__(*args, **kwargs)
        self._input_width = 96
        self._input_height = 96
        self.output_shapes = ((7,), (4,))
        self.age_classes = ("adult_sure", "adult_unsure", "child_sure",
                            "child_unsure", "backhead", "jiaren", "people_unknown")
        self.exp_classes = ("express_bad", "express_good", "express_tongue", "express_unknown")
        self.idx2str_age = {idx: name for idx, name in enumerate(self.age_classes)}
        self.idx2str_exp = {idx: name for idx, name in enumerate(self.exp_classes)}
        self.thresh_age = [0.4292, 0.9500, 0.5643, 0.9900, 0.1725, 0.0900, 0.9900]
        self.thresh_exp = [0.7803, 0.6447, 0.7266, 0.3922]

        self.scale_mean = np.array([0.017, 0.017, 0.017])
        self.channel_mean = np.array([103.94, 116.78, 123.68])  # bgr
        self.transform = Resize((self._input_width, self._input_height), False,
                                mean=self.channel_mean, scale=self.scale_mean)

    def _post_process(self, outputs: list, meta: dict = None):
        age_probs, exp_probs = outputs
        max_idx = np.argmax(age_probs)
        max_confidience = age_probs[max_idx]
        target_label_age = max_idx

        if max_idx == 0 and max_confidience < self.thresh_age[0]:  # adult_sure
            target_label_age = 6
        elif max_idx == 2 and max_confidience < self.thresh_age[2]:  # child_sure
            target_label_age = 6
        elif max_idx == 1 and max_confidience < self.thresh_age[1]:  # adult_unsure
            target_label_age = 6
        elif max_idx == 3 and max_confidience < self.thresh_age[3]:  # child_unsure
            target_label_age = 6
        elif max_idx == 4 and max_confidience < self.thresh_age[4]:  # backhead
            target_label_age = 6
        elif max_idx == 5 and max_confidience < self.thresh_age[5]:  # jiaren
            target_label_age = 6

        target_name_age = self.age_classes[target_label_age]
        target_prob_age = age_probs[target_label_age]

        max_idx = np.argmax(exp_probs)
        max_confidience = exp_probs[max_idx]
        target_label_exp = max_idx

        if max_idx == 0 and max_confidience < self.thresh_exp[0]:  # express_bad
            target_label_exp = 3
        elif max_idx == 1 and max_confidience < self.thresh_exp[1]:  # express_good
            target_label_exp = 3
        elif max_idx == 2 and max_confidience < self.thresh_exp[2]:  # express_tongue
            target_label_exp = 3

        target_name_exp = self.exp_classes[target_label_exp]
        target_prob_exp = exp_probs[target_label_exp]

        out = {'age': target_name_age,
               'age_prob': target_prob_age,
               'age_scores': age_probs,
               'exp': target_name_exp,
               'exp_prob': target_prob_exp,
               'exp_scores': exp_probs
               }
        return out


class FaceAge(TRTClassifier):
    def __init__(self, *args, **kwargs):
        super(FaceAge, self).__init__(*args, **kwargs)
        self.input_res = (96, 96)
        self.input_w, self.input_h = self.input_res
        self.class_names = ("adult", "child", "jiaren", "people_unknown")
        self.thresh = [0.40, 0.40, 0.25, 0.64]
        self.scale = np.array([0.017, 0.017, 0.017])
        self.mean = np.array([103.94, 116.78, 123.68])
        self.transform = Resize((self.input_w, self.input_h), False, self.mean, self.scale)
        self.output_shapes = ((len(self.class_names),),)


class BodyPoseCls(TRTClassifier):
    model_name = "bodyPose"

    def __init__(self, *args, **kwargs):
        super(BodyPoseCls, self).__init__(*args, **kwargs)
        self.input_res = (96, 96)
        self.input_w, self.input_h = self.input_res
        self.class_names = ("liegrovel", "sit", "stand", "unknown")
        self.thresh = [0.90, 0.60, 0.74, 1.0]
        self.scale = np.array([0.017, 0.017, 0.017])
        self.mean = np.array([103.94, 116.78, 123.68])
        self.transform = Resize(self.input_res, True, self.mean, self.scale)
        self.output_shapes = ((1, -1),)


class BodyPoseTop5Cls(TRTClassifier):
    model_name = "bodyTop5"

    def __init__(self, *args, **kwargs):
        super(BodyPoseTop5Cls, self).__init__(*args, **kwargs)
        self.input_res = (96, 128)
        self.input_w, self.input_h = self.input_res
        self.class_names = ("ceju45du", "shuangshouchayao", "wuweishou", "yiweishou", "unknown")
        self.thresh = [0.92, 0.76, 0.98, 0.94, 1.0]
        self.scale = np.array([0.017, 0.017, 0.017])
        self.mean = np.array([104.0, 117.0, 123.0])
        self.transform = Resize(self.input_res, False, self.mean, self.scale)
        self.output_shapes = ((1, -1),)


class EyeStateInferCls(TRTClassifier):
    model_name = "eyeState"

    def __init__(self, *args, **kwargs):
        super(EyeStateInferCls, self).__init__(*args, **kwargs)
        self.input_res = (64, 64)
        self.input_w, self.input_h = self.input_res
        self.class_names = ("close", "open", "unknown")
        self.thresh = [0.979, 0.50, 1.0]
        self.scale = np.array([0.017, 0.017, 0.017])
        self.mean = np.array([103.94, 116.78, 123.68])
        self.transform = Resize(self.input_res, False, self.mean, self.scale)
        self.output_shapes = ((1, -1),)


class ExpressInferCls(TRTClassifier):
    model_name = "faceExpress"

    def __init__(self, *args, **kwargs):
        super(ExpressInferCls, self).__init__(*args, **kwargs)
        self.input_res = (96, 96)
        self.input_w, self.input_h = self.input_res
        self.class_names = ('bad', 'good', 'normal', 'unknown')
        self.thresh = [0.28, 0.16, 0.956, 1.0]
        self.scale = np.array([0.00390625, 0.00390625, 0.00390625])
        self.mean = np.array([0, 0, 0])
        self.transform = Resize(self.input_res, False, self.mean, self.scale)
        self.output_shapes = ((1, -1),)
