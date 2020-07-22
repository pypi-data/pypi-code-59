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


class Evc(Base):
    """
    The Evc class encapsulates a list of evc resources that are managed by the user.
    A list of resources can be retrieved from the server using the Evc.find() method.
    The list can be managed by using the Evc.add() and Evc.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'evc'
    _SDM_ATT_MAP = {
        'DefaultEvc': 'defaultEvc',
        'Enabled': 'enabled',
        'EvcIdentifier': 'evcIdentifier',
        'EvcIdentifierLength': 'evcIdentifierLength',
        'EvcStatus': 'evcStatus',
        'EvcType': 'evcType',
        'ReferenceId': 'referenceId',
        'UntaggedPriorityTagged': 'untaggedPriorityTagged',
    }

    def __init__(self, parent):
        super(Evc, self).__init__(parent)

    @property
    def BwProfile(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.bwprofile_1f77a90148a0ad6bb7139272863d372c.BwProfile): An instance of the BwProfile class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.bwprofile_1f77a90148a0ad6bb7139272863d372c import BwProfile
        return BwProfile(self)

    @property
    def CeVlanIdRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.cevlanidrange_4da1c6bd354a4f3ba5d44ff2c658e8a2.CeVlanIdRange): An instance of the CeVlanIdRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.cevlanidrange_4da1c6bd354a4f3ba5d44ff2c658e8a2 import CeVlanIdRange
        return CeVlanIdRange(self)

    @property
    def DefaultEvc(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DefaultEvc'])
    @DefaultEvc.setter
    def DefaultEvc(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DefaultEvc'], value)

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
    def EvcIdentifier(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EvcIdentifier'])
    @EvcIdentifier.setter
    def EvcIdentifier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EvcIdentifier'], value)

    @property
    def EvcIdentifierLength(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EvcIdentifierLength'])
    @EvcIdentifierLength.setter
    def EvcIdentifierLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EvcIdentifierLength'], value)

    @property
    def EvcStatus(self):
        """
        Returns
        -------
        - str(notActive | newAndNotActive | active | newAndActive | partiallyActive | newAndPartiallyActive): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EvcStatus'])
    @EvcStatus.setter
    def EvcStatus(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EvcStatus'], value)

    @property
    def EvcType(self):
        """
        Returns
        -------
        - str(pointToPoint | multipointToMultipoint): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EvcType'])
    @EvcType.setter
    def EvcType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EvcType'], value)

    @property
    def ReferenceId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReferenceId'])
    @ReferenceId.setter
    def ReferenceId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReferenceId'], value)

    @property
    def UntaggedPriorityTagged(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UntaggedPriorityTagged'])
    @UntaggedPriorityTagged.setter
    def UntaggedPriorityTagged(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UntaggedPriorityTagged'], value)

    def update(self, DefaultEvc=None, Enabled=None, EvcIdentifier=None, EvcIdentifierLength=None, EvcStatus=None, EvcType=None, ReferenceId=None, UntaggedPriorityTagged=None):
        """Updates evc resource on the server.

        Args
        ----
        - DefaultEvc (bool): 
        - Enabled (bool): 
        - EvcIdentifier (str): 
        - EvcIdentifierLength (number): 
        - EvcStatus (str(notActive | newAndNotActive | active | newAndActive | partiallyActive | newAndPartiallyActive)): 
        - EvcType (str(pointToPoint | multipointToMultipoint)): 
        - ReferenceId (number): 
        - UntaggedPriorityTagged (bool): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, DefaultEvc=None, Enabled=None, EvcIdentifier=None, EvcIdentifierLength=None, EvcStatus=None, EvcType=None, ReferenceId=None, UntaggedPriorityTagged=None):
        """Adds a new evc resource on the server and adds it to the container.

        Args
        ----
        - DefaultEvc (bool): 
        - Enabled (bool): 
        - EvcIdentifier (str): 
        - EvcIdentifierLength (number): 
        - EvcStatus (str(notActive | newAndNotActive | active | newAndActive | partiallyActive | newAndPartiallyActive)): 
        - EvcType (str(pointToPoint | multipointToMultipoint)): 
        - ReferenceId (number): 
        - UntaggedPriorityTagged (bool): 

        Returns
        -------
        - self: This instance with all currently retrieved evc resources using find and the newly added evc resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained evc resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, DefaultEvc=None, Enabled=None, EvcIdentifier=None, EvcIdentifierLength=None, EvcStatus=None, EvcType=None, ReferenceId=None, UntaggedPriorityTagged=None):
        """Finds and retrieves evc resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve evc resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all evc resources from the server.

        Args
        ----
        - DefaultEvc (bool): 
        - Enabled (bool): 
        - EvcIdentifier (str): 
        - EvcIdentifierLength (number): 
        - EvcStatus (str(notActive | newAndNotActive | active | newAndActive | partiallyActive | newAndPartiallyActive)): 
        - EvcType (str(pointToPoint | multipointToMultipoint)): 
        - ReferenceId (number): 
        - UntaggedPriorityTagged (bool): 

        Returns
        -------
        - self: This instance with matching evc resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of evc data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the evc resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
