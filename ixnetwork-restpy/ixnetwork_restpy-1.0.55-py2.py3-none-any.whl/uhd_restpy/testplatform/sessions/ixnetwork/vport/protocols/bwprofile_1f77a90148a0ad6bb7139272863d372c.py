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


class BwProfile(Base):
    """
    The BwProfile class encapsulates a list of bwProfile resources that are managed by the user.
    A list of resources can be retrieved from the server using the BwProfile.find() method.
    The list can be managed by using the BwProfile.add() and BwProfile.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'bwProfile'
    _SDM_ATT_MAP = {
        'CbsMagnitude': 'cbsMagnitude',
        'CbsMultiplier': 'cbsMultiplier',
        'Cf': 'cf',
        'CirMagnitude': 'cirMagnitude',
        'CirMultiplier': 'cirMultiplier',
        'Cm': 'cm',
        'EbsMagnitude': 'ebsMagnitude',
        'EbsMultiplier': 'ebsMultiplier',
        'EirMagnitude': 'eirMagnitude',
        'EirMultiplier': 'eirMultiplier',
        'Enabled': 'enabled',
        'PerCos': 'perCos',
        'UserPriorityBits000': 'userPriorityBits000',
        'UserPriorityBits001': 'userPriorityBits001',
        'UserPriorityBits010': 'userPriorityBits010',
        'UserPriorityBits011': 'userPriorityBits011',
        'UserPriorityBits100': 'userPriorityBits100',
        'UserPriorityBits101': 'userPriorityBits101',
        'UserPriorityBits110': 'userPriorityBits110',
        'UserPriorityBits111': 'userPriorityBits111',
    }

    def __init__(self, parent):
        super(BwProfile, self).__init__(parent)

    @property
    def CbsMagnitude(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CbsMagnitude'])
    @CbsMagnitude.setter
    def CbsMagnitude(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CbsMagnitude'], value)

    @property
    def CbsMultiplier(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CbsMultiplier'])
    @CbsMultiplier.setter
    def CbsMultiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CbsMultiplier'], value)

    @property
    def Cf(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Cf'])
    @Cf.setter
    def Cf(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Cf'], value)

    @property
    def CirMagnitude(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CirMagnitude'])
    @CirMagnitude.setter
    def CirMagnitude(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CirMagnitude'], value)

    @property
    def CirMultiplier(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CirMultiplier'])
    @CirMultiplier.setter
    def CirMultiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CirMultiplier'], value)

    @property
    def Cm(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Cm'])
    @Cm.setter
    def Cm(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Cm'], value)

    @property
    def EbsMagnitude(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EbsMagnitude'])
    @EbsMagnitude.setter
    def EbsMagnitude(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EbsMagnitude'], value)

    @property
    def EbsMultiplier(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EbsMultiplier'])
    @EbsMultiplier.setter
    def EbsMultiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EbsMultiplier'], value)

    @property
    def EirMagnitude(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EirMagnitude'])
    @EirMagnitude.setter
    def EirMagnitude(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EirMagnitude'], value)

    @property
    def EirMultiplier(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EirMultiplier'])
    @EirMultiplier.setter
    def EirMultiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EirMultiplier'], value)

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
    def PerCos(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PerCos'])
    @PerCos.setter
    def PerCos(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PerCos'], value)

    @property
    def UserPriorityBits000(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserPriorityBits000'])
    @UserPriorityBits000.setter
    def UserPriorityBits000(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserPriorityBits000'], value)

    @property
    def UserPriorityBits001(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserPriorityBits001'])
    @UserPriorityBits001.setter
    def UserPriorityBits001(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserPriorityBits001'], value)

    @property
    def UserPriorityBits010(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserPriorityBits010'])
    @UserPriorityBits010.setter
    def UserPriorityBits010(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserPriorityBits010'], value)

    @property
    def UserPriorityBits011(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserPriorityBits011'])
    @UserPriorityBits011.setter
    def UserPriorityBits011(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserPriorityBits011'], value)

    @property
    def UserPriorityBits100(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserPriorityBits100'])
    @UserPriorityBits100.setter
    def UserPriorityBits100(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserPriorityBits100'], value)

    @property
    def UserPriorityBits101(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserPriorityBits101'])
    @UserPriorityBits101.setter
    def UserPriorityBits101(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserPriorityBits101'], value)

    @property
    def UserPriorityBits110(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserPriorityBits110'])
    @UserPriorityBits110.setter
    def UserPriorityBits110(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserPriorityBits110'], value)

    @property
    def UserPriorityBits111(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserPriorityBits111'])
    @UserPriorityBits111.setter
    def UserPriorityBits111(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserPriorityBits111'], value)

    def update(self, CbsMagnitude=None, CbsMultiplier=None, Cf=None, CirMagnitude=None, CirMultiplier=None, Cm=None, EbsMagnitude=None, EbsMultiplier=None, EirMagnitude=None, EirMultiplier=None, Enabled=None, PerCos=None, UserPriorityBits000=None, UserPriorityBits001=None, UserPriorityBits010=None, UserPriorityBits011=None, UserPriorityBits100=None, UserPriorityBits101=None, UserPriorityBits110=None, UserPriorityBits111=None):
        """Updates bwProfile resource on the server.

        Args
        ----
        - CbsMagnitude (number): 
        - CbsMultiplier (number): 
        - Cf (bool): 
        - CirMagnitude (number): 
        - CirMultiplier (number): 
        - Cm (bool): 
        - EbsMagnitude (number): 
        - EbsMultiplier (number): 
        - EirMagnitude (number): 
        - EirMultiplier (number): 
        - Enabled (bool): 
        - PerCos (bool): 
        - UserPriorityBits000 (bool): 
        - UserPriorityBits001 (bool): 
        - UserPriorityBits010 (bool): 
        - UserPriorityBits011 (bool): 
        - UserPriorityBits100 (bool): 
        - UserPriorityBits101 (bool): 
        - UserPriorityBits110 (bool): 
        - UserPriorityBits111 (bool): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, CbsMagnitude=None, CbsMultiplier=None, Cf=None, CirMagnitude=None, CirMultiplier=None, Cm=None, EbsMagnitude=None, EbsMultiplier=None, EirMagnitude=None, EirMultiplier=None, Enabled=None, PerCos=None, UserPriorityBits000=None, UserPriorityBits001=None, UserPriorityBits010=None, UserPriorityBits011=None, UserPriorityBits100=None, UserPriorityBits101=None, UserPriorityBits110=None, UserPriorityBits111=None):
        """Adds a new bwProfile resource on the server and adds it to the container.

        Args
        ----
        - CbsMagnitude (number): 
        - CbsMultiplier (number): 
        - Cf (bool): 
        - CirMagnitude (number): 
        - CirMultiplier (number): 
        - Cm (bool): 
        - EbsMagnitude (number): 
        - EbsMultiplier (number): 
        - EirMagnitude (number): 
        - EirMultiplier (number): 
        - Enabled (bool): 
        - PerCos (bool): 
        - UserPriorityBits000 (bool): 
        - UserPriorityBits001 (bool): 
        - UserPriorityBits010 (bool): 
        - UserPriorityBits011 (bool): 
        - UserPriorityBits100 (bool): 
        - UserPriorityBits101 (bool): 
        - UserPriorityBits110 (bool): 
        - UserPriorityBits111 (bool): 

        Returns
        -------
        - self: This instance with all currently retrieved bwProfile resources using find and the newly added bwProfile resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained bwProfile resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, CbsMagnitude=None, CbsMultiplier=None, Cf=None, CirMagnitude=None, CirMultiplier=None, Cm=None, EbsMagnitude=None, EbsMultiplier=None, EirMagnitude=None, EirMultiplier=None, Enabled=None, PerCos=None, UserPriorityBits000=None, UserPriorityBits001=None, UserPriorityBits010=None, UserPriorityBits011=None, UserPriorityBits100=None, UserPriorityBits101=None, UserPriorityBits110=None, UserPriorityBits111=None):
        """Finds and retrieves bwProfile resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bwProfile resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bwProfile resources from the server.

        Args
        ----
        - CbsMagnitude (number): 
        - CbsMultiplier (number): 
        - Cf (bool): 
        - CirMagnitude (number): 
        - CirMultiplier (number): 
        - Cm (bool): 
        - EbsMagnitude (number): 
        - EbsMultiplier (number): 
        - EirMagnitude (number): 
        - EirMultiplier (number): 
        - Enabled (bool): 
        - PerCos (bool): 
        - UserPriorityBits000 (bool): 
        - UserPriorityBits001 (bool): 
        - UserPriorityBits010 (bool): 
        - UserPriorityBits011 (bool): 
        - UserPriorityBits100 (bool): 
        - UserPriorityBits101 (bool): 
        - UserPriorityBits110 (bool): 
        - UserPriorityBits111 (bool): 

        Returns
        -------
        - self: This instance with matching bwProfile resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bwProfile data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bwProfile resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
