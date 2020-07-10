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


class DescribeDevice(object):

    def __init__(self, idc=None, idcName=None, deviceId=None, snNo=None, cabinetNo=None, rackUIndex=None, uNum=None, brand=None, model=None, deviceType=None, assetBelong=None, assetStatus=None, deviceOpenTime=None):
        """
        :param idc: (Optional) 机房英文标识
        :param idcName: (Optional) 机房名称
        :param deviceId: (Optional) 设备Id
        :param snNo: (Optional) 设备SN号
        :param cabinetNo: (Optional) 机柜编码
        :param rackUIndex: (Optional) 所在U位
        :param uNum: (Optional) U数（U）
        :param brand: (Optional) 品牌
        :param model: (Optional) 型号
        :param deviceType: (Optional) 设备类型 server:服务器 network:网络设备 storage:存储设备 other:其他设备
        :param assetBelong: (Optional) 资产归属 own:自备 lease:租赁
        :param assetStatus: (Optional) 资产状态 launched:已上架 opened:已开通 canceling:退订中 operating:操作中 modifing:变更中
        :param deviceOpenTime: (Optional) 开通时间，遵循ISO8601标准，使用UTC时间，格式为：yyyy-MM-ddTHH:mm:ssZ
        """

        self.idc = idc
        self.idcName = idcName
        self.deviceId = deviceId
        self.snNo = snNo
        self.cabinetNo = cabinetNo
        self.rackUIndex = rackUIndex
        self.uNum = uNum
        self.brand = brand
        self.model = model
        self.deviceType = deviceType
        self.assetBelong = assetBelong
        self.assetStatus = assetStatus
        self.deviceOpenTime = deviceOpenTime
