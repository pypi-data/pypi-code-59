# -*- coding: utf-8 -*-

import torch as th
import torch.nn as nn


class Basic(th.nn.Module):
    extension = 1
    least_required_dim = 1

    def __init__(self, dim, step, relu, conv):
        super(Basic, self).__init__()

        self.step = step
        self.relu = relu
        self.conv1 = conv(dim, dim, kernel_size=3, stride=1, padding=1, groups=1, bias=False, dilation=1)
        self.conv2 = conv(dim, dim, kernel_size=3, stride=1, padding=1, groups=1, bias=False, dilation=1)

        nn.init.normal_(self.conv1.weight, 0.0, 0.04)
        nn.init.normal_(self.conv2.weight, 0.0, 0.04)

    def forward(self, x):

        y = self.conv1(x)
        y = self.relu(y)
        y = self.conv2(y)
        y = x + y

        return y


class Bottleneck(th.nn.Module):
    extension = 1
    least_required_dim = 4

    def __init__(self, dim, step, relu, conv):
        super(Bottleneck, self).__init__()

        self.step = step
        self.relu = relu
        self.conv1 = conv(dim, dim // 4, kernel_size=1, bias=False)
        self.conv2 = conv(dim // 4, dim // 4, kernel_size=3, bias=False, padding=1)
        self.conv3 = conv(dim // 4, dim, kernel_size=1, bias=False)

        nn.init.normal_(self.conv1.weight, 0.0, 0.04)
        nn.init.normal_(self.conv2.weight, 0.0, 0.04)
        nn.init.normal_(self.conv3.weight, 0.0, 0.04)

    def forward(self, x):

        y = self.conv1(x)
        y = self.relu(y)
        y = self.conv2(y)
        y = self.relu(y)
        y = self.conv3(y)
        y = x + y

        return y
