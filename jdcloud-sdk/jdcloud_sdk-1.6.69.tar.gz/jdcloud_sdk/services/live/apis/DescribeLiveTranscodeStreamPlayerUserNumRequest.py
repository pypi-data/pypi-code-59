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


class DescribeLiveTranscodeStreamPlayerUserNumRequest(JDCloudRequest):
    """
    查询转码流观看人数
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeLiveTranscodeStreamPlayerUserNumRequest, self).__init__(
            '/describeLiveTranscodeStreamPlayerUserNum', 'GET', header, version)
        self.parameters = parameters


class DescribeLiveTranscodeStreamPlayerUserNumParameters(object):

    def __init__(self, domainName, appName, startTime, ):
        """
        :param domainName: 推流域名
        :param appName: 应用名称
        :param startTime: 查询起始时间，UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'

        """

        self.domainName = domainName
        self.appName = appName
        self.ispName = None
        self.locationName = None
        self.protocolType = None
        self.period = None
        self.startTime = startTime
        self.endTime = None

    def setIspName(self, ispName):
        """
        :param ispName: (Optional) 运营商

        """
        self.ispName = ispName

    def setLocationName(self, locationName):
        """
        :param locationName: (Optional) 查询的区域，如beijing,shanghai。多个用逗号分隔

        """
        self.locationName = locationName

    def setProtocolType(self, protocolType):
        """
        :param protocolType: (Optional) 查询的流协议类型，取值范围："rtmp,hdl,hls"，多个时以逗号分隔

        """
        self.protocolType = protocolType

    def setPeriod(self, period):
        """
        :param period: (Optional) 查询周期，当前取值范围：“oneMin,fiveMin,halfHour,hour,twoHour,sixHour,day,followTime”，分别表示1min，5min，半小时，1小时，2小时，6小时，1天，跟随时间。默认为空，表示fiveMin。当传入followTime时，表示按Endtime-StartTime的周期，只返回一个点

        """
        self.period = period

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 查询截至时间，UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，为空时默认为当前时间

        """
        self.endTime = endTime

