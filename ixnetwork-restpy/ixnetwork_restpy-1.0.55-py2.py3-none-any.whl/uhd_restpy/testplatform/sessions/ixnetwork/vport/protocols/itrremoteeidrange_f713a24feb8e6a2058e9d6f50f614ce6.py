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


class ItrRemoteEidRange(Base):
    """
    The ItrRemoteEidRange class encapsulates a list of itrRemoteEidRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the ItrRemoteEidRange.find() method.
    The list can be managed by using the ItrRemoteEidRange.add() and ItrRemoteEidRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'itrRemoteEidRange'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'EnableMapReplyRecordSegmentMbit': 'enableMapReplyRecordSegmentMbit',
        'Enabled': 'enabled',
        'Family': 'family',
        'KeepQueryingUnlessResolved': 'keepQueryingUnlessResolved',
        'MapResolvingInterval': 'mapResolvingInterval',
        'PrefixLength': 'prefixLength',
        'QueryIntervalUnlessResolved': 'queryIntervalUnlessResolved',
        'StartAddress': 'startAddress',
    }

    def __init__(self, parent):
        super(ItrRemoteEidRange, self).__init__(parent)

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
    def EnableMapReplyRecordSegmentMbit(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMapReplyRecordSegmentMbit'])
    @EnableMapReplyRecordSegmentMbit.setter
    def EnableMapReplyRecordSegmentMbit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMapReplyRecordSegmentMbit'], value)

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
    def KeepQueryingUnlessResolved(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['KeepQueryingUnlessResolved'])
    @KeepQueryingUnlessResolved.setter
    def KeepQueryingUnlessResolved(self, value):
        self._set_attribute(self._SDM_ATT_MAP['KeepQueryingUnlessResolved'], value)

    @property
    def MapResolvingInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MapResolvingInterval'])
    @MapResolvingInterval.setter
    def MapResolvingInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MapResolvingInterval'], value)

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

    @property
    def QueryIntervalUnlessResolved(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['QueryIntervalUnlessResolved'])
    @QueryIntervalUnlessResolved.setter
    def QueryIntervalUnlessResolved(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QueryIntervalUnlessResolved'], value)

    @property
    def StartAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartAddress'])
    @StartAddress.setter
    def StartAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartAddress'], value)

    def update(self, Count=None, EnableMapReplyRecordSegmentMbit=None, Enabled=None, Family=None, KeepQueryingUnlessResolved=None, MapResolvingInterval=None, PrefixLength=None, QueryIntervalUnlessResolved=None, StartAddress=None):
        """Updates itrRemoteEidRange resource on the server.

        Args
        ----
        - Count (number): 
        - EnableMapReplyRecordSegmentMbit (bool): 
        - Enabled (bool): 
        - Family (str(ipv4 | ipv6)): 
        - KeepQueryingUnlessResolved (bool): 
        - MapResolvingInterval (number): 
        - PrefixLength (number): 
        - QueryIntervalUnlessResolved (number): 
        - StartAddress (str): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Count=None, EnableMapReplyRecordSegmentMbit=None, Enabled=None, Family=None, KeepQueryingUnlessResolved=None, MapResolvingInterval=None, PrefixLength=None, QueryIntervalUnlessResolved=None, StartAddress=None):
        """Adds a new itrRemoteEidRange resource on the server and adds it to the container.

        Args
        ----
        - Count (number): 
        - EnableMapReplyRecordSegmentMbit (bool): 
        - Enabled (bool): 
        - Family (str(ipv4 | ipv6)): 
        - KeepQueryingUnlessResolved (bool): 
        - MapResolvingInterval (number): 
        - PrefixLength (number): 
        - QueryIntervalUnlessResolved (number): 
        - StartAddress (str): 

        Returns
        -------
        - self: This instance with all currently retrieved itrRemoteEidRange resources using find and the newly added itrRemoteEidRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained itrRemoteEidRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, EnableMapReplyRecordSegmentMbit=None, Enabled=None, Family=None, KeepQueryingUnlessResolved=None, MapResolvingInterval=None, PrefixLength=None, QueryIntervalUnlessResolved=None, StartAddress=None):
        """Finds and retrieves itrRemoteEidRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve itrRemoteEidRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all itrRemoteEidRange resources from the server.

        Args
        ----
        - Count (number): 
        - EnableMapReplyRecordSegmentMbit (bool): 
        - Enabled (bool): 
        - Family (str(ipv4 | ipv6)): 
        - KeepQueryingUnlessResolved (bool): 
        - MapResolvingInterval (number): 
        - PrefixLength (number): 
        - QueryIntervalUnlessResolved (number): 
        - StartAddress (str): 

        Returns
        -------
        - self: This instance with matching itrRemoteEidRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of itrRemoteEidRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the itrRemoteEidRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
