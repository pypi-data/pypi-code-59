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


class AppList(object):

    def __init__(self, appId=None, arkId=None, appVersion=None, releaseTime=None, appStatus=None, onlineTime=None, tmId=None, tmName=None):
        """
        :param appId: (Optional) App业务编号
        :param arkId: (Optional) 云翼编译编号
        :param appVersion: (Optional) APP版本号
        :param releaseTime: (Optional) 发布时间
        :param appStatus: (Optional) APP状态，0-发布成功，1-发布失败，2-审核通过，3-审核不通过，4-上线，5-下线，99-发布中
        :param onlineTime: (Optional) 上线时间
        :param tmId: (Optional) 物模型编号
        :param tmName: (Optional) 物模型名称
        """

        self.appId = appId
        self.arkId = arkId
        self.appVersion = appVersion
        self.releaseTime = releaseTime
        self.appStatus = appStatus
        self.onlineTime = onlineTime
        self.tmId = tmId
        self.tmName = tmName
