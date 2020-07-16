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


class Querier(Base):
    """
    The Querier class encapsulates a list of querier resources that are managed by the user.
    A list of resources can be retrieved from the server using the Querier.find() method.
    The list can be managed by using the Querier.add() and Querier.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'querier'
    _SDM_ATT_MAP = {
        'DiscardLearnedInfo': 'discardLearnedInfo',
        'Enabled': 'enabled',
        'GeneralQueryInterval': 'generalQueryInterval',
        'GqResponseInterval': 'gqResponseInterval',
        'InterfaceId': 'interfaceId',
        'InterfaceIndex': 'interfaceIndex',
        'InterfaceType': 'interfaceType',
        'Interfaces': 'interfaces',
        'IsQuerier': 'isQuerier',
        'IsRefreshComplete': 'isRefreshComplete',
        'QuerierAddress': 'querierAddress',
        'QuerierWorkingVersion': 'querierWorkingVersion',
        'RobustnessVariable': 'robustnessVariable',
        'RouterAlert': 'routerAlert',
        'SqResponseInterval': 'sqResponseInterval',
        'SqTransmissionCount': 'sqTransmissionCount',
        'StartupQueryCount': 'startupQueryCount',
        'SupportElection': 'supportElection',
        'SupportOlderVersionHost': 'supportOlderVersionHost',
        'SupportOlderVersionQuerier': 'supportOlderVersionQuerier',
        'Version': 'version',
    }

    def __init__(self, parent):
        super(Querier, self).__init__(parent)

    @property
    def LearnedGroupInfo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedgroupinfo_c4e5fdc0403e0f4d6b65c94ff23618de.LearnedGroupInfo): An instance of the LearnedGroupInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedgroupinfo_c4e5fdc0403e0f4d6b65c94ff23618de import LearnedGroupInfo
        return LearnedGroupInfo(self)

    @property
    def DiscardLearnedInfo(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DiscardLearnedInfo'])
    @DiscardLearnedInfo.setter
    def DiscardLearnedInfo(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DiscardLearnedInfo'], value)

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
    def GeneralQueryInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['GeneralQueryInterval'])
    @GeneralQueryInterval.setter
    def GeneralQueryInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GeneralQueryInterval'], value)

    @property
    def GqResponseInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['GqResponseInterval'])
    @GqResponseInterval.setter
    def GqResponseInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GqResponseInterval'], value)

    @property
    def InterfaceId(self):
        """DEPRECATED 
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceId'])
    @InterfaceId.setter
    def InterfaceId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceId'], value)

    @property
    def InterfaceIndex(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceIndex'])
    @InterfaceIndex.setter
    def InterfaceIndex(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceIndex'], value)

    @property
    def InterfaceType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceType'])
    @InterfaceType.setter
    def InterfaceType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceType'], value)

    @property
    def Interfaces(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Interfaces'])
    @Interfaces.setter
    def Interfaces(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Interfaces'], value)

    @property
    def IsQuerier(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsQuerier'])

    @property
    def IsRefreshComplete(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsRefreshComplete'])

    @property
    def QuerierAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['QuerierAddress'])

    @property
    def QuerierWorkingVersion(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['QuerierWorkingVersion'])

    @property
    def RobustnessVariable(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RobustnessVariable'])
    @RobustnessVariable.setter
    def RobustnessVariable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RobustnessVariable'], value)

    @property
    def RouterAlert(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouterAlert'])
    @RouterAlert.setter
    def RouterAlert(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouterAlert'], value)

    @property
    def SqResponseInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SqResponseInterval'])
    @SqResponseInterval.setter
    def SqResponseInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SqResponseInterval'], value)

    @property
    def SqTransmissionCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SqTransmissionCount'])
    @SqTransmissionCount.setter
    def SqTransmissionCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SqTransmissionCount'], value)

    @property
    def StartupQueryCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartupQueryCount'])
    @StartupQueryCount.setter
    def StartupQueryCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartupQueryCount'], value)

    @property
    def SupportElection(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportElection'])
    @SupportElection.setter
    def SupportElection(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportElection'], value)

    @property
    def SupportOlderVersionHost(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportOlderVersionHost'])
    @SupportOlderVersionHost.setter
    def SupportOlderVersionHost(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportOlderVersionHost'], value)

    @property
    def SupportOlderVersionQuerier(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportOlderVersionQuerier'])
    @SupportOlderVersionQuerier.setter
    def SupportOlderVersionQuerier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportOlderVersionQuerier'], value)

    @property
    def Version(self):
        """
        Returns
        -------
        - str(igmpv1 | igmpv2 | igmpv3): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Version'])
    @Version.setter
    def Version(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Version'], value)

    def update(self, DiscardLearnedInfo=None, Enabled=None, GeneralQueryInterval=None, GqResponseInterval=None, InterfaceId=None, InterfaceIndex=None, InterfaceType=None, Interfaces=None, RobustnessVariable=None, RouterAlert=None, SqResponseInterval=None, SqTransmissionCount=None, StartupQueryCount=None, SupportElection=None, SupportOlderVersionHost=None, SupportOlderVersionQuerier=None, Version=None):
        """Updates querier resource on the server.

        Args
        ----
        - DiscardLearnedInfo (bool): 
        - Enabled (bool): 
        - GeneralQueryInterval (number): 
        - GqResponseInterval (number): 
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - InterfaceIndex (number): 
        - InterfaceType (str): 
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): 
        - RobustnessVariable (number): 
        - RouterAlert (bool): 
        - SqResponseInterval (number): 
        - SqTransmissionCount (number): 
        - StartupQueryCount (number): 
        - SupportElection (bool): 
        - SupportOlderVersionHost (bool): 
        - SupportOlderVersionQuerier (bool): 
        - Version (str(igmpv1 | igmpv2 | igmpv3)): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, DiscardLearnedInfo=None, Enabled=None, GeneralQueryInterval=None, GqResponseInterval=None, InterfaceId=None, InterfaceIndex=None, InterfaceType=None, Interfaces=None, RobustnessVariable=None, RouterAlert=None, SqResponseInterval=None, SqTransmissionCount=None, StartupQueryCount=None, SupportElection=None, SupportOlderVersionHost=None, SupportOlderVersionQuerier=None, Version=None):
        """Adds a new querier resource on the server and adds it to the container.

        Args
        ----
        - DiscardLearnedInfo (bool): 
        - Enabled (bool): 
        - GeneralQueryInterval (number): 
        - GqResponseInterval (number): 
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - InterfaceIndex (number): 
        - InterfaceType (str): 
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): 
        - RobustnessVariable (number): 
        - RouterAlert (bool): 
        - SqResponseInterval (number): 
        - SqTransmissionCount (number): 
        - StartupQueryCount (number): 
        - SupportElection (bool): 
        - SupportOlderVersionHost (bool): 
        - SupportOlderVersionQuerier (bool): 
        - Version (str(igmpv1 | igmpv2 | igmpv3)): 

        Returns
        -------
        - self: This instance with all currently retrieved querier resources using find and the newly added querier resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained querier resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, DiscardLearnedInfo=None, Enabled=None, GeneralQueryInterval=None, GqResponseInterval=None, InterfaceId=None, InterfaceIndex=None, InterfaceType=None, Interfaces=None, IsQuerier=None, IsRefreshComplete=None, QuerierAddress=None, QuerierWorkingVersion=None, RobustnessVariable=None, RouterAlert=None, SqResponseInterval=None, SqTransmissionCount=None, StartupQueryCount=None, SupportElection=None, SupportOlderVersionHost=None, SupportOlderVersionQuerier=None, Version=None):
        """Finds and retrieves querier resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve querier resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all querier resources from the server.

        Args
        ----
        - DiscardLearnedInfo (bool): 
        - Enabled (bool): 
        - GeneralQueryInterval (number): 
        - GqResponseInterval (number): 
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - InterfaceIndex (number): 
        - InterfaceType (str): 
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): 
        - IsQuerier (bool): 
        - IsRefreshComplete (bool): 
        - QuerierAddress (str): 
        - QuerierWorkingVersion (number): 
        - RobustnessVariable (number): 
        - RouterAlert (bool): 
        - SqResponseInterval (number): 
        - SqTransmissionCount (number): 
        - StartupQueryCount (number): 
        - SupportElection (bool): 
        - SupportOlderVersionHost (bool): 
        - SupportOlderVersionQuerier (bool): 
        - Version (str(igmpv1 | igmpv2 | igmpv3)): 

        Returns
        -------
        - self: This instance with matching querier resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of querier data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the querier resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def GetInterfaceAccessorIfaceList(self):
        """Executes the getInterfaceAccessorIfaceList operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('getInterfaceAccessorIfaceList', payload=payload, response_object=None)

    def RefreshLearnedInfo(self):
        """Executes the refreshLearnedInfo operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshLearnedInfo', payload=payload, response_object=None)
