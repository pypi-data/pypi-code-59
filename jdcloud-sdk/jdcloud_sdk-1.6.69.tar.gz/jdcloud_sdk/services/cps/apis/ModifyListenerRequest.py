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


class ModifyListenerRequest(JDCloudRequest):
    """
    修改监听器
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyListenerRequest, self).__init__(
            '/regions/{regionId}/listeners/{listenerId}:modifyListenerAttributes', 'POST', header, version)
        self.parameters = parameters


class ModifyListenerParameters(object):

    def __init__(self, regionId, listenerId, ):
        """
        :param regionId: 地域ID，可调用接口（describeCPSLBRegions）获取云物理服务器支持的地域
        :param listenerId: 监听器ID
        """

        self.regionId = regionId
        self.listenerId = listenerId
        self.algorithm = None
        self.stickySession = None
        self.realIp = None
        self.name = None
        self.description = None
        self.healthCheck = None
        self.healthCheckTimeout = None
        self.healthCheckInterval = None
        self.healthyThreshold = None
        self.unhealthyThreshold = None
        self.serverGroupId = None

    def setAlgorithm(self, algorithm):
        """
        :param algorithm: (Optional) 调度算法
        """
        self.algorithm = algorithm

    def setStickySession(self, stickySession):
        """
        :param stickySession: (Optional) 会话保持
        """
        self.stickySession = stickySession

    def setRealIp(self, realIp):
        """
        :param realIp: (Optional) 是否获取真实ip，取值范围on|off
        """
        self.realIp = realIp

    def setName(self, name):
        """
        :param name: (Optional) 名称
        """
        self.name = name

    def setDescription(self, description):
        """
        :param description: (Optional) 描述
        """
        self.description = description

    def setHealthCheck(self, healthCheck):
        """
        :param healthCheck: (Optional) 健康检查
        """
        self.healthCheck = healthCheck

    def setHealthCheckTimeout(self, healthCheckTimeout):
        """
        :param healthCheckTimeout: (Optional) 健康检查响应的最大超时时间
        """
        self.healthCheckTimeout = healthCheckTimeout

    def setHealthCheckInterval(self, healthCheckInterval):
        """
        :param healthCheckInterval: (Optional) 健康检查响应的最大间隔时间
        """
        self.healthCheckInterval = healthCheckInterval

    def setHealthyThreshold(self, healthyThreshold):
        """
        :param healthyThreshold: (Optional) 健康检查结果为success的阈值
        """
        self.healthyThreshold = healthyThreshold

    def setUnhealthyThreshold(self, unhealthyThreshold):
        """
        :param unhealthyThreshold: (Optional) 健康检查结果为fail的阈值
        """
        self.unhealthyThreshold = unhealthyThreshold

    def setServerGroupId(self, serverGroupId):
        """
        :param serverGroupId: (Optional) 服务器组id
        """
        self.serverGroupId = serverGroupId

