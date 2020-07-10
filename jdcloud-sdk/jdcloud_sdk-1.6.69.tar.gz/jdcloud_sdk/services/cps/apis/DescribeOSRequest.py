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


class DescribeOSRequest(JDCloudRequest):
    """
    查询云物理服务器支持的操作系统
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeOSRequest, self).__init__(
            '/regions/{regionId}/os', 'GET', header, version)
        self.parameters = parameters


class DescribeOSParameters(object):

    def __init__(self, regionId, deviceType, ):
        """
        :param regionId: 地域ID，可调用接口（describeRegiones）获取云物理服务器支持的地域
        :param deviceType: 实例类型，可调用接口（describeDeviceTypes）获取指定地域的实例类型，例如：cps.c.normal
        """

        self.regionId = regionId
        self.deviceType = deviceType
        self.osType = None

    def setOsType(self, osType):
        """
        :param osType: (Optional) 操作系统类型，取值范围：CentOS、Ubuntu
        """
        self.osType = osType

