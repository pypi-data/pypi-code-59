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


class Hg(object):

    def __init__(self, scheme=None, host=None, port=None, path=None, httpHeader=None):
        """
        :param scheme: (Optional) 默认值：http。
        :param host: (Optional) 连接到pod的host信息。
        :param port: (Optional) 端口号。
        :param path: (Optional) HTTP的路径。
        :param httpHeader: (Optional) 自定义Http headers
        """

        self.scheme = scheme
        self.host = host
        self.port = port
        self.path = path
        self.httpHeader = httpHeader
