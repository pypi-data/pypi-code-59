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


class SwitchHostRanges(Base):
    """
    The SwitchHostRanges class encapsulates a list of switchHostRanges resources that are managed by the user.
    A list of resources can be retrieved from the server using the SwitchHostRanges.find() method.
    The list can be managed by using the SwitchHostRanges.add() and SwitchHostRanges.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'switchHostRanges'
    _SDM_ATT_MAP = {
        'EnableStaticIp': 'enableStaticIp',
        'EnableVlan': 'enableVlan',
        'Enabled': 'enabled',
        'HostMacAddress': 'hostMacAddress',
        'HostStaticIpv4Address': 'hostStaticIpv4Address',
        'HostVlanid': 'hostVlanid',
        'NumberOfHostsPerPort': 'numberOfHostsPerPort',
    }

    def __init__(self, parent):
        super(SwitchHostRanges, self).__init__(parent)

    @property
    def EnableStaticIp(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableStaticIp'])
    @EnableStaticIp.setter
    def EnableStaticIp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableStaticIp'], value)

    @property
    def EnableVlan(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableVlan'])
    @EnableVlan.setter
    def EnableVlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableVlan'], value)

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
    def HostMacAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['HostMacAddress'])
    @HostMacAddress.setter
    def HostMacAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HostMacAddress'], value)

    @property
    def HostStaticIpv4Address(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['HostStaticIpv4Address'])
    @HostStaticIpv4Address.setter
    def HostStaticIpv4Address(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HostStaticIpv4Address'], value)

    @property
    def HostVlanid(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['HostVlanid'])
    @HostVlanid.setter
    def HostVlanid(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HostVlanid'], value)

    @property
    def NumberOfHostsPerPort(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfHostsPerPort'])
    @NumberOfHostsPerPort.setter
    def NumberOfHostsPerPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfHostsPerPort'], value)

    def update(self, EnableStaticIp=None, EnableVlan=None, Enabled=None, HostMacAddress=None, HostStaticIpv4Address=None, HostVlanid=None, NumberOfHostsPerPort=None):
        """Updates switchHostRanges resource on the server.

        Args
        ----
        - EnableStaticIp (bool): 
        - EnableVlan (bool): 
        - Enabled (bool): 
        - HostMacAddress (str): 
        - HostStaticIpv4Address (str): 
        - HostVlanid (str): 
        - NumberOfHostsPerPort (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, EnableStaticIp=None, EnableVlan=None, Enabled=None, HostMacAddress=None, HostStaticIpv4Address=None, HostVlanid=None, NumberOfHostsPerPort=None):
        """Adds a new switchHostRanges resource on the server and adds it to the container.

        Args
        ----
        - EnableStaticIp (bool): 
        - EnableVlan (bool): 
        - Enabled (bool): 
        - HostMacAddress (str): 
        - HostStaticIpv4Address (str): 
        - HostVlanid (str): 
        - NumberOfHostsPerPort (number): 

        Returns
        -------
        - self: This instance with all currently retrieved switchHostRanges resources using find and the newly added switchHostRanges resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained switchHostRanges resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EnableStaticIp=None, EnableVlan=None, Enabled=None, HostMacAddress=None, HostStaticIpv4Address=None, HostVlanid=None, NumberOfHostsPerPort=None):
        """Finds and retrieves switchHostRanges resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switchHostRanges resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switchHostRanges resources from the server.

        Args
        ----
        - EnableStaticIp (bool): 
        - EnableVlan (bool): 
        - Enabled (bool): 
        - HostMacAddress (str): 
        - HostStaticIpv4Address (str): 
        - HostVlanid (str): 
        - NumberOfHostsPerPort (number): 

        Returns
        -------
        - self: This instance with matching switchHostRanges resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of switchHostRanges data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the switchHostRanges resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
