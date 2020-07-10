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


class InstanceCloudDisk(object):

    def __init__(self, diskId=None, az=None, name=None, description=None, diskType=None, diskSize=None, status=None, createTime=None):
        """
        :param diskId: (Optional) 云硬盘ID
        :param az: (Optional) 所属AZ
        :param name: (Optional) 硬盘名称
        :param description: (Optional) 硬盘描述
        :param diskType: (Optional) 磁盘类型，取值为 ssd, premium-hdd 之一
        :param diskSize: (Optional) 磁盘大小（GiB）
        :param status: (Optional) 云硬盘状态，取值为 creating、available、in-use、extending、restoring、deleting、deleted、error_creating、error_deleting、error_restoring、error_extending 之一
        :param createTime: (Optional) 创建时间
        """

        self.diskId = diskId
        self.az = az
        self.name = name
        self.description = description
        self.diskType = diskType
        self.diskSize = diskSize
        self.status = status
        self.createTime = createTime
