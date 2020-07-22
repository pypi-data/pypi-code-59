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


class LearnedFilter(Base):
    """
    The LearnedFilter class encapsulates a required learnedFilter resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedFilter'
    _SDM_ATT_MAP = {
        'AdvRouterId': 'advRouterId',
        'AreaSummaryLsaCount': 'areaSummaryLsaCount',
        'EnableAdvRouterId': 'enableAdvRouterId',
        'EnableFilter': 'enableFilter',
        'EnableLinkStateId': 'enableLinkStateId',
        'ExcludeAdvRouterId': 'excludeAdvRouterId',
        'ExcludeLinkStateId': 'excludeLinkStateId',
        'ExternalLsaCount': 'externalLsaCount',
        'ExternalSummaryLsaCount': 'externalSummaryLsaCount',
        'IsComplete': 'isComplete',
        'LinkStateId': 'linkStateId',
        'NetworkLsaCount': 'networkLsaCount',
        'NssaLsaCount': 'nssaLsaCount',
        'OpaqueAreaScopeLsaCount': 'opaqueAreaScopeLsaCount',
        'OpaqueAsScopeLsaCount': 'opaqueAsScopeLsaCount',
        'OpaqueLocalScopeLsaCount': 'opaqueLocalScopeLsaCount',
        'RouterLsaCount': 'routerLsaCount',
        'ShowExternalAsLsa': 'showExternalAsLsa',
        'ShowNetworkLsa': 'showNetworkLsa',
        'ShowNssaLsa': 'showNssaLsa',
        'ShowOpaqueAreaLsa': 'showOpaqueAreaLsa',
        'ShowOpaqueDomainLsa': 'showOpaqueDomainLsa',
        'ShowOpaqueLocalLsa': 'showOpaqueLocalLsa',
        'ShowRouterLsa': 'showRouterLsa',
        'ShowSummaryAsLsa': 'showSummaryAsLsa',
        'ShowSummaryIpLsa': 'showSummaryIpLsa',
        'TotalLsaCount': 'totalLsaCount',
    }

    def __init__(self, parent):
        super(LearnedFilter, self).__init__(parent)

    @property
    def AdvRouterId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdvRouterId'])
    @AdvRouterId.setter
    def AdvRouterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AdvRouterId'], value)

    @property
    def AreaSummaryLsaCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AreaSummaryLsaCount'])

    @property
    def EnableAdvRouterId(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAdvRouterId'])
    @EnableAdvRouterId.setter
    def EnableAdvRouterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAdvRouterId'], value)

    @property
    def EnableFilter(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableFilter'])
    @EnableFilter.setter
    def EnableFilter(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableFilter'], value)

    @property
    def EnableLinkStateId(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLinkStateId'])
    @EnableLinkStateId.setter
    def EnableLinkStateId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLinkStateId'], value)

    @property
    def ExcludeAdvRouterId(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExcludeAdvRouterId'])
    @ExcludeAdvRouterId.setter
    def ExcludeAdvRouterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExcludeAdvRouterId'], value)

    @property
    def ExcludeLinkStateId(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExcludeLinkStateId'])
    @ExcludeLinkStateId.setter
    def ExcludeLinkStateId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExcludeLinkStateId'], value)

    @property
    def ExternalLsaCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExternalLsaCount'])

    @property
    def ExternalSummaryLsaCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExternalSummaryLsaCount'])

    @property
    def IsComplete(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsComplete'])

    @property
    def LinkStateId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkStateId'])
    @LinkStateId.setter
    def LinkStateId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkStateId'], value)

    @property
    def NetworkLsaCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkLsaCount'])

    @property
    def NssaLsaCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NssaLsaCount'])

    @property
    def OpaqueAreaScopeLsaCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OpaqueAreaScopeLsaCount'])

    @property
    def OpaqueAsScopeLsaCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OpaqueAsScopeLsaCount'])

    @property
    def OpaqueLocalScopeLsaCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OpaqueLocalScopeLsaCount'])

    @property
    def RouterLsaCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouterLsaCount'])

    @property
    def ShowExternalAsLsa(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShowExternalAsLsa'])
    @ShowExternalAsLsa.setter
    def ShowExternalAsLsa(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ShowExternalAsLsa'], value)

    @property
    def ShowNetworkLsa(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShowNetworkLsa'])
    @ShowNetworkLsa.setter
    def ShowNetworkLsa(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ShowNetworkLsa'], value)

    @property
    def ShowNssaLsa(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShowNssaLsa'])
    @ShowNssaLsa.setter
    def ShowNssaLsa(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ShowNssaLsa'], value)

    @property
    def ShowOpaqueAreaLsa(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShowOpaqueAreaLsa'])
    @ShowOpaqueAreaLsa.setter
    def ShowOpaqueAreaLsa(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ShowOpaqueAreaLsa'], value)

    @property
    def ShowOpaqueDomainLsa(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShowOpaqueDomainLsa'])
    @ShowOpaqueDomainLsa.setter
    def ShowOpaqueDomainLsa(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ShowOpaqueDomainLsa'], value)

    @property
    def ShowOpaqueLocalLsa(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShowOpaqueLocalLsa'])
    @ShowOpaqueLocalLsa.setter
    def ShowOpaqueLocalLsa(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ShowOpaqueLocalLsa'], value)

    @property
    def ShowRouterLsa(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShowRouterLsa'])
    @ShowRouterLsa.setter
    def ShowRouterLsa(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ShowRouterLsa'], value)

    @property
    def ShowSummaryAsLsa(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShowSummaryAsLsa'])
    @ShowSummaryAsLsa.setter
    def ShowSummaryAsLsa(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ShowSummaryAsLsa'], value)

    @property
    def ShowSummaryIpLsa(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShowSummaryIpLsa'])
    @ShowSummaryIpLsa.setter
    def ShowSummaryIpLsa(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ShowSummaryIpLsa'], value)

    @property
    def TotalLsaCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TotalLsaCount'])

    def update(self, AdvRouterId=None, EnableAdvRouterId=None, EnableFilter=None, EnableLinkStateId=None, ExcludeAdvRouterId=None, ExcludeLinkStateId=None, LinkStateId=None, ShowExternalAsLsa=None, ShowNetworkLsa=None, ShowNssaLsa=None, ShowOpaqueAreaLsa=None, ShowOpaqueDomainLsa=None, ShowOpaqueLocalLsa=None, ShowRouterLsa=None, ShowSummaryAsLsa=None, ShowSummaryIpLsa=None):
        """Updates learnedFilter resource on the server.

        Args
        ----
        - AdvRouterId (str): 
        - EnableAdvRouterId (bool): 
        - EnableFilter (bool): 
        - EnableLinkStateId (bool): 
        - ExcludeAdvRouterId (bool): 
        - ExcludeLinkStateId (bool): 
        - LinkStateId (str): 
        - ShowExternalAsLsa (bool): 
        - ShowNetworkLsa (bool): 
        - ShowNssaLsa (bool): 
        - ShowOpaqueAreaLsa (bool): 
        - ShowOpaqueDomainLsa (bool): 
        - ShowOpaqueLocalLsa (bool): 
        - ShowRouterLsa (bool): 
        - ShowSummaryAsLsa (bool): 
        - ShowSummaryIpLsa (bool): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
