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


class SiteEidRange(Base):
    """
    The SiteEidRange class encapsulates a list of siteEidRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the SiteEidRange.find() method.
    The list can be managed by using the SiteEidRange.add() and SiteEidRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'siteEidRange'
    _SDM_ATT_MAP = {
        'Address': 'address',
        'Count': 'count',
        'Enabled': 'enabled',
        'Family': 'family',
        'IncludeOrExclude': 'includeOrExclude',
        'InstanceId': 'instanceId',
        'PrefixLength': 'prefixLength',
    }

    def __init__(self, parent):
        super(SiteEidRange, self).__init__(parent)

    @property
    def Address(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Address'])
    @Address.setter
    def Address(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Address'], value)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])
    @Count.setter
    def Count(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Count'], value)

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
    def Family(self):
        """
        Returns
        -------
        - str(ipv4 | ipv6): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Family'])
    @Family.setter
    def Family(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Family'], value)

    @property
    def IncludeOrExclude(self):
        """
        Returns
        -------
        - str(include | exclude): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeOrExclude'])
    @IncludeOrExclude.setter
    def IncludeOrExclude(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeOrExclude'], value)

    @property
    def InstanceId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InstanceId'])
    @InstanceId.setter
    def InstanceId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InstanceId'], value)

    @property
    def PrefixLength(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrefixLength'])
    @PrefixLength.setter
    def PrefixLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PrefixLength'], value)

    def update(self, Address=None, Count=None, Enabled=None, Family=None, IncludeOrExclude=None, InstanceId=None, PrefixLength=None):
        """Updates siteEidRange resource on the server.

        Args
        ----
        - Address (str): 
        - Count (number): 
        - Enabled (bool): 
        - Family (str(ipv4 | ipv6)): 
        - IncludeOrExclude (str(include | exclude)): 
        - InstanceId (number): 
        - PrefixLength (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Address=None, Count=None, Enabled=None, Family=None, IncludeOrExclude=None, InstanceId=None, PrefixLength=None):
        """Adds a new siteEidRange resource on the server and adds it to the container.

        Args
        ----
        - Address (str): 
        - Count (number): 
        - Enabled (bool): 
        - Family (str(ipv4 | ipv6)): 
        - IncludeOrExclude (str(include | exclude)): 
        - InstanceId (number): 
        - PrefixLength (number): 

        Returns
        -------
        - self: This instance with all currently retrieved siteEidRange resources using find and the newly added siteEidRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained siteEidRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Address=None, Count=None, Enabled=None, Family=None, IncludeOrExclude=None, InstanceId=None, PrefixLength=None):
        """Finds and retrieves siteEidRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve siteEidRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all siteEidRange resources from the server.

        Args
        ----
        - Address (str): 
        - Count (number): 
        - Enabled (bool): 
        - Family (str(ipv4 | ipv6)): 
        - IncludeOrExclude (str(include | exclude)): 
        - InstanceId (number): 
        - PrefixLength (number): 

        Returns
        -------
        - self: This instance with matching siteEidRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of siteEidRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the siteEidRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
