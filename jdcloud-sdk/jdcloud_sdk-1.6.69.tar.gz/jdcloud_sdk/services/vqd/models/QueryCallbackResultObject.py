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


class QueryCallbackResultObject(object):

    def __init__(self, callbackType=None, httpUrl=None, callbackEvents=None, createTime=None, updateTime=None):
        """
        :param callbackType: (Optional) 回调方式
        :param httpUrl: (Optional) HTTP方式的回调URL
        :param callbackEvents: (Optional) 回调事件列表
        :param createTime: (Optional) 创建时间
        :param updateTime: (Optional) 修改时间
        """

        self.callbackType = callbackType
        self.httpUrl = httpUrl
        self.callbackEvents = callbackEvents
        self.createTime = createTime
        self.updateTime = updateTime
