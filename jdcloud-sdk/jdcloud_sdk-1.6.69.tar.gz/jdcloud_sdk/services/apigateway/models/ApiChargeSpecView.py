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


class ApiChargeSpecView(object):

    def __init__(self, apiChargeSpecs, appCode=None, serviceCode=None, showStatus=None, chargeType=None, accessSuccessType=None):
        """
        :param appCode: (Optional) appCode
        :param serviceCode: (Optional) serviceCode
        :param showStatus: (Optional) api中心展示，1展示，0 不展示 默认不展示
        :param chargeType: (Optional) 计费类型 0 标准计费 1 阶梯计费
        :param accessSuccessType: (Optional) 计费方式 0 200请求计费 1 后端处理计费
        :param apiChargeSpecs:  请求参数列表
        """

        self.appCode = appCode
        self.serviceCode = serviceCode
        self.showStatus = showStatus
        self.chargeType = chargeType
        self.accessSuccessType = accessSuccessType
        self.apiChargeSpecs = apiChargeSpecs
