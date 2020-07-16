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


class Atm(Base):
    """
    The Atm class encapsulates a required atm resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'atm'
    _SDM_ATT_MAP = {
        'Encapsulation': 'encapsulation',
        'Vci': 'vci',
        'Vpi': 'vpi',
    }

    def __init__(self, parent):
        super(Atm, self).__init__(parent)

    @property
    def Encapsulation(self):
        """
        Returns
        -------
        - str(vcMuxIpv4 | vcMuxIpv6 | vcMuxBridgeFcs | vcMuxBridgeNoFcs | llcClip | llcBridgeFcs | llcBridgeNoFcs): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Encapsulation'])
    @Encapsulation.setter
    def Encapsulation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Encapsulation'], value)

    @property
    def Vci(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Vci'])
    @Vci.setter
    def Vci(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Vci'], value)

    @property
    def Vpi(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Vpi'])
    @Vpi.setter
    def Vpi(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Vpi'], value)

    def update(self, Encapsulation=None, Vci=None, Vpi=None):
        """Updates atm resource on the server.

        Args
        ----
        - Encapsulation (str(vcMuxIpv4 | vcMuxIpv6 | vcMuxBridgeFcs | vcMuxBridgeNoFcs | llcClip | llcBridgeFcs | llcBridgeNoFcs)): 
        - Vci (number): 
        - Vpi (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
