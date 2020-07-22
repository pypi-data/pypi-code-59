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


class FlowAggregatedStatMatchCriteria131TriggerAttributes(Base):
    """
    The FlowAggregatedStatMatchCriteria131TriggerAttributes class encapsulates a required flowAggregatedStatMatchCriteria131TriggerAttributes resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'flowAggregatedStatMatchCriteria131TriggerAttributes'
    _SDM_ATT_MAP = {
        'ArpDstHwAddr': 'arpDstHwAddr',
        'ArpDstIpv4Addr': 'arpDstIpv4Addr',
        'ArpOpcode': 'arpOpcode',
        'ArpSrcHwAddr': 'arpSrcHwAddr',
        'ArpSrcIpv4Addr': 'arpSrcIpv4Addr',
        'Cookie': 'cookie',
        'EthernetDestination': 'ethernetDestination',
        'EthernetSource': 'ethernetSource',
        'EthernetType': 'ethernetType',
        'ExperimenterData': 'experimenterData',
        'ExperimenterDataLength': 'experimenterDataLength',
        'ExperimenterField': 'experimenterField',
        'ExperimenterHashmask': 'experimenterHashmask',
        'ExperimenterId': 'experimenterId',
        'Icmpv4Code': 'icmpv4Code',
        'Icmpv4Type': 'icmpv4Type',
        'Icmpv6Code': 'icmpv6Code',
        'Icmpv6Type': 'icmpv6Type',
        'InPort': 'inPort',
        'IpDscp': 'ipDscp',
        'IpEcn': 'ipEcn',
        'IpProtocol': 'ipProtocol',
        'Ipv4Destination': 'ipv4Destination',
        'Ipv4Source': 'ipv4Source',
        'Ipv6Destination': 'ipv6Destination',
        'Ipv6ExtHeader': 'ipv6ExtHeader',
        'Ipv6FlowLabel': 'ipv6FlowLabel',
        'Ipv6NdDll': 'ipv6NdDll',
        'Ipv6NdSll': 'ipv6NdSll',
        'Ipv6NdTarget': 'ipv6NdTarget',
        'Ipv6Source': 'ipv6Source',
        'MetaData': 'metaData',
        'MplsBos': 'mplsBos',
        'MplsLabel': 'mplsLabel',
        'MplsTc': 'mplsTc',
        'PbbISid': 'pbbISid',
        'PhysicalInPort': 'physicalInPort',
        'SctpDestination': 'sctpDestination',
        'SctpSource': 'sctpSource',
        'TcpDestination': 'tcpDestination',
        'TcpSource': 'tcpSource',
        'TunnelId': 'tunnelId',
        'UdpDestination': 'udpDestination',
        'UdpSource': 'udpSource',
        'VlanId': 'vlanId',
        'VlanPriority': 'vlanPriority',
    }

    def __init__(self, parent):
        super(FlowAggregatedStatMatchCriteria131TriggerAttributes, self).__init__(parent)

    @property
    def ArpDstHwAddr(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpDstHwAddr'])
    @ArpDstHwAddr.setter
    def ArpDstHwAddr(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpDstHwAddr'], value)

    @property
    def ArpDstIpv4Addr(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpDstIpv4Addr'])
    @ArpDstIpv4Addr.setter
    def ArpDstIpv4Addr(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpDstIpv4Addr'], value)

    @property
    def ArpOpcode(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): 
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
        - dict(arg1:str,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpSrcHwAddr'])
    @ArpSrcHwAddr.setter
    def ArpSrcHwAddr(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpSrcHwAddr'], value)

    @property
    def ArpSrcIpv4Addr(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpSrcIpv4Addr'])
    @ArpSrcIpv4Addr.setter
    def ArpSrcIpv4Addr(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpSrcIpv4Addr'], value)

    @property
    def Cookie(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Cookie'])
    @Cookie.setter
    def Cookie(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Cookie'], value)

    @property
    def EthernetDestination(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetDestination'])
    @EthernetDestination.setter
    def EthernetDestination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetDestination'], value)

    @property
    def EthernetSource(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetSource'])
    @EthernetSource.setter
    def EthernetSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetSource'], value)

    @property
    def EthernetType(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): 
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
        - dict(arg1:str,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterData'])
    @ExperimenterData.setter
    def ExperimenterData(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterData'], value)

    @property
    def ExperimenterDataLength(self):
        """
        Returns
        -------
        - dict(arg1:number,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterDataLength'])
    @ExperimenterDataLength.setter
    def ExperimenterDataLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterDataLength'], value)

    @property
    def ExperimenterField(self):
        """
        Returns
        -------
        - dict(arg1:number,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterField'])
    @ExperimenterField.setter
    def ExperimenterField(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterField'], value)

    @property
    def ExperimenterHashmask(self):
        """
        Returns
        -------
        - dict(arg1:bool,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterHashmask'])
    @ExperimenterHashmask.setter
    def ExperimenterHashmask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterHashmask'], value)

    @property
    def ExperimenterId(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterId'])
    @ExperimenterId.setter
    def ExperimenterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterId'], value)

    @property
    def Icmpv4Code(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): 
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
        - dict(arg1:str,arg2:str): 
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
        - dict(arg1:str,arg2:str): 
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
        - dict(arg1:str,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Icmpv6Type'])
    @Icmpv6Type.setter
    def Icmpv6Type(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Icmpv6Type'], value)

    @property
    def InPort(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): 
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
        - dict(arg1:str,arg2:str): 
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
        - dict(arg1:str,arg2:str): 
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
        - dict(arg1:str,arg2:str): 
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
        - dict(arg1:str,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Destination'])
    @Ipv4Destination.setter
    def Ipv4Destination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4Destination'], value)

    @property
    def Ipv4Source(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Source'])
    @Ipv4Source.setter
    def Ipv4Source(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4Source'], value)

    @property
    def Ipv6Destination(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6Destination'])
    @Ipv6Destination.setter
    def Ipv6Destination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6Destination'], value)

    @property
    def Ipv6ExtHeader(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6ExtHeader'])
    @Ipv6ExtHeader.setter
    def Ipv6ExtHeader(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6ExtHeader'], value)

    @property
    def Ipv6FlowLabel(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6FlowLabel'])
    @Ipv6FlowLabel.setter
    def Ipv6FlowLabel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6FlowLabel'], value)

    @property
    def Ipv6NdDll(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): 
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
        - dict(arg1:str,arg2:str): 
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
        - dict(arg1:str,arg2:str): 
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
        - dict(arg1:str,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6Source'])
    @Ipv6Source.setter
    def Ipv6Source(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6Source'], value)

    @property
    def MetaData(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MetaData'])
    @MetaData.setter
    def MetaData(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MetaData'], value)

    @property
    def MplsBos(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): 
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
        - dict(arg1:str,arg2:str): 
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
        - dict(arg1:str,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsTc'])
    @MplsTc.setter
    def MplsTc(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MplsTc'], value)

    @property
    def PbbISid(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PbbISid'])
    @PbbISid.setter
    def PbbISid(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PbbISid'], value)

    @property
    def PhysicalInPort(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PhysicalInPort'])
    @PhysicalInPort.setter
    def PhysicalInPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PhysicalInPort'], value)

    @property
    def SctpDestination(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): 
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
        - dict(arg1:str,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SctpSource'])
    @SctpSource.setter
    def SctpSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SctpSource'], value)

    @property
    def TcpDestination(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): 
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
        - dict(arg1:str,arg2:str): 
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
        - dict(arg1:str,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelId'])
    @TunnelId.setter
    def TunnelId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TunnelId'], value)

    @property
    def UdpDestination(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): 
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
        - dict(arg1:str,arg2:str): 
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
        - dict(arg1:str,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanId'])
    @VlanId.setter
    def VlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanId'], value)

    @property
    def VlanPriority(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanPriority'])
    @VlanPriority.setter
    def VlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanPriority'], value)

    def update(self, ArpDstHwAddr=None, ArpDstIpv4Addr=None, ArpOpcode=None, ArpSrcHwAddr=None, ArpSrcIpv4Addr=None, Cookie=None, EthernetDestination=None, EthernetSource=None, EthernetType=None, ExperimenterData=None, ExperimenterDataLength=None, ExperimenterField=None, ExperimenterHashmask=None, ExperimenterId=None, Icmpv4Code=None, Icmpv4Type=None, Icmpv6Code=None, Icmpv6Type=None, InPort=None, IpDscp=None, IpEcn=None, IpProtocol=None, Ipv4Destination=None, Ipv4Source=None, Ipv6Destination=None, Ipv6ExtHeader=None, Ipv6FlowLabel=None, Ipv6NdDll=None, Ipv6NdSll=None, Ipv6NdTarget=None, Ipv6Source=None, MetaData=None, MplsBos=None, MplsLabel=None, MplsTc=None, PbbISid=None, PhysicalInPort=None, SctpDestination=None, SctpSource=None, TcpDestination=None, TcpSource=None, TunnelId=None, UdpDestination=None, UdpSource=None, VlanId=None, VlanPriority=None):
        """Updates flowAggregatedStatMatchCriteria131TriggerAttributes resource on the server.

        Args
        ----
        - ArpDstHwAddr (dict(arg1:str,arg2:str)): 
        - ArpDstIpv4Addr (dict(arg1:str,arg2:str)): 
        - ArpOpcode (dict(arg1:str,arg2:str)): 
        - ArpSrcHwAddr (dict(arg1:str,arg2:str)): 
        - ArpSrcIpv4Addr (dict(arg1:str,arg2:str)): 
        - Cookie (dict(arg1:str,arg2:str)): 
        - EthernetDestination (dict(arg1:str,arg2:str)): 
        - EthernetSource (dict(arg1:str,arg2:str)): 
        - EthernetType (dict(arg1:str,arg2:str)): 
        - ExperimenterData (dict(arg1:str,arg2:str)): 
        - ExperimenterDataLength (dict(arg1:number,arg2:str)): 
        - ExperimenterField (dict(arg1:number,arg2:str)): 
        - ExperimenterHashmask (dict(arg1:bool,arg2:str)): 
        - ExperimenterId (dict(arg1:str,arg2:str)): 
        - Icmpv4Code (dict(arg1:str,arg2:str)): 
        - Icmpv4Type (dict(arg1:str,arg2:str)): 
        - Icmpv6Code (dict(arg1:str,arg2:str)): 
        - Icmpv6Type (dict(arg1:str,arg2:str)): 
        - InPort (dict(arg1:str,arg2:str)): 
        - IpDscp (dict(arg1:str,arg2:str)): 
        - IpEcn (dict(arg1:str,arg2:str)): 
        - IpProtocol (dict(arg1:str,arg2:str)): 
        - Ipv4Destination (dict(arg1:str,arg2:str)): 
        - Ipv4Source (dict(arg1:str,arg2:str)): 
        - Ipv6Destination (dict(arg1:str,arg2:str)): 
        - Ipv6ExtHeader (dict(arg1:str,arg2:str)): 
        - Ipv6FlowLabel (dict(arg1:str,arg2:str)): 
        - Ipv6NdDll (dict(arg1:str,arg2:str)): 
        - Ipv6NdSll (dict(arg1:str,arg2:str)): 
        - Ipv6NdTarget (dict(arg1:str,arg2:str)): 
        - Ipv6Source (dict(arg1:str,arg2:str)): 
        - MetaData (dict(arg1:str,arg2:str)): 
        - MplsBos (dict(arg1:str,arg2:str)): 
        - MplsLabel (dict(arg1:str,arg2:str)): 
        - MplsTc (dict(arg1:str,arg2:str)): 
        - PbbISid (dict(arg1:str,arg2:str)): 
        - PhysicalInPort (dict(arg1:str,arg2:str)): 
        - SctpDestination (dict(arg1:str,arg2:str)): 
        - SctpSource (dict(arg1:str,arg2:str)): 
        - TcpDestination (dict(arg1:str,arg2:str)): 
        - TcpSource (dict(arg1:str,arg2:str)): 
        - TunnelId (dict(arg1:str,arg2:str)): 
        - UdpDestination (dict(arg1:str,arg2:str)): 
        - UdpSource (dict(arg1:str,arg2:str)): 
        - VlanId (dict(arg1:str,arg2:str)): 
        - VlanPriority (dict(arg1:str,arg2:str)): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
