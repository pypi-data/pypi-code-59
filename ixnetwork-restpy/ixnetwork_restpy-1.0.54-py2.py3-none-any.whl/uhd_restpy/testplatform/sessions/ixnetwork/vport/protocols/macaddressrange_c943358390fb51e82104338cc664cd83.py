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


class MacAddressRange(Base):
    """
    The MacAddressRange class encapsulates a list of macAddressRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the MacAddressRange.find() method.
    The list can be managed by using the MacAddressRange.add() and MacAddressRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'macAddressRange'
    _SDM_ATT_MAP = {
        'EnableVlan': 'enableVlan',
        'Enabled': 'enabled',
        'IncrementVlan': 'incrementVlan',
        'IncrementVlanMode': 'incrementVlanMode',
        'IncremetVlanMode': 'incremetVlanMode',
        'MacCount': 'macCount',
        'MacCountPerL2Site': 'macCountPerL2Site',
        'MacIncrement': 'macIncrement',
        'SkipVlanIdZero': 'skipVlanIdZero',
        'StartMacAddress': 'startMacAddress',
        'TotalMacCount': 'totalMacCount',
        'Tpid': 'tpid',
        'VlanCount': 'vlanCount',
        'VlanId': 'vlanId',
        'VlanPriority': 'vlanPriority',
    }

    def __init__(self, parent):
        super(MacAddressRange, self).__init__(parent)

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
    def IncrementVlan(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrementVlan'])
    @IncrementVlan.setter
    def IncrementVlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrementVlan'], value)

    @property
    def IncrementVlanMode(self):
        """
        Returns
        -------
        - str(noIncrement | parallelIncrement | innerFirst | outerFirst): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrementVlanMode'])
    @IncrementVlanMode.setter
    def IncrementVlanMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrementVlanMode'], value)

    @property
    def IncremetVlanMode(self):
        """DEPRECATED 
        Returns
        -------
        - str(noIncrement | parallelIncrement | innerFirst | outerFirst): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncremetVlanMode'])
    @IncremetVlanMode.setter
    def IncremetVlanMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncremetVlanMode'], value)

    @property
    def MacCount(self):
        """DEPRECATED 
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MacCount'])
    @MacCount.setter
    def MacCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MacCount'], value)

    @property
    def MacCountPerL2Site(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MacCountPerL2Site'])
    @MacCountPerL2Site.setter
    def MacCountPerL2Site(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MacCountPerL2Site'], value)

    @property
    def MacIncrement(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MacIncrement'])
    @MacIncrement.setter
    def MacIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MacIncrement'], value)

    @property
    def SkipVlanIdZero(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SkipVlanIdZero'])
    @SkipVlanIdZero.setter
    def SkipVlanIdZero(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SkipVlanIdZero'], value)

    @property
    def StartMacAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartMacAddress'])
    @StartMacAddress.setter
    def StartMacAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartMacAddress'], value)

    @property
    def TotalMacCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TotalMacCount'])

    @property
    def Tpid(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Tpid'])
    @Tpid.setter
    def Tpid(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Tpid'], value)

    @property
    def VlanCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanCount'])
    @VlanCount.setter
    def VlanCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanCount'], value)

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

    def update(self, EnableVlan=None, Enabled=None, IncrementVlan=None, IncrementVlanMode=None, IncremetVlanMode=None, MacCount=None, MacCountPerL2Site=None, MacIncrement=None, SkipVlanIdZero=None, StartMacAddress=None, Tpid=None, VlanCount=None, VlanId=None, VlanPriority=None):
        """Updates macAddressRange resource on the server.

        Args
        ----
        - EnableVlan (bool): 
        - Enabled (bool): 
        - IncrementVlan (bool): 
        - IncrementVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): 
        - IncremetVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): 
        - MacCount (number): 
        - MacCountPerL2Site (number): 
        - MacIncrement (bool): 
        - SkipVlanIdZero (bool): 
        - StartMacAddress (str): 
        - Tpid (str): 
        - VlanCount (number): 
        - VlanId (str): 
        - VlanPriority (str): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, EnableVlan=None, Enabled=None, IncrementVlan=None, IncrementVlanMode=None, IncremetVlanMode=None, MacCount=None, MacCountPerL2Site=None, MacIncrement=None, SkipVlanIdZero=None, StartMacAddress=None, Tpid=None, VlanCount=None, VlanId=None, VlanPriority=None):
        """Adds a new macAddressRange resource on the server and adds it to the container.

        Args
        ----
        - EnableVlan (bool): 
        - Enabled (bool): 
        - IncrementVlan (bool): 
        - IncrementVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): 
        - IncremetVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): 
        - MacCount (number): 
        - MacCountPerL2Site (number): 
        - MacIncrement (bool): 
        - SkipVlanIdZero (bool): 
        - StartMacAddress (str): 
        - Tpid (str): 
        - VlanCount (number): 
        - VlanId (str): 
        - VlanPriority (str): 

        Returns
        -------
        - self: This instance with all currently retrieved macAddressRange resources using find and the newly added macAddressRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained macAddressRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EnableVlan=None, Enabled=None, IncrementVlan=None, IncrementVlanMode=None, IncremetVlanMode=None, MacCount=None, MacCountPerL2Site=None, MacIncrement=None, SkipVlanIdZero=None, StartMacAddress=None, TotalMacCount=None, Tpid=None, VlanCount=None, VlanId=None, VlanPriority=None):
        """Finds and retrieves macAddressRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve macAddressRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all macAddressRange resources from the server.

        Args
        ----
        - EnableVlan (bool): 
        - Enabled (bool): 
        - IncrementVlan (bool): 
        - IncrementVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): 
        - IncremetVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): 
        - MacCount (number): 
        - MacCountPerL2Site (number): 
        - MacIncrement (bool): 
        - SkipVlanIdZero (bool): 
        - StartMacAddress (str): 
        - TotalMacCount (number): 
        - Tpid (str): 
        - VlanCount (number): 
        - VlanId (str): 
        - VlanPriority (str): 

        Returns
        -------
        - self: This instance with matching macAddressRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of macAddressRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the macAddressRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
