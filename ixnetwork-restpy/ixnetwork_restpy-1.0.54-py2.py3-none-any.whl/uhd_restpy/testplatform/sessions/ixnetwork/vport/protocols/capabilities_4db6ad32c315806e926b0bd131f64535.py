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


class Capabilities(Base):
    """
    The Capabilities class encapsulates a required capabilities resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'capabilities'
    _SDM_ATT_MAP = {
        'AdVpls': 'adVpls',
        'Evpn': 'evpn',
        'FetchDetailedIpV4UnicastInfo': 'fetchDetailedIpV4UnicastInfo',
        'FetchDetailedIpV6UnicastInfo': 'fetchDetailedIpV6UnicastInfo',
        'IpV4Mpls': 'ipV4Mpls',
        'IpV4MplsVpn': 'ipV4MplsVpn',
        'IpV4Multicast': 'ipV4Multicast',
        'IpV4MulticastMplsVpn': 'ipV4MulticastMplsVpn',
        'IpV4MulticastVpn': 'ipV4MulticastVpn',
        'IpV4Unicast': 'ipV4Unicast',
        'IpV6Mpls': 'ipV6Mpls',
        'IpV6MplsVpn': 'ipV6MplsVpn',
        'IpV6Multicast': 'ipV6Multicast',
        'IpV6MulticastMplsVpn': 'ipV6MulticastMplsVpn',
        'IpV6MulticastVpn': 'ipV6MulticastVpn',
        'IpV6Unicast': 'ipV6Unicast',
        'Vpls': 'vpls',
    }

    def __init__(self, parent):
        super(Capabilities, self).__init__(parent)

    @property
    def AdVpls(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdVpls'])
    @AdVpls.setter
    def AdVpls(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AdVpls'], value)

    @property
    def Evpn(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Evpn'])
    @Evpn.setter
    def Evpn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Evpn'], value)

    @property
    def FetchDetailedIpV4UnicastInfo(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FetchDetailedIpV4UnicastInfo'])
    @FetchDetailedIpV4UnicastInfo.setter
    def FetchDetailedIpV4UnicastInfo(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FetchDetailedIpV4UnicastInfo'], value)

    @property
    def FetchDetailedIpV6UnicastInfo(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FetchDetailedIpV6UnicastInfo'])
    @FetchDetailedIpV6UnicastInfo.setter
    def FetchDetailedIpV6UnicastInfo(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FetchDetailedIpV6UnicastInfo'], value)

    @property
    def IpV4Mpls(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpV4Mpls'])
    @IpV4Mpls.setter
    def IpV4Mpls(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpV4Mpls'], value)

    @property
    def IpV4MplsVpn(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpV4MplsVpn'])
    @IpV4MplsVpn.setter
    def IpV4MplsVpn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpV4MplsVpn'], value)

    @property
    def IpV4Multicast(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpV4Multicast'])
    @IpV4Multicast.setter
    def IpV4Multicast(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpV4Multicast'], value)

    @property
    def IpV4MulticastMplsVpn(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpV4MulticastMplsVpn'])
    @IpV4MulticastMplsVpn.setter
    def IpV4MulticastMplsVpn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpV4MulticastMplsVpn'], value)

    @property
    def IpV4MulticastVpn(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpV4MulticastVpn'])
    @IpV4MulticastVpn.setter
    def IpV4MulticastVpn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpV4MulticastVpn'], value)

    @property
    def IpV4Unicast(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpV4Unicast'])
    @IpV4Unicast.setter
    def IpV4Unicast(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpV4Unicast'], value)

    @property
    def IpV6Mpls(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpV6Mpls'])
    @IpV6Mpls.setter
    def IpV6Mpls(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpV6Mpls'], value)

    @property
    def IpV6MplsVpn(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpV6MplsVpn'])
    @IpV6MplsVpn.setter
    def IpV6MplsVpn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpV6MplsVpn'], value)

    @property
    def IpV6Multicast(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpV6Multicast'])
    @IpV6Multicast.setter
    def IpV6Multicast(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpV6Multicast'], value)

    @property
    def IpV6MulticastMplsVpn(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpV6MulticastMplsVpn'])
    @IpV6MulticastMplsVpn.setter
    def IpV6MulticastMplsVpn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpV6MulticastMplsVpn'], value)

    @property
    def IpV6MulticastVpn(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpV6MulticastVpn'])
    @IpV6MulticastVpn.setter
    def IpV6MulticastVpn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpV6MulticastVpn'], value)

    @property
    def IpV6Unicast(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpV6Unicast'])
    @IpV6Unicast.setter
    def IpV6Unicast(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpV6Unicast'], value)

    @property
    def Vpls(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Vpls'])
    @Vpls.setter
    def Vpls(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Vpls'], value)

    def update(self, AdVpls=None, Evpn=None, FetchDetailedIpV4UnicastInfo=None, FetchDetailedIpV6UnicastInfo=None, IpV4Mpls=None, IpV4MplsVpn=None, IpV4Multicast=None, IpV4MulticastMplsVpn=None, IpV4MulticastVpn=None, IpV4Unicast=None, IpV6Mpls=None, IpV6MplsVpn=None, IpV6Multicast=None, IpV6MulticastMplsVpn=None, IpV6MulticastVpn=None, IpV6Unicast=None, Vpls=None):
        """Updates capabilities resource on the server.

        Args
        ----
        - AdVpls (bool): 
        - Evpn (bool): 
        - FetchDetailedIpV4UnicastInfo (bool): 
        - FetchDetailedIpV6UnicastInfo (bool): 
        - IpV4Mpls (bool): 
        - IpV4MplsVpn (bool): 
        - IpV4Multicast (bool): 
        - IpV4MulticastMplsVpn (bool): 
        - IpV4MulticastVpn (bool): 
        - IpV4Unicast (bool): 
        - IpV6Mpls (bool): 
        - IpV6MplsVpn (bool): 
        - IpV6Multicast (bool): 
        - IpV6MulticastMplsVpn (bool): 
        - IpV6MulticastVpn (bool): 
        - IpV6Unicast (bool): 
        - Vpls (bool): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
