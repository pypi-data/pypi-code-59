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


class LoongrayQueryPageRequest(JDCloudRequest):
    """
    朗瑞分页查询设备信息,支持一个或多个条件
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(LoongrayQueryPageRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/devices:loongrayQueryPage', 'GET', header, version)
        self.parameters = parameters


class LoongrayQueryPageParameters(object):

    def __init__(self, instanceId, regionId, ):
        """
        :param instanceId: 设备归属的实例ID
        :param regionId: 设备归属的实例所在区域
        """

        self.instanceId = instanceId
        self.regionId = regionId
        self.deviceName = None
        self.manufacturer = None
        self.model = None
        self.status = None
        self.productKey = None
        self.deviceType = None
        self.nowPage = None
        self.pageSize = None
        self.order = None
        self.direction = None
        self.parentId = None
        self.orderId = None
        self.deviceCollectorType = None

    def setDeviceName(self, deviceName):
        """
        :param deviceName: (Optional) 设备名称，模糊匹配
        """
        self.deviceName = deviceName

    def setManufacturer(self, manufacturer):
        """
        :param manufacturer: (Optional) 设备厂商，模糊匹配
        """
        self.manufacturer = manufacturer

    def setModel(self, model):
        """
        :param model: (Optional) 设备型号，模糊匹配
        """
        self.model = model

    def setStatus(self, status):
        """
        :param status: (Optional) 设备状态 0-未激活，1-激活离线，2-激活在线
        """
        self.status = status

    def setProductKey(self, productKey):
        """
        :param productKey: (Optional) 设备所归属的产品Key
        """
        self.productKey = productKey

    def setDeviceType(self, deviceType):
        """
        :param deviceType: (Optional) 设备类型，同产品类型，0-设备，1-网关
        """
        self.deviceType = deviceType

    def setNowPage(self, nowPage):
        """
        :param nowPage: (Optional) 当前页数
        """
        self.nowPage = nowPage

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 每页的数据条数
        """
        self.pageSize = pageSize

    def setOrder(self, order):
        """
        :param order: (Optional) 排序关键字--name,type,productKey,status--最多支持一个字段
        """
        self.order = order

    def setDirection(self, direction):
        """
        :param direction: (Optional) 顺序，升序降序--asc,desc
        """
        self.direction = direction

    def setParentId(self, parentId):
        """
        :param parentId: (Optional) 父设备Id
        """
        self.parentId = parentId

    def setOrderId(self, orderId):
        """
        :param orderId: (Optional) 订单号
        """
        self.orderId = orderId

    def setDeviceCollectorType(self, deviceCollectorType):
        """
        :param deviceCollectorType: (Optional) 设备采集器类型
        """
        self.deviceCollectorType = deviceCollectorType

