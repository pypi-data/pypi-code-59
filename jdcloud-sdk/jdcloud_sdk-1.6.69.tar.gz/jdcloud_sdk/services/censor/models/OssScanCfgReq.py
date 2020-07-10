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


class OssScanCfgReq(object):

    def __init__(self, scanType, bucketsInfo, freezeAction, imageInfo, videoInfo, id=None, startTime=None, endTime=None, frameInfo=None):
        """
        :param id: (Optional) id标识,更新时传入，新增时传0
        :param scanType:  检测类型，increment-增量，stock-存量
        :param startTime: (Optional) 存量检测的开始时间，增量时无意义
        :param endTime: (Optional) 存量检测的截止时间，增量时无意义
        :param bucketsInfo:  需要检测的oss bucket信息
        :param freezeAction:  冻结方式，policy-修改权限，remove-移动到备份文件夹，目前仅支持remove
        :param imageInfo:  图片配置
        :param videoInfo:  视频配置
        :param frameInfo: (Optional) 视频截帧配置, 暂不支持
        """

        self.id = id
        self.scanType = scanType
        self.startTime = startTime
        self.endTime = endTime
        self.bucketsInfo = bucketsInfo
        self.freezeAction = freezeAction
        self.imageInfo = imageInfo
        self.videoInfo = videoInfo
        self.frameInfo = frameInfo
