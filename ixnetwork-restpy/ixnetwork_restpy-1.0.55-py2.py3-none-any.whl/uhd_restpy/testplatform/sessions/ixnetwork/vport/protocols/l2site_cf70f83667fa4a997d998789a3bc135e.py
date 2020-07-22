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


class L2Site(Base):
    """
    The L2Site class encapsulates a list of l2Site resources that are managed by the user.
    A list of resources can be retrieved from the server using the L2Site.find() method.
    The list can be managed by using the L2Site.add() and L2Site.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'l2Site'
    _SDM_ATT_MAP = {
        'DistinguishAssignedIncrement': 'distinguishAssignedIncrement',
        'DistinguishIpIncrement': 'distinguishIpIncrement',
        'DistinguishNumberIncrementAs': 'distinguishNumberIncrementAs',
        'EnableBfdVccv': 'enableBfdVccv',
        'EnableCluster': 'enableCluster',
        'EnableControlWord': 'enableControlWord',
        'EnableL2SiteAsTrafficEndpoint': 'enableL2SiteAsTrafficEndpoint',
        'EnableSequenceDelivery': 'enableSequenceDelivery',
        'EnableVccvPing': 'enableVccvPing',
        'Enabled': 'enabled',
        'IsLearnedInfoRefreshed': 'isLearnedInfoRefreshed',
        'Mtu': 'mtu',
        'NoOfL2Site': 'noOfL2Site',
        'RouteDistinguisherAs': 'routeDistinguisherAs',
        'RouteDistinguisherAssignedNum': 'routeDistinguisherAssignedNum',
        'RouteDistinguisherIp': 'routeDistinguisherIp',
        'RouteDistinguisherType': 'routeDistinguisherType',
        'RouteTargetAs': 'routeTargetAs',
        'RouteTargetAssignedNum': 'routeTargetAssignedNum',
        'RouteTargetIp': 'routeTargetIp',
        'RouteTargetType': 'routeTargetType',
        'SiteId': 'siteId',
        'SiteIdIncrement': 'siteIdIncrement',
        'TargetAssignedNumberIncrement': 'targetAssignedNumberIncrement',
        'TargetIncrementAs': 'targetIncrementAs',
        'TargetIpIncrement': 'targetIpIncrement',
        'TrafficGroupId': 'trafficGroupId',
    }

    def __init__(self, parent):
        super(L2Site, self).__init__(parent)

    @property
    def Cluster(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.cluster_d68b61bb2cd5e48de06e56c1bb4b9cfb.Cluster): An instance of the Cluster class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.cluster_d68b61bb2cd5e48de06e56c1bb4b9cfb import Cluster
        return Cluster(self)._select()

    @property
    def LabelBlock(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.labelblock_6eb7f626a2a3e5d82b8862a7747ea32b.LabelBlock): An instance of the LabelBlock class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.labelblock_6eb7f626a2a3e5d82b8862a7747ea32b import LabelBlock
        return LabelBlock(self)

    @property
    def LearnedRoute(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedroute_2e9f44106274f7979df822941b6bf36d.LearnedRoute): An instance of the LearnedRoute class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedroute_2e9f44106274f7979df822941b6bf36d import LearnedRoute
        return LearnedRoute(self)

    @property
    def MacAddressRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.macaddressrange_c943358390fb51e82104338cc664cd83.MacAddressRange): An instance of the MacAddressRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.macaddressrange_c943358390fb51e82104338cc664cd83 import MacAddressRange
        return MacAddressRange(self)

    @property
    def DistinguishAssignedIncrement(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DistinguishAssignedIncrement'])
    @DistinguishAssignedIncrement.setter
    def DistinguishAssignedIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DistinguishAssignedIncrement'], value)

    @property
    def DistinguishIpIncrement(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DistinguishIpIncrement'])
    @DistinguishIpIncrement.setter
    def DistinguishIpIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DistinguishIpIncrement'], value)

    @property
    def DistinguishNumberIncrementAs(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DistinguishNumberIncrementAs'])
    @DistinguishNumberIncrementAs.setter
    def DistinguishNumberIncrementAs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DistinguishNumberIncrementAs'], value)

    @property
    def EnableBfdVccv(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableBfdVccv'])
    @EnableBfdVccv.setter
    def EnableBfdVccv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableBfdVccv'], value)

    @property
    def EnableCluster(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableCluster'])
    @EnableCluster.setter
    def EnableCluster(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableCluster'], value)

    @property
    def EnableControlWord(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableControlWord'])
    @EnableControlWord.setter
    def EnableControlWord(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableControlWord'], value)

    @property
    def EnableL2SiteAsTrafficEndpoint(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableL2SiteAsTrafficEndpoint'])
    @EnableL2SiteAsTrafficEndpoint.setter
    def EnableL2SiteAsTrafficEndpoint(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableL2SiteAsTrafficEndpoint'], value)

    @property
    def EnableSequenceDelivery(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSequenceDelivery'])
    @EnableSequenceDelivery.setter
    def EnableSequenceDelivery(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSequenceDelivery'], value)

    @property
    def EnableVccvPing(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableVccvPing'])
    @EnableVccvPing.setter
    def EnableVccvPing(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableVccvPing'], value)

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
    def IsLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsLearnedInfoRefreshed'])

    @property
    def Mtu(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mtu'])
    @Mtu.setter
    def Mtu(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mtu'], value)

    @property
    def NoOfL2Site(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfL2Site'])
    @NoOfL2Site.setter
    def NoOfL2Site(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfL2Site'], value)

    @property
    def RouteDistinguisherAs(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteDistinguisherAs'])
    @RouteDistinguisherAs.setter
    def RouteDistinguisherAs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouteDistinguisherAs'], value)

    @property
    def RouteDistinguisherAssignedNum(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteDistinguisherAssignedNum'])
    @RouteDistinguisherAssignedNum.setter
    def RouteDistinguisherAssignedNum(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouteDistinguisherAssignedNum'], value)

    @property
    def RouteDistinguisherIp(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteDistinguisherIp'])
    @RouteDistinguisherIp.setter
    def RouteDistinguisherIp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouteDistinguisherIp'], value)

    @property
    def RouteDistinguisherType(self):
        """
        Returns
        -------
        - str(twoOctetAs | ip | fourOctetAs): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteDistinguisherType'])
    @RouteDistinguisherType.setter
    def RouteDistinguisherType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouteDistinguisherType'], value)

    @property
    def RouteTargetAs(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteTargetAs'])
    @RouteTargetAs.setter
    def RouteTargetAs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouteTargetAs'], value)

    @property
    def RouteTargetAssignedNum(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteTargetAssignedNum'])
    @RouteTargetAssignedNum.setter
    def RouteTargetAssignedNum(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouteTargetAssignedNum'], value)

    @property
    def RouteTargetIp(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteTargetIp'])
    @RouteTargetIp.setter
    def RouteTargetIp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouteTargetIp'], value)

    @property
    def RouteTargetType(self):
        """
        Returns
        -------
        - str(as | ip): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteTargetType'])
    @RouteTargetType.setter
    def RouteTargetType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouteTargetType'], value)

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
    def SiteIdIncrement(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SiteIdIncrement'])
    @SiteIdIncrement.setter
    def SiteIdIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SiteIdIncrement'], value)

    @property
    def TargetAssignedNumberIncrement(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TargetAssignedNumberIncrement'])
    @TargetAssignedNumberIncrement.setter
    def TargetAssignedNumberIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TargetAssignedNumberIncrement'], value)

    @property
    def TargetIncrementAs(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TargetIncrementAs'])
    @TargetIncrementAs.setter
    def TargetIncrementAs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TargetIncrementAs'], value)

    @property
    def TargetIpIncrement(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TargetIpIncrement'])
    @TargetIpIncrement.setter
    def TargetIpIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TargetIpIncrement'], value)

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

    def update(self, DistinguishAssignedIncrement=None, DistinguishIpIncrement=None, DistinguishNumberIncrementAs=None, EnableBfdVccv=None, EnableCluster=None, EnableControlWord=None, EnableL2SiteAsTrafficEndpoint=None, EnableSequenceDelivery=None, EnableVccvPing=None, Enabled=None, Mtu=None, NoOfL2Site=None, RouteDistinguisherAs=None, RouteDistinguisherAssignedNum=None, RouteDistinguisherIp=None, RouteDistinguisherType=None, RouteTargetAs=None, RouteTargetAssignedNum=None, RouteTargetIp=None, RouteTargetType=None, SiteId=None, SiteIdIncrement=None, TargetAssignedNumberIncrement=None, TargetIncrementAs=None, TargetIpIncrement=None, TrafficGroupId=None):
        """Updates l2Site resource on the server.

        Args
        ----
        - DistinguishAssignedIncrement (number): 
        - DistinguishIpIncrement (str): 
        - DistinguishNumberIncrementAs (number): 
        - EnableBfdVccv (bool): 
        - EnableCluster (bool): 
        - EnableControlWord (bool): 
        - EnableL2SiteAsTrafficEndpoint (bool): 
        - EnableSequenceDelivery (bool): 
        - EnableVccvPing (bool): 
        - Enabled (bool): 
        - Mtu (number): 
        - NoOfL2Site (number): 
        - RouteDistinguisherAs (number): 
        - RouteDistinguisherAssignedNum (number): 
        - RouteDistinguisherIp (str): 
        - RouteDistinguisherType (str(twoOctetAs | ip | fourOctetAs)): 
        - RouteTargetAs (number): 
        - RouteTargetAssignedNum (number): 
        - RouteTargetIp (str): 
        - RouteTargetType (str(as | ip)): 
        - SiteId (number): 
        - SiteIdIncrement (number): 
        - TargetAssignedNumberIncrement (number): 
        - TargetIncrementAs (number): 
        - TargetIpIncrement (str): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, DistinguishAssignedIncrement=None, DistinguishIpIncrement=None, DistinguishNumberIncrementAs=None, EnableBfdVccv=None, EnableCluster=None, EnableControlWord=None, EnableL2SiteAsTrafficEndpoint=None, EnableSequenceDelivery=None, EnableVccvPing=None, Enabled=None, Mtu=None, NoOfL2Site=None, RouteDistinguisherAs=None, RouteDistinguisherAssignedNum=None, RouteDistinguisherIp=None, RouteDistinguisherType=None, RouteTargetAs=None, RouteTargetAssignedNum=None, RouteTargetIp=None, RouteTargetType=None, SiteId=None, SiteIdIncrement=None, TargetAssignedNumberIncrement=None, TargetIncrementAs=None, TargetIpIncrement=None, TrafficGroupId=None):
        """Adds a new l2Site resource on the server and adds it to the container.

        Args
        ----
        - DistinguishAssignedIncrement (number): 
        - DistinguishIpIncrement (str): 
        - DistinguishNumberIncrementAs (number): 
        - EnableBfdVccv (bool): 
        - EnableCluster (bool): 
        - EnableControlWord (bool): 
        - EnableL2SiteAsTrafficEndpoint (bool): 
        - EnableSequenceDelivery (bool): 
        - EnableVccvPing (bool): 
        - Enabled (bool): 
        - Mtu (number): 
        - NoOfL2Site (number): 
        - RouteDistinguisherAs (number): 
        - RouteDistinguisherAssignedNum (number): 
        - RouteDistinguisherIp (str): 
        - RouteDistinguisherType (str(twoOctetAs | ip | fourOctetAs)): 
        - RouteTargetAs (number): 
        - RouteTargetAssignedNum (number): 
        - RouteTargetIp (str): 
        - RouteTargetType (str(as | ip)): 
        - SiteId (number): 
        - SiteIdIncrement (number): 
        - TargetAssignedNumberIncrement (number): 
        - TargetIncrementAs (number): 
        - TargetIpIncrement (str): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 

        Returns
        -------
        - self: This instance with all currently retrieved l2Site resources using find and the newly added l2Site resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained l2Site resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, DistinguishAssignedIncrement=None, DistinguishIpIncrement=None, DistinguishNumberIncrementAs=None, EnableBfdVccv=None, EnableCluster=None, EnableControlWord=None, EnableL2SiteAsTrafficEndpoint=None, EnableSequenceDelivery=None, EnableVccvPing=None, Enabled=None, IsLearnedInfoRefreshed=None, Mtu=None, NoOfL2Site=None, RouteDistinguisherAs=None, RouteDistinguisherAssignedNum=None, RouteDistinguisherIp=None, RouteDistinguisherType=None, RouteTargetAs=None, RouteTargetAssignedNum=None, RouteTargetIp=None, RouteTargetType=None, SiteId=None, SiteIdIncrement=None, TargetAssignedNumberIncrement=None, TargetIncrementAs=None, TargetIpIncrement=None, TrafficGroupId=None):
        """Finds and retrieves l2Site resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve l2Site resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all l2Site resources from the server.

        Args
        ----
        - DistinguishAssignedIncrement (number): 
        - DistinguishIpIncrement (str): 
        - DistinguishNumberIncrementAs (number): 
        - EnableBfdVccv (bool): 
        - EnableCluster (bool): 
        - EnableControlWord (bool): 
        - EnableL2SiteAsTrafficEndpoint (bool): 
        - EnableSequenceDelivery (bool): 
        - EnableVccvPing (bool): 
        - Enabled (bool): 
        - IsLearnedInfoRefreshed (bool): 
        - Mtu (number): 
        - NoOfL2Site (number): 
        - RouteDistinguisherAs (number): 
        - RouteDistinguisherAssignedNum (number): 
        - RouteDistinguisherIp (str): 
        - RouteDistinguisherType (str(twoOctetAs | ip | fourOctetAs)): 
        - RouteTargetAs (number): 
        - RouteTargetAssignedNum (number): 
        - RouteTargetIp (str): 
        - RouteTargetType (str(as | ip)): 
        - SiteId (number): 
        - SiteIdIncrement (number): 
        - TargetAssignedNumberIncrement (number): 
        - TargetIncrementAs (number): 
        - TargetIpIncrement (str): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 

        Returns
        -------
        - self: This instance with matching l2Site resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of l2Site data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the l2Site resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def RefreshLearnedInfo(self):
        """Executes the refreshLearnedInfo operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshLearnedInfo', payload=payload, response_object=None)
