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


class UserAccessKey(object):

    def __init__(self, id=None, pin=None, account=None, accessKey=None, accessKeySecret=None, expire=None, created=None, modified=None, modifier=None, state=None, yn=None):
        """
        :param id: (Optional) 用户通行id
        :param pin: (Optional) 用户名
        :param account: (Optional) 用户账号
        :param accessKey: (Optional) 访问密钥，AccessKey用于程序方式调用云服务API
        :param accessKeySecret: (Optional) AccessKeySecret是用来验证用户的密钥
        :param expire: (Optional) 到期时间
        :param created: (Optional) 创建时间
        :param modified: (Optional) 更新时间
        :param modifier: (Optional) 更新操作人
        :param state: (Optional) 状态
        :param yn: (Optional) 
        """

        self.id = id
        self.pin = pin
        self.account = account
        self.accessKey = accessKey
        self.accessKeySecret = accessKeySecret
        self.expire = expire
        self.created = created
        self.modified = modified
        self.modifier = modifier
        self.state = state
        self.yn = yn
