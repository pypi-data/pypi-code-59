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


class FlowStatLearnedInformation(Base):
    """
    The FlowStatLearnedInformation class encapsulates a list of flowStatLearnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the FlowStatLearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'flowStatLearnedInformation'
    _SDM_ATT_MAP = {
        'ActiveNanoSeconds': 'activeNanoSeconds',
        'ActiveSeconds': 'activeSeconds',
        'ApplyActionsInstruction': 'applyActionsInstruction',
        'ApplyMeterInstruction': 'applyMeterInstruction',
        'ArpDstHwAddr': 'arpDstHwAddr',
        'ArpDstHwAddressMask': 'arpDstHwAddressMask',
        'ArpDstIpv4Address': 'arpDstIpv4Address',
        'ArpDstIpv4AddressMask': 'arpDstIpv4AddressMask',
        'ArpOpcode': 'arpOpcode',
        'ArpSrcHwAddr': 'arpSrcHwAddr',
        'ArpSrcHwAddressMask': 'arpSrcHwAddressMask',
        'ArpSrcIpv4Address': 'arpSrcIpv4Address',
        'ArpSrcIpv4AddressMask': 'arpSrcIpv4AddressMask',
        'BytesCount': 'bytesCount',
        'ClearActionsInstruction': 'clearActionsInstruction',
        'Cookie': 'cookie',
        'CookieMask': 'cookieMask',
        'DataPathId': 'dataPathId',
        'DataPathIdAsHex': 'dataPathIdAsHex',
        'ErrorCode': 'errorCode',
        'ErrorType': 'errorType',
        'EthernetDestination': 'ethernetDestination',
        'EthernetDestinationMask': 'ethernetDestinationMask',
        'EthernetSource': 'ethernetSource',
        'EthernetSourceMask': 'ethernetSourceMask',
        'EthernetType': 'ethernetType',
        'ExperimenterData': 'experimenterData',
        'ExperimenterDataLength': 'experimenterDataLength',
        'ExperimenterField': 'experimenterField',
        'ExperimenterHashmask': 'experimenterHashmask',
        'ExperimenterId': 'experimenterId',
        'ExperimenterInstruction': 'experimenterInstruction',
        'Flags': 'flags',
        'GoToTableInstruction': 'goToTableInstruction',
        'HardTimeout': 'hardTimeout',
        'Icmpv4Code': 'icmpv4Code',
        'Icmpv4Type': 'icmpv4Type',
        'Icmpv6Code': 'icmpv6Code',
        'Icmpv6Type': 'icmpv6Type',
        'IdleTimeout': 'idleTimeout',
        'InPort': 'inPort',
        'IpDscp': 'ipDscp',
        'IpEcn': 'ipEcn',
        'IpProtocol': 'ipProtocol',
        'Ipv4Destination': 'ipv4Destination',
        'Ipv4Source': 'ipv4Source',
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
        'Latency': 'latency',
        'LocalIp': 'localIp',
        'Metadata': 'metadata',
        'MetadataMask': 'metadataMask',
        'MplsBos': 'mplsBos',
        'MplsLabel': 'mplsLabel',
        'MplsTc': 'mplsTc',
        'NegotiatedVersion': 'negotiatedVersion',
        'NoOfApplyActions': 'noOfApplyActions',
        'NoOfWriteActions': 'noOfWriteActions',
        'NumberOfActions': 'numberOfActions',
        'OutGroup': 'outGroup',
        'OutPort': 'outPort',
        'PacketsCount': 'packetsCount',
        'PbbISid': 'pbbISid',
        'PbbISidMask': 'pbbISidMask',
        'PhysicalInPort': 'physicalInPort',
        'Priority': 'priority',
        'RemoteIp': 'remoteIp',
        'ReplyState': 'replyState',
        'SctpDestination': 'sctpDestination',
        'SctpSource': 'sctpSource',
        'TableId': 'tableId',
        'TcpDestination': 'tcpDestination',
        'TcpSource': 'tcpSource',
        'TransportDestinationIcmpCode': 'transportDestinationIcmpCode',
        'TransportSourceIcmpType': 'transportSourceIcmpType',
        'TunnelId': 'tunnelId',
        'TunnelIdMask': 'tunnelIdMask',
        'UdpDestination': 'udpDestination',
        'UdpSource': 'udpSource',
        'VlanId': 'vlanId',
        'VlanMask': 'vlanMask',
        'VlanPriority': 'vlanPriority',
        'WriteActionsInstruction': 'writeActionsInstruction',
        'WriteMetadataInstruction': 'writeMetadataInstruction',
    }

    def __init__(self, parent):
        super(FlowStatLearnedInformation, self).__init__(parent)

    @property
    def ActiveNanoSeconds(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActiveNanoSeconds'])

    @property
    def ActiveSeconds(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActiveSeconds'])

    @property
    def ApplyActionsInstruction(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApplyActionsInstruction'])

    @property
    def ApplyMeterInstruction(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApplyMeterInstruction'])

    @property
    def ArpDstHwAddr(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpDstHwAddr'])

    @property
    def ArpDstHwAddressMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpDstHwAddressMask'])

    @property
    def ArpDstIpv4Address(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpDstIpv4Address'])

    @property
    def ArpDstIpv4AddressMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpDstIpv4AddressMask'])

    @property
    def ArpOpcode(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpOpcode'])

    @property
    def ArpSrcHwAddr(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpSrcHwAddr'])

    @property
    def ArpSrcHwAddressMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpSrcHwAddressMask'])

    @property
    def ArpSrcIpv4Address(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpSrcIpv4Address'])

    @property
    def ArpSrcIpv4AddressMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpSrcIpv4AddressMask'])

    @property
    def BytesCount(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BytesCount'])

    @property
    def ClearActionsInstruction(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ClearActionsInstruction'])

    @property
    def Cookie(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Cookie'])

    @property
    def CookieMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CookieMask'])

    @property
    def DataPathId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathId'])

    @property
    def DataPathIdAsHex(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathIdAsHex'])

    @property
    def ErrorCode(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrorCode'])

    @property
    def ErrorType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrorType'])

    @property
    def EthernetDestination(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetDestination'])

    @property
    def EthernetDestinationMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetDestinationMask'])

    @property
    def EthernetSource(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetSource'])

    @property
    def EthernetSourceMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetSourceMask'])

    @property
    def EthernetType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetType'])

    @property
    def ExperimenterData(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterData'])

    @property
    def ExperimenterDataLength(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterDataLength'])

    @property
    def ExperimenterField(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterField'])

    @property
    def ExperimenterHashmask(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterHashmask'])

    @property
    def ExperimenterId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterId'])

    @property
    def ExperimenterInstruction(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterInstruction'])

    @property
    def Flags(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Flags'])

    @property
    def GoToTableInstruction(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['GoToTableInstruction'])

    @property
    def HardTimeout(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['HardTimeout'])

    @property
    def Icmpv4Code(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Icmpv4Code'])

    @property
    def Icmpv4Type(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Icmpv4Type'])

    @property
    def Icmpv6Code(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Icmpv6Code'])

    @property
    def Icmpv6Type(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Icmpv6Type'])

    @property
    def IdleTimeout(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IdleTimeout'])

    @property
    def InPort(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InPort'])

    @property
    def IpDscp(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpDscp'])

    @property
    def IpEcn(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpEcn'])

    @property
    def IpProtocol(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpProtocol'])

    @property
    def Ipv4Destination(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Destination'])

    @property
    def Ipv4Source(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Source'])

    @property
    def Ipv6Destination(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6Destination'])

    @property
    def Ipv6DestinationMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6DestinationMask'])

    @property
    def Ipv6ExtHeader(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6ExtHeader'])

    @property
    def Ipv6ExtHeaderMask(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6ExtHeaderMask'])

    @property
    def Ipv6FlowLabel(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6FlowLabel'])

    @property
    def Ipv6FlowLabelMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6FlowLabelMask'])

    @property
    def Ipv6NdDll(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6NdDll'])

    @property
    def Ipv6NdSll(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6NdSll'])

    @property
    def Ipv6NdTarget(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6NdTarget'])

    @property
    def Ipv6Source(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6Source'])

    @property
    def Ipv6SourceMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6SourceMask'])

    @property
    def Latency(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Latency'])

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalIp'])

    @property
    def Metadata(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Metadata'])

    @property
    def MetadataMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MetadataMask'])

    @property
    def MplsBos(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsBos'])

    @property
    def MplsLabel(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsLabel'])

    @property
    def MplsTc(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsTc'])

    @property
    def NegotiatedVersion(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NegotiatedVersion'])

    @property
    def NoOfApplyActions(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfApplyActions'])

    @property
    def NoOfWriteActions(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfWriteActions'])

    @property
    def NumberOfActions(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfActions'])

    @property
    def OutGroup(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutGroup'])

    @property
    def OutPort(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutPort'])

    @property
    def PacketsCount(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketsCount'])

    @property
    def PbbISid(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PbbISid'])

    @property
    def PbbISidMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PbbISidMask'])

    @property
    def PhysicalInPort(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PhysicalInPort'])

    @property
    def Priority(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Priority'])

    @property
    def RemoteIp(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteIp'])

    @property
    def ReplyState(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReplyState'])

    @property
    def SctpDestination(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SctpDestination'])

    @property
    def SctpSource(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SctpSource'])

    @property
    def TableId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TableId'])

    @property
    def TcpDestination(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TcpDestination'])

    @property
    def TcpSource(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TcpSource'])

    @property
    def TransportDestinationIcmpCode(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransportDestinationIcmpCode'])

    @property
    def TransportSourceIcmpType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransportSourceIcmpType'])

    @property
    def TunnelId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelId'])

    @property
    def TunnelIdMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelIdMask'])

    @property
    def UdpDestination(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UdpDestination'])

    @property
    def UdpSource(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UdpSource'])

    @property
    def VlanId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanId'])

    @property
    def VlanMask(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanMask'])

    @property
    def VlanPriority(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanPriority'])

    @property
    def WriteActionsInstruction(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['WriteActionsInstruction'])

    @property
    def WriteMetadataInstruction(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['WriteMetadataInstruction'])

    def find(self, ActiveNanoSeconds=None, ActiveSeconds=None, ApplyActionsInstruction=None, ApplyMeterInstruction=None, ArpDstHwAddr=None, ArpDstHwAddressMask=None, ArpDstIpv4Address=None, ArpDstIpv4AddressMask=None, ArpOpcode=None, ArpSrcHwAddr=None, ArpSrcHwAddressMask=None, ArpSrcIpv4Address=None, ArpSrcIpv4AddressMask=None, BytesCount=None, ClearActionsInstruction=None, Cookie=None, CookieMask=None, DataPathId=None, DataPathIdAsHex=None, ErrorCode=None, ErrorType=None, EthernetDestination=None, EthernetDestinationMask=None, EthernetSource=None, EthernetSourceMask=None, EthernetType=None, ExperimenterData=None, ExperimenterDataLength=None, ExperimenterField=None, ExperimenterHashmask=None, ExperimenterId=None, ExperimenterInstruction=None, Flags=None, GoToTableInstruction=None, HardTimeout=None, Icmpv4Code=None, Icmpv4Type=None, Icmpv6Code=None, Icmpv6Type=None, IdleTimeout=None, InPort=None, IpDscp=None, IpEcn=None, IpProtocol=None, Ipv4Destination=None, Ipv4Source=None, Ipv6Destination=None, Ipv6DestinationMask=None, Ipv6ExtHeader=None, Ipv6ExtHeaderMask=None, Ipv6FlowLabel=None, Ipv6FlowLabelMask=None, Ipv6NdDll=None, Ipv6NdSll=None, Ipv6NdTarget=None, Ipv6Source=None, Ipv6SourceMask=None, Latency=None, LocalIp=None, Metadata=None, MetadataMask=None, MplsBos=None, MplsLabel=None, MplsTc=None, NegotiatedVersion=None, NoOfApplyActions=None, NoOfWriteActions=None, NumberOfActions=None, OutGroup=None, OutPort=None, PacketsCount=None, PbbISid=None, PbbISidMask=None, PhysicalInPort=None, Priority=None, RemoteIp=None, ReplyState=None, SctpDestination=None, SctpSource=None, TableId=None, TcpDestination=None, TcpSource=None, TransportDestinationIcmpCode=None, TransportSourceIcmpType=None, TunnelId=None, TunnelIdMask=None, UdpDestination=None, UdpSource=None, VlanId=None, VlanMask=None, VlanPriority=None, WriteActionsInstruction=None, WriteMetadataInstruction=None):
        """Finds and retrieves flowStatLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve flowStatLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all flowStatLearnedInformation resources from the server.

        Args
        ----
        - ActiveNanoSeconds (number): 
        - ActiveSeconds (number): 
        - ApplyActionsInstruction (str): 
        - ApplyMeterInstruction (str): 
        - ArpDstHwAddr (str): 
        - ArpDstHwAddressMask (str): 
        - ArpDstIpv4Address (str): 
        - ArpDstIpv4AddressMask (str): 
        - ArpOpcode (str): 
        - ArpSrcHwAddr (str): 
        - ArpSrcHwAddressMask (str): 
        - ArpSrcIpv4Address (str): 
        - ArpSrcIpv4AddressMask (str): 
        - BytesCount (str): 
        - ClearActionsInstruction (str): 
        - Cookie (str): 
        - CookieMask (str): 
        - DataPathId (str): 
        - DataPathIdAsHex (str): 
        - ErrorCode (str): 
        - ErrorType (str): 
        - EthernetDestination (str): 
        - EthernetDestinationMask (str): 
        - EthernetSource (str): 
        - EthernetSourceMask (str): 
        - EthernetType (str): 
        - ExperimenterData (str): 
        - ExperimenterDataLength (number): 
        - ExperimenterField (number): 
        - ExperimenterHashmask (bool): 
        - ExperimenterId (str): 
        - ExperimenterInstruction (str): 
        - Flags (str): 
        - GoToTableInstruction (str): 
        - HardTimeout (number): 
        - Icmpv4Code (str): 
        - Icmpv4Type (str): 
        - Icmpv6Code (str): 
        - Icmpv6Type (str): 
        - IdleTimeout (number): 
        - InPort (str): 
        - IpDscp (str): 
        - IpEcn (str): 
        - IpProtocol (str): 
        - Ipv4Destination (str): 
        - Ipv4Source (str): 
        - Ipv6Destination (str): 
        - Ipv6DestinationMask (str): 
        - Ipv6ExtHeader (number): 
        - Ipv6ExtHeaderMask (number): 
        - Ipv6FlowLabel (str): 
        - Ipv6FlowLabelMask (str): 
        - Ipv6NdDll (str): 
        - Ipv6NdSll (str): 
        - Ipv6NdTarget (str): 
        - Ipv6Source (str): 
        - Ipv6SourceMask (str): 
        - Latency (number): 
        - LocalIp (str): 
        - Metadata (str): 
        - MetadataMask (str): 
        - MplsBos (str): 
        - MplsLabel (str): 
        - MplsTc (str): 
        - NegotiatedVersion (str): 
        - NoOfApplyActions (str): 
        - NoOfWriteActions (str): 
        - NumberOfActions (str): 
        - OutGroup (number): 
        - OutPort (number): 
        - PacketsCount (str): 
        - PbbISid (str): 
        - PbbISidMask (str): 
        - PhysicalInPort (str): 
        - Priority (number): 
        - RemoteIp (str): 
        - ReplyState (str): 
        - SctpDestination (str): 
        - SctpSource (str): 
        - TableId (str): 
        - TcpDestination (str): 
        - TcpSource (str): 
        - TransportDestinationIcmpCode (str): 
        - TransportSourceIcmpType (str): 
        - TunnelId (str): 
        - TunnelIdMask (str): 
        - UdpDestination (str): 
        - UdpSource (str): 
        - VlanId (str): 
        - VlanMask (number): 
        - VlanPriority (str): 
        - WriteActionsInstruction (str): 
        - WriteMetadataInstruction (str): 

        Returns
        -------
        - self: This instance with matching flowStatLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of flowStatLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the flowStatLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
