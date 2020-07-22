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


class Lan(Base):
    """
    The Lan class encapsulates a list of lan resources that are managed by the user.
    A list of resources can be retrieved from the server using the Lan.find() method.
    The list can be managed by using the Lan.add() and Lan.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'lan'
    _SDM_ATT_MAP = {
        'AtmEncapsulation': 'atmEncapsulation',
        'Bmac': 'bmac',
        'Count': 'count',
        'CountPerVc': 'countPerVc',
        'EnableBmac': 'enableBmac',
        'EnableIncrementMac': 'enableIncrementMac',
        'EnableIncrementVlan': 'enableIncrementVlan',
        'EnableSiteId': 'enableSiteId',
        'EnableVlan': 'enableVlan',
        'Enabled': 'enabled',
        'FrEncapsulation': 'frEncapsulation',
        'IncrementPerVcVlanMode': 'incrementPerVcVlanMode',
        'IncrementVlanMode': 'incrementVlanMode',
        'IncremetVlanMode': 'incremetVlanMode',
        'Mac': 'mac',
        'MacRangeMode': 'macRangeMode',
        'NumberOfVcs': 'numberOfVcs',
        'SiteId': 'siteId',
        'SkipVlanIdZero': 'skipVlanIdZero',
        'Tpid': 'tpid',
        'TrafficGroupId': 'trafficGroupId',
        'VlanCount': 'vlanCount',
        'VlanId': 'vlanId',
        'VlanPriority': 'vlanPriority',
    }

    def __init__(self, parent):
        super(Lan, self).__init__(parent)

    @property
    def AtmEncapsulation(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../atm): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AtmEncapsulation'])
    @AtmEncapsulation.setter
    def AtmEncapsulation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AtmEncapsulation'], value)

    @property
    def Bmac(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Bmac'])
    @Bmac.setter
    def Bmac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Bmac'], value)

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
    def CountPerVc(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CountPerVc'])
    @CountPerVc.setter
    def CountPerVc(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CountPerVc'], value)

    @property
    def EnableBmac(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableBmac'])
    @EnableBmac.setter
    def EnableBmac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableBmac'], value)

    @property
    def EnableIncrementMac(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableIncrementMac'])
    @EnableIncrementMac.setter
    def EnableIncrementMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableIncrementMac'], value)

    @property
    def EnableIncrementVlan(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableIncrementVlan'])
    @EnableIncrementVlan.setter
    def EnableIncrementVlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableIncrementVlan'], value)

    @property
    def EnableSiteId(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSiteId'])
    @EnableSiteId.setter
    def EnableSiteId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSiteId'], value)

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
    def FrEncapsulation(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../fr): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FrEncapsulation'])
    @FrEncapsulation.setter
    def FrEncapsulation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FrEncapsulation'], value)

    @property
    def IncrementPerVcVlanMode(self):
        """
        Returns
        -------
        - str(noIncrement | parallelIncrement | innerFirst | outerFirst): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrementPerVcVlanMode'])
    @IncrementPerVcVlanMode.setter
    def IncrementPerVcVlanMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrementPerVcVlanMode'], value)

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
    def Mac(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mac'])
    @Mac.setter
    def Mac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mac'], value)

    @property
    def MacRangeMode(self):
        """
        Returns
        -------
        - str(normal | bundled): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MacRangeMode'])
    @MacRangeMode.setter
    def MacRangeMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MacRangeMode'], value)

    @property
    def NumberOfVcs(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfVcs'])
    @NumberOfVcs.setter
    def NumberOfVcs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfVcs'], value)

    @property
    def SiteId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SiteId'])
    @SiteId.setter
    def SiteId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SiteId'], value)

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
    def TrafficGroupId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficGroupId'])
    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficGroupId'], value)

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

    def update(self, AtmEncapsulation=None, Bmac=None, Count=None, CountPerVc=None, EnableBmac=None, EnableIncrementMac=None, EnableIncrementVlan=None, EnableSiteId=None, EnableVlan=None, Enabled=None, FrEncapsulation=None, IncrementPerVcVlanMode=None, IncrementVlanMode=None, IncremetVlanMode=None, Mac=None, MacRangeMode=None, NumberOfVcs=None, SiteId=None, SkipVlanIdZero=None, Tpid=None, TrafficGroupId=None, VlanCount=None, VlanId=None, VlanPriority=None):
        """Updates lan resource on the server.

        Args
        ----
        - AtmEncapsulation (str(None | /api/v1/sessions/1/ixnetwork/vport/.../atm)): 
        - Bmac (str): 
        - Count (number): 
        - CountPerVc (number): 
        - EnableBmac (bool): 
        - EnableIncrementMac (bool): 
        - EnableIncrementVlan (bool): 
        - EnableSiteId (bool): 
        - EnableVlan (bool): 
        - Enabled (bool): 
        - FrEncapsulation (str(None | /api/v1/sessions/1/ixnetwork/vport/.../fr)): 
        - IncrementPerVcVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): 
        - IncrementVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): 
        - IncremetVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): 
        - Mac (str): 
        - MacRangeMode (str(normal | bundled)): 
        - NumberOfVcs (number): 
        - SiteId (number): 
        - SkipVlanIdZero (bool): 
        - Tpid (str): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 
        - VlanCount (number): 
        - VlanId (str): 
        - VlanPriority (str): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AtmEncapsulation=None, Bmac=None, Count=None, CountPerVc=None, EnableBmac=None, EnableIncrementMac=None, EnableIncrementVlan=None, EnableSiteId=None, EnableVlan=None, Enabled=None, FrEncapsulation=None, IncrementPerVcVlanMode=None, IncrementVlanMode=None, IncremetVlanMode=None, Mac=None, MacRangeMode=None, NumberOfVcs=None, SiteId=None, SkipVlanIdZero=None, Tpid=None, TrafficGroupId=None, VlanCount=None, VlanId=None, VlanPriority=None):
        """Adds a new lan resource on the server and adds it to the container.

        Args
        ----
        - AtmEncapsulation (str(None | /api/v1/sessions/1/ixnetwork/vport/.../atm)): 
        - Bmac (str): 
        - Count (number): 
        - CountPerVc (number): 
        - EnableBmac (bool): 
        - EnableIncrementMac (bool): 
        - EnableIncrementVlan (bool): 
        - EnableSiteId (bool): 
        - EnableVlan (bool): 
        - Enabled (bool): 
        - FrEncapsulation (str(None | /api/v1/sessions/1/ixnetwork/vport/.../fr)): 
        - IncrementPerVcVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): 
        - IncrementVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): 
        - IncremetVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): 
        - Mac (str): 
        - MacRangeMode (str(normal | bundled)): 
        - NumberOfVcs (number): 
        - SiteId (number): 
        - SkipVlanIdZero (bool): 
        - Tpid (str): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 
        - VlanCount (number): 
        - VlanId (str): 
        - VlanPriority (str): 

        Returns
        -------
        - self: This instance with all currently retrieved lan resources using find and the newly added lan resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained lan resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AtmEncapsulation=None, Bmac=None, Count=None, CountPerVc=None, EnableBmac=None, EnableIncrementMac=None, EnableIncrementVlan=None, EnableSiteId=None, EnableVlan=None, Enabled=None, FrEncapsulation=None, IncrementPerVcVlanMode=None, IncrementVlanMode=None, IncremetVlanMode=None, Mac=None, MacRangeMode=None, NumberOfVcs=None, SiteId=None, SkipVlanIdZero=None, Tpid=None, TrafficGroupId=None, VlanCount=None, VlanId=None, VlanPriority=None):
        """Finds and retrieves lan resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve lan resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all lan resources from the server.

        Args
        ----
        - AtmEncapsulation (str(None | /api/v1/sessions/1/ixnetwork/vport/.../atm)): 
        - Bmac (str): 
        - Count (number): 
        - CountPerVc (number): 
        - EnableBmac (bool): 
        - EnableIncrementMac (bool): 
        - EnableIncrementVlan (bool): 
        - EnableSiteId (bool): 
        - EnableVlan (bool): 
        - Enabled (bool): 
        - FrEncapsulation (str(None | /api/v1/sessions/1/ixnetwork/vport/.../fr)): 
        - IncrementPerVcVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): 
        - IncrementVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): 
        - IncremetVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): 
        - Mac (str): 
        - MacRangeMode (str(normal | bundled)): 
        - NumberOfVcs (number): 
        - SiteId (number): 
        - SkipVlanIdZero (bool): 
        - Tpid (str): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 
        - VlanCount (number): 
        - VlanId (str): 
        - VlanPriority (str): 

        Returns
        -------
        - self: This instance with matching lan resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of lan data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the lan resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
