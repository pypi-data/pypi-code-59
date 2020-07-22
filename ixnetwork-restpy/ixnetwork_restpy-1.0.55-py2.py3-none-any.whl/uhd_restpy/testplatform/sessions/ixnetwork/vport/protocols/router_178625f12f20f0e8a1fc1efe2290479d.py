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


class Router(Base):
    """
    The Router class encapsulates a list of router resources that are managed by the user.
    A list of resources can be retrieved from the server using the Router.find() method.
    The list can be managed by using the Router.add() and Router.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'router'
    _SDM_ATT_MAP = {
        'AuthorizationPassword': 'authorizationPassword',
        'EnableAuthorization': 'enableAuthorization',
        'Enabled': 'enabled',
        'InterfaceId': 'interfaceId',
        'ReceiveType': 'receiveType',
        'ResponseMode': 'responseMode',
        'SendType': 'sendType',
        'TrafficGroupId': 'trafficGroupId',
        'UpdateInterval': 'updateInterval',
        'UpdateIntervalOffset': 'updateIntervalOffset',
    }

    def __init__(self, parent):
        super(Router, self).__init__(parent)

    @property
    def RouteRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.routerange_8e3502cfa312d16639d619c61c5aeb3a.RouteRange): An instance of the RouteRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.routerange_8e3502cfa312d16639d619c61c5aeb3a import RouteRange
        return RouteRange(self)

    @property
    def AuthorizationPassword(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AuthorizationPassword'])
    @AuthorizationPassword.setter
    def AuthorizationPassword(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AuthorizationPassword'], value)

    @property
    def EnableAuthorization(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAuthorization'])
    @EnableAuthorization.setter
    def EnableAuthorization(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAuthorization'], value)

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
    def InterfaceId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceId'])
    @InterfaceId.setter
    def InterfaceId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceId'], value)

    @property
    def ReceiveType(self):
        """
        Returns
        -------
        - str(receiveVersion1 | receiveVersion2 | receiveVersion1And2): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceiveType'])
    @ReceiveType.setter
    def ReceiveType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReceiveType'], value)

    @property
    def ResponseMode(self):
        """
        Returns
        -------
        - str(default | splitHorizon | poisonReverse | splitHorizonSpaceSaver | silent): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ResponseMode'])
    @ResponseMode.setter
    def ResponseMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ResponseMode'], value)

    @property
    def SendType(self):
        """
        Returns
        -------
        - str(multicast | broadcastV1 | broadcastV2): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendType'])
    @SendType.setter
    def SendType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendType'], value)

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
    def UpdateInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpdateInterval'])
    @UpdateInterval.setter
    def UpdateInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpdateInterval'], value)

    @property
    def UpdateIntervalOffset(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpdateIntervalOffset'])
    @UpdateIntervalOffset.setter
    def UpdateIntervalOffset(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpdateIntervalOffset'], value)

    def update(self, AuthorizationPassword=None, EnableAuthorization=None, Enabled=None, InterfaceId=None, ReceiveType=None, ResponseMode=None, SendType=None, TrafficGroupId=None, UpdateInterval=None, UpdateIntervalOffset=None):
        """Updates router resource on the server.

        Args
        ----
        - AuthorizationPassword (str): 
        - EnableAuthorization (bool): 
        - Enabled (bool): 
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - ReceiveType (str(receiveVersion1 | receiveVersion2 | receiveVersion1And2)): 
        - ResponseMode (str(default | splitHorizon | poisonReverse | splitHorizonSpaceSaver | silent)): 
        - SendType (str(multicast | broadcastV1 | broadcastV2)): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 
        - UpdateInterval (number): 
        - UpdateIntervalOffset (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AuthorizationPassword=None, EnableAuthorization=None, Enabled=None, InterfaceId=None, ReceiveType=None, ResponseMode=None, SendType=None, TrafficGroupId=None, UpdateInterval=None, UpdateIntervalOffset=None):
        """Adds a new router resource on the server and adds it to the container.

        Args
        ----
        - AuthorizationPassword (str): 
        - EnableAuthorization (bool): 
        - Enabled (bool): 
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - ReceiveType (str(receiveVersion1 | receiveVersion2 | receiveVersion1And2)): 
        - ResponseMode (str(default | splitHorizon | poisonReverse | splitHorizonSpaceSaver | silent)): 
        - SendType (str(multicast | broadcastV1 | broadcastV2)): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 
        - UpdateInterval (number): 
        - UpdateIntervalOffset (number): 

        Returns
        -------
        - self: This instance with all currently retrieved router resources using find and the newly added router resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained router resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AuthorizationPassword=None, EnableAuthorization=None, Enabled=None, InterfaceId=None, ReceiveType=None, ResponseMode=None, SendType=None, TrafficGroupId=None, UpdateInterval=None, UpdateIntervalOffset=None):
        """Finds and retrieves router resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve router resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all router resources from the server.

        Args
        ----
        - AuthorizationPassword (str): 
        - EnableAuthorization (bool): 
        - Enabled (bool): 
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - ReceiveType (str(receiveVersion1 | receiveVersion2 | receiveVersion1And2)): 
        - ResponseMode (str(default | splitHorizon | poisonReverse | splitHorizonSpaceSaver | silent)): 
        - SendType (str(multicast | broadcastV1 | broadcastV2)): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 
        - UpdateInterval (number): 
        - UpdateIntervalOffset (number): 

        Returns
        -------
        - self: This instance with matching router resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of router data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the router resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
