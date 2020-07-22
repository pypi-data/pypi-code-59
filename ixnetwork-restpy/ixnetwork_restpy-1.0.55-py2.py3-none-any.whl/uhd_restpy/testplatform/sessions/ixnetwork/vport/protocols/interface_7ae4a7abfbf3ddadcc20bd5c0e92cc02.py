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
        'AdvertiseNetworkRange': 'advertiseNetworkRange',
        'AreaId': 'areaId',
        'AuthenticationMethods': 'authenticationMethods',
        'AuthenticationPassword': 'authenticationPassword',
        'BBit': 'bBit',
        'ConnectedToDut': 'connectedToDut',
        'DeadInterval': 'deadInterval',
        'EBit': 'eBit',
        'EnableAdvertiseRouterLsaLoopback': 'enableAdvertiseRouterLsaLoopback',
        'EnableBfdRegistration': 'enableBfdRegistration',
        'EnableFastHello': 'enableFastHello',
        'Enabled': 'enabled',
        'EntryColumn': 'entryColumn',
        'EntryRow': 'entryRow',
        'HelloInterval': 'helloInterval',
        'HelloMultiplier': 'helloMultiplier',
        'InterfaceIndex': 'interfaceIndex',
        'InterfaceIpAddress': 'interfaceIpAddress',
        'InterfaceIpMaskAddress': 'interfaceIpMaskAddress',
        'InterfaceType': 'interfaceType',
        'Interfaces': 'interfaces',
        'IsLearnedInfoRefreshed': 'isLearnedInfoRefreshed',
        'LinkTypes': 'linkTypes',
        'Md5AuthenticationKey': 'md5AuthenticationKey',
        'Md5AuthenticationKeyId': 'md5AuthenticationKeyId',
        'Metric': 'metric',
        'Mtu': 'mtu',
        'NeighborIpAddress': 'neighborIpAddress',
        'NeighborRouterId': 'neighborRouterId',
        'NetworkRangeIp': 'networkRangeIp',
        'NetworkRangeIpByMask': 'networkRangeIpByMask',
        'NetworkRangeIpIncrementBy': 'networkRangeIpIncrementBy',
        'NetworkRangeIpMask': 'networkRangeIpMask',
        'NetworkRangeLinkType': 'networkRangeLinkType',
        'NetworkRangeRouterId': 'networkRangeRouterId',
        'NetworkRangeRouterIdIncrementBy': 'networkRangeRouterIdIncrementBy',
        'NetworkRangeTeEnable': 'networkRangeTeEnable',
        'NetworkRangeTeMaxBandwidth': 'networkRangeTeMaxBandwidth',
        'NetworkRangeTeMetric': 'networkRangeTeMetric',
        'NetworkRangeTeResMaxBandwidth': 'networkRangeTeResMaxBandwidth',
        'NetworkRangeTeUnreservedBwPriority': 'networkRangeTeUnreservedBwPriority',
        'NetworkType': 'networkType',
        'NoOfCols': 'noOfCols',
        'NoOfRows': 'noOfRows',
        'Options': 'options',
        'Priority': 'priority',
        'ProtocolInterface': 'protocolInterface',
        'ShowExternal': 'showExternal',
        'ShowNssa': 'showNssa',
        'TeAdminGroup': 'teAdminGroup',
        'TeEnable': 'teEnable',
        'TeMaxBandwidth': 'teMaxBandwidth',
        'TeMetricLevel': 'teMetricLevel',
        'TeResMaxBandwidth': 'teResMaxBandwidth',
        'TeUnreservedBwPriority': 'teUnreservedBwPriority',
        'ValidateReceivedMtuSize': 'validateReceivedMtuSize',
    }

    def __init__(self, parent):
        super(Interface, self).__init__(parent)

    @property
    def LearnedFilter(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedfilter_eefb8bda61928c41bfe3478f93e66c1f.LearnedFilter): An instance of the LearnedFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedfilter_eefb8bda61928c41bfe3478f93e66c1f import LearnedFilter
        return LearnedFilter(self)._select()

    @property
    def LearnedLsa(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedlsa_f8981275ed1dafbf0040b50e74f8ef42.LearnedLsa): An instance of the LearnedLsa class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedlsa_f8981275ed1dafbf0040b50e74f8ef42 import LearnedLsa
        return LearnedLsa(self)

    @property
    def AdvertiseNetworkRange(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdvertiseNetworkRange'])
    @AdvertiseNetworkRange.setter
    def AdvertiseNetworkRange(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AdvertiseNetworkRange'], value)

    @property
    def AreaId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AreaId'])
    @AreaId.setter
    def AreaId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AreaId'], value)

    @property
    def AuthenticationMethods(self):
        """
        Returns
        -------
        - str(null | password | md5): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AuthenticationMethods'])
    @AuthenticationMethods.setter
    def AuthenticationMethods(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AuthenticationMethods'], value)

    @property
    def AuthenticationPassword(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AuthenticationPassword'])
    @AuthenticationPassword.setter
    def AuthenticationPassword(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AuthenticationPassword'], value)

    @property
    def BBit(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BBit'])
    @BBit.setter
    def BBit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BBit'], value)

    @property
    def ConnectedToDut(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectedToDut'])
    @ConnectedToDut.setter
    def ConnectedToDut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ConnectedToDut'], value)

    @property
    def DeadInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DeadInterval'])
    @DeadInterval.setter
    def DeadInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DeadInterval'], value)

    @property
    def EBit(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EBit'])
    @EBit.setter
    def EBit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EBit'], value)

    @property
    def EnableAdvertiseRouterLsaLoopback(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAdvertiseRouterLsaLoopback'])
    @EnableAdvertiseRouterLsaLoopback.setter
    def EnableAdvertiseRouterLsaLoopback(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAdvertiseRouterLsaLoopback'], value)

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
    def EnableFastHello(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableFastHello'])
    @EnableFastHello.setter
    def EnableFastHello(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableFastHello'], value)

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
    def EntryColumn(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EntryColumn'])
    @EntryColumn.setter
    def EntryColumn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EntryColumn'], value)

    @property
    def EntryRow(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EntryRow'])
    @EntryRow.setter
    def EntryRow(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EntryRow'], value)

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
    def HelloMultiplier(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['HelloMultiplier'])
    @HelloMultiplier.setter
    def HelloMultiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HelloMultiplier'], value)

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
    def InterfaceIpAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceIpAddress'])
    @InterfaceIpAddress.setter
    def InterfaceIpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceIpAddress'], value)

    @property
    def InterfaceIpMaskAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceIpMaskAddress'])
    @InterfaceIpMaskAddress.setter
    def InterfaceIpMaskAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceIpMaskAddress'], value)

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
    def IsLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsLearnedInfoRefreshed'])

    @property
    def LinkTypes(self):
        """
        Returns
        -------
        - str(pointToPoint | transit | stub | virtual): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkTypes'])
    @LinkTypes.setter
    def LinkTypes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkTypes'], value)

    @property
    def Md5AuthenticationKey(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Md5AuthenticationKey'])
    @Md5AuthenticationKey.setter
    def Md5AuthenticationKey(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Md5AuthenticationKey'], value)

    @property
    def Md5AuthenticationKeyId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Md5AuthenticationKeyId'])
    @Md5AuthenticationKeyId.setter
    def Md5AuthenticationKeyId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Md5AuthenticationKeyId'], value)

    @property
    def Metric(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Metric'])
    @Metric.setter
    def Metric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Metric'], value)

    @property
    def Mtu(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mtu'])
    @Mtu.setter
    def Mtu(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mtu'], value)

    @property
    def NeighborIpAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NeighborIpAddress'])
    @NeighborIpAddress.setter
    def NeighborIpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NeighborIpAddress'], value)

    @property
    def NeighborRouterId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NeighborRouterId'])
    @NeighborRouterId.setter
    def NeighborRouterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NeighborRouterId'], value)

    @property
    def NetworkRangeIp(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkRangeIp'])
    @NetworkRangeIp.setter
    def NetworkRangeIp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkRangeIp'], value)

    @property
    def NetworkRangeIpByMask(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkRangeIpByMask'])
    @NetworkRangeIpByMask.setter
    def NetworkRangeIpByMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkRangeIpByMask'], value)

    @property
    def NetworkRangeIpIncrementBy(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkRangeIpIncrementBy'])
    @NetworkRangeIpIncrementBy.setter
    def NetworkRangeIpIncrementBy(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkRangeIpIncrementBy'], value)

    @property
    def NetworkRangeIpMask(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkRangeIpMask'])
    @NetworkRangeIpMask.setter
    def NetworkRangeIpMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkRangeIpMask'], value)

    @property
    def NetworkRangeLinkType(self):
        """
        Returns
        -------
        - str(broadcast | pointToPoint): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkRangeLinkType'])
    @NetworkRangeLinkType.setter
    def NetworkRangeLinkType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkRangeLinkType'], value)

    @property
    def NetworkRangeRouterId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkRangeRouterId'])
    @NetworkRangeRouterId.setter
    def NetworkRangeRouterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkRangeRouterId'], value)

    @property
    def NetworkRangeRouterIdIncrementBy(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkRangeRouterIdIncrementBy'])
    @NetworkRangeRouterIdIncrementBy.setter
    def NetworkRangeRouterIdIncrementBy(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkRangeRouterIdIncrementBy'], value)

    @property
    def NetworkRangeTeEnable(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkRangeTeEnable'])
    @NetworkRangeTeEnable.setter
    def NetworkRangeTeEnable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkRangeTeEnable'], value)

    @property
    def NetworkRangeTeMaxBandwidth(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkRangeTeMaxBandwidth'])
    @NetworkRangeTeMaxBandwidth.setter
    def NetworkRangeTeMaxBandwidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkRangeTeMaxBandwidth'], value)

    @property
    def NetworkRangeTeMetric(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkRangeTeMetric'])
    @NetworkRangeTeMetric.setter
    def NetworkRangeTeMetric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkRangeTeMetric'], value)

    @property
    def NetworkRangeTeResMaxBandwidth(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkRangeTeResMaxBandwidth'])
    @NetworkRangeTeResMaxBandwidth.setter
    def NetworkRangeTeResMaxBandwidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkRangeTeResMaxBandwidth'], value)

    @property
    def NetworkRangeTeUnreservedBwPriority(self):
        """
        Returns
        -------
        - dict(arg1:number,arg2:number,arg3:number,arg4:number,arg5:number,arg6:number,arg7:number,arg8:number): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkRangeTeUnreservedBwPriority'])
    @NetworkRangeTeUnreservedBwPriority.setter
    def NetworkRangeTeUnreservedBwPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkRangeTeUnreservedBwPriority'], value)

    @property
    def NetworkType(self):
        """
        Returns
        -------
        - str(pointToPoint | broadcast | pointToMultipoint): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkType'])
    @NetworkType.setter
    def NetworkType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkType'], value)

    @property
    def NoOfCols(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfCols'])
    @NoOfCols.setter
    def NoOfCols(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfCols'], value)

    @property
    def NoOfRows(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfRows'])
    @NoOfRows.setter
    def NoOfRows(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfRows'], value)

    @property
    def Options(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Options'])
    @Options.setter
    def Options(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Options'], value)

    @property
    def Priority(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Priority'])
    @Priority.setter
    def Priority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Priority'], value)

    @property
    def ProtocolInterface(self):
        """DEPRECATED 
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolInterface'])
    @ProtocolInterface.setter
    def ProtocolInterface(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProtocolInterface'], value)

    @property
    def ShowExternal(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShowExternal'])
    @ShowExternal.setter
    def ShowExternal(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ShowExternal'], value)

    @property
    def ShowNssa(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShowNssa'])
    @ShowNssa.setter
    def ShowNssa(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ShowNssa'], value)

    @property
    def TeAdminGroup(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeAdminGroup'])
    @TeAdminGroup.setter
    def TeAdminGroup(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeAdminGroup'], value)

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
    def TeMaxBandwidth(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeMaxBandwidth'])
    @TeMaxBandwidth.setter
    def TeMaxBandwidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeMaxBandwidth'], value)

    @property
    def TeMetricLevel(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeMetricLevel'])
    @TeMetricLevel.setter
    def TeMetricLevel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeMetricLevel'], value)

    @property
    def TeResMaxBandwidth(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeResMaxBandwidth'])
    @TeResMaxBandwidth.setter
    def TeResMaxBandwidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeResMaxBandwidth'], value)

    @property
    def TeUnreservedBwPriority(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str,arg3:str,arg4:str,arg5:str,arg6:str,arg7:str,arg8:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeUnreservedBwPriority'])
    @TeUnreservedBwPriority.setter
    def TeUnreservedBwPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeUnreservedBwPriority'], value)

    @property
    def ValidateReceivedMtuSize(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ValidateReceivedMtuSize'])
    @ValidateReceivedMtuSize.setter
    def ValidateReceivedMtuSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ValidateReceivedMtuSize'], value)

    def update(self, AdvertiseNetworkRange=None, AreaId=None, AuthenticationMethods=None, AuthenticationPassword=None, BBit=None, ConnectedToDut=None, DeadInterval=None, EBit=None, EnableAdvertiseRouterLsaLoopback=None, EnableBfdRegistration=None, EnableFastHello=None, Enabled=None, EntryColumn=None, EntryRow=None, HelloInterval=None, HelloMultiplier=None, InterfaceIndex=None, InterfaceIpAddress=None, InterfaceIpMaskAddress=None, InterfaceType=None, Interfaces=None, LinkTypes=None, Md5AuthenticationKey=None, Md5AuthenticationKeyId=None, Metric=None, Mtu=None, NeighborIpAddress=None, NeighborRouterId=None, NetworkRangeIp=None, NetworkRangeIpByMask=None, NetworkRangeIpIncrementBy=None, NetworkRangeIpMask=None, NetworkRangeLinkType=None, NetworkRangeRouterId=None, NetworkRangeRouterIdIncrementBy=None, NetworkRangeTeEnable=None, NetworkRangeTeMaxBandwidth=None, NetworkRangeTeMetric=None, NetworkRangeTeResMaxBandwidth=None, NetworkRangeTeUnreservedBwPriority=None, NetworkType=None, NoOfCols=None, NoOfRows=None, Options=None, Priority=None, ProtocolInterface=None, ShowExternal=None, ShowNssa=None, TeAdminGroup=None, TeEnable=None, TeMaxBandwidth=None, TeMetricLevel=None, TeResMaxBandwidth=None, TeUnreservedBwPriority=None, ValidateReceivedMtuSize=None):
        """Updates interface resource on the server.

        Args
        ----
        - AdvertiseNetworkRange (bool): 
        - AreaId (number): 
        - AuthenticationMethods (str(null | password | md5)): 
        - AuthenticationPassword (str): 
        - BBit (bool): 
        - ConnectedToDut (bool): 
        - DeadInterval (number): 
        - EBit (bool): 
        - EnableAdvertiseRouterLsaLoopback (bool): 
        - EnableBfdRegistration (bool): 
        - EnableFastHello (bool): 
        - Enabled (bool): 
        - EntryColumn (number): 
        - EntryRow (number): 
        - HelloInterval (number): 
        - HelloMultiplier (number): 
        - InterfaceIndex (number): 
        - InterfaceIpAddress (str): 
        - InterfaceIpMaskAddress (str): 
        - InterfaceType (str): 
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): 
        - LinkTypes (str(pointToPoint | transit | stub | virtual)): 
        - Md5AuthenticationKey (str): 
        - Md5AuthenticationKeyId (number): 
        - Metric (number): 
        - Mtu (number): 
        - NeighborIpAddress (str): 
        - NeighborRouterId (str): 
        - NetworkRangeIp (str): 
        - NetworkRangeIpByMask (bool): 
        - NetworkRangeIpIncrementBy (str): 
        - NetworkRangeIpMask (number): 
        - NetworkRangeLinkType (str(broadcast | pointToPoint)): 
        - NetworkRangeRouterId (str): 
        - NetworkRangeRouterIdIncrementBy (str): 
        - NetworkRangeTeEnable (bool): 
        - NetworkRangeTeMaxBandwidth (number): 
        - NetworkRangeTeMetric (number): 
        - NetworkRangeTeResMaxBandwidth (number): 
        - NetworkRangeTeUnreservedBwPriority (dict(arg1:number,arg2:number,arg3:number,arg4:number,arg5:number,arg6:number,arg7:number,arg8:number)): 
        - NetworkType (str(pointToPoint | broadcast | pointToMultipoint)): 
        - NoOfCols (number): 
        - NoOfRows (number): 
        - Options (number): 
        - Priority (number): 
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - ShowExternal (bool): 
        - ShowNssa (bool): 
        - TeAdminGroup (str): 
        - TeEnable (bool): 
        - TeMaxBandwidth (str): 
        - TeMetricLevel (number): 
        - TeResMaxBandwidth (str): 
        - TeUnreservedBwPriority (dict(arg1:str,arg2:str,arg3:str,arg4:str,arg5:str,arg6:str,arg7:str,arg8:str)): 
        - ValidateReceivedMtuSize (bool): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AdvertiseNetworkRange=None, AreaId=None, AuthenticationMethods=None, AuthenticationPassword=None, BBit=None, ConnectedToDut=None, DeadInterval=None, EBit=None, EnableAdvertiseRouterLsaLoopback=None, EnableBfdRegistration=None, EnableFastHello=None, Enabled=None, EntryColumn=None, EntryRow=None, HelloInterval=None, HelloMultiplier=None, InterfaceIndex=None, InterfaceIpAddress=None, InterfaceIpMaskAddress=None, InterfaceType=None, Interfaces=None, LinkTypes=None, Md5AuthenticationKey=None, Md5AuthenticationKeyId=None, Metric=None, Mtu=None, NeighborIpAddress=None, NeighborRouterId=None, NetworkRangeIp=None, NetworkRangeIpByMask=None, NetworkRangeIpIncrementBy=None, NetworkRangeIpMask=None, NetworkRangeLinkType=None, NetworkRangeRouterId=None, NetworkRangeRouterIdIncrementBy=None, NetworkRangeTeEnable=None, NetworkRangeTeMaxBandwidth=None, NetworkRangeTeMetric=None, NetworkRangeTeResMaxBandwidth=None, NetworkRangeTeUnreservedBwPriority=None, NetworkType=None, NoOfCols=None, NoOfRows=None, Options=None, Priority=None, ProtocolInterface=None, ShowExternal=None, ShowNssa=None, TeAdminGroup=None, TeEnable=None, TeMaxBandwidth=None, TeMetricLevel=None, TeResMaxBandwidth=None, TeUnreservedBwPriority=None, ValidateReceivedMtuSize=None):
        """Adds a new interface resource on the server and adds it to the container.

        Args
        ----
        - AdvertiseNetworkRange (bool): 
        - AreaId (number): 
        - AuthenticationMethods (str(null | password | md5)): 
        - AuthenticationPassword (str): 
        - BBit (bool): 
        - ConnectedToDut (bool): 
        - DeadInterval (number): 
        - EBit (bool): 
        - EnableAdvertiseRouterLsaLoopback (bool): 
        - EnableBfdRegistration (bool): 
        - EnableFastHello (bool): 
        - Enabled (bool): 
        - EntryColumn (number): 
        - EntryRow (number): 
        - HelloInterval (number): 
        - HelloMultiplier (number): 
        - InterfaceIndex (number): 
        - InterfaceIpAddress (str): 
        - InterfaceIpMaskAddress (str): 
        - InterfaceType (str): 
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): 
        - LinkTypes (str(pointToPoint | transit | stub | virtual)): 
        - Md5AuthenticationKey (str): 
        - Md5AuthenticationKeyId (number): 
        - Metric (number): 
        - Mtu (number): 
        - NeighborIpAddress (str): 
        - NeighborRouterId (str): 
        - NetworkRangeIp (str): 
        - NetworkRangeIpByMask (bool): 
        - NetworkRangeIpIncrementBy (str): 
        - NetworkRangeIpMask (number): 
        - NetworkRangeLinkType (str(broadcast | pointToPoint)): 
        - NetworkRangeRouterId (str): 
        - NetworkRangeRouterIdIncrementBy (str): 
        - NetworkRangeTeEnable (bool): 
        - NetworkRangeTeMaxBandwidth (number): 
        - NetworkRangeTeMetric (number): 
        - NetworkRangeTeResMaxBandwidth (number): 
        - NetworkRangeTeUnreservedBwPriority (dict(arg1:number,arg2:number,arg3:number,arg4:number,arg5:number,arg6:number,arg7:number,arg8:number)): 
        - NetworkType (str(pointToPoint | broadcast | pointToMultipoint)): 
        - NoOfCols (number): 
        - NoOfRows (number): 
        - Options (number): 
        - Priority (number): 
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - ShowExternal (bool): 
        - ShowNssa (bool): 
        - TeAdminGroup (str): 
        - TeEnable (bool): 
        - TeMaxBandwidth (str): 
        - TeMetricLevel (number): 
        - TeResMaxBandwidth (str): 
        - TeUnreservedBwPriority (dict(arg1:str,arg2:str,arg3:str,arg4:str,arg5:str,arg6:str,arg7:str,arg8:str)): 
        - ValidateReceivedMtuSize (bool): 

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

    def find(self, AdvertiseNetworkRange=None, AreaId=None, AuthenticationMethods=None, AuthenticationPassword=None, BBit=None, ConnectedToDut=None, DeadInterval=None, EBit=None, EnableAdvertiseRouterLsaLoopback=None, EnableBfdRegistration=None, EnableFastHello=None, Enabled=None, EntryColumn=None, EntryRow=None, HelloInterval=None, HelloMultiplier=None, InterfaceIndex=None, InterfaceIpAddress=None, InterfaceIpMaskAddress=None, InterfaceType=None, Interfaces=None, IsLearnedInfoRefreshed=None, LinkTypes=None, Md5AuthenticationKey=None, Md5AuthenticationKeyId=None, Metric=None, Mtu=None, NeighborIpAddress=None, NeighborRouterId=None, NetworkRangeIp=None, NetworkRangeIpByMask=None, NetworkRangeIpIncrementBy=None, NetworkRangeIpMask=None, NetworkRangeLinkType=None, NetworkRangeRouterId=None, NetworkRangeRouterIdIncrementBy=None, NetworkRangeTeEnable=None, NetworkRangeTeMaxBandwidth=None, NetworkRangeTeMetric=None, NetworkRangeTeResMaxBandwidth=None, NetworkRangeTeUnreservedBwPriority=None, NetworkType=None, NoOfCols=None, NoOfRows=None, Options=None, Priority=None, ProtocolInterface=None, ShowExternal=None, ShowNssa=None, TeAdminGroup=None, TeEnable=None, TeMaxBandwidth=None, TeMetricLevel=None, TeResMaxBandwidth=None, TeUnreservedBwPriority=None, ValidateReceivedMtuSize=None):
        """Finds and retrieves interface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve interface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all interface resources from the server.

        Args
        ----
        - AdvertiseNetworkRange (bool): 
        - AreaId (number): 
        - AuthenticationMethods (str(null | password | md5)): 
        - AuthenticationPassword (str): 
        - BBit (bool): 
        - ConnectedToDut (bool): 
        - DeadInterval (number): 
        - EBit (bool): 
        - EnableAdvertiseRouterLsaLoopback (bool): 
        - EnableBfdRegistration (bool): 
        - EnableFastHello (bool): 
        - Enabled (bool): 
        - EntryColumn (number): 
        - EntryRow (number): 
        - HelloInterval (number): 
        - HelloMultiplier (number): 
        - InterfaceIndex (number): 
        - InterfaceIpAddress (str): 
        - InterfaceIpMaskAddress (str): 
        - InterfaceType (str): 
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): 
        - IsLearnedInfoRefreshed (bool): 
        - LinkTypes (str(pointToPoint | transit | stub | virtual)): 
        - Md5AuthenticationKey (str): 
        - Md5AuthenticationKeyId (number): 
        - Metric (number): 
        - Mtu (number): 
        - NeighborIpAddress (str): 
        - NeighborRouterId (str): 
        - NetworkRangeIp (str): 
        - NetworkRangeIpByMask (bool): 
        - NetworkRangeIpIncrementBy (str): 
        - NetworkRangeIpMask (number): 
        - NetworkRangeLinkType (str(broadcast | pointToPoint)): 
        - NetworkRangeRouterId (str): 
        - NetworkRangeRouterIdIncrementBy (str): 
        - NetworkRangeTeEnable (bool): 
        - NetworkRangeTeMaxBandwidth (number): 
        - NetworkRangeTeMetric (number): 
        - NetworkRangeTeResMaxBandwidth (number): 
        - NetworkRangeTeUnreservedBwPriority (dict(arg1:number,arg2:number,arg3:number,arg4:number,arg5:number,arg6:number,arg7:number,arg8:number)): 
        - NetworkType (str(pointToPoint | broadcast | pointToMultipoint)): 
        - NoOfCols (number): 
        - NoOfRows (number): 
        - Options (number): 
        - Priority (number): 
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - ShowExternal (bool): 
        - ShowNssa (bool): 
        - TeAdminGroup (str): 
        - TeEnable (bool): 
        - TeMaxBandwidth (str): 
        - TeMetricLevel (number): 
        - TeResMaxBandwidth (str): 
        - TeUnreservedBwPriority (dict(arg1:str,arg2:str,arg3:str,arg4:str,arg5:str,arg6:str,arg7:str,arg8:str)): 
        - ValidateReceivedMtuSize (bool): 

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

    def RefreshLearnedInfo(self):
        """Executes the refreshLearnedInfo operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshLearnedInfo', payload=payload, response_object=None)
