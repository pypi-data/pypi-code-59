# MIT LICENSE
#
# Copyright 1997 - 2020 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE. 
from uhd_restpy.base import Base
from uhd_restpy.files import Files


class Router(Base):
    """
    The Router class encapsulates a list of router resources that are managed by the user.
    A list of resources can be retrieved from the server using the Router.find() method.
    The list can be managed by using the Router.add() and Router.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'router'
    _SDM_ATT_MAP = {
        'AreaAddressList': 'areaAddressList',
        'AreaAuthType': 'areaAuthType',
        'AreaReceivedPasswordList': 'areaReceivedPasswordList',
        'AreaTransmitPassword': 'areaTransmitPassword',
        'BroadcastRootPriority': 'broadcastRootPriority',
        'CapabilityRouterId': 'capabilityRouterId',
        'DeviceId': 'deviceId',
        'DevicePriority': 'devicePriority',
        'DomainAuthType': 'domainAuthType',
        'DomainReceivedPasswordList': 'domainReceivedPasswordList',
        'DomainTransmitPassword': 'domainTransmitPassword',
        'EnableAttached': 'enableAttached',
        'EnableAutoLoopback': 'enableAutoLoopback',
        'EnableDiscardLearnedLsps': 'enableDiscardLearnedLsps',
        'EnableHelloPadding': 'enableHelloPadding',
        'EnableHitlessRestart': 'enableHitlessRestart',
        'EnableHostName': 'enableHostName',
        'EnableIgnoreMtPortCapability': 'enableIgnoreMtPortCapability',
        'EnableIgnoreRecvMd5': 'enableIgnoreRecvMd5',
        'EnableMtIpv6': 'enableMtIpv6',
        'EnableMtuProbe': 'enableMtuProbe',
        'EnableMultiTopology': 'enableMultiTopology',
        'EnableOverloaded': 'enableOverloaded',
        'EnablePartitionRepair': 'enablePartitionRepair',
        'EnableTrillOam': 'enableTrillOam',
        'EnableWideMetric': 'enableWideMetric',
        'Enabled': 'enabled',
        'FTagValue': 'fTagValue',
        'FilterIpv4MulticastTlvs': 'filterIpv4MulticastTlvs',
        'FilterIpv6MulticastTlvs': 'filterIpv6MulticastTlvs',
        'FilterLearnedIpv4Prefixes': 'filterLearnedIpv4Prefixes',
        'FilterLearnedIpv6Prefixes': 'filterLearnedIpv6Prefixes',
        'FilterLearnedRbridges': 'filterLearnedRbridges',
        'FilterLearnedSpbRbridges': 'filterLearnedSpbRbridges',
        'FilterLearnedTrillMacUnicast': 'filterLearnedTrillMacUnicast',
        'FilterMacMulticastTlvs': 'filterMacMulticastTlvs',
        'HostName': 'hostName',
        'InterLspMgroupPduBurstGap': 'interLspMgroupPduBurstGap',
        'LspLifeTime': 'lspLifeTime',
        'LspMaxSize': 'lspMaxSize',
        'LspMgroupPduMinTransmissionInterval': 'lspMgroupPduMinTransmissionInterval',
        'LspRefreshRate': 'lspRefreshRate',
        'MaxAreaAddresses': 'maxAreaAddresses',
        'MaxLspMgroupPdusPerBurst': 'maxLspMgroupPdusPerBurst',
        'NumberOfMtuProbes': 'numberOfMtuProbes',
        'NumberOfMultiDestinationTrees': 'numberOfMultiDestinationTrees',
        'OriginatingLspBufSize': 'originatingLspBufSize',
        'PsnpInterval': 'psnpInterval',
        'RestartMode': 'restartMode',
        'RestartTime': 'restartTime',
        'RestartVersion': 'restartVersion',
        'StartFtagValue': 'startFtagValue',
        'SwitchId': 'switchId',
        'SwitchIdPriority': 'switchIdPriority',
        'SystemId': 'systemId',
        'TeEnable': 'teEnable',
        'TeRouterId': 'teRouterId',
        'TrafficGroupId': 'trafficGroupId',
    }

    def __init__(self, parent):
        super(Router, self).__init__(parent)

    @property
    def CustomTlv(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtlv_c6e90911b9acf4e885879d319ee6cb26.CustomTlv): An instance of the CustomTlv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtlv_c6e90911b9acf4e885879d319ee6cb26 import CustomTlv
        return CustomTlv(self)

    @property
    def CustomTopology(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopology_0a794682277db03b3f27dfdb007e3556.CustomTopology): An instance of the CustomTopology class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopology_0a794682277db03b3f27dfdb007e3556 import CustomTopology
        return CustomTopology(self)

    @property
    def DceMulticastIpv4GroupRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcemulticastipv4grouprange_8ecdaf01632ffda39d16b74617d88e07.DceMulticastIpv4GroupRange): An instance of the DceMulticastIpv4GroupRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcemulticastipv4grouprange_8ecdaf01632ffda39d16b74617d88e07 import DceMulticastIpv4GroupRange
        return DceMulticastIpv4GroupRange(self)

    @property
    def DceMulticastIpv6GroupRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcemulticastipv6grouprange_ee1ce31a05c19e355e26b903fe96dd54.DceMulticastIpv6GroupRange): An instance of the DceMulticastIpv6GroupRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcemulticastipv6grouprange_ee1ce31a05c19e355e26b903fe96dd54 import DceMulticastIpv6GroupRange
        return DceMulticastIpv6GroupRange(self)

    @property
    def DceMulticastMacRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcemulticastmacrange_90be9e76bbe2bdae2a6ce97da2935c7d.DceMulticastMacRange): An instance of the DceMulticastMacRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcemulticastmacrange_90be9e76bbe2bdae2a6ce97da2935c7d import DceMulticastMacRange
        return DceMulticastMacRange(self)

    @property
    def DceNetworkRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcenetworkrange_649f45d7df9ebec58e184822ad21e8aa.DceNetworkRange): An instance of the DceNetworkRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcenetworkrange_649f45d7df9ebec58e184822ad21e8aa import DceNetworkRange
        return DceNetworkRange(self)

    @property
    def DceTopologyRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcetopologyrange_769d462a4362502b4f2bc8320eb8d2dc.DceTopologyRange): An instance of the DceTopologyRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcetopologyrange_769d462a4362502b4f2bc8320eb8d2dc import DceTopologyRange
        return DceTopologyRange(self)

    @property
    def Interface(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_ddc6ed85db77afb3c40ee4824b274478.Interface): An instance of the Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_ddc6ed85db77afb3c40ee4824b274478 import Interface
        return Interface(self)

    @property
    def LearnedInformation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedinformation_5daa72987f01dd021a869ed0b1553524.LearnedInformation): An instance of the LearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedinformation_5daa72987f01dd021a869ed0b1553524 import LearnedInformation
        return LearnedInformation(self)._select()

    @property
    def NetworkRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.networkrange_02c79ff0750dbeaa7564c44b5ac629d8.NetworkRange): An instance of the NetworkRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.networkrange_02c79ff0750dbeaa7564c44b5ac629d8 import NetworkRange
        return NetworkRange(self)

    @property
    def RouteRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.routerange_e55904caea8ea54d18de0639128c8009.RouteRange): An instance of the RouteRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.routerange_e55904caea8ea54d18de0639128c8009 import RouteRange
        return RouteRange(self)

    @property
    def SpbNetworkRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.spbnetworkrange_525415b0593fd4072368412490b137fa.SpbNetworkRange): An instance of the SpbNetworkRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.spbnetworkrange_525415b0593fd4072368412490b137fa import SpbNetworkRange
        return SpbNetworkRange(self)

    @property
    def SpbTopologyRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.spbtopologyrange_18dd7169f415a4811ddde5fbb7efc8de.SpbTopologyRange): An instance of the SpbTopologyRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.spbtopologyrange_18dd7169f415a4811ddde5fbb7efc8de import SpbTopologyRange
        return SpbTopologyRange(self)

    @property
    def TrillPingOam(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.trillpingoam_472a7a28792c47a3a744e2cafe3b4072.TrillPingOam): An instance of the TrillPingOam class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.trillpingoam_472a7a28792c47a3a744e2cafe3b4072 import TrillPingOam
        return TrillPingOam(self)._select()

    @property
    def TrillUnicastMacRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.trillunicastmacrange_e4411b15921d22225097886c77d0492d.TrillUnicastMacRange): An instance of the TrillUnicastMacRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.trillunicastmacrange_e4411b15921d22225097886c77d0492d import TrillUnicastMacRange
        return TrillUnicastMacRange(self)

    @property
    def AreaAddressList(self):
        """
        Returns
        -------
        - list(str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AreaAddressList'])
    @AreaAddressList.setter
    def AreaAddressList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AreaAddressList'], value)

    @property
    def AreaAuthType(self):
        """
        Returns
        -------
        - str(none | password | md5): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AreaAuthType'])
    @AreaAuthType.setter
    def AreaAuthType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AreaAuthType'], value)

    @property
    def AreaReceivedPasswordList(self):
        """
        Returns
        -------
        - list(str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AreaReceivedPasswordList'])
    @AreaReceivedPasswordList.setter
    def AreaReceivedPasswordList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AreaReceivedPasswordList'], value)

    @property
    def AreaTransmitPassword(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AreaTransmitPassword'])
    @AreaTransmitPassword.setter
    def AreaTransmitPassword(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AreaTransmitPassword'], value)

    @property
    def BroadcastRootPriority(self):
        """DEPRECATED 
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BroadcastRootPriority'])
    @BroadcastRootPriority.setter
    def BroadcastRootPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BroadcastRootPriority'], value)

    @property
    def CapabilityRouterId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CapabilityRouterId'])
    @CapabilityRouterId.setter
    def CapabilityRouterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CapabilityRouterId'], value)

    @property
    def DeviceId(self):
        """DEPRECATED 
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DeviceId'])
    @DeviceId.setter
    def DeviceId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DeviceId'], value)

    @property
    def DevicePriority(self):
        """DEPRECATED 
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DevicePriority'])
    @DevicePriority.setter
    def DevicePriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DevicePriority'], value)

    @property
    def DomainAuthType(self):
        """
        Returns
        -------
        - str(none | password | md5): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DomainAuthType'])
    @DomainAuthType.setter
    def DomainAuthType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DomainAuthType'], value)

    @property
    def DomainReceivedPasswordList(self):
        """
        Returns
        -------
        - list(str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DomainReceivedPasswordList'])
    @DomainReceivedPasswordList.setter
    def DomainReceivedPasswordList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DomainReceivedPasswordList'], value)

    @property
    def DomainTransmitPassword(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DomainTransmitPassword'])
    @DomainTransmitPassword.setter
    def DomainTransmitPassword(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DomainTransmitPassword'], value)

    @property
    def EnableAttached(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAttached'])
    @EnableAttached.setter
    def EnableAttached(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAttached'], value)

    @property
    def EnableAutoLoopback(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAutoLoopback'])
    @EnableAutoLoopback.setter
    def EnableAutoLoopback(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAutoLoopback'], value)

    @property
    def EnableDiscardLearnedLsps(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDiscardLearnedLsps'])
    @EnableDiscardLearnedLsps.setter
    def EnableDiscardLearnedLsps(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableDiscardLearnedLsps'], value)

    @property
    def EnableHelloPadding(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableHelloPadding'])
    @EnableHelloPadding.setter
    def EnableHelloPadding(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableHelloPadding'], value)

    @property
    def EnableHitlessRestart(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableHitlessRestart'])
    @EnableHitlessRestart.setter
    def EnableHitlessRestart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableHitlessRestart'], value)

    @property
    def EnableHostName(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableHostName'])
    @EnableHostName.setter
    def EnableHostName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableHostName'], value)

    @property
    def EnableIgnoreMtPortCapability(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableIgnoreMtPortCapability'])
    @EnableIgnoreMtPortCapability.setter
    def EnableIgnoreMtPortCapability(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableIgnoreMtPortCapability'], value)

    @property
    def EnableIgnoreRecvMd5(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableIgnoreRecvMd5'])
    @EnableIgnoreRecvMd5.setter
    def EnableIgnoreRecvMd5(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableIgnoreRecvMd5'], value)

    @property
    def EnableMtIpv6(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMtIpv6'])
    @EnableMtIpv6.setter
    def EnableMtIpv6(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMtIpv6'], value)

    @property
    def EnableMtuProbe(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMtuProbe'])
    @EnableMtuProbe.setter
    def EnableMtuProbe(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMtuProbe'], value)

    @property
    def EnableMultiTopology(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMultiTopology'])
    @EnableMultiTopology.setter
    def EnableMultiTopology(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMultiTopology'], value)

    @property
    def EnableOverloaded(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableOverloaded'])
    @EnableOverloaded.setter
    def EnableOverloaded(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableOverloaded'], value)

    @property
    def EnablePartitionRepair(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePartitionRepair'])
    @EnablePartitionRepair.setter
    def EnablePartitionRepair(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePartitionRepair'], value)

    @property
    def EnableTrillOam(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableTrillOam'])
    @EnableTrillOam.setter
    def EnableTrillOam(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableTrillOam'], value)

    @property
    def EnableWideMetric(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableWideMetric'])
    @EnableWideMetric.setter
    def EnableWideMetric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableWideMetric'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def FTagValue(self):
        """DEPRECATED 
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FTagValue'])
    @FTagValue.setter
    def FTagValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FTagValue'], value)

    @property
    def FilterIpv4MulticastTlvs(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FilterIpv4MulticastTlvs'])
    @FilterIpv4MulticastTlvs.setter
    def FilterIpv4MulticastTlvs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FilterIpv4MulticastTlvs'], value)

    @property
    def FilterIpv6MulticastTlvs(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FilterIpv6MulticastTlvs'])
    @FilterIpv6MulticastTlvs.setter
    def FilterIpv6MulticastTlvs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FilterIpv6MulticastTlvs'], value)

    @property
    def FilterLearnedIpv4Prefixes(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FilterLearnedIpv4Prefixes'])
    @FilterLearnedIpv4Prefixes.setter
    def FilterLearnedIpv4Prefixes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FilterLearnedIpv4Prefixes'], value)

    @property
    def FilterLearnedIpv6Prefixes(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FilterLearnedIpv6Prefixes'])
    @FilterLearnedIpv6Prefixes.setter
    def FilterLearnedIpv6Prefixes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FilterLearnedIpv6Prefixes'], value)

    @property
    def FilterLearnedRbridges(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FilterLearnedRbridges'])
    @FilterLearnedRbridges.setter
    def FilterLearnedRbridges(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FilterLearnedRbridges'], value)

    @property
    def FilterLearnedSpbRbridges(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FilterLearnedSpbRbridges'])
    @FilterLearnedSpbRbridges.setter
    def FilterLearnedSpbRbridges(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FilterLearnedSpbRbridges'], value)

    @property
    def FilterLearnedTrillMacUnicast(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FilterLearnedTrillMacUnicast'])
    @FilterLearnedTrillMacUnicast.setter
    def FilterLearnedTrillMacUnicast(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FilterLearnedTrillMacUnicast'], value)

    @property
    def FilterMacMulticastTlvs(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FilterMacMulticastTlvs'])
    @FilterMacMulticastTlvs.setter
    def FilterMacMulticastTlvs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FilterMacMulticastTlvs'], value)

    @property
    def HostName(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['HostName'])
    @HostName.setter
    def HostName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HostName'], value)

    @property
    def InterLspMgroupPduBurstGap(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterLspMgroupPduBurstGap'])
    @InterLspMgroupPduBurstGap.setter
    def InterLspMgroupPduBurstGap(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterLspMgroupPduBurstGap'], value)

    @property
    def LspLifeTime(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LspLifeTime'])
    @LspLifeTime.setter
    def LspLifeTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LspLifeTime'], value)

    @property
    def LspMaxSize(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LspMaxSize'])
    @LspMaxSize.setter
    def LspMaxSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LspMaxSize'], value)

    @property
    def LspMgroupPduMinTransmissionInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LspMgroupPduMinTransmissionInterval'])
    @LspMgroupPduMinTransmissionInterval.setter
    def LspMgroupPduMinTransmissionInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LspMgroupPduMinTransmissionInterval'], value)

    @property
    def LspRefreshRate(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LspRefreshRate'])
    @LspRefreshRate.setter
    def LspRefreshRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LspRefreshRate'], value)

    @property
    def MaxAreaAddresses(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxAreaAddresses'])
    @MaxAreaAddresses.setter
    def MaxAreaAddresses(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxAreaAddresses'], value)

    @property
    def MaxLspMgroupPdusPerBurst(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxLspMgroupPdusPerBurst'])
    @MaxLspMgroupPdusPerBurst.setter
    def MaxLspMgroupPdusPerBurst(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxLspMgroupPdusPerBurst'], value)

    @property
    def NumberOfMtuProbes(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfMtuProbes'])
    @NumberOfMtuProbes.setter
    def NumberOfMtuProbes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfMtuProbes'], value)

    @property
    def NumberOfMultiDestinationTrees(self):
        """DEPRECATED 
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfMultiDestinationTrees'])
    @NumberOfMultiDestinationTrees.setter
    def NumberOfMultiDestinationTrees(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfMultiDestinationTrees'], value)

    @property
    def OriginatingLspBufSize(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OriginatingLspBufSize'])
    @OriginatingLspBufSize.setter
    def OriginatingLspBufSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OriginatingLspBufSize'], value)

    @property
    def PsnpInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PsnpInterval'])
    @PsnpInterval.setter
    def PsnpInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PsnpInterval'], value)

    @property
    def RestartMode(self):
        """
        Returns
        -------
        - str(normalRouter | restartingRouter | startingRouter | helperRouter): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RestartMode'])
    @RestartMode.setter
    def RestartMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RestartMode'], value)

    @property
    def RestartTime(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RestartTime'])
    @RestartTime.setter
    def RestartTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RestartTime'], value)

    @property
    def RestartVersion(self):
        """
        Returns
        -------
        - str(version3 | version4): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RestartVersion'])
    @RestartVersion.setter
    def RestartVersion(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RestartVersion'], value)

    @property
    def StartFtagValue(self):
        """DEPRECATED 
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartFtagValue'])
    @StartFtagValue.setter
    def StartFtagValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartFtagValue'], value)

    @property
    def SwitchId(self):
        """DEPRECATED 
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SwitchId'])
    @SwitchId.setter
    def SwitchId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SwitchId'], value)

    @property
    def SwitchIdPriority(self):
        """DEPRECATED 
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SwitchIdPriority'])
    @SwitchIdPriority.setter
    def SwitchIdPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SwitchIdPriority'], value)

    @property
    def SystemId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SystemId'])
    @SystemId.setter
    def SystemId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SystemId'], value)

    @property
    def TeEnable(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeEnable'])
    @TeEnable.setter
    def TeEnable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeEnable'], value)

    @property
    def TeRouterId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeRouterId'])
    @TeRouterId.setter
    def TeRouterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeRouterId'], value)

    @property
    def TrafficGroupId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficGroupId'])
    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficGroupId'], value)

    def update(self, AreaAddressList=None, AreaAuthType=None, AreaReceivedPasswordList=None, AreaTransmitPassword=None, BroadcastRootPriority=None, CapabilityRouterId=None, DeviceId=None, DevicePriority=None, DomainAuthType=None, DomainReceivedPasswordList=None, DomainTransmitPassword=None, EnableAttached=None, EnableAutoLoopback=None, EnableDiscardLearnedLsps=None, EnableHelloPadding=None, EnableHitlessRestart=None, EnableHostName=None, EnableIgnoreMtPortCapability=None, EnableIgnoreRecvMd5=None, EnableMtIpv6=None, EnableMtuProbe=None, EnableMultiTopology=None, EnableOverloaded=None, EnablePartitionRepair=None, EnableTrillOam=None, EnableWideMetric=None, Enabled=None, FTagValue=None, FilterIpv4MulticastTlvs=None, FilterIpv6MulticastTlvs=None, FilterLearnedIpv4Prefixes=None, FilterLearnedIpv6Prefixes=None, FilterLearnedRbridges=None, FilterLearnedSpbRbridges=None, FilterLearnedTrillMacUnicast=None, FilterMacMulticastTlvs=None, HostName=None, InterLspMgroupPduBurstGap=None, LspLifeTime=None, LspMaxSize=None, LspMgroupPduMinTransmissionInterval=None, LspRefreshRate=None, MaxAreaAddresses=None, MaxLspMgroupPdusPerBurst=None, NumberOfMtuProbes=None, NumberOfMultiDestinationTrees=None, OriginatingLspBufSize=None, PsnpInterval=None, RestartMode=None, RestartTime=None, RestartVersion=None, StartFtagValue=None, SwitchId=None, SwitchIdPriority=None, SystemId=None, TeEnable=None, TeRouterId=None, TrafficGroupId=None):
        """Updates router resource on the server.

        Args
        ----
        - AreaAddressList (list(str)): 
        - AreaAuthType (str(none | password | md5)): 
        - AreaReceivedPasswordList (list(str)): 
        - AreaTransmitPassword (str): 
        - BroadcastRootPriority (number): 
        - CapabilityRouterId (str): 
        - DeviceId (number): 
        - DevicePriority (number): 
        - DomainAuthType (str(none | password | md5)): 
        - DomainReceivedPasswordList (list(str)): 
        - DomainTransmitPassword (str): 
        - EnableAttached (bool): 
        - EnableAutoLoopback (bool): 
        - EnableDiscardLearnedLsps (bool): 
        - EnableHelloPadding (bool): 
        - EnableHitlessRestart (bool): 
        - EnableHostName (bool): 
        - EnableIgnoreMtPortCapability (bool): 
        - EnableIgnoreRecvMd5 (bool): 
        - EnableMtIpv6 (bool): 
        - EnableMtuProbe (bool): 
        - EnableMultiTopology (bool): 
        - EnableOverloaded (bool): 
        - EnablePartitionRepair (bool): 
        - EnableTrillOam (bool): 
        - EnableWideMetric (bool): 
        - Enabled (bool): 
        - FTagValue (number): 
        - FilterIpv4MulticastTlvs (bool): 
        - FilterIpv6MulticastTlvs (bool): 
        - FilterLearnedIpv4Prefixes (bool): 
        - FilterLearnedIpv6Prefixes (bool): 
        - FilterLearnedRbridges (bool): 
        - FilterLearnedSpbRbridges (bool): 
        - FilterLearnedTrillMacUnicast (bool): 
        - FilterMacMulticastTlvs (bool): 
        - HostName (str): 
        - InterLspMgroupPduBurstGap (number): 
        - LspLifeTime (number): 
        - LspMaxSize (number): 
        - LspMgroupPduMinTransmissionInterval (number): 
        - LspRefreshRate (number): 
        - MaxAreaAddresses (number): 
        - MaxLspMgroupPdusPerBurst (number): 
        - NumberOfMtuProbes (number): 
        - NumberOfMultiDestinationTrees (number): 
        - OriginatingLspBufSize (number): 
        - PsnpInterval (number): 
        - RestartMode (str(normalRouter | restartingRouter | startingRouter | helperRouter)): 
        - RestartTime (number): 
        - RestartVersion (str(version3 | version4)): 
        - StartFtagValue (number): 
        - SwitchId (number): 
        - SwitchIdPriority (number): 
        - SystemId (str): 
        - TeEnable (bool): 
        - TeRouterId (str): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AreaAddressList=None, AreaAuthType=None, AreaReceivedPasswordList=None, AreaTransmitPassword=None, BroadcastRootPriority=None, CapabilityRouterId=None, DeviceId=None, DevicePriority=None, DomainAuthType=None, DomainReceivedPasswordList=None, DomainTransmitPassword=None, EnableAttached=None, EnableAutoLoopback=None, EnableDiscardLearnedLsps=None, EnableHelloPadding=None, EnableHitlessRestart=None, EnableHostName=None, EnableIgnoreMtPortCapability=None, EnableIgnoreRecvMd5=None, EnableMtIpv6=None, EnableMtuProbe=None, EnableMultiTopology=None, EnableOverloaded=None, EnablePartitionRepair=None, EnableTrillOam=None, EnableWideMetric=None, Enabled=None, FTagValue=None, FilterIpv4MulticastTlvs=None, FilterIpv6MulticastTlvs=None, FilterLearnedIpv4Prefixes=None, FilterLearnedIpv6Prefixes=None, FilterLearnedRbridges=None, FilterLearnedSpbRbridges=None, FilterLearnedTrillMacUnicast=None, FilterMacMulticastTlvs=None, HostName=None, InterLspMgroupPduBurstGap=None, LspLifeTime=None, LspMaxSize=None, LspMgroupPduMinTransmissionInterval=None, LspRefreshRate=None, MaxAreaAddresses=None, MaxLspMgroupPdusPerBurst=None, NumberOfMtuProbes=None, NumberOfMultiDestinationTrees=None, OriginatingLspBufSize=None, PsnpInterval=None, RestartMode=None, RestartTime=None, RestartVersion=None, StartFtagValue=None, SwitchId=None, SwitchIdPriority=None, SystemId=None, TeEnable=None, TeRouterId=None, TrafficGroupId=None):
        """Adds a new router resource on the server and adds it to the container.

        Args
        ----
        - AreaAddressList (list(str)): 
        - AreaAuthType (str(none | password | md5)): 
        - AreaReceivedPasswordList (list(str)): 
        - AreaTransmitPassword (str): 
        - BroadcastRootPriority (number): 
        - CapabilityRouterId (str): 
        - DeviceId (number): 
        - DevicePriority (number): 
        - DomainAuthType (str(none | password | md5)): 
        - DomainReceivedPasswordList (list(str)): 
        - DomainTransmitPassword (str): 
        - EnableAttached (bool): 
        - EnableAutoLoopback (bool): 
        - EnableDiscardLearnedLsps (bool): 
        - EnableHelloPadding (bool): 
        - EnableHitlessRestart (bool): 
        - EnableHostName (bool): 
        - EnableIgnoreMtPortCapability (bool): 
        - EnableIgnoreRecvMd5 (bool): 
        - EnableMtIpv6 (bool): 
        - EnableMtuProbe (bool): 
        - EnableMultiTopology (bool): 
        - EnableOverloaded (bool): 
        - EnablePartitionRepair (bool): 
        - EnableTrillOam (bool): 
        - EnableWideMetric (bool): 
        - Enabled (bool): 
        - FTagValue (number): 
        - FilterIpv4MulticastTlvs (bool): 
        - FilterIpv6MulticastTlvs (bool): 
        - FilterLearnedIpv4Prefixes (bool): 
        - FilterLearnedIpv6Prefixes (bool): 
        - FilterLearnedRbridges (bool): 
        - FilterLearnedSpbRbridges (bool): 
        - FilterLearnedTrillMacUnicast (bool): 
        - FilterMacMulticastTlvs (bool): 
        - HostName (str): 
        - InterLspMgroupPduBurstGap (number): 
        - LspLifeTime (number): 
        - LspMaxSize (number): 
        - LspMgroupPduMinTransmissionInterval (number): 
        - LspRefreshRate (number): 
        - MaxAreaAddresses (number): 
        - MaxLspMgroupPdusPerBurst (number): 
        - NumberOfMtuProbes (number): 
        - NumberOfMultiDestinationTrees (number): 
        - OriginatingLspBufSize (number): 
        - PsnpInterval (number): 
        - RestartMode (str(normalRouter | restartingRouter | startingRouter | helperRouter)): 
        - RestartTime (number): 
        - RestartVersion (str(version3 | version4)): 
        - StartFtagValue (number): 
        - SwitchId (number): 
        - SwitchIdPriority (number): 
        - SystemId (str): 
        - TeEnable (bool): 
        - TeRouterId (str): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 

        Returns
        -------
        - self: This instance with all currently retrieved router resources using find and the newly added router resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained router resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AreaAddressList=None, AreaAuthType=None, AreaReceivedPasswordList=None, AreaTransmitPassword=None, BroadcastRootPriority=None, CapabilityRouterId=None, DeviceId=None, DevicePriority=None, DomainAuthType=None, DomainReceivedPasswordList=None, DomainTransmitPassword=None, EnableAttached=None, EnableAutoLoopback=None, EnableDiscardLearnedLsps=None, EnableHelloPadding=None, EnableHitlessRestart=None, EnableHostName=None, EnableIgnoreMtPortCapability=None, EnableIgnoreRecvMd5=None, EnableMtIpv6=None, EnableMtuProbe=None, EnableMultiTopology=None, EnableOverloaded=None, EnablePartitionRepair=None, EnableTrillOam=None, EnableWideMetric=None, Enabled=None, FTagValue=None, FilterIpv4MulticastTlvs=None, FilterIpv6MulticastTlvs=None, FilterLearnedIpv4Prefixes=None, FilterLearnedIpv6Prefixes=None, FilterLearnedRbridges=None, FilterLearnedSpbRbridges=None, FilterLearnedTrillMacUnicast=None, FilterMacMulticastTlvs=None, HostName=None, InterLspMgroupPduBurstGap=None, LspLifeTime=None, LspMaxSize=None, LspMgroupPduMinTransmissionInterval=None, LspRefreshRate=None, MaxAreaAddresses=None, MaxLspMgroupPdusPerBurst=None, NumberOfMtuProbes=None, NumberOfMultiDestinationTrees=None, OriginatingLspBufSize=None, PsnpInterval=None, RestartMode=None, RestartTime=None, RestartVersion=None, StartFtagValue=None, SwitchId=None, SwitchIdPriority=None, SystemId=None, TeEnable=None, TeRouterId=None, TrafficGroupId=None):
        """Finds and retrieves router resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve router resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all router resources from the server.

        Args
        ----
        - AreaAddressList (list(str)): 
        - AreaAuthType (str(none | password | md5)): 
        - AreaReceivedPasswordList (list(str)): 
        - AreaTransmitPassword (str): 
        - BroadcastRootPriority (number): 
        - CapabilityRouterId (str): 
        - DeviceId (number): 
        - DevicePriority (number): 
        - DomainAuthType (str(none | password | md5)): 
        - DomainReceivedPasswordList (list(str)): 
        - DomainTransmitPassword (str): 
        - EnableAttached (bool): 
        - EnableAutoLoopback (bool): 
        - EnableDiscardLearnedLsps (bool): 
        - EnableHelloPadding (bool): 
        - EnableHitlessRestart (bool): 
        - EnableHostName (bool): 
        - EnableIgnoreMtPortCapability (bool): 
        - EnableIgnoreRecvMd5 (bool): 
        - EnableMtIpv6 (bool): 
        - EnableMtuProbe (bool): 
        - EnableMultiTopology (bool): 
        - EnableOverloaded (bool): 
        - EnablePartitionRepair (bool): 
        - EnableTrillOam (bool): 
        - EnableWideMetric (bool): 
        - Enabled (bool): 
        - FTagValue (number): 
        - FilterIpv4MulticastTlvs (bool): 
        - FilterIpv6MulticastTlvs (bool): 
        - FilterLearnedIpv4Prefixes (bool): 
        - FilterLearnedIpv6Prefixes (bool): 
        - FilterLearnedRbridges (bool): 
        - FilterLearnedSpbRbridges (bool): 
        - FilterLearnedTrillMacUnicast (bool): 
        - FilterMacMulticastTlvs (bool): 
        - HostName (str): 
        - InterLspMgroupPduBurstGap (number): 
        - LspLifeTime (number): 
        - LspMaxSize (number): 
        - LspMgroupPduMinTransmissionInterval (number): 
        - LspRefreshRate (number): 
        - MaxAreaAddresses (number): 
        - MaxLspMgroupPdusPerBurst (number): 
        - NumberOfMtuProbes (number): 
        - NumberOfMultiDestinationTrees (number): 
        - OriginatingLspBufSize (number): 
        - PsnpInterval (number): 
        - RestartMode (str(normalRouter | restartingRouter | startingRouter | helperRouter)): 
        - RestartTime (number): 
        - RestartVersion (str(version3 | version4)): 
        - StartFtagValue (number): 
        - SwitchId (number): 
        - SwitchIdPriority (number): 
        - SystemId (str): 
        - TeEnable (bool): 
        - TeRouterId (str): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 

        Returns
        -------
        - self: This instance with matching router resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of router data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the router resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def RefreshLearnedInformation(self):
        """Executes the refreshLearnedInformation operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshLearnedInformation', payload=payload, response_object=None)

    def SendTrillOamPing(self):
        """Executes the sendTrillOamPing operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('sendTrillOamPing', payload=payload, response_object=None)
