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


class SetHttpSslRequest(JDCloudRequest):
    """
    设置CDN域名SSL配置
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(SetHttpSslRequest, self).__init__(
            '/domains/{domainId}:setHttpSsl', 'POST', header, version)
        self.parameters = parameters


class SetHttpSslParameters(object):

    def __init__(self, domainId, ):
        """
        :param domainId: 域名ID
        """

        self.domainId = domainId
        self.source = None
        self.title = None
        self.sslCert = None
        self.sslKey = None
        self.jumpType = None
        self.enabled = None

    def setSource(self, source):
        """
        :param source: (Optional) 证书来源。取值范围：default
        """
        self.source = source

    def setTitle(self, title):
        """
        :param title: (Optional) 证书标题
        """
        self.title = title

    def setSslCert(self, sslCert):
        """
        :param sslCert: (Optional) 证书内容
        """
        self.sslCert = sslCert

    def setSslKey(self, sslKey):
        """
        :param sslKey: (Optional) 证书私钥
        """
        self.sslKey = sslKey

    def setJumpType(self, jumpType):
        """
        :param jumpType: (Optional) 跳转类型。取值范围：
default - 采用回源域名的默认协议
http - 强制采用http协议回源
https - 强制采用https协议回源

        """
        self.jumpType = jumpType

    def setEnabled(self, enabled):
        """
        :param enabled: (Optional) SSL配置启用状态
        """
        self.enabled = enabled

