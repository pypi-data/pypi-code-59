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


class UpdateAccessKeyRequest(JDCloudRequest):
    """
    更新密钥
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UpdateAccessKeyRequest, self).__init__(
            '/regions/{regionId}/accessKeys/{accessKeyId}', 'PATCH', header, version)
        self.parameters = parameters


class UpdateAccessKeyParameters(object):

    def __init__(self, regionId, accessKeyId, ):
        """
        :param regionId: 地域ID
        :param accessKeyId: access key id
        """

        self.regionId = regionId
        self.accessKeyId = accessKeyId
        self.description = None
        self.accessKeyType = None
        self.accessKey = None

    def setDescription(self, description):
        """
        :param description: (Optional) 描述
        """
        self.description = description

    def setAccessKeyType(self, accessKeyType):
        """
        :param accessKeyType: (Optional) 密钥类型
        """
        self.accessKeyType = accessKeyType

    def setAccessKey(self, accessKey):
        """
        :param accessKey: (Optional) Access Key
        """
        self.accessKey = accessKey

