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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class OperateRRRequest(JDCloudRequest):
    """
    启用、停用、删除主域名下的解析记录
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(OperateRRRequest, self).__init__(
            '/regions/{regionId}/domain/{domainId}/RROperate', 'POST', header, version)
        self.parameters = parameters


class OperateRRParameters(object):

    def __init__(self, regionId, domainId, ids, action):
        """
        :param regionId: 实例所属的地域ID
        :param domainId: 域名ID，请使用getDomains接口获取。
        :param ids: 需要操作的解析记录ID，请使用searchRR接口获取。
        :param action: 操作类型，on->启用 off->停用 del->删除
        """

        self.regionId = regionId
        self.domainId = domainId
        self.ids = ids
        self.action = action

