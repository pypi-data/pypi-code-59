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


class IncludeIpFecRange(Base):
    """
    The IncludeIpFecRange class encapsulates a list of includeIpFecRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the IncludeIpFecRange.find() method.
    The list can be managed by using the IncludeIpFecRange.add() and IncludeIpFecRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'includeIpFecRange'
    _SDM_ATT_MAP = {
        'EnableExactPrefixMatch': 'enableExactPrefixMatch',
        'Enabled': 'enabled',
        'FirstNetwork': 'firstNetwork',
        'MaskWidth': 'maskWidth',
        'NumberOfNetworks': 'numberOfNetworks',
    }

    def __init__(self, parent):
        super(IncludeIpFecRange, self).__init__(parent)

    @property
    def EnableExactPrefixMatch(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableExactPrefixMatch'])
    @EnableExactPrefixMatch.setter
    def EnableExactPrefixMatch(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableExactPrefixMatch'], value)

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
    def FirstNetwork(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FirstNetwork'])
    @FirstNetwork.setter
    def FirstNetwork(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FirstNetwork'], value)

    @property
    def MaskWidth(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaskWidth'])
    @MaskWidth.setter
    def MaskWidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaskWidth'], value)

    @property
    def NumberOfNetworks(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfNetworks'])
    @NumberOfNetworks.setter
    def NumberOfNetworks(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfNetworks'], value)

    def update(self, EnableExactPrefixMatch=None, Enabled=None, FirstNetwork=None, MaskWidth=None, NumberOfNetworks=None):
        """Updates includeIpFecRange resource on the server.

        Args
        ----
        - EnableExactPrefixMatch (bool): 
        - Enabled (bool): 
        - FirstNetwork (str): 
        - MaskWidth (number): 
        - NumberOfNetworks (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, EnableExactPrefixMatch=None, Enabled=None, FirstNetwork=None, MaskWidth=None, NumberOfNetworks=None):
        """Adds a new includeIpFecRange resource on the server and adds it to the container.

        Args
        ----
        - EnableExactPrefixMatch (bool): 
        - Enabled (bool): 
        - FirstNetwork (str): 
        - MaskWidth (number): 
        - NumberOfNetworks (number): 

        Returns
        -------
        - self: This instance with all currently retrieved includeIpFecRange resources using find and the newly added includeIpFecRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained includeIpFecRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EnableExactPrefixMatch=None, Enabled=None, FirstNetwork=None, MaskWidth=None, NumberOfNetworks=None):
        """Finds and retrieves includeIpFecRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve includeIpFecRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all includeIpFecRange resources from the server.

        Args
        ----
        - EnableExactPrefixMatch (bool): 
        - Enabled (bool): 
        - FirstNetwork (str): 
        - MaskWidth (number): 
        - NumberOfNetworks (number): 

        Returns
        -------
        - self: This instance with matching includeIpFecRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of includeIpFecRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the includeIpFecRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
