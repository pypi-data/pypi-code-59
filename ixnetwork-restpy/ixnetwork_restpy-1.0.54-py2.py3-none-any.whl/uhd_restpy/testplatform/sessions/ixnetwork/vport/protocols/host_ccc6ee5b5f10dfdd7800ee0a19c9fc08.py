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


class Host(Base):
    """
    The Host class encapsulates a list of host resources that are managed by the user.
    A list of resources can be retrieved from the server using the Host.find() method.
    The list can be managed by using the Host.add() and Host.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'host'
    _SDM_ATT_MAP = {
        'EnableImmediateResp': 'enableImmediateResp',
        'EnableQueryResMode': 'enableQueryResMode',
        'EnableRouterAlert': 'enableRouterAlert',
        'EnableSpecificResMode': 'enableSpecificResMode',
        'EnableSuppressReport': 'enableSuppressReport',
        'EnableUnsolicitedResMode': 'enableUnsolicitedResMode',
        'Enabled': 'enabled',
        'InterfaceIndex': 'interfaceIndex',
        'InterfaceType': 'interfaceType',
        'Interfaces': 'interfaces',
        'ProtocolInterface': 'protocolInterface',
        'ReportFreq': 'reportFreq',
        'RobustnessVariable': 'robustnessVariable',
        'TrafficGroupId': 'trafficGroupId',
        'Version': 'version',
    }

    def __init__(self, parent):
        super(Host, self).__init__(parent)

    @property
    def GroupRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.grouprange_24a71c3cd8132c5bc9c3c0de300abf10.GroupRange): An instance of the GroupRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.grouprange_24a71c3cd8132c5bc9c3c0de300abf10 import GroupRange
        return GroupRange(self)

    @property
    def EnableImmediateResp(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableImmediateResp'])
    @EnableImmediateResp.setter
    def EnableImmediateResp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableImmediateResp'], value)

    @property
    def EnableQueryResMode(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableQueryResMode'])
    @EnableQueryResMode.setter
    def EnableQueryResMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableQueryResMode'], value)

    @property
    def EnableRouterAlert(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableRouterAlert'])
    @EnableRouterAlert.setter
    def EnableRouterAlert(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableRouterAlert'], value)

    @property
    def EnableSpecificResMode(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSpecificResMode'])
    @EnableSpecificResMode.setter
    def EnableSpecificResMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSpecificResMode'], value)

    @property
    def EnableSuppressReport(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSuppressReport'])
    @EnableSuppressReport.setter
    def EnableSuppressReport(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSuppressReport'], value)

    @property
    def EnableUnsolicitedResMode(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableUnsolicitedResMode'])
    @EnableUnsolicitedResMode.setter
    def EnableUnsolicitedResMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableUnsolicitedResMode'], value)

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
    def ProtocolInterface(self):
        """DEPRECATED 
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolInterface'])
    @ProtocolInterface.setter
    def ProtocolInterface(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProtocolInterface'], value)

    @property
    def ReportFreq(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReportFreq'])
    @ReportFreq.setter
    def ReportFreq(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReportFreq'], value)

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
    def Version(self):
        """
        Returns
        -------
        - str(version1 | version2): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Version'])
    @Version.setter
    def Version(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Version'], value)

    def update(self, EnableImmediateResp=None, EnableQueryResMode=None, EnableRouterAlert=None, EnableSpecificResMode=None, EnableSuppressReport=None, EnableUnsolicitedResMode=None, Enabled=None, InterfaceIndex=None, InterfaceType=None, Interfaces=None, ProtocolInterface=None, ReportFreq=None, RobustnessVariable=None, TrafficGroupId=None, Version=None):
        """Updates host resource on the server.

        Args
        ----
        - EnableImmediateResp (bool): 
        - EnableQueryResMode (bool): 
        - EnableRouterAlert (bool): 
        - EnableSpecificResMode (bool): 
        - EnableSuppressReport (bool): 
        - EnableUnsolicitedResMode (bool): 
        - Enabled (bool): 
        - InterfaceIndex (number): 
        - InterfaceType (str): 
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): 
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - ReportFreq (number): 
        - RobustnessVariable (number): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 
        - Version (str(version1 | version2)): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, EnableImmediateResp=None, EnableQueryResMode=None, EnableRouterAlert=None, EnableSpecificResMode=None, EnableSuppressReport=None, EnableUnsolicitedResMode=None, Enabled=None, InterfaceIndex=None, InterfaceType=None, Interfaces=None, ProtocolInterface=None, ReportFreq=None, RobustnessVariable=None, TrafficGroupId=None, Version=None):
        """Adds a new host resource on the server and adds it to the container.

        Args
        ----
        - EnableImmediateResp (bool): 
        - EnableQueryResMode (bool): 
        - EnableRouterAlert (bool): 
        - EnableSpecificResMode (bool): 
        - EnableSuppressReport (bool): 
        - EnableUnsolicitedResMode (bool): 
        - Enabled (bool): 
        - InterfaceIndex (number): 
        - InterfaceType (str): 
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): 
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - ReportFreq (number): 
        - RobustnessVariable (number): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 
        - Version (str(version1 | version2)): 

        Returns
        -------
        - self: This instance with all currently retrieved host resources using find and the newly added host resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained host resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EnableImmediateResp=None, EnableQueryResMode=None, EnableRouterAlert=None, EnableSpecificResMode=None, EnableSuppressReport=None, EnableUnsolicitedResMode=None, Enabled=None, InterfaceIndex=None, InterfaceType=None, Interfaces=None, ProtocolInterface=None, ReportFreq=None, RobustnessVariable=None, TrafficGroupId=None, Version=None):
        """Finds and retrieves host resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve host resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all host resources from the server.

        Args
        ----
        - EnableImmediateResp (bool): 
        - EnableQueryResMode (bool): 
        - EnableRouterAlert (bool): 
        - EnableSpecificResMode (bool): 
        - EnableSuppressReport (bool): 
        - EnableUnsolicitedResMode (bool): 
        - Enabled (bool): 
        - InterfaceIndex (number): 
        - InterfaceType (str): 
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): 
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - ReportFreq (number): 
        - RobustnessVariable (number): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 
        - Version (str(version1 | version2)): 

        Returns
        -------
        - self: This instance with matching host resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of host data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the host resources from the server available through an iterator or index

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
