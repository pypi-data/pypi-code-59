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


class PortStatLearnedInformation(Base):
    """
    The PortStatLearnedInformation class encapsulates a list of portStatLearnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the PortStatLearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'portStatLearnedInformation'
    _SDM_ATT_MAP = {
        'Collisions': 'collisions',
        'CrcErrors': 'crcErrors',
        'DataPathId': 'dataPathId',
        'DataPathIdAsHex': 'dataPathIdAsHex',
        'Duration': 'duration',
        'DurationInNsec': 'durationInNsec',
        'ErrorCode': 'errorCode',
        'ErrorType': 'errorType',
        'FrameAlignmentErrors': 'frameAlignmentErrors',
        'Latency': 'latency',
        'LocalIp': 'localIp',
        'NegotiatedVersion': 'negotiatedVersion',
        'PacketsDroppedByRx': 'packetsDroppedByRx',
        'PacketsDroppedByTx': 'packetsDroppedByTx',
        'PacketsWithRxOverrun': 'packetsWithRxOverrun',
        'PortNo': 'portNo',
        'ReceivedBytes': 'receivedBytes',
        'ReceivedErrors': 'receivedErrors',
        'ReceivedPackets': 'receivedPackets',
        'RemoteIp': 'remoteIp',
        'ReplyState': 'replyState',
        'TransmitErrors': 'transmitErrors',
        'TransmittedBytes': 'transmittedBytes',
        'TransmittedPackets': 'transmittedPackets',
    }

    def __init__(self, parent):
        super(PortStatLearnedInformation, self).__init__(parent)

    @property
    def Collisions(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Collisions'])

    @property
    def CrcErrors(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CrcErrors'])

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
    def Duration(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Duration'])

    @property
    def DurationInNsec(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DurationInNsec'])

    @property
    def ErrorCode(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrorCode'])

    @property
    def ErrorType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrorType'])

    @property
    def FrameAlignmentErrors(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FrameAlignmentErrors'])

    @property
    def Latency(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Latency'])

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalIp'])

    @property
    def NegotiatedVersion(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NegotiatedVersion'])

    @property
    def PacketsDroppedByRx(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketsDroppedByRx'])

    @property
    def PacketsDroppedByTx(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketsDroppedByTx'])

    @property
    def PacketsWithRxOverrun(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketsWithRxOverrun'])

    @property
    def PortNo(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortNo'])

    @property
    def ReceivedBytes(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceivedBytes'])

    @property
    def ReceivedErrors(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceivedErrors'])

    @property
    def ReceivedPackets(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceivedPackets'])

    @property
    def RemoteIp(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteIp'])

    @property
    def ReplyState(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReplyState'])

    @property
    def TransmitErrors(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransmitErrors'])

    @property
    def TransmittedBytes(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransmittedBytes'])

    @property
    def TransmittedPackets(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransmittedPackets'])

    def find(self, Collisions=None, CrcErrors=None, DataPathId=None, DataPathIdAsHex=None, Duration=None, DurationInNsec=None, ErrorCode=None, ErrorType=None, FrameAlignmentErrors=None, Latency=None, LocalIp=None, NegotiatedVersion=None, PacketsDroppedByRx=None, PacketsDroppedByTx=None, PacketsWithRxOverrun=None, PortNo=None, ReceivedBytes=None, ReceivedErrors=None, ReceivedPackets=None, RemoteIp=None, ReplyState=None, TransmitErrors=None, TransmittedBytes=None, TransmittedPackets=None):
        """Finds and retrieves portStatLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve portStatLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all portStatLearnedInformation resources from the server.

        Args
        ----
        - Collisions (str): 
        - CrcErrors (str): 
        - DataPathId (str): 
        - DataPathIdAsHex (str): 
        - Duration (number): 
        - DurationInNsec (number): 
        - ErrorCode (str): 
        - ErrorType (str): 
        - FrameAlignmentErrors (str): 
        - Latency (number): 
        - LocalIp (str): 
        - NegotiatedVersion (str): 
        - PacketsDroppedByRx (str): 
        - PacketsDroppedByTx (str): 
        - PacketsWithRxOverrun (str): 
        - PortNo (number): 
        - ReceivedBytes (str): 
        - ReceivedErrors (str): 
        - ReceivedPackets (str): 
        - RemoteIp (str): 
        - ReplyState (str): 
        - TransmitErrors (str): 
        - TransmittedBytes (str): 
        - TransmittedPackets (str): 

        Returns
        -------
        - self: This instance with matching portStatLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of portStatLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the portStatLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
