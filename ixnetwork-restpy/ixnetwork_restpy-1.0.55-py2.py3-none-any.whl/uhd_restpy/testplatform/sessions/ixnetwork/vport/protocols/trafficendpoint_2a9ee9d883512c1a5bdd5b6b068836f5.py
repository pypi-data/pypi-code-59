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


class TrafficEndPoint(Base):
    """
    The TrafficEndPoint class encapsulates a list of trafficEndPoint resources that are managed by the user.
    A list of resources can be retrieved from the server using the TrafficEndPoint.find() method.
    The list can be managed by using the TrafficEndPoint.add() and TrafficEndPoint.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'trafficEndPoint'
    _SDM_ATT_MAP = {
        'ArpViaInterface': 'arpViaInterface',
        'CustomEtherHeaderLength': 'customEtherHeaderLength',
        'CustomEtherHeaderValue': 'customEtherHeaderValue',
        'CustomEtherType': 'customEtherType',
        'CustomIpHeaderLength': 'customIpHeaderLength',
        'CustomIpHeaderValue': 'customIpHeaderValue',
        'CustomIpProtocol': 'customIpProtocol',
        'DestinationPort': 'destinationPort',
        'EnableMacInMac': 'enableMacInMac',
        'EnableVlan': 'enableVlan',
        'EtherType': 'etherType',
        'GatewayMac': 'gatewayMac',
        'IpAddress': 'ipAddress',
        'IpMask': 'ipMask',
        'IpProtocol': 'ipProtocol',
        'IpTos': 'ipTos',
        'Ipv4Dscp': 'ipv4Dscp',
        'Ipv4Ecn': 'ipv4Ecn',
        'Ipv6Address': 'ipv6Address',
        'Ipv6AddressMask': 'ipv6AddressMask',
        'Ipv6CustomHeaderLength': 'ipv6CustomHeaderLength',
        'Ipv6CustomHeaderValue': 'ipv6CustomHeaderValue',
        'Ipv6CustomNextHeader': 'ipv6CustomNextHeader',
        'Ipv6Dscp': 'ipv6Dscp',
        'Ipv6Ecn': 'ipv6Ecn',
        'Ipv6FlowLabel': 'ipv6FlowLabel',
        'Ipv6NextHeader': 'ipv6NextHeader',
        'MacAddress': 'macAddress',
        'MplsInnerMacSource': 'mplsInnerMacSource',
        'MplsInnerVlanId': 'mplsInnerVlanId',
        'MplsInnerVlanPriority': 'mplsInnerVlanPriority',
        'MplsLabel': 'mplsLabel',
        'MplsLabelStackSize': 'mplsLabelStackSize',
        'MplsPayloadType': 'mplsPayloadType',
        'MplsTrafficClass': 'mplsTrafficClass',
        'Name': 'name',
        'PbbDestinamtionMac': 'pbbDestinamtionMac',
        'PbbEtherType': 'pbbEtherType',
        'PbbIsId': 'pbbIsId',
        'PbbSourceMac': 'pbbSourceMac',
        'PbbVlanId': 'pbbVlanId',
        'PbbVlanPcp': 'pbbVlanPcp',
        'ProtocolInterface': 'protocolInterface',
        'RangeSize': 'rangeSize',
        'SourcePort': 'sourcePort',
        'UdpDestination': 'udpDestination',
        'UdpSource': 'udpSource',
        'VlanCount': 'vlanCount',
        'VlanId': 'vlanId',
        'VlanPriority': 'vlanPriority',
    }

    def __init__(self, parent):
        super(TrafficEndPoint, self).__init__(parent)

    @property
    def ArpViaInterface(self):
        """DEPRECATED 
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpViaInterface'])
    @ArpViaInterface.setter
    def ArpViaInterface(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpViaInterface'], value)

    @property
    def CustomEtherHeaderLength(self):
        """DEPRECATED 
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomEtherHeaderLength'])
    @CustomEtherHeaderLength.setter
    def CustomEtherHeaderLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustomEtherHeaderLength'], value)

    @property
    def CustomEtherHeaderValue(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomEtherHeaderValue'])
    @CustomEtherHeaderValue.setter
    def CustomEtherHeaderValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustomEtherHeaderValue'], value)

    @property
    def CustomEtherType(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomEtherType'])
    @CustomEtherType.setter
    def CustomEtherType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustomEtherType'], value)

    @property
    def CustomIpHeaderLength(self):
        """DEPRECATED 
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomIpHeaderLength'])
    @CustomIpHeaderLength.setter
    def CustomIpHeaderLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustomIpHeaderLength'], value)

    @property
    def CustomIpHeaderValue(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomIpHeaderValue'])
    @CustomIpHeaderValue.setter
    def CustomIpHeaderValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustomIpHeaderValue'], value)

    @property
    def CustomIpProtocol(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomIpProtocol'])
    @CustomIpProtocol.setter
    def CustomIpProtocol(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustomIpProtocol'], value)

    @property
    def DestinationPort(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DestinationPort'])
    @DestinationPort.setter
    def DestinationPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DestinationPort'], value)

    @property
    def EnableMacInMac(self):
        """DEPRECATED 
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMacInMac'])
    @EnableMacInMac.setter
    def EnableMacInMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMacInMac'], value)

    @property
    def EnableVlan(self):
        """DEPRECATED 
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableVlan'])
    @EnableVlan.setter
    def EnableVlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableVlan'], value)

    @property
    def EtherType(self):
        """DEPRECATED 
        Returns
        -------
        - str(custom | ipv4 | ipv6 | mplsUnicast): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EtherType'])
    @EtherType.setter
    def EtherType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EtherType'], value)

    @property
    def GatewayMac(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['GatewayMac'])
    @GatewayMac.setter
    def GatewayMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GatewayMac'], value)

    @property
    def IpAddress(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpAddress'])
    @IpAddress.setter
    def IpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpAddress'], value)

    @property
    def IpMask(self):
        """DEPRECATED 
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpMask'])
    @IpMask.setter
    def IpMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpMask'], value)

    @property
    def IpProtocol(self):
        """DEPRECATED 
        Returns
        -------
        - str(custom | tcp | udp): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpProtocol'])
    @IpProtocol.setter
    def IpProtocol(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpProtocol'], value)

    @property
    def IpTos(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpTos'])
    @IpTos.setter
    def IpTos(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpTos'], value)

    @property
    def Ipv4Dscp(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Dscp'])
    @Ipv4Dscp.setter
    def Ipv4Dscp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4Dscp'], value)

    @property
    def Ipv4Ecn(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Ecn'])
    @Ipv4Ecn.setter
    def Ipv4Ecn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4Ecn'], value)

    @property
    def Ipv6Address(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6Address'])
    @Ipv6Address.setter
    def Ipv6Address(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6Address'], value)

    @property
    def Ipv6AddressMask(self):
        """DEPRECATED 
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6AddressMask'])
    @Ipv6AddressMask.setter
    def Ipv6AddressMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6AddressMask'], value)

    @property
    def Ipv6CustomHeaderLength(self):
        """DEPRECATED 
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6CustomHeaderLength'])
    @Ipv6CustomHeaderLength.setter
    def Ipv6CustomHeaderLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6CustomHeaderLength'], value)

    @property
    def Ipv6CustomHeaderValue(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6CustomHeaderValue'])
    @Ipv6CustomHeaderValue.setter
    def Ipv6CustomHeaderValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6CustomHeaderValue'], value)

    @property
    def Ipv6CustomNextHeader(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6CustomNextHeader'])
    @Ipv6CustomNextHeader.setter
    def Ipv6CustomNextHeader(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6CustomNextHeader'], value)

    @property
    def Ipv6Dscp(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6Dscp'])
    @Ipv6Dscp.setter
    def Ipv6Dscp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6Dscp'], value)

    @property
    def Ipv6Ecn(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6Ecn'])
    @Ipv6Ecn.setter
    def Ipv6Ecn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6Ecn'], value)

    @property
    def Ipv6FlowLabel(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6FlowLabel'])
    @Ipv6FlowLabel.setter
    def Ipv6FlowLabel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6FlowLabel'], value)

    @property
    def Ipv6NextHeader(self):
        """DEPRECATED 
        Returns
        -------
        - str(custom | tcp | udp): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6NextHeader'])
    @Ipv6NextHeader.setter
    def Ipv6NextHeader(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6NextHeader'], value)

    @property
    def MacAddress(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MacAddress'])
    @MacAddress.setter
    def MacAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MacAddress'], value)

    @property
    def MplsInnerMacSource(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsInnerMacSource'])
    @MplsInnerMacSource.setter
    def MplsInnerMacSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MplsInnerMacSource'], value)

    @property
    def MplsInnerVlanId(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsInnerVlanId'])
    @MplsInnerVlanId.setter
    def MplsInnerVlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MplsInnerVlanId'], value)

    @property
    def MplsInnerVlanPriority(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsInnerVlanPriority'])
    @MplsInnerVlanPriority.setter
    def MplsInnerVlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MplsInnerVlanPriority'], value)

    @property
    def MplsLabel(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsLabel'])
    @MplsLabel.setter
    def MplsLabel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MplsLabel'], value)

    @property
    def MplsLabelStackSize(self):
        """DEPRECATED 
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsLabelStackSize'])
    @MplsLabelStackSize.setter
    def MplsLabelStackSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MplsLabelStackSize'], value)

    @property
    def MplsPayloadType(self):
        """DEPRECATED 
        Returns
        -------
        - str(ethernet | ipv4 | ipv6): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsPayloadType'])
    @MplsPayloadType.setter
    def MplsPayloadType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MplsPayloadType'], value)

    @property
    def MplsTrafficClass(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsTrafficClass'])
    @MplsTrafficClass.setter
    def MplsTrafficClass(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MplsTrafficClass'], value)

    @property
    def Name(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def PbbDestinamtionMac(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PbbDestinamtionMac'])
    @PbbDestinamtionMac.setter
    def PbbDestinamtionMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PbbDestinamtionMac'], value)

    @property
    def PbbEtherType(self):
        """DEPRECATED 
        Returns
        -------
        - str(bEtherType8100 | bEtherType88A8 | bEtherType88E7 | bEtherType9100 | bEtherType9200): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PbbEtherType'])
    @PbbEtherType.setter
    def PbbEtherType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PbbEtherType'], value)

    @property
    def PbbIsId(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PbbIsId'])
    @PbbIsId.setter
    def PbbIsId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PbbIsId'], value)

    @property
    def PbbSourceMac(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PbbSourceMac'])
    @PbbSourceMac.setter
    def PbbSourceMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PbbSourceMac'], value)

    @property
    def PbbVlanId(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PbbVlanId'])
    @PbbVlanId.setter
    def PbbVlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PbbVlanId'], value)

    @property
    def PbbVlanPcp(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PbbVlanPcp'])
    @PbbVlanPcp.setter
    def PbbVlanPcp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PbbVlanPcp'], value)

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
    def RangeSize(self):
        """DEPRECATED 
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RangeSize'])
    @RangeSize.setter
    def RangeSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RangeSize'], value)

    @property
    def SourcePort(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourcePort'])
    @SourcePort.setter
    def SourcePort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SourcePort'], value)

    @property
    def UdpDestination(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UdpDestination'])
    @UdpDestination.setter
    def UdpDestination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UdpDestination'], value)

    @property
    def UdpSource(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UdpSource'])
    @UdpSource.setter
    def UdpSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UdpSource'], value)

    @property
    def VlanCount(self):
        """DEPRECATED 
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanCount'])
    @VlanCount.setter
    def VlanCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanCount'], value)

    @property
    def VlanId(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanId'])
    @VlanId.setter
    def VlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanId'], value)

    @property
    def VlanPriority(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanPriority'])
    @VlanPriority.setter
    def VlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanPriority'], value)

    def update(self, ArpViaInterface=None, CustomEtherHeaderLength=None, CustomEtherHeaderValue=None, CustomEtherType=None, CustomIpHeaderLength=None, CustomIpHeaderValue=None, CustomIpProtocol=None, DestinationPort=None, EnableMacInMac=None, EnableVlan=None, EtherType=None, GatewayMac=None, IpAddress=None, IpMask=None, IpProtocol=None, IpTos=None, Ipv4Dscp=None, Ipv4Ecn=None, Ipv6Address=None, Ipv6AddressMask=None, Ipv6CustomHeaderLength=None, Ipv6CustomHeaderValue=None, Ipv6CustomNextHeader=None, Ipv6Dscp=None, Ipv6Ecn=None, Ipv6FlowLabel=None, Ipv6NextHeader=None, MacAddress=None, MplsInnerMacSource=None, MplsInnerVlanId=None, MplsInnerVlanPriority=None, MplsLabel=None, MplsLabelStackSize=None, MplsPayloadType=None, MplsTrafficClass=None, Name=None, PbbDestinamtionMac=None, PbbEtherType=None, PbbIsId=None, PbbSourceMac=None, PbbVlanId=None, PbbVlanPcp=None, ProtocolInterface=None, RangeSize=None, SourcePort=None, UdpDestination=None, UdpSource=None, VlanCount=None, VlanId=None, VlanPriority=None):
        """Updates trafficEndPoint resource on the server.

        Args
        ----
        - ArpViaInterface (bool): 
        - CustomEtherHeaderLength (number): 
        - CustomEtherHeaderValue (str): 
        - CustomEtherType (str): 
        - CustomIpHeaderLength (number): 
        - CustomIpHeaderValue (str): 
        - CustomIpProtocol (str): 
        - DestinationPort (str): 
        - EnableMacInMac (bool): 
        - EnableVlan (bool): 
        - EtherType (str(custom | ipv4 | ipv6 | mplsUnicast)): 
        - GatewayMac (str): 
        - IpAddress (str): 
        - IpMask (number): 
        - IpProtocol (str(custom | tcp | udp)): 
        - IpTos (str): 
        - Ipv4Dscp (str): 
        - Ipv4Ecn (str): 
        - Ipv6Address (str): 
        - Ipv6AddressMask (number): 
        - Ipv6CustomHeaderLength (number): 
        - Ipv6CustomHeaderValue (str): 
        - Ipv6CustomNextHeader (str): 
        - Ipv6Dscp (str): 
        - Ipv6Ecn (str): 
        - Ipv6FlowLabel (str): 
        - Ipv6NextHeader (str(custom | tcp | udp)): 
        - MacAddress (str): 
        - MplsInnerMacSource (str): 
        - MplsInnerVlanId (str): 
        - MplsInnerVlanPriority (str): 
        - MplsLabel (str): 
        - MplsLabelStackSize (number): 
        - MplsPayloadType (str(ethernet | ipv4 | ipv6)): 
        - MplsTrafficClass (str): 
        - Name (str): 
        - PbbDestinamtionMac (str): 
        - PbbEtherType (str(bEtherType8100 | bEtherType88A8 | bEtherType88E7 | bEtherType9100 | bEtherType9200)): 
        - PbbIsId (str): 
        - PbbSourceMac (str): 
        - PbbVlanId (str): 
        - PbbVlanPcp (str): 
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - RangeSize (number): 
        - SourcePort (str): 
        - UdpDestination (str): 
        - UdpSource (str): 
        - VlanCount (number): 
        - VlanId (str): 
        - VlanPriority (str): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ArpViaInterface=None, CustomEtherHeaderLength=None, CustomEtherHeaderValue=None, CustomEtherType=None, CustomIpHeaderLength=None, CustomIpHeaderValue=None, CustomIpProtocol=None, DestinationPort=None, EnableMacInMac=None, EnableVlan=None, EtherType=None, GatewayMac=None, IpAddress=None, IpMask=None, IpProtocol=None, IpTos=None, Ipv4Dscp=None, Ipv4Ecn=None, Ipv6Address=None, Ipv6AddressMask=None, Ipv6CustomHeaderLength=None, Ipv6CustomHeaderValue=None, Ipv6CustomNextHeader=None, Ipv6Dscp=None, Ipv6Ecn=None, Ipv6FlowLabel=None, Ipv6NextHeader=None, MacAddress=None, MplsInnerMacSource=None, MplsInnerVlanId=None, MplsInnerVlanPriority=None, MplsLabel=None, MplsLabelStackSize=None, MplsPayloadType=None, MplsTrafficClass=None, Name=None, PbbDestinamtionMac=None, PbbEtherType=None, PbbIsId=None, PbbSourceMac=None, PbbVlanId=None, PbbVlanPcp=None, ProtocolInterface=None, RangeSize=None, SourcePort=None, UdpDestination=None, UdpSource=None, VlanCount=None, VlanId=None, VlanPriority=None):
        """Adds a new trafficEndPoint resource on the server and adds it to the container.

        Args
        ----
        - ArpViaInterface (bool): 
        - CustomEtherHeaderLength (number): 
        - CustomEtherHeaderValue (str): 
        - CustomEtherType (str): 
        - CustomIpHeaderLength (number): 
        - CustomIpHeaderValue (str): 
        - CustomIpProtocol (str): 
        - DestinationPort (str): 
        - EnableMacInMac (bool): 
        - EnableVlan (bool): 
        - EtherType (str(custom | ipv4 | ipv6 | mplsUnicast)): 
        - GatewayMac (str): 
        - IpAddress (str): 
        - IpMask (number): 
        - IpProtocol (str(custom | tcp | udp)): 
        - IpTos (str): 
        - Ipv4Dscp (str): 
        - Ipv4Ecn (str): 
        - Ipv6Address (str): 
        - Ipv6AddressMask (number): 
        - Ipv6CustomHeaderLength (number): 
        - Ipv6CustomHeaderValue (str): 
        - Ipv6CustomNextHeader (str): 
        - Ipv6Dscp (str): 
        - Ipv6Ecn (str): 
        - Ipv6FlowLabel (str): 
        - Ipv6NextHeader (str(custom | tcp | udp)): 
        - MacAddress (str): 
        - MplsInnerMacSource (str): 
        - MplsInnerVlanId (str): 
        - MplsInnerVlanPriority (str): 
        - MplsLabel (str): 
        - MplsLabelStackSize (number): 
        - MplsPayloadType (str(ethernet | ipv4 | ipv6)): 
        - MplsTrafficClass (str): 
        - Name (str): 
        - PbbDestinamtionMac (str): 
        - PbbEtherType (str(bEtherType8100 | bEtherType88A8 | bEtherType88E7 | bEtherType9100 | bEtherType9200)): 
        - PbbIsId (str): 
        - PbbSourceMac (str): 
        - PbbVlanId (str): 
        - PbbVlanPcp (str): 
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - RangeSize (number): 
        - SourcePort (str): 
        - UdpDestination (str): 
        - UdpSource (str): 
        - VlanCount (number): 
        - VlanId (str): 
        - VlanPriority (str): 

        Returns
        -------
        - self: This instance with all currently retrieved trafficEndPoint resources using find and the newly added trafficEndPoint resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained trafficEndPoint resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ArpViaInterface=None, CustomEtherHeaderLength=None, CustomEtherHeaderValue=None, CustomEtherType=None, CustomIpHeaderLength=None, CustomIpHeaderValue=None, CustomIpProtocol=None, DestinationPort=None, EnableMacInMac=None, EnableVlan=None, EtherType=None, GatewayMac=None, IpAddress=None, IpMask=None, IpProtocol=None, IpTos=None, Ipv4Dscp=None, Ipv4Ecn=None, Ipv6Address=None, Ipv6AddressMask=None, Ipv6CustomHeaderLength=None, Ipv6CustomHeaderValue=None, Ipv6CustomNextHeader=None, Ipv6Dscp=None, Ipv6Ecn=None, Ipv6FlowLabel=None, Ipv6NextHeader=None, MacAddress=None, MplsInnerMacSource=None, MplsInnerVlanId=None, MplsInnerVlanPriority=None, MplsLabel=None, MplsLabelStackSize=None, MplsPayloadType=None, MplsTrafficClass=None, Name=None, PbbDestinamtionMac=None, PbbEtherType=None, PbbIsId=None, PbbSourceMac=None, PbbVlanId=None, PbbVlanPcp=None, ProtocolInterface=None, RangeSize=None, SourcePort=None, UdpDestination=None, UdpSource=None, VlanCount=None, VlanId=None, VlanPriority=None):
        """Finds and retrieves trafficEndPoint resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve trafficEndPoint resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all trafficEndPoint resources from the server.

        Args
        ----
        - ArpViaInterface (bool): 
        - CustomEtherHeaderLength (number): 
        - CustomEtherHeaderValue (str): 
        - CustomEtherType (str): 
        - CustomIpHeaderLength (number): 
        - CustomIpHeaderValue (str): 
        - CustomIpProtocol (str): 
        - DestinationPort (str): 
        - EnableMacInMac (bool): 
        - EnableVlan (bool): 
        - EtherType (str(custom | ipv4 | ipv6 | mplsUnicast)): 
        - GatewayMac (str): 
        - IpAddress (str): 
        - IpMask (number): 
        - IpProtocol (str(custom | tcp | udp)): 
        - IpTos (str): 
        - Ipv4Dscp (str): 
        - Ipv4Ecn (str): 
        - Ipv6Address (str): 
        - Ipv6AddressMask (number): 
        - Ipv6CustomHeaderLength (number): 
        - Ipv6CustomHeaderValue (str): 
        - Ipv6CustomNextHeader (str): 
        - Ipv6Dscp (str): 
        - Ipv6Ecn (str): 
        - Ipv6FlowLabel (str): 
        - Ipv6NextHeader (str(custom | tcp | udp)): 
        - MacAddress (str): 
        - MplsInnerMacSource (str): 
        - MplsInnerVlanId (str): 
        - MplsInnerVlanPriority (str): 
        - MplsLabel (str): 
        - MplsLabelStackSize (number): 
        - MplsPayloadType (str(ethernet | ipv4 | ipv6)): 
        - MplsTrafficClass (str): 
        - Name (str): 
        - PbbDestinamtionMac (str): 
        - PbbEtherType (str(bEtherType8100 | bEtherType88A8 | bEtherType88E7 | bEtherType9100 | bEtherType9200)): 
        - PbbIsId (str): 
        - PbbSourceMac (str): 
        - PbbVlanId (str): 
        - PbbVlanPcp (str): 
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - RangeSize (number): 
        - SourcePort (str): 
        - UdpDestination (str): 
        - UdpSource (str): 
        - VlanCount (number): 
        - VlanId (str): 
        - VlanPriority (str): 

        Returns
        -------
        - self: This instance with matching trafficEndPoint resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of trafficEndPoint data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the trafficEndPoint resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
