# -*- coding: UTF-8 -*-
import cv2
import numpy as np
from ..core import TRTInference
from ..utils import Resize

__all__ = ["InsightFace", ]


class InsightFace(TRTInference):
    model_name = "insightface"

    def __init__(self, *args, **kwargs):
        super(InsightFace, self).__init__(*args, **kwargs)
        self._input_width = 112
        self._input_height = 112
        self.output_shapes = ((512,),)
        self.transform = Resize((self._input_width, self._input_height), False, color_mode=cv2.COLOR_BGR2RGB)

    def _post_process(self, outputs: list, meta: dict = None):
        outputs = [emb / np.linalg.norm(emb) for emb in outputs]
        return outputs
