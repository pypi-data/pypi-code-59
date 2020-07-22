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


class LearnedInfo(Base):
    """
    The LearnedInfo class encapsulates a list of learnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the LearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedInfo'
    _SDM_ATT_MAP = {
        'DesMinTxInterval': 'desMinTxInterval',
        'MyDisc': 'myDisc',
        'MyIpAddress': 'myIpAddress',
        'PeerDisc': 'peerDisc',
        'PeerFlags': 'peerFlags',
        'PeerIpAddress': 'peerIpAddress',
        'PeerState': 'peerState',
        'PeerUpTime': 'peerUpTime',
        'ProtocolUsingSession': 'protocolUsingSession',
        'ReqMinEchoInterval': 'reqMinEchoInterval',
        'ReqMinRxInterval': 'reqMinRxInterval',
        'SessionState': 'sessionState',
        'SessionType': 'sessionType',
    }

    def __init__(self, parent):
        super(LearnedInfo, self).__init__(parent)

    @property
    def DesMinTxInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DesMinTxInterval'])

    @property
    def MyDisc(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MyDisc'])

    @property
    def MyIpAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MyIpAddress'])

    @property
    def PeerDisc(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeerDisc'])

    @property
    def PeerFlags(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeerFlags'])

    @property
    def PeerIpAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeerIpAddress'])

    @property
    def PeerState(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeerState'])

    @property
    def PeerUpTime(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeerUpTime'])

    @property
    def ProtocolUsingSession(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolUsingSession'])

    @property
    def ReqMinEchoInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReqMinEchoInterval'])

    @property
    def ReqMinRxInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReqMinRxInterval'])

    @property
    def SessionState(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionState'])

    @property
    def SessionType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionType'])

    def find(self, DesMinTxInterval=None, MyDisc=None, MyIpAddress=None, PeerDisc=None, PeerFlags=None, PeerIpAddress=None, PeerState=None, PeerUpTime=None, ProtocolUsingSession=None, ReqMinEchoInterval=None, ReqMinRxInterval=None, SessionState=None, SessionType=None):
        """Finds and retrieves learnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedInfo resources from the server.

        Args
        ----
        - DesMinTxInterval (number): 
        - MyDisc (number): 
        - MyIpAddress (str): 
        - PeerDisc (number): 
        - PeerFlags (str): 
        - PeerIpAddress (str): 
        - PeerState (str): 
        - PeerUpTime (number): 
        - ProtocolUsingSession (str): 
        - ReqMinEchoInterval (number): 
        - ReqMinRxInterval (number): 
        - SessionState (str): 
        - SessionType (str): 

        Returns
        -------
        - self: This instance with matching learnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
