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


class InstanceTemplateData(object):

    def __init__(self, instanceType=None, vpcId=None, imageId=None, includePassword=None, systemDisk=None, dataDisks=None, primaryNetworkInterface=None, elasticIp=None, keyNames=None, chargeOnStopped=None):
        """
        :param instanceType: (Optional) 实例规格
        :param vpcId: (Optional) 主网卡所属VPC的ID
        :param imageId: (Optional) 镜像ID
        :param includePassword: (Optional) 启动模板中是否包含自定义密码，true：包含密码，false：不包含密码
        :param systemDisk: (Optional) 系统盘信息
        :param dataDisks: (Optional) 数据盘信息，本地盘(local类型)做系统盘的云主机可挂载8块数据盘，云硬盘(cloud类型)做系统盘的云主机可挂载7块数据盘。
        :param primaryNetworkInterface: (Optional) 主网卡信息
        :param elasticIp: (Optional) 主网卡主IP关联的弹性IP规格
        :param keyNames: (Optional) 密钥对名称；当前只支持一个
        :param chargeOnStopped: (Optional) 停机不计费的标志， keepCharging(默认)：关机后继续计费；stopCharging：关机后停止计费。
        """

        self.instanceType = instanceType
        self.vpcId = vpcId
        self.imageId = imageId
        self.includePassword = includePassword
        self.systemDisk = systemDisk
        self.dataDisks = dataDisks
        self.primaryNetworkInterface = primaryNetworkInterface
        self.elasticIp = elasticIp
        self.keyNames = keyNames
        self.chargeOnStopped = chargeOnStopped
