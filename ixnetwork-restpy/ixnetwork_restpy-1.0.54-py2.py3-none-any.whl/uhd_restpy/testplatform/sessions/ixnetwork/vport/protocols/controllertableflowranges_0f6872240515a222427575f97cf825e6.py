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


class ControllerTableFlowRanges(Base):
    """
    The ControllerTableFlowRanges class encapsulates a list of controllerTableFlowRanges resources that are managed by the user.
    A list of resources can be retrieved from the server using the ControllerTableFlowRanges.find() method.
    The list can be managed by using the ControllerTableFlowRanges.add() and ControllerTableFlowRanges.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'controllerTableFlowRanges'
    _SDM_ATT_MAP = {
        'ArpDstHwAddr': 'arpDstHwAddr',
        'ArpDstHwAddrMask': 'arpDstHwAddrMask',
        'ArpDstIpv4Addr': 'arpDstIpv4Addr',
        'ArpDstIpv4AddrMask': 'arpDstIpv4AddrMask',
        'ArpOpcode': 'arpOpcode',
        'ArpSrcHwAddr': 'arpSrcHwAddr',
        'ArpSrcHwAddrMask': 'arpSrcHwAddrMask',
        'ArpSrcIpv4Addr': 'arpSrcIpv4Addr',
        'ArpSrcIpv4AddrMask': 'arpSrcIpv4AddrMask',
        'CheckOverlapFlags': 'checkOverlapFlags',
        'Cookie': 'cookie',
        'CookieMask': 'cookieMask',
        'Description': 'description',
        'Enabled': 'enabled',
        'EthernetDestination': 'ethernetDestination',
        'EthernetDestinationMask': 'ethernetDestinationMask',
        'EthernetSource': 'ethernetSource',
        'EthernetSourceMask': 'ethernetSourceMask',
        'EthernetType': 'ethernetType',
        'ExperimenterData': 'experimenterData',
        'ExperimenterDatalength': 'experimenterDatalength',
        'ExperimenterField': 'experimenterField',
        'ExperimenterHasMask': 'experimenterHasMask',
        'ExperimenterId': 'experimenterId',
        'FlowAdvertise': 'flowAdvertise',
        'FlowModStatus': 'flowModStatus',
        'HardTimeout': 'hardTimeout',
        'Icmpv4Code': 'icmpv4Code',
        'Icmpv4Type': 'icmpv4Type',
        'Icmpv6Code': 'icmpv6Code',
        'Icmpv6Type': 'icmpv6Type',
        'IdleTimeout': 'idleTimeout',
        'InPhyPort': 'inPhyPort',
        'InPort': 'inPort',
        'IpDscp': 'ipDscp',
        'IpEcn': 'ipEcn',
        'IpProtocol': 'ipProtocol',
        'Ipv4Destination': 'ipv4Destination',
        'Ipv4DestinationMask': 'ipv4DestinationMask',
        'Ipv4Source': 'ipv4Source',
        'Ipv4SourceMask': 'ipv4SourceMask',
        'Ipv6Destination': 'ipv6Destination',
        'Ipv6DestinationMask': 'ipv6DestinationMask',
        'Ipv6ExtHeader': 'ipv6ExtHeader',
        'Ipv6ExtHeaderMask': 'ipv6ExtHeaderMask',
        'Ipv6FlowLabel': 'ipv6FlowLabel',
        'Ipv6FlowLabelMask': 'ipv6FlowLabelMask',
        'Ipv6NdDll': 'ipv6NdDll',
        'Ipv6NdSll': 'ipv6NdSll',
        'Ipv6NdTarget': 'ipv6NdTarget',
        'Ipv6Source': 'ipv6Source',
        'Ipv6SourceMask': 'ipv6SourceMask',
        'MatchType': 'matchType',
        'Metadata': 'metadata',
        'MetadataMask': 'metadataMask',
        'MplsBos': 'mplsBos',
        'MplsLabel': 'mplsLabel',
        'MplsTc': 'mplsTc',
        'NoByteCounts': 'noByteCounts',
        'NoPacketCounts': 'noPacketCounts',
        'NumberOfFlows': 'numberOfFlows',
        'PbbIsId': 'pbbIsId',
        'PbbIsIdMask': 'pbbIsIdMask',
        'Priority': 'priority',
        'ResetCounts': 'resetCounts',
        'SctpDestination': 'sctpDestination',
        'SctpSource': 'sctpSource',
        'SendFlowRemoved': 'sendFlowRemoved',
        'TcpDestination': 'tcpDestination',
        'TcpSource': 'tcpSource',
        'TunnelId': 'tunnelId',
        'TunnelIdMask': 'tunnelIdMask',
        'UdpDestination': 'udpDestination',
        'UdpSource': 'udpSource',
        'VlanId': 'vlanId',
        'VlanIdMask': 'vlanIdMask',
        'VlanMatchType': 'vlanMatchType',
        'VlanPriority': 'vlanPriority',
    }

    def __init__(self, parent):
        super(ControllerTableFlowRanges, self).__init__(parent)

    @property
    def Instructions(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructions_5497c86fc28b0188cf9eea0ca484ecbf.Instructions): An instance of the Instructions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructions_5497c86fc28b0188cf9eea0ca484ecbf import Instructions
        return Instructions(self)

    @property
    def ArpDstHwAddr(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpDstHwAddr'])
    @ArpDstHwAddr.setter
    def ArpDstHwAddr(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpDstHwAddr'], value)

    @property
    def ArpDstHwAddrMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpDstHwAddrMask'])
    @ArpDstHwAddrMask.setter
    def ArpDstHwAddrMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpDstHwAddrMask'], value)

    @property
    def ArpDstIpv4Addr(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpDstIpv4Addr'])
    @ArpDstIpv4Addr.setter
    def ArpDstIpv4Addr(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpDstIpv4Addr'], value)

    @property
    def ArpDstIpv4AddrMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpDstIpv4AddrMask'])
    @ArpDstIpv4AddrMask.setter
    def ArpDstIpv4AddrMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpDstIpv4AddrMask'], value)

    @property
    def ArpOpcode(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpOpcode'])
    @ArpOpcode.setter
    def ArpOpcode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpOpcode'], value)

    @property
    def ArpSrcHwAddr(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpSrcHwAddr'])
    @ArpSrcHwAddr.setter
    def ArpSrcHwAddr(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpSrcHwAddr'], value)

    @property
    def ArpSrcHwAddrMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpSrcHwAddrMask'])
    @ArpSrcHwAddrMask.setter
    def ArpSrcHwAddrMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpSrcHwAddrMask'], value)

    @property
    def ArpSrcIpv4Addr(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpSrcIpv4Addr'])
    @ArpSrcIpv4Addr.setter
    def ArpSrcIpv4Addr(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpSrcIpv4Addr'], value)

    @property
    def ArpSrcIpv4AddrMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpSrcIpv4AddrMask'])
    @ArpSrcIpv4AddrMask.setter
    def ArpSrcIpv4AddrMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpSrcIpv4AddrMask'], value)

    @property
    def CheckOverlapFlags(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CheckOverlapFlags'])
    @CheckOverlapFlags.setter
    def CheckOverlapFlags(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CheckOverlapFlags'], value)

    @property
    def Cookie(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Cookie'])
    @Cookie.setter
    def Cookie(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Cookie'], value)

    @property
    def CookieMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CookieMask'])
    @CookieMask.setter
    def CookieMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CookieMask'], value)

    @property
    def Description(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Description'])
    @Description.setter
    def Description(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Description'], value)

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
    def EthernetDestination(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetDestination'])
    @EthernetDestination.setter
    def EthernetDestination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetDestination'], value)

    @property
    def EthernetDestinationMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetDestinationMask'])
    @EthernetDestinationMask.setter
    def EthernetDestinationMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetDestinationMask'], value)

    @property
    def EthernetSource(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetSource'])
    @EthernetSource.setter
    def EthernetSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetSource'], value)

    @property
    def EthernetSourceMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetSourceMask'])
    @EthernetSourceMask.setter
    def EthernetSourceMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetSourceMask'], value)

    @property
    def EthernetType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetType'])
    @EthernetType.setter
    def EthernetType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetType'], value)

    @property
    def ExperimenterData(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterData'])
    @ExperimenterData.setter
    def ExperimenterData(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterData'], value)

    @property
    def ExperimenterDatalength(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterDatalength'])
    @ExperimenterDatalength.setter
    def ExperimenterDatalength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterDatalength'], value)

    @property
    def ExperimenterField(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterField'])
    @ExperimenterField.setter
    def ExperimenterField(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterField'], value)

    @property
    def ExperimenterHasMask(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterHasMask'])
    @ExperimenterHasMask.setter
    def ExperimenterHasMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterHasMask'], value)

    @property
    def ExperimenterId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterId'])
    @ExperimenterId.setter
    def ExperimenterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterId'], value)

    @property
    def FlowAdvertise(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowAdvertise'])
    @FlowAdvertise.setter
    def FlowAdvertise(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowAdvertise'], value)

    @property
    def FlowModStatus(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowModStatus'])

    @property
    def HardTimeout(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['HardTimeout'])
    @HardTimeout.setter
    def HardTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HardTimeout'], value)

    @property
    def Icmpv4Code(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Icmpv4Code'])
    @Icmpv4Code.setter
    def Icmpv4Code(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Icmpv4Code'], value)

    @property
    def Icmpv4Type(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Icmpv4Type'])
    @Icmpv4Type.setter
    def Icmpv4Type(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Icmpv4Type'], value)

    @property
    def Icmpv6Code(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Icmpv6Code'])
    @Icmpv6Code.setter
    def Icmpv6Code(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Icmpv6Code'], value)

    @property
    def Icmpv6Type(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Icmpv6Type'])
    @Icmpv6Type.setter
    def Icmpv6Type(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Icmpv6Type'], value)

    @property
    def IdleTimeout(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IdleTimeout'])
    @IdleTimeout.setter
    def IdleTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IdleTimeout'], value)

    @property
    def InPhyPort(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InPhyPort'])
    @InPhyPort.setter
    def InPhyPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InPhyPort'], value)

    @property
    def InPort(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InPort'])
    @InPort.setter
    def InPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InPort'], value)

    @property
    def IpDscp(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpDscp'])
    @IpDscp.setter
    def IpDscp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpDscp'], value)

    @property
    def IpEcn(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpEcn'])
    @IpEcn.setter
    def IpEcn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpEcn'], value)

    @property
    def IpProtocol(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpProtocol'])
    @IpProtocol.setter
    def IpProtocol(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpProtocol'], value)

    @property
    def Ipv4Destination(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Destination'])
    @Ipv4Destination.setter
    def Ipv4Destination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4Destination'], value)

    @property
    def Ipv4DestinationMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4DestinationMask'])
    @Ipv4DestinationMask.setter
    def Ipv4DestinationMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4DestinationMask'], value)

    @property
    def Ipv4Source(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Source'])
    @Ipv4Source.setter
    def Ipv4Source(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4Source'], value)

    @property
    def Ipv4SourceMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4SourceMask'])
    @Ipv4SourceMask.setter
    def Ipv4SourceMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4SourceMask'], value)

    @property
    def Ipv6Destination(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6Destination'])
    @Ipv6Destination.setter
    def Ipv6Destination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6Destination'], value)

    @property
    def Ipv6DestinationMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6DestinationMask'])
    @Ipv6DestinationMask.setter
    def Ipv6DestinationMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6DestinationMask'], value)

    @property
    def Ipv6ExtHeader(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6ExtHeader'])
    @Ipv6ExtHeader.setter
    def Ipv6ExtHeader(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6ExtHeader'], value)

    @property
    def Ipv6ExtHeaderMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6ExtHeaderMask'])
    @Ipv6ExtHeaderMask.setter
    def Ipv6ExtHeaderMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6ExtHeaderMask'], value)

    @property
    def Ipv6FlowLabel(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6FlowLabel'])
    @Ipv6FlowLabel.setter
    def Ipv6FlowLabel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6FlowLabel'], value)

    @property
    def Ipv6FlowLabelMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6FlowLabelMask'])
    @Ipv6FlowLabelMask.setter
    def Ipv6FlowLabelMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6FlowLabelMask'], value)

    @property
    def Ipv6NdDll(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6NdDll'])
    @Ipv6NdDll.setter
    def Ipv6NdDll(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6NdDll'], value)

    @property
    def Ipv6NdSll(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6NdSll'])
    @Ipv6NdSll.setter
    def Ipv6NdSll(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6NdSll'], value)

    @property
    def Ipv6NdTarget(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6NdTarget'])
    @Ipv6NdTarget.setter
    def Ipv6NdTarget(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6NdTarget'], value)

    @property
    def Ipv6Source(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6Source'])
    @Ipv6Source.setter
    def Ipv6Source(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6Source'], value)

    @property
    def Ipv6SourceMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6SourceMask'])
    @Ipv6SourceMask.setter
    def Ipv6SourceMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6SourceMask'], value)

    @property
    def MatchType(self):
        """
        Returns
        -------
        - str(loose | strict): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MatchType'])
    @MatchType.setter
    def MatchType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MatchType'], value)

    @property
    def Metadata(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Metadata'])
    @Metadata.setter
    def Metadata(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Metadata'], value)

    @property
    def MetadataMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MetadataMask'])
    @MetadataMask.setter
    def MetadataMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MetadataMask'], value)

    @property
    def MplsBos(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsBos'])
    @MplsBos.setter
    def MplsBos(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MplsBos'], value)

    @property
    def MplsLabel(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsLabel'])
    @MplsLabel.setter
    def MplsLabel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MplsLabel'], value)

    @property
    def MplsTc(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsTc'])
    @MplsTc.setter
    def MplsTc(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MplsTc'], value)

    @property
    def NoByteCounts(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoByteCounts'])
    @NoByteCounts.setter
    def NoByteCounts(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoByteCounts'], value)

    @property
    def NoPacketCounts(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoPacketCounts'])
    @NoPacketCounts.setter
    def NoPacketCounts(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoPacketCounts'], value)

    @property
    def NumberOfFlows(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfFlows'])
    @NumberOfFlows.setter
    def NumberOfFlows(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfFlows'], value)

    @property
    def PbbIsId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PbbIsId'])
    @PbbIsId.setter
    def PbbIsId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PbbIsId'], value)

    @property
    def PbbIsIdMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PbbIsIdMask'])
    @PbbIsIdMask.setter
    def PbbIsIdMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PbbIsIdMask'], value)

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
    def ResetCounts(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ResetCounts'])
    @ResetCounts.setter
    def ResetCounts(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ResetCounts'], value)

    @property
    def SctpDestination(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SctpDestination'])
    @SctpDestination.setter
    def SctpDestination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SctpDestination'], value)

    @property
    def SctpSource(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SctpSource'])
    @SctpSource.setter
    def SctpSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SctpSource'], value)

    @property
    def SendFlowRemoved(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendFlowRemoved'])
    @SendFlowRemoved.setter
    def SendFlowRemoved(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendFlowRemoved'], value)

    @property
    def TcpDestination(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TcpDestination'])
    @TcpDestination.setter
    def TcpDestination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TcpDestination'], value)

    @property
    def TcpSource(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TcpSource'])
    @TcpSource.setter
    def TcpSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TcpSource'], value)

    @property
    def TunnelId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelId'])
    @TunnelId.setter
    def TunnelId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TunnelId'], value)

    @property
    def TunnelIdMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelIdMask'])
    @TunnelIdMask.setter
    def TunnelIdMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TunnelIdMask'], value)

    @property
    def UdpDestination(self):
        """
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
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UdpSource'])
    @UdpSource.setter
    def UdpSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UdpSource'], value)

    @property
    def VlanId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanId'])
    @VlanId.setter
    def VlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanId'], value)

    @property
    def VlanIdMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanIdMask'])
    @VlanIdMask.setter
    def VlanIdMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanIdMask'], value)

    @property
    def VlanMatchType(self):
        """
        Returns
        -------
        - str(anyVlanTag | withoutVlanTag | withVlanTag | specificVlanTag): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanMatchType'])
    @VlanMatchType.setter
    def VlanMatchType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanMatchType'], value)

    @property
    def VlanPriority(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanPriority'])
    @VlanPriority.setter
    def VlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanPriority'], value)

    def update(self, ArpDstHwAddr=None, ArpDstHwAddrMask=None, ArpDstIpv4Addr=None, ArpDstIpv4AddrMask=None, ArpOpcode=None, ArpSrcHwAddr=None, ArpSrcHwAddrMask=None, ArpSrcIpv4Addr=None, ArpSrcIpv4AddrMask=None, CheckOverlapFlags=None, Cookie=None, CookieMask=None, Description=None, Enabled=None, EthernetDestination=None, EthernetDestinationMask=None, EthernetSource=None, EthernetSourceMask=None, EthernetType=None, ExperimenterData=None, ExperimenterDatalength=None, ExperimenterField=None, ExperimenterHasMask=None, ExperimenterId=None, FlowAdvertise=None, HardTimeout=None, Icmpv4Code=None, Icmpv4Type=None, Icmpv6Code=None, Icmpv6Type=None, IdleTimeout=None, InPhyPort=None, InPort=None, IpDscp=None, IpEcn=None, IpProtocol=None, Ipv4Destination=None, Ipv4DestinationMask=None, Ipv4Source=None, Ipv4SourceMask=None, Ipv6Destination=None, Ipv6DestinationMask=None, Ipv6ExtHeader=None, Ipv6ExtHeaderMask=None, Ipv6FlowLabel=None, Ipv6FlowLabelMask=None, Ipv6NdDll=None, Ipv6NdSll=None, Ipv6NdTarget=None, Ipv6Source=None, Ipv6SourceMask=None, MatchType=None, Metadata=None, MetadataMask=None, MplsBos=None, MplsLabel=None, MplsTc=None, NoByteCounts=None, NoPacketCounts=None, NumberOfFlows=None, PbbIsId=None, PbbIsIdMask=None, Priority=None, ResetCounts=None, SctpDestination=None, SctpSource=None, SendFlowRemoved=None, TcpDestination=None, TcpSource=None, TunnelId=None, TunnelIdMask=None, UdpDestination=None, UdpSource=None, VlanId=None, VlanIdMask=None, VlanMatchType=None, VlanPriority=None):
        """Updates controllerTableFlowRanges resource on the server.

        Args
        ----
        - ArpDstHwAddr (str): 
        - ArpDstHwAddrMask (str): 
        - ArpDstIpv4Addr (str): 
        - ArpDstIpv4AddrMask (str): 
        - ArpOpcode (str): 
        - ArpSrcHwAddr (str): 
        - ArpSrcHwAddrMask (str): 
        - ArpSrcIpv4Addr (str): 
        - ArpSrcIpv4AddrMask (str): 
        - CheckOverlapFlags (bool): 
        - Cookie (str): 
        - CookieMask (str): 
        - Description (str): 
        - Enabled (bool): 
        - EthernetDestination (str): 
        - EthernetDestinationMask (str): 
        - EthernetSource (str): 
        - EthernetSourceMask (str): 
        - EthernetType (str): 
        - ExperimenterData (str): 
        - ExperimenterDatalength (number): 
        - ExperimenterField (number): 
        - ExperimenterHasMask (bool): 
        - ExperimenterId (str): 
        - FlowAdvertise (bool): 
        - HardTimeout (number): 
        - Icmpv4Code (str): 
        - Icmpv4Type (str): 
        - Icmpv6Code (str): 
        - Icmpv6Type (str): 
        - IdleTimeout (number): 
        - InPhyPort (str): 
        - InPort (str): 
        - IpDscp (str): 
        - IpEcn (str): 
        - IpProtocol (str): 
        - Ipv4Destination (str): 
        - Ipv4DestinationMask (str): 
        - Ipv4Source (str): 
        - Ipv4SourceMask (str): 
        - Ipv6Destination (str): 
        - Ipv6DestinationMask (str): 
        - Ipv6ExtHeader (str): 
        - Ipv6ExtHeaderMask (str): 
        - Ipv6FlowLabel (str): 
        - Ipv6FlowLabelMask (str): 
        - Ipv6NdDll (str): 
        - Ipv6NdSll (str): 
        - Ipv6NdTarget (str): 
        - Ipv6Source (str): 
        - Ipv6SourceMask (str): 
        - MatchType (str(loose | strict)): 
        - Metadata (str): 
        - MetadataMask (str): 
        - MplsBos (str): 
        - MplsLabel (str): 
        - MplsTc (str): 
        - NoByteCounts (bool): 
        - NoPacketCounts (bool): 
        - NumberOfFlows (number): 
        - PbbIsId (str): 
        - PbbIsIdMask (str): 
        - Priority (number): 
        - ResetCounts (bool): 
        - SctpDestination (str): 
        - SctpSource (str): 
        - SendFlowRemoved (bool): 
        - TcpDestination (str): 
        - TcpSource (str): 
        - TunnelId (str): 
        - TunnelIdMask (str): 
        - UdpDestination (str): 
        - UdpSource (str): 
        - VlanId (str): 
        - VlanIdMask (str): 
        - VlanMatchType (str(anyVlanTag | withoutVlanTag | withVlanTag | specificVlanTag)): 
        - VlanPriority (str): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ArpDstHwAddr=None, ArpDstHwAddrMask=None, ArpDstIpv4Addr=None, ArpDstIpv4AddrMask=None, ArpOpcode=None, ArpSrcHwAddr=None, ArpSrcHwAddrMask=None, ArpSrcIpv4Addr=None, ArpSrcIpv4AddrMask=None, CheckOverlapFlags=None, Cookie=None, CookieMask=None, Description=None, Enabled=None, EthernetDestination=None, EthernetDestinationMask=None, EthernetSource=None, EthernetSourceMask=None, EthernetType=None, ExperimenterData=None, ExperimenterDatalength=None, ExperimenterField=None, ExperimenterHasMask=None, ExperimenterId=None, FlowAdvertise=None, HardTimeout=None, Icmpv4Code=None, Icmpv4Type=None, Icmpv6Code=None, Icmpv6Type=None, IdleTimeout=None, InPhyPort=None, InPort=None, IpDscp=None, IpEcn=None, IpProtocol=None, Ipv4Destination=None, Ipv4DestinationMask=None, Ipv4Source=None, Ipv4SourceMask=None, Ipv6Destination=None, Ipv6DestinationMask=None, Ipv6ExtHeader=None, Ipv6ExtHeaderMask=None, Ipv6FlowLabel=None, Ipv6FlowLabelMask=None, Ipv6NdDll=None, Ipv6NdSll=None, Ipv6NdTarget=None, Ipv6Source=None, Ipv6SourceMask=None, MatchType=None, Metadata=None, MetadataMask=None, MplsBos=None, MplsLabel=None, MplsTc=None, NoByteCounts=None, NoPacketCounts=None, NumberOfFlows=None, PbbIsId=None, PbbIsIdMask=None, Priority=None, ResetCounts=None, SctpDestination=None, SctpSource=None, SendFlowRemoved=None, TcpDestination=None, TcpSource=None, TunnelId=None, TunnelIdMask=None, UdpDestination=None, UdpSource=None, VlanId=None, VlanIdMask=None, VlanMatchType=None, VlanPriority=None):
        """Adds a new controllerTableFlowRanges resource on the server and adds it to the container.

        Args
        ----
        - ArpDstHwAddr (str): 
        - ArpDstHwAddrMask (str): 
        - ArpDstIpv4Addr (str): 
        - ArpDstIpv4AddrMask (str): 
        - ArpOpcode (str): 
        - ArpSrcHwAddr (str): 
        - ArpSrcHwAddrMask (str): 
        - ArpSrcIpv4Addr (str): 
        - ArpSrcIpv4AddrMask (str): 
        - CheckOverlapFlags (bool): 
        - Cookie (str): 
        - CookieMask (str): 
        - Description (str): 
        - Enabled (bool): 
        - EthernetDestination (str): 
        - EthernetDestinationMask (str): 
        - EthernetSource (str): 
        - EthernetSourceMask (str): 
        - EthernetType (str): 
        - ExperimenterData (str): 
        - ExperimenterDatalength (number): 
        - ExperimenterField (number): 
        - ExperimenterHasMask (bool): 
        - ExperimenterId (str): 
        - FlowAdvertise (bool): 
        - HardTimeout (number): 
        - Icmpv4Code (str): 
        - Icmpv4Type (str): 
        - Icmpv6Code (str): 
        - Icmpv6Type (str): 
        - IdleTimeout (number): 
        - InPhyPort (str): 
        - InPort (str): 
        - IpDscp (str): 
        - IpEcn (str): 
        - IpProtocol (str): 
        - Ipv4Destination (str): 
        - Ipv4DestinationMask (str): 
        - Ipv4Source (str): 
        - Ipv4SourceMask (str): 
        - Ipv6Destination (str): 
        - Ipv6DestinationMask (str): 
        - Ipv6ExtHeader (str): 
        - Ipv6ExtHeaderMask (str): 
        - Ipv6FlowLabel (str): 
        - Ipv6FlowLabelMask (str): 
        - Ipv6NdDll (str): 
        - Ipv6NdSll (str): 
        - Ipv6NdTarget (str): 
        - Ipv6Source (str): 
        - Ipv6SourceMask (str): 
        - MatchType (str(loose | strict)): 
        - Metadata (str): 
        - MetadataMask (str): 
        - MplsBos (str): 
        - MplsLabel (str): 
        - MplsTc (str): 
        - NoByteCounts (bool): 
        - NoPacketCounts (bool): 
        - NumberOfFlows (number): 
        - PbbIsId (str): 
        - PbbIsIdMask (str): 
        - Priority (number): 
        - ResetCounts (bool): 
        - SctpDestination (str): 
        - SctpSource (str): 
        - SendFlowRemoved (bool): 
        - TcpDestination (str): 
        - TcpSource (str): 
        - TunnelId (str): 
        - TunnelIdMask (str): 
        - UdpDestination (str): 
        - UdpSource (str): 
        - VlanId (str): 
        - VlanIdMask (str): 
        - VlanMatchType (str(anyVlanTag | withoutVlanTag | withVlanTag | specificVlanTag)): 
        - VlanPriority (str): 

        Returns
        -------
        - self: This instance with all currently retrieved controllerTableFlowRanges resources using find and the newly added controllerTableFlowRanges resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained controllerTableFlowRanges resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ArpDstHwAddr=None, ArpDstHwAddrMask=None, ArpDstIpv4Addr=None, ArpDstIpv4AddrMask=None, ArpOpcode=None, ArpSrcHwAddr=None, ArpSrcHwAddrMask=None, ArpSrcIpv4Addr=None, ArpSrcIpv4AddrMask=None, CheckOverlapFlags=None, Cookie=None, CookieMask=None, Description=None, Enabled=None, EthernetDestination=None, EthernetDestinationMask=None, EthernetSource=None, EthernetSourceMask=None, EthernetType=None, ExperimenterData=None, ExperimenterDatalength=None, ExperimenterField=None, ExperimenterHasMask=None, ExperimenterId=None, FlowAdvertise=None, FlowModStatus=None, HardTimeout=None, Icmpv4Code=None, Icmpv4Type=None, Icmpv6Code=None, Icmpv6Type=None, IdleTimeout=None, InPhyPort=None, InPort=None, IpDscp=None, IpEcn=None, IpProtocol=None, Ipv4Destination=None, Ipv4DestinationMask=None, Ipv4Source=None, Ipv4SourceMask=None, Ipv6Destination=None, Ipv6DestinationMask=None, Ipv6ExtHeader=None, Ipv6ExtHeaderMask=None, Ipv6FlowLabel=None, Ipv6FlowLabelMask=None, Ipv6NdDll=None, Ipv6NdSll=None, Ipv6NdTarget=None, Ipv6Source=None, Ipv6SourceMask=None, MatchType=None, Metadata=None, MetadataMask=None, MplsBos=None, MplsLabel=None, MplsTc=None, NoByteCounts=None, NoPacketCounts=None, NumberOfFlows=None, PbbIsId=None, PbbIsIdMask=None, Priority=None, ResetCounts=None, SctpDestination=None, SctpSource=None, SendFlowRemoved=None, TcpDestination=None, TcpSource=None, TunnelId=None, TunnelIdMask=None, UdpDestination=None, UdpSource=None, VlanId=None, VlanIdMask=None, VlanMatchType=None, VlanPriority=None):
        """Finds and retrieves controllerTableFlowRanges resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve controllerTableFlowRanges resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all controllerTableFlowRanges resources from the server.

        Args
        ----
        - ArpDstHwAddr (str): 
        - ArpDstHwAddrMask (str): 
        - ArpDstIpv4Addr (str): 
        - ArpDstIpv4AddrMask (str): 
        - ArpOpcode (str): 
        - ArpSrcHwAddr (str): 
        - ArpSrcHwAddrMask (str): 
        - ArpSrcIpv4Addr (str): 
        - ArpSrcIpv4AddrMask (str): 
        - CheckOverlapFlags (bool): 
        - Cookie (str): 
        - CookieMask (str): 
        - Description (str): 
        - Enabled (bool): 
        - EthernetDestination (str): 
        - EthernetDestinationMask (str): 
        - EthernetSource (str): 
        - EthernetSourceMask (str): 
        - EthernetType (str): 
        - ExperimenterData (str): 
        - ExperimenterDatalength (number): 
        - ExperimenterField (number): 
        - ExperimenterHasMask (bool): 
        - ExperimenterId (str): 
        - FlowAdvertise (bool): 
        - FlowModStatus (str): 
        - HardTimeout (number): 
        - Icmpv4Code (str): 
        - Icmpv4Type (str): 
        - Icmpv6Code (str): 
        - Icmpv6Type (str): 
        - IdleTimeout (number): 
        - InPhyPort (str): 
        - InPort (str): 
        - IpDscp (str): 
        - IpEcn (str): 
        - IpProtocol (str): 
        - Ipv4Destination (str): 
        - Ipv4DestinationMask (str): 
        - Ipv4Source (str): 
        - Ipv4SourceMask (str): 
        - Ipv6Destination (str): 
        - Ipv6DestinationMask (str): 
        - Ipv6ExtHeader (str): 
        - Ipv6ExtHeaderMask (str): 
        - Ipv6FlowLabel (str): 
        - Ipv6FlowLabelMask (str): 
        - Ipv6NdDll (str): 
        - Ipv6NdSll (str): 
        - Ipv6NdTarget (str): 
        - Ipv6Source (str): 
        - Ipv6SourceMask (str): 
        - MatchType (str(loose | strict)): 
        - Metadata (str): 
        - MetadataMask (str): 
        - MplsBos (str): 
        - MplsLabel (str): 
        - MplsTc (str): 
        - NoByteCounts (bool): 
        - NoPacketCounts (bool): 
        - NumberOfFlows (number): 
        - PbbIsId (str): 
        - PbbIsIdMask (str): 
        - Priority (number): 
        - ResetCounts (bool): 
        - SctpDestination (str): 
        - SctpSource (str): 
        - SendFlowRemoved (bool): 
        - TcpDestination (str): 
        - TcpSource (str): 
        - TunnelId (str): 
        - TunnelIdMask (str): 
        - UdpDestination (str): 
        - UdpSource (str): 
        - VlanId (str): 
        - VlanIdMask (str): 
        - VlanMatchType (str(anyVlanTag | withoutVlanTag | withVlanTag | specificVlanTag)): 
        - VlanPriority (str): 

        Returns
        -------
        - self: This instance with matching controllerTableFlowRanges resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of controllerTableFlowRanges data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the controllerTableFlowRanges resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def UpdateFlowMod(self, *args, **kwargs):
        """Executes the updateFlowMod operation on the server.

        updateFlowMod(Arg2=enum)bool
        ----------------------------
        - Arg2 (str(sendFlowAdd | sendFlowModify | sendFlowRemove)): 
        - Returns bool: 

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('updateFlowMod', payload=payload, response_object=None)
