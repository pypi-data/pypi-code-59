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


class Source(Base):
    """
    The Source class encapsulates a list of source resources that are managed by the user.
    A list of resources can be retrieved from the server using the Source.find() method.
    The list can be managed by using the Source.add() and Source.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'source'
    _SDM_ATT_MAP = {
        'DiscardSgJoinStates': 'discardSgJoinStates',
        'Enabled': 'enabled',
        'GroupAddress': 'groupAddress',
        'GroupCount': 'groupCount',
        'GroupMappingMode': 'groupMappingMode',
        'GroupMaskWidth': 'groupMaskWidth',
        'MulticastDataLength': 'multicastDataLength',
        'RegisterProbeTime': 'registerProbeTime',
        'RpAddress': 'rpAddress',
        'SendNullRegAtBegin': 'sendNullRegAtBegin',
        'SourceAddress': 'sourceAddress',
        'SourceCount': 'sourceCount',
        'SuppressionTime': 'suppressionTime',
        'SwitchOverInterval': 'switchOverInterval',
        'TxIterationGap': 'txIterationGap',
        'UdpDstPort': 'udpDstPort',
        'UdpSrcPort': 'udpSrcPort',
    }

    def __init__(self, parent):
        super(Source, self).__init__(parent)

    @property
    def LearnedSgState(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedsgstate_97f510f2a61d501f738002d53b1058e7.LearnedSgState): An instance of the LearnedSgState class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedsgstate_97f510f2a61d501f738002d53b1058e7 import LearnedSgState
        return LearnedSgState(self)

    @property
    def DiscardSgJoinStates(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DiscardSgJoinStates'])
    @DiscardSgJoinStates.setter
    def DiscardSgJoinStates(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DiscardSgJoinStates'], value)

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
    def GroupAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupAddress'])
    @GroupAddress.setter
    def GroupAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GroupAddress'], value)

    @property
    def GroupCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupCount'])
    @GroupCount.setter
    def GroupCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GroupCount'], value)

    @property
    def GroupMappingMode(self):
        """
        Returns
        -------
        - str(fullyMeshed | oneToOne): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupMappingMode'])
    @GroupMappingMode.setter
    def GroupMappingMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GroupMappingMode'], value)

    @property
    def GroupMaskWidth(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupMaskWidth'])
    @GroupMaskWidth.setter
    def GroupMaskWidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GroupMaskWidth'], value)

    @property
    def MulticastDataLength(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MulticastDataLength'])
    @MulticastDataLength.setter
    def MulticastDataLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MulticastDataLength'], value)

    @property
    def RegisterProbeTime(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RegisterProbeTime'])
    @RegisterProbeTime.setter
    def RegisterProbeTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RegisterProbeTime'], value)

    @property
    def RpAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RpAddress'])
    @RpAddress.setter
    def RpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RpAddress'], value)

    @property
    def SendNullRegAtBegin(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendNullRegAtBegin'])
    @SendNullRegAtBegin.setter
    def SendNullRegAtBegin(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendNullRegAtBegin'], value)

    @property
    def SourceAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceAddress'])
    @SourceAddress.setter
    def SourceAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SourceAddress'], value)

    @property
    def SourceCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceCount'])
    @SourceCount.setter
    def SourceCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SourceCount'], value)

    @property
    def SuppressionTime(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SuppressionTime'])
    @SuppressionTime.setter
    def SuppressionTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SuppressionTime'], value)

    @property
    def SwitchOverInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SwitchOverInterval'])
    @SwitchOverInterval.setter
    def SwitchOverInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SwitchOverInterval'], value)

    @property
    def TxIterationGap(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxIterationGap'])
    @TxIterationGap.setter
    def TxIterationGap(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TxIterationGap'], value)

    @property
    def UdpDstPort(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UdpDstPort'])
    @UdpDstPort.setter
    def UdpDstPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UdpDstPort'], value)

    @property
    def UdpSrcPort(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UdpSrcPort'])
    @UdpSrcPort.setter
    def UdpSrcPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UdpSrcPort'], value)

    def update(self, DiscardSgJoinStates=None, Enabled=None, GroupAddress=None, GroupCount=None, GroupMappingMode=None, GroupMaskWidth=None, MulticastDataLength=None, RegisterProbeTime=None, RpAddress=None, SendNullRegAtBegin=None, SourceAddress=None, SourceCount=None, SuppressionTime=None, SwitchOverInterval=None, TxIterationGap=None, UdpDstPort=None, UdpSrcPort=None):
        """Updates source resource on the server.

        Args
        ----
        - DiscardSgJoinStates (bool): 
        - Enabled (bool): 
        - GroupAddress (str): 
        - GroupCount (number): 
        - GroupMappingMode (str(fullyMeshed | oneToOne)): 
        - GroupMaskWidth (number): 
        - MulticastDataLength (number): 
        - RegisterProbeTime (number): 
        - RpAddress (str): 
        - SendNullRegAtBegin (bool): 
        - SourceAddress (str): 
        - SourceCount (number): 
        - SuppressionTime (number): 
        - SwitchOverInterval (number): 
        - TxIterationGap (number): 
        - UdpDstPort (number): 
        - UdpSrcPort (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, DiscardSgJoinStates=None, Enabled=None, GroupAddress=None, GroupCount=None, GroupMappingMode=None, GroupMaskWidth=None, MulticastDataLength=None, RegisterProbeTime=None, RpAddress=None, SendNullRegAtBegin=None, SourceAddress=None, SourceCount=None, SuppressionTime=None, SwitchOverInterval=None, TxIterationGap=None, UdpDstPort=None, UdpSrcPort=None):
        """Adds a new source resource on the server and adds it to the container.

        Args
        ----
        - DiscardSgJoinStates (bool): 
        - Enabled (bool): 
        - GroupAddress (str): 
        - GroupCount (number): 
        - GroupMappingMode (str(fullyMeshed | oneToOne)): 
        - GroupMaskWidth (number): 
        - MulticastDataLength (number): 
        - RegisterProbeTime (number): 
        - RpAddress (str): 
        - SendNullRegAtBegin (bool): 
        - SourceAddress (str): 
        - SourceCount (number): 
        - SuppressionTime (number): 
        - SwitchOverInterval (number): 
        - TxIterationGap (number): 
        - UdpDstPort (number): 
        - UdpSrcPort (number): 

        Returns
        -------
        - self: This instance with all currently retrieved source resources using find and the newly added source resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained source resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, DiscardSgJoinStates=None, Enabled=None, GroupAddress=None, GroupCount=None, GroupMappingMode=None, GroupMaskWidth=None, MulticastDataLength=None, RegisterProbeTime=None, RpAddress=None, SendNullRegAtBegin=None, SourceAddress=None, SourceCount=None, SuppressionTime=None, SwitchOverInterval=None, TxIterationGap=None, UdpDstPort=None, UdpSrcPort=None):
        """Finds and retrieves source resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve source resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all source resources from the server.

        Args
        ----
        - DiscardSgJoinStates (bool): 
        - Enabled (bool): 
        - GroupAddress (str): 
        - GroupCount (number): 
        - GroupMappingMode (str(fullyMeshed | oneToOne)): 
        - GroupMaskWidth (number): 
        - MulticastDataLength (number): 
        - RegisterProbeTime (number): 
        - RpAddress (str): 
        - SendNullRegAtBegin (bool): 
        - SourceAddress (str): 
        - SourceCount (number): 
        - SuppressionTime (number): 
        - SwitchOverInterval (number): 
        - TxIterationGap (number): 
        - UdpDstPort (number): 
        - UdpSrcPort (number): 

        Returns
        -------
        - self: This instance with matching source resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of source data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the source resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
