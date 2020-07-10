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


class WebRuleSpec(object):

    def __init__(self, domain, protocol, originType, algorithm, webSocketStatus, serviceIp=None, port=None, httpsPort=None, originAddr=None, onlineAddr=None, originDomain=None, forceJump=None, customPortStatus=None, httpOrigin=None, geoRsRoute=None):
        """
        :param serviceIp: (Optional) 高防 IP
        :param domain:  子域名
        :param protocol:  协议: http, https 至少一个为 true
        :param port: (Optional) HTTP 协议的端口号, 如80, 81; 如果 protocol.http 为 true, 至少配置一个端口, 最多添加 5 个
        :param httpsPort: (Optional) HTTPS 协议的端口号, 如443, 8443; 如果 protocol.https 为 true, 至少配置一个端口, 最多添加 5 个
        :param originType:  回源类型：A 或者 CNAME
        :param originAddr: (Optional) originType 为 A 时, 需要设置该字段
        :param onlineAddr: (Optional) 备用的回源地址列表, 可以配置为一个域名或者多个 ip 地址
        :param originDomain: (Optional) 回源域名, originType 为 CNAME 时需要指定该字段
        :param algorithm:  转发规则. <br>- wrr: 带权重的轮询<br>- rr:  不带权重的轮询<br>- sh:  源地址hash
        :param forceJump: (Optional) 是否开启 HTTPS 强制跳转, protocol.http 和 protocol.https 都为 true 时此参数生效. <br>- 0: 不开启强制跳转. <br>- 1: 开启强制跳转
        :param customPortStatus: (Optional) 是否为自定义端口号. 0: 默认<br>- 1: 自定义
        :param httpOrigin: (Optional) 是否开启 HTTP 回源, protocol.https 为 true 时此参数生效. <br>- 0: 不开启. <br>- 1: 开启
        :param webSocketStatus:  是否开启 WebSocket.<br>- 0: 不开启<br>- 1: 开启
        :param geoRsRoute: (Optional) 按区域分流回源配置
        """

        self.serviceIp = serviceIp
        self.domain = domain
        self.protocol = protocol
        self.port = port
        self.httpsPort = httpsPort
        self.originType = originType
        self.originAddr = originAddr
        self.onlineAddr = onlineAddr
        self.originDomain = originDomain
        self.algorithm = algorithm
        self.forceJump = forceJump
        self.customPortStatus = customPortStatus
        self.httpOrigin = httpOrigin
        self.webSocketStatus = webSocketStatus
        self.geoRsRoute = geoRsRoute
