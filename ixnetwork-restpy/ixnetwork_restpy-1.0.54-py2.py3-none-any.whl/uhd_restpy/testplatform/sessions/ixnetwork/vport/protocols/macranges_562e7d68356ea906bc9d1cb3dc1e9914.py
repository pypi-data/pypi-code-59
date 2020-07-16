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


class MacRanges(Base):
    """
    The MacRanges class encapsulates a list of macRanges resources that are managed by the user.
    A list of resources can be retrieved from the server using the MacRanges.find() method.
    The list can be managed by using the MacRanges.add() and MacRanges.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'macRanges'
    _SDM_ATT_MAP = {
        'CVlanId': 'cVlanId',
        'CVlanPriority': 'cVlanPriority',
        'CVlanTpId': 'cVlanTpId',
        'Count': 'count',
        'EnableVlan': 'enableVlan',
        'Enabled': 'enabled',
        'ITagethernetType': 'iTagethernetType',
        'ITagiSid': 'iTagiSid',
        'SVlanId': 'sVlanId',
        'SVlanPriority': 'sVlanPriority',
        'SVlanTpId': 'sVlanTpId',
        'StartMacAddress': 'startMacAddress',
        'Step': 'step',
        'TrafficGroupId': 'trafficGroupId',
        'Type': 'type',
    }

    def __init__(self, parent):
        super(MacRanges, self).__init__(parent)

    @property
    def CVlanId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CVlanId'])
    @CVlanId.setter
    def CVlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CVlanId'], value)

    @property
    def CVlanPriority(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CVlanPriority'])
    @CVlanPriority.setter
    def CVlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CVlanPriority'], value)

    @property
    def CVlanTpId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CVlanTpId'])
    @CVlanTpId.setter
    def CVlanTpId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CVlanTpId'], value)

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
    def ITagethernetType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ITagethernetType'])

    @property
    def ITagiSid(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ITagiSid'])
    @ITagiSid.setter
    def ITagiSid(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ITagiSid'], value)

    @property
    def SVlanId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SVlanId'])
    @SVlanId.setter
    def SVlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SVlanId'], value)

    @property
    def SVlanPriority(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SVlanPriority'])
    @SVlanPriority.setter
    def SVlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SVlanPriority'], value)

    @property
    def SVlanTpId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SVlanTpId'])
    @SVlanTpId.setter
    def SVlanTpId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SVlanTpId'], value)

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
    def Step(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step'])
    @Step.setter
    def Step(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step'], value)

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
    def Type(self):
        """
        Returns
        -------
        - str(singleVlan | stackedVlan): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])
    @Type.setter
    def Type(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Type'], value)

    def update(self, CVlanId=None, CVlanPriority=None, CVlanTpId=None, Count=None, EnableVlan=None, Enabled=None, ITagiSid=None, SVlanId=None, SVlanPriority=None, SVlanTpId=None, StartMacAddress=None, Step=None, TrafficGroupId=None, Type=None):
        """Updates macRanges resource on the server.

        Args
        ----
        - CVlanId (number): 
        - CVlanPriority (number): 
        - CVlanTpId (str): 
        - Count (number): 
        - EnableVlan (bool): 
        - Enabled (bool): 
        - ITagiSid (number): 
        - SVlanId (number): 
        - SVlanPriority (number): 
        - SVlanTpId (str): 
        - StartMacAddress (str): 
        - Step (str): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 
        - Type (str(singleVlan | stackedVlan)): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, CVlanId=None, CVlanPriority=None, CVlanTpId=None, Count=None, EnableVlan=None, Enabled=None, ITagiSid=None, SVlanId=None, SVlanPriority=None, SVlanTpId=None, StartMacAddress=None, Step=None, TrafficGroupId=None, Type=None):
        """Adds a new macRanges resource on the server and adds it to the container.

        Args
        ----
        - CVlanId (number): 
        - CVlanPriority (number): 
        - CVlanTpId (str): 
        - Count (number): 
        - EnableVlan (bool): 
        - Enabled (bool): 
        - ITagiSid (number): 
        - SVlanId (number): 
        - SVlanPriority (number): 
        - SVlanTpId (str): 
        - StartMacAddress (str): 
        - Step (str): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 
        - Type (str(singleVlan | stackedVlan)): 

        Returns
        -------
        - self: This instance with all currently retrieved macRanges resources using find and the newly added macRanges resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained macRanges resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, CVlanId=None, CVlanPriority=None, CVlanTpId=None, Count=None, EnableVlan=None, Enabled=None, ITagethernetType=None, ITagiSid=None, SVlanId=None, SVlanPriority=None, SVlanTpId=None, StartMacAddress=None, Step=None, TrafficGroupId=None, Type=None):
        """Finds and retrieves macRanges resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve macRanges resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all macRanges resources from the server.

        Args
        ----
        - CVlanId (number): 
        - CVlanPriority (number): 
        - CVlanTpId (str): 
        - Count (number): 
        - EnableVlan (bool): 
        - Enabled (bool): 
        - ITagethernetType (str): 
        - ITagiSid (number): 
        - SVlanId (number): 
        - SVlanPriority (number): 
        - SVlanTpId (str): 
        - StartMacAddress (str): 
        - Step (str): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 
        - Type (str(singleVlan | stackedVlan)): 

        Returns
        -------
        - self: This instance with matching macRanges resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of macRanges data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the macRanges resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
