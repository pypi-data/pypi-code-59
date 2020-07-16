from collections import Iterable

import cv2
import numpy as np


class Compose:
    def __init__(self, transforms):
        self.transforms = transforms

    def __call__(self, x):
        for t in self.transforms:
            x = t(x)
        return x


class Normalize:
    def __init__(self, mean, std):
        self.mean = mean
        self.std = std

    def __call__(self, x):
        x = x - self.mean
        x = x / self.std
        return x


class DeNormalize:
    def __init__(self, mean, std):
        self.mean = mean
        self.std = std

    def __call__(self, x):
        x = x * self.std
        x = x + self.mean
        return x


class Resize:
    def __init__(self, size, padding_value=None, interpolation=None):
        if isinstance(size, Iterable):
            size = tuple(int(i) for i in size)
        else:
            size = (int(size), int(size))

        self.size = size
        self.interpolation = interpolation
        self.padding_value = padding_value

    def __call__(self, img):
        if self.padding_value is None:
            if self.interpolation is None:
                return cv2.resize(img, self.size)
            else:
                return cv2.resize(img, self.size, interpolation=self.interpolation)

        fy = self.size[0] / img.shape[0]
        fx = self.size[1] / img.shape[1]

        fx = fy = min(fx, fy)
        if self.interpolation is None:
            img = cv2.resize(img, None, fx=fx, fy=fy)
        else:
            img = cv2.resize(img, None, fx=fx, fy=fy, interpolation=self.interpolation)

        h, w = img.shape[0], img.shape[1]
        ph1 = (self.size[0] - h) // 2
        pw1 = (self.size[1] - w) // 2
        ph2 = ph1 + h
        pw2 = pw1 + w

        if len(img.shape) == 2:
            new_img = np.empty(shape=self.size, dtype=img.dtype)
            new_img.fill(self.padding_value)
        elif len(img.shape) == 3:
            new_img = np.empty(shape=self.size + (img.shape[2],), dtype=img.dtype)
            new_img.fill(self.padding_value)
        else:
            raise NotImplementedError()

        new_img[ph1:ph2, pw1:pw2, ...] = img
        return new_img
