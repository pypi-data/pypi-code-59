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


class Link(Base):
    """
    The Link class encapsulates a list of link resources that are managed by the user.
    A list of resources can be retrieved from the server using the Link.find() method.
    The list can be managed by using the Link.add() and Link.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'link'
    _SDM_ATT_MAP = {
        'ActorKey': 'actorKey',
        'ActorPortNumber': 'actorPortNumber',
        'ActorPortPriority': 'actorPortPriority',
        'ActorSystemId': 'actorSystemId',
        'ActorSystemPriority': 'actorSystemPriority',
        'AdministrativeKey': 'administrativeKey',
        'AggregationFlagState': 'aggregationFlagState',
        'AutoPickPortMac': 'autoPickPortMac',
        'CollectingFlag': 'collectingFlag',
        'CollectorMaxDelay': 'collectorMaxDelay',
        'DistributingFlag': 'distributingFlag',
        'Enabled': 'enabled',
        'InterMarkerPduDelay': 'interMarkerPduDelay',
        'LacpActivity': 'lacpActivity',
        'LacpTimeout': 'lacpTimeout',
        'LacpduPeriodicTimeInterval': 'lacpduPeriodicTimeInterval',
        'MarkerRequestMode': 'markerRequestMode',
        'MarkerResponseWaitTime': 'markerResponseWaitTime',
        'PortMac': 'portMac',
        'SendMarkerRequestOnLagChange': 'sendMarkerRequestOnLagChange',
        'SendPeriodicMarkerRequest': 'sendPeriodicMarkerRequest',
        'SupportRespondingToMarker': 'supportRespondingToMarker',
        'SyncFlag': 'syncFlag',
        'UpdateRequired': 'updateRequired',
    }

    def __init__(self, parent):
        super(Link, self).__init__(parent)

    @property
    def ActorKey(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActorKey'])
    @ActorKey.setter
    def ActorKey(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ActorKey'], value)

    @property
    def ActorPortNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActorPortNumber'])
    @ActorPortNumber.setter
    def ActorPortNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ActorPortNumber'], value)

    @property
    def ActorPortPriority(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActorPortPriority'])
    @ActorPortPriority.setter
    def ActorPortPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ActorPortPriority'], value)

    @property
    def ActorSystemId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActorSystemId'])
    @ActorSystemId.setter
    def ActorSystemId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ActorSystemId'], value)

    @property
    def ActorSystemPriority(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActorSystemPriority'])
    @ActorSystemPriority.setter
    def ActorSystemPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ActorSystemPriority'], value)

    @property
    def AdministrativeKey(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdministrativeKey'])
    @AdministrativeKey.setter
    def AdministrativeKey(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AdministrativeKey'], value)

    @property
    def AggregationFlagState(self):
        """
        Returns
        -------
        - str(disable | auto): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AggregationFlagState'])
    @AggregationFlagState.setter
    def AggregationFlagState(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AggregationFlagState'], value)

    @property
    def AutoPickPortMac(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutoPickPortMac'])
    @AutoPickPortMac.setter
    def AutoPickPortMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AutoPickPortMac'], value)

    @property
    def CollectingFlag(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CollectingFlag'])
    @CollectingFlag.setter
    def CollectingFlag(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CollectingFlag'], value)

    @property
    def CollectorMaxDelay(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CollectorMaxDelay'])
    @CollectorMaxDelay.setter
    def CollectorMaxDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CollectorMaxDelay'], value)

    @property
    def DistributingFlag(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DistributingFlag'])
    @DistributingFlag.setter
    def DistributingFlag(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DistributingFlag'], value)

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
    def InterMarkerPduDelay(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterMarkerPduDelay'])
    @InterMarkerPduDelay.setter
    def InterMarkerPduDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterMarkerPduDelay'], value)

    @property
    def LacpActivity(self):
        """
        Returns
        -------
        - str(active | passive): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LacpActivity'])
    @LacpActivity.setter
    def LacpActivity(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LacpActivity'], value)

    @property
    def LacpTimeout(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LacpTimeout'])
    @LacpTimeout.setter
    def LacpTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LacpTimeout'], value)

    @property
    def LacpduPeriodicTimeInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LacpduPeriodicTimeInterval'])
    @LacpduPeriodicTimeInterval.setter
    def LacpduPeriodicTimeInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LacpduPeriodicTimeInterval'], value)

    @property
    def MarkerRequestMode(self):
        """
        Returns
        -------
        - str(fixed | random): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MarkerRequestMode'])
    @MarkerRequestMode.setter
    def MarkerRequestMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MarkerRequestMode'], value)

    @property
    def MarkerResponseWaitTime(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MarkerResponseWaitTime'])
    @MarkerResponseWaitTime.setter
    def MarkerResponseWaitTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MarkerResponseWaitTime'], value)

    @property
    def PortMac(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortMac'])
    @PortMac.setter
    def PortMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortMac'], value)

    @property
    def SendMarkerRequestOnLagChange(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendMarkerRequestOnLagChange'])
    @SendMarkerRequestOnLagChange.setter
    def SendMarkerRequestOnLagChange(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendMarkerRequestOnLagChange'], value)

    @property
    def SendPeriodicMarkerRequest(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendPeriodicMarkerRequest'])
    @SendPeriodicMarkerRequest.setter
    def SendPeriodicMarkerRequest(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendPeriodicMarkerRequest'], value)

    @property
    def SupportRespondingToMarker(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportRespondingToMarker'])
    @SupportRespondingToMarker.setter
    def SupportRespondingToMarker(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportRespondingToMarker'], value)

    @property
    def SyncFlag(self):
        """
        Returns
        -------
        - str(disable | auto): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SyncFlag'])
    @SyncFlag.setter
    def SyncFlag(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SyncFlag'], value)

    @property
    def UpdateRequired(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpdateRequired'])

    def update(self, ActorKey=None, ActorPortNumber=None, ActorPortPriority=None, ActorSystemId=None, ActorSystemPriority=None, AdministrativeKey=None, AggregationFlagState=None, AutoPickPortMac=None, CollectingFlag=None, CollectorMaxDelay=None, DistributingFlag=None, Enabled=None, InterMarkerPduDelay=None, LacpActivity=None, LacpTimeout=None, LacpduPeriodicTimeInterval=None, MarkerRequestMode=None, MarkerResponseWaitTime=None, PortMac=None, SendMarkerRequestOnLagChange=None, SendPeriodicMarkerRequest=None, SupportRespondingToMarker=None, SyncFlag=None):
        """Updates link resource on the server.

        Args
        ----
        - ActorKey (number): 
        - ActorPortNumber (number): 
        - ActorPortPriority (number): 
        - ActorSystemId (str): 
        - ActorSystemPriority (number): 
        - AdministrativeKey (number): 
        - AggregationFlagState (str(disable | auto)): 
        - AutoPickPortMac (bool): 
        - CollectingFlag (bool): 
        - CollectorMaxDelay (number): 
        - DistributingFlag (bool): 
        - Enabled (bool): 
        - InterMarkerPduDelay (str): 
        - LacpActivity (str(active | passive)): 
        - LacpTimeout (number): 
        - LacpduPeriodicTimeInterval (number): 
        - MarkerRequestMode (str(fixed | random)): 
        - MarkerResponseWaitTime (number): 
        - PortMac (str): 
        - SendMarkerRequestOnLagChange (bool): 
        - SendPeriodicMarkerRequest (bool): 
        - SupportRespondingToMarker (bool): 
        - SyncFlag (str(disable | auto)): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ActorKey=None, ActorPortNumber=None, ActorPortPriority=None, ActorSystemId=None, ActorSystemPriority=None, AdministrativeKey=None, AggregationFlagState=None, AutoPickPortMac=None, CollectingFlag=None, CollectorMaxDelay=None, DistributingFlag=None, Enabled=None, InterMarkerPduDelay=None, LacpActivity=None, LacpTimeout=None, LacpduPeriodicTimeInterval=None, MarkerRequestMode=None, MarkerResponseWaitTime=None, PortMac=None, SendMarkerRequestOnLagChange=None, SendPeriodicMarkerRequest=None, SupportRespondingToMarker=None, SyncFlag=None):
        """Adds a new link resource on the server and adds it to the container.

        Args
        ----
        - ActorKey (number): 
        - ActorPortNumber (number): 
        - ActorPortPriority (number): 
        - ActorSystemId (str): 
        - ActorSystemPriority (number): 
        - AdministrativeKey (number): 
        - AggregationFlagState (str(disable | auto)): 
        - AutoPickPortMac (bool): 
        - CollectingFlag (bool): 
        - CollectorMaxDelay (number): 
        - DistributingFlag (bool): 
        - Enabled (bool): 
        - InterMarkerPduDelay (str): 
        - LacpActivity (str(active | passive)): 
        - LacpTimeout (number): 
        - LacpduPeriodicTimeInterval (number): 
        - MarkerRequestMode (str(fixed | random)): 
        - MarkerResponseWaitTime (number): 
        - PortMac (str): 
        - SendMarkerRequestOnLagChange (bool): 
        - SendPeriodicMarkerRequest (bool): 
        - SupportRespondingToMarker (bool): 
        - SyncFlag (str(disable | auto)): 

        Returns
        -------
        - self: This instance with all currently retrieved link resources using find and the newly added link resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained link resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ActorKey=None, ActorPortNumber=None, ActorPortPriority=None, ActorSystemId=None, ActorSystemPriority=None, AdministrativeKey=None, AggregationFlagState=None, AutoPickPortMac=None, CollectingFlag=None, CollectorMaxDelay=None, DistributingFlag=None, Enabled=None, InterMarkerPduDelay=None, LacpActivity=None, LacpTimeout=None, LacpduPeriodicTimeInterval=None, MarkerRequestMode=None, MarkerResponseWaitTime=None, PortMac=None, SendMarkerRequestOnLagChange=None, SendPeriodicMarkerRequest=None, SupportRespondingToMarker=None, SyncFlag=None, UpdateRequired=None):
        """Finds and retrieves link resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve link resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all link resources from the server.

        Args
        ----
        - ActorKey (number): 
        - ActorPortNumber (number): 
        - ActorPortPriority (number): 
        - ActorSystemId (str): 
        - ActorSystemPriority (number): 
        - AdministrativeKey (number): 
        - AggregationFlagState (str(disable | auto)): 
        - AutoPickPortMac (bool): 
        - CollectingFlag (bool): 
        - CollectorMaxDelay (number): 
        - DistributingFlag (bool): 
        - Enabled (bool): 
        - InterMarkerPduDelay (str): 
        - LacpActivity (str(active | passive)): 
        - LacpTimeout (number): 
        - LacpduPeriodicTimeInterval (number): 
        - MarkerRequestMode (str(fixed | random)): 
        - MarkerResponseWaitTime (number): 
        - PortMac (str): 
        - SendMarkerRequestOnLagChange (bool): 
        - SendPeriodicMarkerRequest (bool): 
        - SupportRespondingToMarker (bool): 
        - SyncFlag (str(disable | auto)): 
        - UpdateRequired (bool): 

        Returns
        -------
        - self: This instance with matching link resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of link data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the link resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
