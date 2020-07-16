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


class TunnelHeadToLeaf(Base):
    """
    The TunnelHeadToLeaf class encapsulates a list of tunnelHeadToLeaf resources that are managed by the user.
    A list of resources can be retrieved from the server using the TunnelHeadToLeaf.find() method.
    The list can be managed by using the TunnelHeadToLeaf.add() and TunnelHeadToLeaf.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'tunnelHeadToLeaf'
    _SDM_ATT_MAP = {
        'DutHopType': 'dutHopType',
        'DutPrefixLength': 'dutPrefixLength',
        'Enabled': 'enabled',
        'HeadIpStart': 'headIpStart',
        'IsAppendTunnelLeaf': 'isAppendTunnelLeaf',
        'IsPrependDut': 'isPrependDut',
        'IsSendingAsEro': 'isSendingAsEro',
        'IsSendingAsSero': 'isSendingAsSero',
        'SubObjectList': 'subObjectList',
        'TunnelLeafCount': 'tunnelLeafCount',
        'TunnelLeafHopType': 'tunnelLeafHopType',
        'TunnelLeafIpStart': 'tunnelLeafIpStart',
        'TunnelLeafPrefixLength': 'tunnelLeafPrefixLength',
    }

    def __init__(self, parent):
        super(TunnelHeadToLeaf, self).__init__(parent)

    @property
    def DutHopType(self):
        """
        Returns
        -------
        - str(strict | loose): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DutHopType'])
    @DutHopType.setter
    def DutHopType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DutHopType'], value)

    @property
    def DutPrefixLength(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DutPrefixLength'])
    @DutPrefixLength.setter
    def DutPrefixLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DutPrefixLength'], value)

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
    def HeadIpStart(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['HeadIpStart'])

    @property
    def IsAppendTunnelLeaf(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsAppendTunnelLeaf'])
    @IsAppendTunnelLeaf.setter
    def IsAppendTunnelLeaf(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsAppendTunnelLeaf'], value)

    @property
    def IsPrependDut(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsPrependDut'])
    @IsPrependDut.setter
    def IsPrependDut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsPrependDut'], value)

    @property
    def IsSendingAsEro(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsSendingAsEro'])
    @IsSendingAsEro.setter
    def IsSendingAsEro(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsSendingAsEro'], value)

    @property
    def IsSendingAsSero(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsSendingAsSero'])
    @IsSendingAsSero.setter
    def IsSendingAsSero(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsSendingAsSero'], value)

    @property
    def SubObjectList(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SubObjectList'])
    @SubObjectList.setter
    def SubObjectList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SubObjectList'], value)

    @property
    def TunnelLeafCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelLeafCount'])
    @TunnelLeafCount.setter
    def TunnelLeafCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TunnelLeafCount'], value)

    @property
    def TunnelLeafHopType(self):
        """
        Returns
        -------
        - str(strict | loose): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelLeafHopType'])
    @TunnelLeafHopType.setter
    def TunnelLeafHopType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TunnelLeafHopType'], value)

    @property
    def TunnelLeafIpStart(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelLeafIpStart'])
    @TunnelLeafIpStart.setter
    def TunnelLeafIpStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TunnelLeafIpStart'], value)

    @property
    def TunnelLeafPrefixLength(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelLeafPrefixLength'])
    @TunnelLeafPrefixLength.setter
    def TunnelLeafPrefixLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TunnelLeafPrefixLength'], value)

    def update(self, DutHopType=None, DutPrefixLength=None, Enabled=None, IsAppendTunnelLeaf=None, IsPrependDut=None, IsSendingAsEro=None, IsSendingAsSero=None, SubObjectList=None, TunnelLeafCount=None, TunnelLeafHopType=None, TunnelLeafIpStart=None, TunnelLeafPrefixLength=None):
        """Updates tunnelHeadToLeaf resource on the server.

        Args
        ----
        - DutHopType (str(strict | loose)): 
        - DutPrefixLength (number): 
        - Enabled (bool): 
        - IsAppendTunnelLeaf (bool): 
        - IsPrependDut (bool): 
        - IsSendingAsEro (bool): 
        - IsSendingAsSero (bool): 
        - SubObjectList (str): 
        - TunnelLeafCount (number): 
        - TunnelLeafHopType (str(strict | loose)): 
        - TunnelLeafIpStart (str): 
        - TunnelLeafPrefixLength (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, DutHopType=None, DutPrefixLength=None, Enabled=None, IsAppendTunnelLeaf=None, IsPrependDut=None, IsSendingAsEro=None, IsSendingAsSero=None, SubObjectList=None, TunnelLeafCount=None, TunnelLeafHopType=None, TunnelLeafIpStart=None, TunnelLeafPrefixLength=None):
        """Adds a new tunnelHeadToLeaf resource on the server and adds it to the container.

        Args
        ----
        - DutHopType (str(strict | loose)): 
        - DutPrefixLength (number): 
        - Enabled (bool): 
        - IsAppendTunnelLeaf (bool): 
        - IsPrependDut (bool): 
        - IsSendingAsEro (bool): 
        - IsSendingAsSero (bool): 
        - SubObjectList (str): 
        - TunnelLeafCount (number): 
        - TunnelLeafHopType (str(strict | loose)): 
        - TunnelLeafIpStart (str): 
        - TunnelLeafPrefixLength (number): 

        Returns
        -------
        - self: This instance with all currently retrieved tunnelHeadToLeaf resources using find and the newly added tunnelHeadToLeaf resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained tunnelHeadToLeaf resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, DutHopType=None, DutPrefixLength=None, Enabled=None, HeadIpStart=None, IsAppendTunnelLeaf=None, IsPrependDut=None, IsSendingAsEro=None, IsSendingAsSero=None, SubObjectList=None, TunnelLeafCount=None, TunnelLeafHopType=None, TunnelLeafIpStart=None, TunnelLeafPrefixLength=None):
        """Finds and retrieves tunnelHeadToLeaf resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve tunnelHeadToLeaf resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all tunnelHeadToLeaf resources from the server.

        Args
        ----
        - DutHopType (str(strict | loose)): 
        - DutPrefixLength (number): 
        - Enabled (bool): 
        - HeadIpStart (str): 
        - IsAppendTunnelLeaf (bool): 
        - IsPrependDut (bool): 
        - IsSendingAsEro (bool): 
        - IsSendingAsSero (bool): 
        - SubObjectList (str): 
        - TunnelLeafCount (number): 
        - TunnelLeafHopType (str(strict | loose)): 
        - TunnelLeafIpStart (str): 
        - TunnelLeafPrefixLength (number): 

        Returns
        -------
        - self: This instance with matching tunnelHeadToLeaf resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of tunnelHeadToLeaf data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the tunnelHeadToLeaf resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
