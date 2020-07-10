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


class ModifyInstanceNameRequest(JDCloudRequest):
    """
    修改实例名称，可支持中文，实例名的具体规则可参见帮助中心文档:[名称及密码限制](../../documentation/Database-and-Cache-Service/RDS/Introduction/Restrictions/SQLServer-Restrictions.md)
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyInstanceNameRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:modifyInstanceName', 'POST', header, version)
        self.parameters = parameters


class ModifyInstanceNameParameters(object):

    def __init__(self, regionId, instanceId, instanceName):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param instanceId: RDS 实例ID，唯一标识一个RDS实例
        :param instanceName: 实例名称，名称支持中文，实例名的具体规则可参见帮助中心文档:[名称及密码限制](../../../documentation/Database-and-Cache-Service/RDS/Introduction/Restrictions/SQLServer-Restrictions.md)
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.instanceName = instanceName

