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


class DescribeLogsetsRequest(JDCloudRequest):
    """
    查询日志集列表。支持按照名称进行模糊查询。结果中包含了该日志集是否存在日志主题的信息。存在日志主题的日志集不允许删除。
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeLogsetsRequest, self).__init__(
            '/regions/{regionId}/logsets', 'GET', header, version)
        self.parameters = parameters


class DescribeLogsetsParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: 地域 Id
        """

        self.regionId = regionId
        self.pageNumber = None
        self.pageSize = None
        self.name = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 当前所在页，默认为1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 页面大小，默认为20；取值范围[1, 100]
        """
        self.pageSize = pageSize

    def setName(self, name):
        """
        :param name: (Optional) 日志集名称
        """
        self.name = name

