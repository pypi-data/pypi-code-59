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


class GeneralLearnedInfo(Base):
    """
    The GeneralLearnedInfo class encapsulates a list of generalLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the GeneralLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'generalLearnedInfo'
    _SDM_ATT_MAP = {
        'AverageRtt': 'averageRtt',
        'BfdSessionMyState': 'bfdSessionMyState',
        'BfdSessionPeerState': 'bfdSessionPeerState',
        'CcInUse': 'ccInUse',
        'CvInUse': 'cvInUse',
        'Fec': 'fec',
        'IncomingLabelStack': 'incomingLabelStack',
        'IncomingLspLabel': 'incomingLspLabel',
        'IncomingPwLabel': 'incomingPwLabel',
        'LspPingReachability': 'lspPingReachability',
        'MaxRtt': 'maxRtt',
        'MinRtt': 'minRtt',
        'MyDiscriminator': 'myDiscriminator',
        'MyIpAddress': 'myIpAddress',
        'OutgoingLabelStack': 'outgoingLabelStack',
        'OutgoingLspLabel': 'outgoingLspLabel',
        'OutgoingPwLabel': 'outgoingPwLabel',
        'PeerDiscriminator': 'peerDiscriminator',
        'PeerIpAddress': 'peerIpAddress',
        'PingAttempts': 'pingAttempts',
        'PingFailures': 'pingFailures',
        'PingReplyTx': 'pingReplyTx',
        'PingRequestRx': 'pingRequestRx',
        'PingSuccess': 'pingSuccess',
        'ReceivedMinRxInterval': 'receivedMinRxInterval',
        'ReceivedMultiplier': 'receivedMultiplier',
        'ReceivedPeerFlags': 'receivedPeerFlags',
        'ReceivedTxInterval': 'receivedTxInterval',
        'ReturnCode': 'returnCode',
        'ReturnSubcode': 'returnSubcode',
        'SignalingProtocol': 'signalingProtocol',
        'TunnelEndpointType': 'tunnelEndpointType',
        'TunnelType': 'tunnelType',
    }

    def __init__(self, parent):
        super(GeneralLearnedInfo, self).__init__(parent)

    @property
    def AverageRtt(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AverageRtt'])

    @property
    def BfdSessionMyState(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BfdSessionMyState'])

    @property
    def BfdSessionPeerState(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BfdSessionPeerState'])

    @property
    def CcInUse(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CcInUse'])

    @property
    def CvInUse(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CvInUse'])

    @property
    def Fec(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Fec'])

    @property
    def IncomingLabelStack(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncomingLabelStack'])

    @property
    def IncomingLspLabel(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncomingLspLabel'])

    @property
    def IncomingPwLabel(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncomingPwLabel'])

    @property
    def LspPingReachability(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LspPingReachability'])

    @property
    def MaxRtt(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRtt'])

    @property
    def MinRtt(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinRtt'])

    @property
    def MyDiscriminator(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MyDiscriminator'])

    @property
    def MyIpAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MyIpAddress'])

    @property
    def OutgoingLabelStack(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutgoingLabelStack'])

    @property
    def OutgoingLspLabel(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutgoingLspLabel'])

    @property
    def OutgoingPwLabel(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutgoingPwLabel'])

    @property
    def PeerDiscriminator(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeerDiscriminator'])

    @property
    def PeerIpAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeerIpAddress'])

    @property
    def PingAttempts(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PingAttempts'])

    @property
    def PingFailures(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PingFailures'])

    @property
    def PingReplyTx(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PingReplyTx'])

    @property
    def PingRequestRx(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PingRequestRx'])

    @property
    def PingSuccess(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PingSuccess'])

    @property
    def ReceivedMinRxInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceivedMinRxInterval'])

    @property
    def ReceivedMultiplier(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceivedMultiplier'])

    @property
    def ReceivedPeerFlags(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceivedPeerFlags'])

    @property
    def ReceivedTxInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceivedTxInterval'])

    @property
    def ReturnCode(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReturnCode'])

    @property
    def ReturnSubcode(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReturnSubcode'])

    @property
    def SignalingProtocol(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SignalingProtocol'])

    @property
    def TunnelEndpointType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelEndpointType'])

    @property
    def TunnelType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelType'])

    def find(self, AverageRtt=None, BfdSessionMyState=None, BfdSessionPeerState=None, CcInUse=None, CvInUse=None, Fec=None, IncomingLabelStack=None, IncomingLspLabel=None, IncomingPwLabel=None, LspPingReachability=None, MaxRtt=None, MinRtt=None, MyDiscriminator=None, MyIpAddress=None, OutgoingLabelStack=None, OutgoingLspLabel=None, OutgoingPwLabel=None, PeerDiscriminator=None, PeerIpAddress=None, PingAttempts=None, PingFailures=None, PingReplyTx=None, PingRequestRx=None, PingSuccess=None, ReceivedMinRxInterval=None, ReceivedMultiplier=None, ReceivedPeerFlags=None, ReceivedTxInterval=None, ReturnCode=None, ReturnSubcode=None, SignalingProtocol=None, TunnelEndpointType=None, TunnelType=None):
        """Finds and retrieves generalLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve generalLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all generalLearnedInfo resources from the server.

        Args
        ----
        - AverageRtt (str): 
        - BfdSessionMyState (str): 
        - BfdSessionPeerState (str): 
        - CcInUse (str): 
        - CvInUse (str): 
        - Fec (str): 
        - IncomingLabelStack (str): 
        - IncomingLspLabel (str): 
        - IncomingPwLabel (str): 
        - LspPingReachability (str): 
        - MaxRtt (str): 
        - MinRtt (str): 
        - MyDiscriminator (number): 
        - MyIpAddress (str): 
        - OutgoingLabelStack (str): 
        - OutgoingLspLabel (str): 
        - OutgoingPwLabel (str): 
        - PeerDiscriminator (number): 
        - PeerIpAddress (str): 
        - PingAttempts (number): 
        - PingFailures (number): 
        - PingReplyTx (number): 
        - PingRequestRx (number): 
        - PingSuccess (number): 
        - ReceivedMinRxInterval (number): 
        - ReceivedMultiplier (number): 
        - ReceivedPeerFlags (str): 
        - ReceivedTxInterval (number): 
        - ReturnCode (str): 
        - ReturnSubcode (number): 
        - SignalingProtocol (str): 
        - TunnelEndpointType (str): 
        - TunnelType (str): 

        Returns
        -------
        - self: This instance with matching generalLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of generalLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the generalLearnedInfo resources from the server available through an iterator or index

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
