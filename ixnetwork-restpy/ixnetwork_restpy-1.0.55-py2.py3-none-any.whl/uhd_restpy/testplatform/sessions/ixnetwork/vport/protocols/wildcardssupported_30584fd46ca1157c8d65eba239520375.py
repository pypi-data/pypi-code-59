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


class WildcardsSupported(Base):
    """
    The WildcardsSupported class encapsulates a required wildcardsSupported resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'wildcardsSupported'
    _SDM_ATT_MAP = {
        'EthernetDestinationAddress': 'ethernetDestinationAddress',
        'EthernetFrameType': 'ethernetFrameType',
        'EthernetSourceAddress': 'ethernetSourceAddress',
        'IpDestinationAddress': 'ipDestinationAddress',
        'IpProtocol': 'ipProtocol',
        'IpSourceAddress': 'ipSourceAddress',
        'IpTos': 'ipTos',
        'SwitchInputPort': 'switchInputPort',
        'TcpUdpDestinationPort': 'tcpUdpDestinationPort',
        'TcpUdpSourcePort': 'tcpUdpSourcePort',
        'VlanId': 'vlanId',
        'VlanPriority': 'vlanPriority',
    }

    def __init__(self, parent):
        super(WildcardsSupported, self).__init__(parent)

    @property
    def EthernetDestinationAddress(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetDestinationAddress'])
    @EthernetDestinationAddress.setter
    def EthernetDestinationAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetDestinationAddress'], value)

    @property
    def EthernetFrameType(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetFrameType'])
    @EthernetFrameType.setter
    def EthernetFrameType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetFrameType'], value)

    @property
    def EthernetSourceAddress(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetSourceAddress'])
    @EthernetSourceAddress.setter
    def EthernetSourceAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetSourceAddress'], value)

    @property
    def IpDestinationAddress(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpDestinationAddress'])
    @IpDestinationAddress.setter
    def IpDestinationAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpDestinationAddress'], value)

    @property
    def IpProtocol(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpProtocol'])
    @IpProtocol.setter
    def IpProtocol(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpProtocol'], value)

    @property
    def IpSourceAddress(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpSourceAddress'])
    @IpSourceAddress.setter
    def IpSourceAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpSourceAddress'], value)

    @property
    def IpTos(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpTos'])
    @IpTos.setter
    def IpTos(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpTos'], value)

    @property
    def SwitchInputPort(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SwitchInputPort'])
    @SwitchInputPort.setter
    def SwitchInputPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SwitchInputPort'], value)

    @property
    def TcpUdpDestinationPort(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TcpUdpDestinationPort'])
    @TcpUdpDestinationPort.setter
    def TcpUdpDestinationPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TcpUdpDestinationPort'], value)

    @property
    def TcpUdpSourcePort(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TcpUdpSourcePort'])
    @TcpUdpSourcePort.setter
    def TcpUdpSourcePort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TcpUdpSourcePort'], value)

    @property
    def VlanId(self):
        """
        Returns
        -------
        - bool: 
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
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanPriority'])
    @VlanPriority.setter
    def VlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanPriority'], value)

    def update(self, EthernetDestinationAddress=None, EthernetFrameType=None, EthernetSourceAddress=None, IpDestinationAddress=None, IpProtocol=None, IpSourceAddress=None, IpTos=None, SwitchInputPort=None, TcpUdpDestinationPort=None, TcpUdpSourcePort=None, VlanId=None, VlanPriority=None):
        """Updates wildcardsSupported resource on the server.

        Args
        ----
        - EthernetDestinationAddress (bool): 
        - EthernetFrameType (bool): 
        - EthernetSourceAddress (bool): 
        - IpDestinationAddress (bool): 
        - IpProtocol (bool): 
        - IpSourceAddress (bool): 
        - IpTos (bool): 
        - SwitchInputPort (bool): 
        - TcpUdpDestinationPort (bool): 
        - TcpUdpSourcePort (bool): 
        - VlanId (bool): 
        - VlanPriority (bool): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
