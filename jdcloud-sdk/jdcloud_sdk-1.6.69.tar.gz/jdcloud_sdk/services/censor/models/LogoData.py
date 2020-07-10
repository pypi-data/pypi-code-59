# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.


class LogoData(object):

    def __init__(self, logoType=None, name=None, x=None, y=None, w=None, h=None):
        """
        :param logoType: (Optional) 识别出的logo类型，取值为TV （台标）
        :param name: (Optional) 识别出的logo名称
        :param x: (Optional) 以图片左上角为坐标原点，logo区域左上角到y轴距离
        :param y: (Optional) 以图片左上角为坐标原点，logo区域左上角到x轴距离
        :param w: (Optional) logo区域宽度
        :param h: (Optional) logo区域高度
        """

        self.logoType = logoType
        self.name = name
        self.x = x
        self.y = y
        self.w = w
        self.h = h
