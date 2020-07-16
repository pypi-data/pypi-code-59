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


class Interface(Base):
    """
    The Interface class encapsulates a list of interface resources that are managed by the user.
    A list of resources can be retrieved from the server using the Interface.find() method.
    The list can be managed by using the Interface.add() and Interface.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'interface'
    _SDM_ATT_MAP = {
        'AddressFamily': 'addressFamily',
        'AutoPickUpstreamNeighbor': 'autoPickUpstreamNeighbor',
        'BootstrapEnable': 'bootstrapEnable',
        'BootstrapHashMaskLen': 'bootstrapHashMaskLen',
        'BootstrapInterval': 'bootstrapInterval',
        'BootstrapPriority': 'bootstrapPriority',
        'BootstrapTimeout': 'bootstrapTimeout',
        'DisableTriggeredHello': 'disableTriggeredHello',
        'DiscardDataMdtTlv': 'discardDataMdtTlv',
        'DiscardLearnedRpInfo': 'discardLearnedRpInfo',
        'EnableBfdRegistration': 'enableBfdRegistration',
        'EnableV4MappedV6Address': 'enableV4MappedV6Address',
        'Enabled': 'enabled',
        'ForceSemanticFragmentation': 'forceSemanticFragmentation',
        'GenerationIdMode': 'generationIdMode',
        'HelloHoldTime': 'helloHoldTime',
        'HelloInterval': 'helloInterval',
        'InterfaceId': 'interfaceId',
        'InterfaceIndex': 'interfaceIndex',
        'InterfaceType': 'interfaceType',
        'Interfaces': 'interfaces',
        'IsRefreshRpSetComplete': 'isRefreshRpSetComplete',
        'LanPruneDelay': 'lanPruneDelay',
        'LanPruneDelayTBit': 'lanPruneDelayTBit',
        'LearnSelectedRpSet': 'learnSelectedRpSet',
        'OverrideInterval': 'overrideInterval',
        'SendBiDirCapableOption': 'sendBiDirCapableOption',
        'SendGenIdOption': 'sendGenIdOption',
        'SendHelloLanPruneDelayOption': 'sendHelloLanPruneDelayOption',
        'ShowSelectedRpSetOnly': 'showSelectedRpSetOnly',
        'SupportUnicastBootstrap': 'supportUnicastBootstrap',
        'TrafficGroupId': 'trafficGroupId',
        'TriggeredHelloDelay': 'triggeredHelloDelay',
        'UpstreamNeighbor': 'upstreamNeighbor',
    }

    def __init__(self, parent):
        super(Interface, self).__init__(parent)

    @property
    def CrpRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.crprange_8776c1167223a7b7e2074526e0a79818.CrpRange): An instance of the CrpRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.crprange_8776c1167223a7b7e2074526e0a79818 import CrpRange
        return CrpRange(self)

    @property
    def DataMdt(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.datamdt_231fc24d0d8504f2e83eec8bb5851dc9.DataMdt): An instance of the DataMdt class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.datamdt_231fc24d0d8504f2e83eec8bb5851dc9 import DataMdt
        return DataMdt(self)

    @property
    def JoinPrune(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.joinprune_4a760ec43de3757183b31a22a48ae945.JoinPrune): An instance of the JoinPrune class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.joinprune_4a760ec43de3757183b31a22a48ae945 import JoinPrune
        return JoinPrune(self)

    @property
    def LearnedBsrInfo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedbsrinfo_5140858f0d0b7f27d3f2dbaa1f587379.LearnedBsrInfo): An instance of the LearnedBsrInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedbsrinfo_5140858f0d0b7f27d3f2dbaa1f587379 import LearnedBsrInfo
        return LearnedBsrInfo(self)

    @property
    def LearnedCrpInfo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedcrpinfo_8687e4b7e63bedfb41ebdefefced4f65.LearnedCrpInfo): An instance of the LearnedCrpInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedcrpinfo_8687e4b7e63bedfb41ebdefefced4f65 import LearnedCrpInfo
        return LearnedCrpInfo(self)

    @property
    def LearnedMdtInfo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedmdtinfo_99de95f4da54d8e12122404426cb53d7.LearnedMdtInfo): An instance of the LearnedMdtInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedmdtinfo_99de95f4da54d8e12122404426cb53d7 import LearnedMdtInfo
        return LearnedMdtInfo(self)

    @property
    def Source(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.source_a7e9b6299ed6647a14c4205308be5c75.Source): An instance of the Source class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.source_a7e9b6299ed6647a14c4205308be5c75 import Source
        return Source(self)

    @property
    def AddressFamily(self):
        """
        Returns
        -------
        - str(ipv4 | ipv6): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddressFamily'])
    @AddressFamily.setter
    def AddressFamily(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AddressFamily'], value)

    @property
    def AutoPickUpstreamNeighbor(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutoPickUpstreamNeighbor'])
    @AutoPickUpstreamNeighbor.setter
    def AutoPickUpstreamNeighbor(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AutoPickUpstreamNeighbor'], value)

    @property
    def BootstrapEnable(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BootstrapEnable'])
    @BootstrapEnable.setter
    def BootstrapEnable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BootstrapEnable'], value)

    @property
    def BootstrapHashMaskLen(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BootstrapHashMaskLen'])
    @BootstrapHashMaskLen.setter
    def BootstrapHashMaskLen(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BootstrapHashMaskLen'], value)

    @property
    def BootstrapInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BootstrapInterval'])
    @BootstrapInterval.setter
    def BootstrapInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BootstrapInterval'], value)

    @property
    def BootstrapPriority(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BootstrapPriority'])
    @BootstrapPriority.setter
    def BootstrapPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BootstrapPriority'], value)

    @property
    def BootstrapTimeout(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BootstrapTimeout'])
    @BootstrapTimeout.setter
    def BootstrapTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BootstrapTimeout'], value)

    @property
    def DisableTriggeredHello(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DisableTriggeredHello'])
    @DisableTriggeredHello.setter
    def DisableTriggeredHello(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DisableTriggeredHello'], value)

    @property
    def DiscardDataMdtTlv(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DiscardDataMdtTlv'])
    @DiscardDataMdtTlv.setter
    def DiscardDataMdtTlv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DiscardDataMdtTlv'], value)

    @property
    def DiscardLearnedRpInfo(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DiscardLearnedRpInfo'])
    @DiscardLearnedRpInfo.setter
    def DiscardLearnedRpInfo(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DiscardLearnedRpInfo'], value)

    @property
    def EnableBfdRegistration(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableBfdRegistration'])
    @EnableBfdRegistration.setter
    def EnableBfdRegistration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableBfdRegistration'], value)

    @property
    def EnableV4MappedV6Address(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableV4MappedV6Address'])
    @EnableV4MappedV6Address.setter
    def EnableV4MappedV6Address(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableV4MappedV6Address'], value)

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
    def ForceSemanticFragmentation(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ForceSemanticFragmentation'])
    @ForceSemanticFragmentation.setter
    def ForceSemanticFragmentation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ForceSemanticFragmentation'], value)

    @property
    def GenerationIdMode(self):
        """
        Returns
        -------
        - str(incremental | random | constant): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['GenerationIdMode'])
    @GenerationIdMode.setter
    def GenerationIdMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GenerationIdMode'], value)

    @property
    def HelloHoldTime(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['HelloHoldTime'])
    @HelloHoldTime.setter
    def HelloHoldTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HelloHoldTime'], value)

    @property
    def HelloInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['HelloInterval'])
    @HelloInterval.setter
    def HelloInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HelloInterval'], value)

    @property
    def InterfaceId(self):
        """DEPRECATED 
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceId'])
    @InterfaceId.setter
    def InterfaceId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceId'], value)

    @property
    def InterfaceIndex(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceIndex'])
    @InterfaceIndex.setter
    def InterfaceIndex(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceIndex'], value)

    @property
    def InterfaceType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceType'])
    @InterfaceType.setter
    def InterfaceType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceType'], value)

    @property
    def Interfaces(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Interfaces'])
    @Interfaces.setter
    def Interfaces(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Interfaces'], value)

    @property
    def IsRefreshRpSetComplete(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsRefreshRpSetComplete'])

    @property
    def LanPruneDelay(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LanPruneDelay'])
    @LanPruneDelay.setter
    def LanPruneDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LanPruneDelay'], value)

    @property
    def LanPruneDelayTBit(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LanPruneDelayTBit'])
    @LanPruneDelayTBit.setter
    def LanPruneDelayTBit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LanPruneDelayTBit'], value)

    @property
    def LearnSelectedRpSet(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearnSelectedRpSet'])
    @LearnSelectedRpSet.setter
    def LearnSelectedRpSet(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LearnSelectedRpSet'], value)

    @property
    def OverrideInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OverrideInterval'])
    @OverrideInterval.setter
    def OverrideInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OverrideInterval'], value)

    @property
    def SendBiDirCapableOption(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendBiDirCapableOption'])
    @SendBiDirCapableOption.setter
    def SendBiDirCapableOption(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendBiDirCapableOption'], value)

    @property
    def SendGenIdOption(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendGenIdOption'])
    @SendGenIdOption.setter
    def SendGenIdOption(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendGenIdOption'], value)

    @property
    def SendHelloLanPruneDelayOption(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendHelloLanPruneDelayOption'])
    @SendHelloLanPruneDelayOption.setter
    def SendHelloLanPruneDelayOption(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendHelloLanPruneDelayOption'], value)

    @property
    def ShowSelectedRpSetOnly(self):
        """DEPRECATED 
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShowSelectedRpSetOnly'])
    @ShowSelectedRpSetOnly.setter
    def ShowSelectedRpSetOnly(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ShowSelectedRpSetOnly'], value)

    @property
    def SupportUnicastBootstrap(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportUnicastBootstrap'])
    @SupportUnicastBootstrap.setter
    def SupportUnicastBootstrap(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportUnicastBootstrap'], value)

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

    @property
    def TriggeredHelloDelay(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TriggeredHelloDelay'])
    @TriggeredHelloDelay.setter
    def TriggeredHelloDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TriggeredHelloDelay'], value)

    @property
    def UpstreamNeighbor(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamNeighbor'])
    @UpstreamNeighbor.setter
    def UpstreamNeighbor(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamNeighbor'], value)

    def update(self, AddressFamily=None, AutoPickUpstreamNeighbor=None, BootstrapEnable=None, BootstrapHashMaskLen=None, BootstrapInterval=None, BootstrapPriority=None, BootstrapTimeout=None, DisableTriggeredHello=None, DiscardDataMdtTlv=None, DiscardLearnedRpInfo=None, EnableBfdRegistration=None, EnableV4MappedV6Address=None, Enabled=None, ForceSemanticFragmentation=None, GenerationIdMode=None, HelloHoldTime=None, HelloInterval=None, InterfaceId=None, InterfaceIndex=None, InterfaceType=None, Interfaces=None, LanPruneDelay=None, LanPruneDelayTBit=None, LearnSelectedRpSet=None, OverrideInterval=None, SendBiDirCapableOption=None, SendGenIdOption=None, SendHelloLanPruneDelayOption=None, ShowSelectedRpSetOnly=None, SupportUnicastBootstrap=None, TrafficGroupId=None, TriggeredHelloDelay=None, UpstreamNeighbor=None):
        """Updates interface resource on the server.

        Args
        ----
        - AddressFamily (str(ipv4 | ipv6)): 
        - AutoPickUpstreamNeighbor (bool): 
        - BootstrapEnable (bool): 
        - BootstrapHashMaskLen (number): 
        - BootstrapInterval (number): 
        - BootstrapPriority (number): 
        - BootstrapTimeout (number): 
        - DisableTriggeredHello (bool): 
        - DiscardDataMdtTlv (bool): 
        - DiscardLearnedRpInfo (bool): 
        - EnableBfdRegistration (bool): 
        - EnableV4MappedV6Address (bool): 
        - Enabled (bool): 
        - ForceSemanticFragmentation (bool): 
        - GenerationIdMode (str(incremental | random | constant)): 
        - HelloHoldTime (number): 
        - HelloInterval (number): 
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - InterfaceIndex (number): 
        - InterfaceType (str): 
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): 
        - LanPruneDelay (number): 
        - LanPruneDelayTBit (bool): 
        - LearnSelectedRpSet (bool): 
        - OverrideInterval (number): 
        - SendBiDirCapableOption (bool): 
        - SendGenIdOption (bool): 
        - SendHelloLanPruneDelayOption (bool): 
        - ShowSelectedRpSetOnly (bool): 
        - SupportUnicastBootstrap (bool): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 
        - TriggeredHelloDelay (number): 
        - UpstreamNeighbor (str): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AddressFamily=None, AutoPickUpstreamNeighbor=None, BootstrapEnable=None, BootstrapHashMaskLen=None, BootstrapInterval=None, BootstrapPriority=None, BootstrapTimeout=None, DisableTriggeredHello=None, DiscardDataMdtTlv=None, DiscardLearnedRpInfo=None, EnableBfdRegistration=None, EnableV4MappedV6Address=None, Enabled=None, ForceSemanticFragmentation=None, GenerationIdMode=None, HelloHoldTime=None, HelloInterval=None, InterfaceId=None, InterfaceIndex=None, InterfaceType=None, Interfaces=None, LanPruneDelay=None, LanPruneDelayTBit=None, LearnSelectedRpSet=None, OverrideInterval=None, SendBiDirCapableOption=None, SendGenIdOption=None, SendHelloLanPruneDelayOption=None, ShowSelectedRpSetOnly=None, SupportUnicastBootstrap=None, TrafficGroupId=None, TriggeredHelloDelay=None, UpstreamNeighbor=None):
        """Adds a new interface resource on the server and adds it to the container.

        Args
        ----
        - AddressFamily (str(ipv4 | ipv6)): 
        - AutoPickUpstreamNeighbor (bool): 
        - BootstrapEnable (bool): 
        - BootstrapHashMaskLen (number): 
        - BootstrapInterval (number): 
        - BootstrapPriority (number): 
        - BootstrapTimeout (number): 
        - DisableTriggeredHello (bool): 
        - DiscardDataMdtTlv (bool): 
        - DiscardLearnedRpInfo (bool): 
        - EnableBfdRegistration (bool): 
        - EnableV4MappedV6Address (bool): 
        - Enabled (bool): 
        - ForceSemanticFragmentation (bool): 
        - GenerationIdMode (str(incremental | random | constant)): 
        - HelloHoldTime (number): 
        - HelloInterval (number): 
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - InterfaceIndex (number): 
        - InterfaceType (str): 
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): 
        - LanPruneDelay (number): 
        - LanPruneDelayTBit (bool): 
        - LearnSelectedRpSet (bool): 
        - OverrideInterval (number): 
        - SendBiDirCapableOption (bool): 
        - SendGenIdOption (bool): 
        - SendHelloLanPruneDelayOption (bool): 
        - ShowSelectedRpSetOnly (bool): 
        - SupportUnicastBootstrap (bool): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 
        - TriggeredHelloDelay (number): 
        - UpstreamNeighbor (str): 

        Returns
        -------
        - self: This instance with all currently retrieved interface resources using find and the newly added interface resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained interface resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AddressFamily=None, AutoPickUpstreamNeighbor=None, BootstrapEnable=None, BootstrapHashMaskLen=None, BootstrapInterval=None, BootstrapPriority=None, BootstrapTimeout=None, DisableTriggeredHello=None, DiscardDataMdtTlv=None, DiscardLearnedRpInfo=None, EnableBfdRegistration=None, EnableV4MappedV6Address=None, Enabled=None, ForceSemanticFragmentation=None, GenerationIdMode=None, HelloHoldTime=None, HelloInterval=None, InterfaceId=None, InterfaceIndex=None, InterfaceType=None, Interfaces=None, IsRefreshRpSetComplete=None, LanPruneDelay=None, LanPruneDelayTBit=None, LearnSelectedRpSet=None, OverrideInterval=None, SendBiDirCapableOption=None, SendGenIdOption=None, SendHelloLanPruneDelayOption=None, ShowSelectedRpSetOnly=None, SupportUnicastBootstrap=None, TrafficGroupId=None, TriggeredHelloDelay=None, UpstreamNeighbor=None):
        """Finds and retrieves interface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve interface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all interface resources from the server.

        Args
        ----
        - AddressFamily (str(ipv4 | ipv6)): 
        - AutoPickUpstreamNeighbor (bool): 
        - BootstrapEnable (bool): 
        - BootstrapHashMaskLen (number): 
        - BootstrapInterval (number): 
        - BootstrapPriority (number): 
        - BootstrapTimeout (number): 
        - DisableTriggeredHello (bool): 
        - DiscardDataMdtTlv (bool): 
        - DiscardLearnedRpInfo (bool): 
        - EnableBfdRegistration (bool): 
        - EnableV4MappedV6Address (bool): 
        - Enabled (bool): 
        - ForceSemanticFragmentation (bool): 
        - GenerationIdMode (str(incremental | random | constant)): 
        - HelloHoldTime (number): 
        - HelloInterval (number): 
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - InterfaceIndex (number): 
        - InterfaceType (str): 
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): 
        - IsRefreshRpSetComplete (bool): 
        - LanPruneDelay (number): 
        - LanPruneDelayTBit (bool): 
        - LearnSelectedRpSet (bool): 
        - OverrideInterval (number): 
        - SendBiDirCapableOption (bool): 
        - SendGenIdOption (bool): 
        - SendHelloLanPruneDelayOption (bool): 
        - ShowSelectedRpSetOnly (bool): 
        - SupportUnicastBootstrap (bool): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 
        - TriggeredHelloDelay (number): 
        - UpstreamNeighbor (str): 

        Returns
        -------
        - self: This instance with matching interface resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of interface data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the interface resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def GetInterfaceAccessorIfaceList(self):
        """Executes the getInterfaceAccessorIfaceList operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('getInterfaceAccessorIfaceList', payload=payload, response_object=None)

    def RefreshCrpBsrLearnedInfo(self):
        """Executes the refreshCrpBsrLearnedInfo operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshCrpBsrLearnedInfo', payload=payload, response_object=None)
