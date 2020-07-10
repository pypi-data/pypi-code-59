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


class DescribeImagesRequest(JDCloudRequest):
    """
    查询镜像信息列表。<br>
通过此接口可以查询到京东云官方镜像、第三方镜像、私有镜像、或其他用户共享给您的镜像。<br>
此接口支持分页查询，默认每页20条。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeImagesRequest, self).__init__(
            '/regions/{regionId}/images', 'GET', header, version)
        self.parameters = parameters


class DescribeImagesParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: 地域ID
        """

        self.regionId = regionId
        self.imageSource = None
        self.serviceCode = None
        self.offline = None
        self.platform = None
        self.ids = None
        self.rootDeviceType = None
        self.launchPermission = None
        self.status = None
        self.pageNumber = None
        self.pageSize = None

    def setImageSource(self, imageSource):
        """
        :param imageSource: (Optional) 镜像来源，如果没有指定ids参数，此参数必传；取值范围：public、shared、thirdparty、private、community
        """
        self.imageSource = imageSource

    def setServiceCode(self, serviceCode):
        """
        :param serviceCode: (Optional) 产品线标识，非必传，不传的时候返回全部产品线镜像
        """
        self.serviceCode = serviceCode

    def setOffline(self, offline):
        """
        :param offline: (Optional) 是否下线，默认值为false；imageSource为public或者thirdparty时，此参数才有意义，其它情况下此参数无效；指定镜像ID查询时，此参数无效
        """
        self.offline = offline

    def setPlatform(self, platform):
        """
        :param platform: (Optional) 操作系统平台，取值范围：Windows Server、CentOS、Ubuntu
        """
        self.platform = platform

    def setIds(self, ids):
        """
        :param ids: (Optional) 镜像ID列表，如果指定了此参数，其它参数可为空
        """
        self.ids = ids

    def setRootDeviceType(self, rootDeviceType):
        """
        :param rootDeviceType: (Optional) 镜像支持的系统盘类型，[localDisk,cloudDisk]
        """
        self.rootDeviceType = rootDeviceType

    def setLaunchPermission(self, launchPermission):
        """
        :param launchPermission: (Optional) 镜像的使用权限[all, specifiedUsers，ownerOnly]，可选参数，仅当imageSource取值private时有效
        """
        self.launchPermission = launchPermission

    def setStatus(self, status):
        """
        :param status: (Optional) <a href="http://docs.jdcloud.com/virtual-machines/api/image_status">参考镜像状态</a>
        """
        self.status = status

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码；默认为1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小；默认为20；取值范围[10, 100]
        """
        self.pageSize = pageSize

