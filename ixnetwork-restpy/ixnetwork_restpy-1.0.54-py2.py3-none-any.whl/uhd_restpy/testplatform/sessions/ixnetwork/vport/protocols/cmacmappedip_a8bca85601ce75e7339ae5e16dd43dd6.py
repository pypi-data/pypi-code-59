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


class CMacMappedIp(Base):
    """
    The CMacMappedIp class encapsulates a list of cMacMappedIp resources that are managed by the user.
    A list of resources can be retrieved from the server using the CMacMappedIp.find() method.
    The list can be managed by using the CMacMappedIp.add() and CMacMappedIp.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'cMacMappedIp'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'IpAddress': 'ipAddress',
        'IpStep': 'ipStep',
        'IpType': 'ipType',
    }

    def __init__(self, parent):
        super(CMacMappedIp, self).__init__(parent)

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
    def IpAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpAddress'])
    @IpAddress.setter
    def IpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpAddress'], value)

    @property
    def IpStep(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpStep'])
    @IpStep.setter
    def IpStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpStep'], value)

    @property
    def IpType(self):
        """
        Returns
        -------
        - str(ipv4 | ipv6): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpType'])
    @IpType.setter
    def IpType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpType'], value)

    def update(self, Enabled=None, IpAddress=None, IpStep=None, IpType=None):
        """Updates cMacMappedIp resource on the server.

        Args
        ----
        - Enabled (bool): 
        - IpAddress (str): 
        - IpStep (number): 
        - IpType (str(ipv4 | ipv6)): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, IpAddress=None, IpStep=None, IpType=None):
        """Adds a new cMacMappedIp resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): 
        - IpAddress (str): 
        - IpStep (number): 
        - IpType (str(ipv4 | ipv6)): 

        Returns
        -------
        - self: This instance with all currently retrieved cMacMappedIp resources using find and the newly added cMacMappedIp resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained cMacMappedIp resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, IpAddress=None, IpStep=None, IpType=None):
        """Finds and retrieves cMacMappedIp resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve cMacMappedIp resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all cMacMappedIp resources from the server.

        Args
        ----
        - Enabled (bool): 
        - IpAddress (str): 
        - IpStep (number): 
        - IpType (str(ipv4 | ipv6)): 

        Returns
        -------
        - self: This instance with matching cMacMappedIp resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of cMacMappedIp data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the cMacMappedIp resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
