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


class OfChannelSwitchLearnedInfo(Base):
    """
    The OfChannelSwitchLearnedInfo class encapsulates a list of ofChannelSwitchLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the OfChannelSwitchLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'ofChannelSwitchLearnedInfo'
    _SDM_ATT_MAP = {
        'ActionsSupported': 'actionsSupported',
        'AveragePacketInReplyDelay': 'averagePacketInReplyDelay',
        'Capabilities': 'capabilities',
        'ConfigFlags': 'configFlags',
        'ConfiguredPacketInReplyCount': 'configuredPacketInReplyCount',
        'ConfiguredPacketInSentCount': 'configuredPacketInSentCount',
        'DataPathId': 'dataPathId',
        'DataPathIdAsHex': 'dataPathIdAsHex',
        'FlowRate': 'flowRate',
        'GenerationId': 'generationId',
        'LastErrorCode': 'lastErrorCode',
        'LastErrorType': 'lastErrorType',
        'LocalIp': 'localIp',
        'MaxBufferSize': 'maxBufferSize',
        'MaxPacketInBytes': 'maxPacketInBytes',
        'NegotiatedVersion': 'negotiatedVersion',
        'NumberOfAuxiliaryConnection': 'numberOfAuxiliaryConnection',
        'NumberOfErrorsSent': 'numberOfErrorsSent',
        'NumberOfPorts': 'numberOfPorts',
        'NumberofTable': 'numberofTable',
        'RemoteIp': 'remoteIp',
        'RemotePortNumber': 'remotePortNumber',
        'SessionType': 'sessionType',
    }

    def __init__(self, parent):
        super(OfChannelSwitchLearnedInfo, self).__init__(parent)

    @property
    def OfChannelPortsSwitchLearnedInfo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannelportsswitchlearnedinfo_770d062c951b9c0656d18c015b1eec07.OfChannelPortsSwitchLearnedInfo): An instance of the OfChannelPortsSwitchLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannelportsswitchlearnedinfo_770d062c951b9c0656d18c015b1eec07 import OfChannelPortsSwitchLearnedInfo
        return OfChannelPortsSwitchLearnedInfo(self)

    @property
    def OfChannelSessionPeersLearnedInformation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannelsessionpeerslearnedinformation_377947b17842c6df2a85c6dec7bb2f70.OfChannelSessionPeersLearnedInformation): An instance of the OfChannelSessionPeersLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannelsessionpeerslearnedinformation_377947b17842c6df2a85c6dec7bb2f70 import OfChannelSessionPeersLearnedInformation
        return OfChannelSessionPeersLearnedInformation(self)

    @property
    def ActionsSupported(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActionsSupported'])

    @property
    def AveragePacketInReplyDelay(self):
        """DEPRECATED 
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AveragePacketInReplyDelay'])
    @AveragePacketInReplyDelay.setter
    def AveragePacketInReplyDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AveragePacketInReplyDelay'], value)

    @property
    def Capabilities(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Capabilities'])

    @property
    def ConfigFlags(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConfigFlags'])

    @property
    def ConfiguredPacketInReplyCount(self):
        """DEPRECATED 
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConfiguredPacketInReplyCount'])
    @ConfiguredPacketInReplyCount.setter
    def ConfiguredPacketInReplyCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ConfiguredPacketInReplyCount'], value)

    @property
    def ConfiguredPacketInSentCount(self):
        """DEPRECATED 
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConfiguredPacketInSentCount'])
    @ConfiguredPacketInSentCount.setter
    def ConfiguredPacketInSentCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ConfiguredPacketInSentCount'], value)

    @property
    def DataPathId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathId'])

    @property
    def DataPathIdAsHex(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathIdAsHex'])

    @property
    def FlowRate(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowRate'])

    @property
    def GenerationId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['GenerationId'])

    @property
    def LastErrorCode(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LastErrorCode'])

    @property
    def LastErrorType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LastErrorType'])

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalIp'])

    @property
    def MaxBufferSize(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxBufferSize'])

    @property
    def MaxPacketInBytes(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxPacketInBytes'])

    @property
    def NegotiatedVersion(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NegotiatedVersion'])

    @property
    def NumberOfAuxiliaryConnection(self):
        """DEPRECATED 
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfAuxiliaryConnection'])
    @NumberOfAuxiliaryConnection.setter
    def NumberOfAuxiliaryConnection(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfAuxiliaryConnection'], value)

    @property
    def NumberOfErrorsSent(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfErrorsSent'])

    @property
    def NumberOfPorts(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfPorts'])

    @property
    def NumberofTable(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberofTable'])

    @property
    def RemoteIp(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteIp'])

    @property
    def RemotePortNumber(self):
        """DEPRECATED 
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemotePortNumber'])
    @RemotePortNumber.setter
    def RemotePortNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RemotePortNumber'], value)

    @property
    def SessionType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionType'])

    def update(self, AveragePacketInReplyDelay=None, ConfiguredPacketInReplyCount=None, ConfiguredPacketInSentCount=None, NumberOfAuxiliaryConnection=None, RemotePortNumber=None):
        """Updates ofChannelSwitchLearnedInfo resource on the server.

        Args
        ----
        - AveragePacketInReplyDelay (number): 
        - ConfiguredPacketInReplyCount (number): 
        - ConfiguredPacketInSentCount (number): 
        - NumberOfAuxiliaryConnection (number): 
        - RemotePortNumber (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, ActionsSupported=None, AveragePacketInReplyDelay=None, Capabilities=None, ConfigFlags=None, ConfiguredPacketInReplyCount=None, ConfiguredPacketInSentCount=None, DataPathId=None, DataPathIdAsHex=None, FlowRate=None, GenerationId=None, LastErrorCode=None, LastErrorType=None, LocalIp=None, MaxBufferSize=None, MaxPacketInBytes=None, NegotiatedVersion=None, NumberOfAuxiliaryConnection=None, NumberOfErrorsSent=None, NumberOfPorts=None, NumberofTable=None, RemoteIp=None, RemotePortNumber=None, SessionType=None):
        """Finds and retrieves ofChannelSwitchLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ofChannelSwitchLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ofChannelSwitchLearnedInfo resources from the server.

        Args
        ----
        - ActionsSupported (str): 
        - AveragePacketInReplyDelay (number): 
        - Capabilities (str): 
        - ConfigFlags (str): 
        - ConfiguredPacketInReplyCount (number): 
        - ConfiguredPacketInSentCount (number): 
        - DataPathId (str): 
        - DataPathIdAsHex (str): 
        - FlowRate (number): 
        - GenerationId (number): 
        - LastErrorCode (str): 
        - LastErrorType (str): 
        - LocalIp (str): 
        - MaxBufferSize (number): 
        - MaxPacketInBytes (number): 
        - NegotiatedVersion (number): 
        - NumberOfAuxiliaryConnection (number): 
        - NumberOfErrorsSent (number): 
        - NumberOfPorts (number): 
        - NumberofTable (number): 
        - RemoteIp (str): 
        - RemotePortNumber (number): 
        - SessionType (str): 

        Returns
        -------
        - self: This instance with matching ofChannelSwitchLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ofChannelSwitchLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ofChannelSwitchLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddRecordForTrigger(self):
        """Executes the addRecordForTrigger operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('addRecordForTrigger', payload=payload, response_object=None)
