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


class TagKeysReqVo(object):

    def __init__(self, serviceCodes=None, tagFilters=None):
        """
        :param serviceCodes: (Optional) 产品线名称列表
标签系统支持的产品线名称如下
- vm               disk        sqlserver  es          mongodb               ip
- memcached        redis       drds       rds         database              db_ro
- percona          percona_ro  mariadb    mariadb_ro  pg                    cdn
- nativecontainer  pod         zfs        jqs         kubernetesNodegroup   jcq

        :param tagFilters: (Optional) 标签过滤列表
        """

        self.serviceCodes = serviceCodes
        self.tagFilters = tagFilters
