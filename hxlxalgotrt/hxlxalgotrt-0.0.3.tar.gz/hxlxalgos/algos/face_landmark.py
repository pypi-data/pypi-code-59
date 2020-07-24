# -*- coding: UTF-8 -*-
import numpy as np
from ..core import TRTInference
from ..utils import Resize

__all__ = ["PFLD", ]


class PFLD(TRTInference):
    model_name = "PFLD"

    def __init__(self, nrof_pts=7, *args, **kwargs):
        super(PFLD, self).__init__(*args, **kwargs)
        self.nrof_pts = nrof_pts
        self._input_width = 112
        self._input_height = 112
        self.output_shapes = ((nrof_pts, 2),)
        self.scale_mean = np.array([0.017, 0.017, 0.017])
        self.channel_mean = np.array([104.0, 116.0, 124.0])  # bgr
        self.transform = Resize((self._input_width, self._input_height), False,
                                mean=self.channel_mean, scale=self.scale_mean)

    def _post_process(self, outputs: list, meta: dict = None):
        outputs = [np.clip(arr, 0, 1) for arr in outputs]
        return outputs
