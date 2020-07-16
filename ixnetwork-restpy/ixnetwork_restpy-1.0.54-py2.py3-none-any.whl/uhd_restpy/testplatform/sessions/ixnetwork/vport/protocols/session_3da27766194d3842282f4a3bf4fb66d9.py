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


class Session(Base):
    """
    The Session class encapsulates a list of session resources that are managed by the user.
    A list of resources can be retrieved from the server using the Session.find() method.
    The list can be managed by using the Session.add() and Session.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'session'
    _SDM_ATT_MAP = {
        'BfdSessionType': 'bfdSessionType',
        'Enabled': 'enabled',
        'EnabledAutoChooseSource': 'enabledAutoChooseSource',
        'IpType': 'ipType',
        'LocalBfdAddress': 'localBfdAddress',
        'MyDisc': 'myDisc',
        'RemoteBfdAddress': 'remoteBfdAddress',
        'RemoteDisc': 'remoteDisc',
        'RemoteDiscLearned': 'remoteDiscLearned',
    }

    def __init__(self, parent):
        super(Session, self).__init__(parent)

    @property
    def BfdSessionType(self):
        """
        Returns
        -------
        - str(singleHop | multipleHops): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BfdSessionType'])
    @BfdSessionType.setter
    def BfdSessionType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BfdSessionType'], value)

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
    def EnabledAutoChooseSource(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnabledAutoChooseSource'])
    @EnabledAutoChooseSource.setter
    def EnabledAutoChooseSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnabledAutoChooseSource'], value)

    @property
    def IpType(self):
        """
        Returns
        -------
        - str(ipv4 | ipv6): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpType'])
    @IpType.setter
    def IpType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpType'], value)

    @property
    def LocalBfdAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalBfdAddress'])
    @LocalBfdAddress.setter
    def LocalBfdAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LocalBfdAddress'], value)

    @property
    def MyDisc(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MyDisc'])
    @MyDisc.setter
    def MyDisc(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MyDisc'], value)

    @property
    def RemoteBfdAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteBfdAddress'])
    @RemoteBfdAddress.setter
    def RemoteBfdAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RemoteBfdAddress'], value)

    @property
    def RemoteDisc(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteDisc'])
    @RemoteDisc.setter
    def RemoteDisc(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RemoteDisc'], value)

    @property
    def RemoteDiscLearned(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteDiscLearned'])
    @RemoteDiscLearned.setter
    def RemoteDiscLearned(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RemoteDiscLearned'], value)

    def update(self, BfdSessionType=None, Enabled=None, EnabledAutoChooseSource=None, IpType=None, LocalBfdAddress=None, MyDisc=None, RemoteBfdAddress=None, RemoteDisc=None, RemoteDiscLearned=None):
        """Updates session resource on the server.

        Args
        ----
        - BfdSessionType (str(singleHop | multipleHops)): 
        - Enabled (bool): 
        - EnabledAutoChooseSource (bool): 
        - IpType (str(ipv4 | ipv6)): 
        - LocalBfdAddress (str): 
        - MyDisc (number): 
        - RemoteBfdAddress (str): 
        - RemoteDisc (number): 
        - RemoteDiscLearned (bool): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, BfdSessionType=None, Enabled=None, EnabledAutoChooseSource=None, IpType=None, LocalBfdAddress=None, MyDisc=None, RemoteBfdAddress=None, RemoteDisc=None, RemoteDiscLearned=None):
        """Adds a new session resource on the server and adds it to the container.

        Args
        ----
        - BfdSessionType (str(singleHop | multipleHops)): 
        - Enabled (bool): 
        - EnabledAutoChooseSource (bool): 
        - IpType (str(ipv4 | ipv6)): 
        - LocalBfdAddress (str): 
        - MyDisc (number): 
        - RemoteBfdAddress (str): 
        - RemoteDisc (number): 
        - RemoteDiscLearned (bool): 

        Returns
        -------
        - self: This instance with all currently retrieved session resources using find and the newly added session resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained session resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, BfdSessionType=None, Enabled=None, EnabledAutoChooseSource=None, IpType=None, LocalBfdAddress=None, MyDisc=None, RemoteBfdAddress=None, RemoteDisc=None, RemoteDiscLearned=None):
        """Finds and retrieves session resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve session resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all session resources from the server.

        Args
        ----
        - BfdSessionType (str(singleHop | multipleHops)): 
        - Enabled (bool): 
        - EnabledAutoChooseSource (bool): 
        - IpType (str(ipv4 | ipv6)): 
        - LocalBfdAddress (str): 
        - MyDisc (number): 
        - RemoteBfdAddress (str): 
        - RemoteDisc (number): 
        - RemoteDiscLearned (bool): 

        Returns
        -------
        - self: This instance with matching session resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of session data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the session resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
