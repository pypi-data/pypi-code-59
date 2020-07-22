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
        'DisableAutoGenerateLinkLsa': 'disableAutoGenerateLinkLsa',
        'DisableAutoGenerateRouterLsa': 'disableAutoGenerateRouterLsa',
        'DiscardLearnedLsa': 'discardLearnedLsa',
        'EnableGracefulRestartHelperMode': 'enableGracefulRestartHelperMode',
        'EnableStrictLsaChecking': 'enableStrictLsaChecking',
        'EnableSupportReasonSwReloadOrUpgrade': 'enableSupportReasonSwReloadOrUpgrade',
        'EnableSupportReasonSwRestart': 'enableSupportReasonSwRestart',
        'EnableSupportReasonSwitchToRedundantControlProcessor': 'enableSupportReasonSwitchToRedundantControlProcessor',
        'EnableSupportReasonUnknown': 'enableSupportReasonUnknown',
        'EnableSupportRfc5838': 'enableSupportRfc5838',
        'Enabled': 'enabled',
        'IsLearnedLsaRefreshed': 'isLearnedLsaRefreshed',
        'LsaRefreshTime': 'lsaRefreshTime',
        'LsaRetransmitTime': 'lsaRetransmitTime',
        'MaxNumLsaPerSecond': 'maxNumLsaPerSecond',
        'RouterId': 'routerId',
        'TrafficGroupId': 'trafficGroupId',
    }

    def __init__(self, parent):
        super(Router, self).__init__(parent)

    @property
    def Interface(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_ee3b04c1da65cc99c5a7a503492ed84b.Interface): An instance of the Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_ee3b04c1da65cc99c5a7a503492ed84b import Interface
        return Interface(self)

    @property
    def LearnedLsa(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedlsa_833c63bd6c25e1b5eae9fe3cf4256d16.LearnedLsa): An instance of the LearnedLsa class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedlsa_833c63bd6c25e1b5eae9fe3cf4256d16 import LearnedLsa
        return LearnedLsa(self)

    @property
    def NetworkRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.networkrange_c0c2b62f912fb146b24872fd01a280b9.NetworkRange): An instance of the NetworkRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.networkrange_c0c2b62f912fb146b24872fd01a280b9 import NetworkRange
        return NetworkRange(self)

    @property
    def RouteRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.routerange_e8b63d512383712e41b15bd4c306347b.RouteRange): An instance of the RouteRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.routerange_e8b63d512383712e41b15bd4c306347b import RouteRange
        return RouteRange(self)

    @property
    def UserLsaGroup(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.userlsagroup_7795cb447526ddc4b75100787366e015.UserLsaGroup): An instance of the UserLsaGroup class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.userlsagroup_7795cb447526ddc4b75100787366e015 import UserLsaGroup
        return UserLsaGroup(self)

    @property
    def DisableAutoGenerateLinkLsa(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DisableAutoGenerateLinkLsa'])
    @DisableAutoGenerateLinkLsa.setter
    def DisableAutoGenerateLinkLsa(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DisableAutoGenerateLinkLsa'], value)

    @property
    def DisableAutoGenerateRouterLsa(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DisableAutoGenerateRouterLsa'])
    @DisableAutoGenerateRouterLsa.setter
    def DisableAutoGenerateRouterLsa(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DisableAutoGenerateRouterLsa'], value)

    @property
    def DiscardLearnedLsa(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DiscardLearnedLsa'])
    @DiscardLearnedLsa.setter
    def DiscardLearnedLsa(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DiscardLearnedLsa'], value)

    @property
    def EnableGracefulRestartHelperMode(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableGracefulRestartHelperMode'])
    @EnableGracefulRestartHelperMode.setter
    def EnableGracefulRestartHelperMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableGracefulRestartHelperMode'], value)

    @property
    def EnableStrictLsaChecking(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableStrictLsaChecking'])
    @EnableStrictLsaChecking.setter
    def EnableStrictLsaChecking(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableStrictLsaChecking'], value)

    @property
    def EnableSupportReasonSwReloadOrUpgrade(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSupportReasonSwReloadOrUpgrade'])
    @EnableSupportReasonSwReloadOrUpgrade.setter
    def EnableSupportReasonSwReloadOrUpgrade(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSupportReasonSwReloadOrUpgrade'], value)

    @property
    def EnableSupportReasonSwRestart(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSupportReasonSwRestart'])
    @EnableSupportReasonSwRestart.setter
    def EnableSupportReasonSwRestart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSupportReasonSwRestart'], value)

    @property
    def EnableSupportReasonSwitchToRedundantControlProcessor(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSupportReasonSwitchToRedundantControlProcessor'])
    @EnableSupportReasonSwitchToRedundantControlProcessor.setter
    def EnableSupportReasonSwitchToRedundantControlProcessor(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSupportReasonSwitchToRedundantControlProcessor'], value)

    @property
    def EnableSupportReasonUnknown(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSupportReasonUnknown'])
    @EnableSupportReasonUnknown.setter
    def EnableSupportReasonUnknown(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSupportReasonUnknown'], value)

    @property
    def EnableSupportRfc5838(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSupportRfc5838'])
    @EnableSupportRfc5838.setter
    def EnableSupportRfc5838(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSupportRfc5838'], value)

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
    def IsLearnedLsaRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsLearnedLsaRefreshed'])

    @property
    def LsaRefreshTime(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LsaRefreshTime'])
    @LsaRefreshTime.setter
    def LsaRefreshTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LsaRefreshTime'], value)

    @property
    def LsaRetransmitTime(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LsaRetransmitTime'])
    @LsaRetransmitTime.setter
    def LsaRetransmitTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LsaRetransmitTime'], value)

    @property
    def MaxNumLsaPerSecond(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxNumLsaPerSecond'])
    @MaxNumLsaPerSecond.setter
    def MaxNumLsaPerSecond(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxNumLsaPerSecond'], value)

    @property
    def RouterId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouterId'])
    @RouterId.setter
    def RouterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouterId'], value)

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

    def update(self, DisableAutoGenerateLinkLsa=None, DisableAutoGenerateRouterLsa=None, DiscardLearnedLsa=None, EnableGracefulRestartHelperMode=None, EnableStrictLsaChecking=None, EnableSupportReasonSwReloadOrUpgrade=None, EnableSupportReasonSwRestart=None, EnableSupportReasonSwitchToRedundantControlProcessor=None, EnableSupportReasonUnknown=None, EnableSupportRfc5838=None, Enabled=None, LsaRefreshTime=None, LsaRetransmitTime=None, MaxNumLsaPerSecond=None, RouterId=None, TrafficGroupId=None):
        """Updates router resource on the server.

        Args
        ----
        - DisableAutoGenerateLinkLsa (bool): 
        - DisableAutoGenerateRouterLsa (bool): 
        - DiscardLearnedLsa (bool): 
        - EnableGracefulRestartHelperMode (bool): 
        - EnableStrictLsaChecking (bool): 
        - EnableSupportReasonSwReloadOrUpgrade (bool): 
        - EnableSupportReasonSwRestart (bool): 
        - EnableSupportReasonSwitchToRedundantControlProcessor (bool): 
        - EnableSupportReasonUnknown (bool): 
        - EnableSupportRfc5838 (bool): 
        - Enabled (bool): 
        - LsaRefreshTime (number): 
        - LsaRetransmitTime (number): 
        - MaxNumLsaPerSecond (number): 
        - RouterId (str): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, DisableAutoGenerateLinkLsa=None, DisableAutoGenerateRouterLsa=None, DiscardLearnedLsa=None, EnableGracefulRestartHelperMode=None, EnableStrictLsaChecking=None, EnableSupportReasonSwReloadOrUpgrade=None, EnableSupportReasonSwRestart=None, EnableSupportReasonSwitchToRedundantControlProcessor=None, EnableSupportReasonUnknown=None, EnableSupportRfc5838=None, Enabled=None, LsaRefreshTime=None, LsaRetransmitTime=None, MaxNumLsaPerSecond=None, RouterId=None, TrafficGroupId=None):
        """Adds a new router resource on the server and adds it to the container.

        Args
        ----
        - DisableAutoGenerateLinkLsa (bool): 
        - DisableAutoGenerateRouterLsa (bool): 
        - DiscardLearnedLsa (bool): 
        - EnableGracefulRestartHelperMode (bool): 
        - EnableStrictLsaChecking (bool): 
        - EnableSupportReasonSwReloadOrUpgrade (bool): 
        - EnableSupportReasonSwRestart (bool): 
        - EnableSupportReasonSwitchToRedundantControlProcessor (bool): 
        - EnableSupportReasonUnknown (bool): 
        - EnableSupportRfc5838 (bool): 
        - Enabled (bool): 
        - LsaRefreshTime (number): 
        - LsaRetransmitTime (number): 
        - MaxNumLsaPerSecond (number): 
        - RouterId (str): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 

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

    def find(self, DisableAutoGenerateLinkLsa=None, DisableAutoGenerateRouterLsa=None, DiscardLearnedLsa=None, EnableGracefulRestartHelperMode=None, EnableStrictLsaChecking=None, EnableSupportReasonSwReloadOrUpgrade=None, EnableSupportReasonSwRestart=None, EnableSupportReasonSwitchToRedundantControlProcessor=None, EnableSupportReasonUnknown=None, EnableSupportRfc5838=None, Enabled=None, IsLearnedLsaRefreshed=None, LsaRefreshTime=None, LsaRetransmitTime=None, MaxNumLsaPerSecond=None, RouterId=None, TrafficGroupId=None):
        """Finds and retrieves router resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve router resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all router resources from the server.

        Args
        ----
        - DisableAutoGenerateLinkLsa (bool): 
        - DisableAutoGenerateRouterLsa (bool): 
        - DiscardLearnedLsa (bool): 
        - EnableGracefulRestartHelperMode (bool): 
        - EnableStrictLsaChecking (bool): 
        - EnableSupportReasonSwReloadOrUpgrade (bool): 
        - EnableSupportReasonSwRestart (bool): 
        - EnableSupportReasonSwitchToRedundantControlProcessor (bool): 
        - EnableSupportReasonUnknown (bool): 
        - EnableSupportRfc5838 (bool): 
        - Enabled (bool): 
        - IsLearnedLsaRefreshed (bool): 
        - LsaRefreshTime (number): 
        - LsaRetransmitTime (number): 
        - MaxNumLsaPerSecond (number): 
        - RouterId (str): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 

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

    def GracefulRouterRestart(self, *args, **kwargs):
        """Executes the gracefulRouterRestart operation on the server.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        gracefulRouterRestart(Arg2=number, Arg3=enum, Arg4=number)string
        ----------------------------------------------------------------
        - Arg2 (number): 
        - Arg3 (str(softwareReloadOrUpgrade | softwareRestart | switchToRedundantControlProcessor | unknown)): 
        - Arg4 (number): 
        - Returns str: 

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('gracefulRouterRestart', payload=payload, response_object=None)

    def RefreshLearnedLsa(self):
        """Executes the refreshLearnedLsa operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshLearnedLsa', payload=payload, response_object=None)
