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


class DhcpV4DiscoveredInfo(Base):
    """
    The DhcpV4DiscoveredInfo class encapsulates a required dhcpV4DiscoveredInfo resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcpV4DiscoveredInfo'
    _SDM_ATT_MAP = {
        'Gateway': 'gateway',
        'Ipv4Address': 'ipv4Address',
        'Ipv4Mask': 'ipv4Mask',
        'IsDhcpV4LearnedInfoRefreshed': 'isDhcpV4LearnedInfoRefreshed',
        'LeaseDuration': 'leaseDuration',
        'ProtocolInterface': 'protocolInterface',
        'Tlv': 'tlv',
    }

    def __init__(self, parent):
        super(DhcpV4DiscoveredInfo, self).__init__(parent)

    @property
    def Gateway(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Gateway'])

    @property
    def Ipv4Address(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Address'])

    @property
    def Ipv4Mask(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Mask'])

    @property
    def IsDhcpV4LearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsDhcpV4LearnedInfoRefreshed'])

    @property
    def LeaseDuration(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LeaseDuration'])

    @property
    def ProtocolInterface(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolInterface'])

    @property
    def Tlv(self):
        """
        Returns
        -------
        - list(dict(arg1:number,arg2:str)): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Tlv'])
