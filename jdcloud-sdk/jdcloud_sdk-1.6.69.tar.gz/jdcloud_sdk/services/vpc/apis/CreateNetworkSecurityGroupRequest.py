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


class CreateNetworkSecurityGroupRequest(JDCloudRequest):
    """
    创建安全组
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateNetworkSecurityGroupRequest, self).__init__(
            '/regions/{regionId}/networkSecurityGroups/', 'POST', header, version)
        self.parameters = parameters


class CreateNetworkSecurityGroupParameters(object):

    def __init__(self, regionId, vpcId, networkSecurityGroupName, ):
        """
        :param regionId: Region ID
        :param vpcId: 私有网络ID
        :param networkSecurityGroupName: 安全组名称，只允许输入中文、数字、大小写字母、英文下划线“_”及中划线“-”，不允许为空且不超过32字符。
        """

        self.regionId = regionId
        self.vpcId = vpcId
        self.networkSecurityGroupName = networkSecurityGroupName
        self.description = None

    def setDescription(self, description):
        """
        :param description: (Optional) 描述,​ 允许输入UTF-8编码下的全部字符，不超过256字符
        """
        self.description = description

