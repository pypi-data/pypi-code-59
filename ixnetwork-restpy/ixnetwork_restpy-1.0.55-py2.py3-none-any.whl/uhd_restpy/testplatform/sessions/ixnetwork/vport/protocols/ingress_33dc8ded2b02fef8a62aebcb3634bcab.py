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


class Ingress(Base):
    """
    The Ingress class encapsulates a required ingress resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'ingress'
    _SDM_ATT_MAP = {
        'EnableEro': 'enableEro',
        'Ero': 'ero',
        'PrefixLength': 'prefixLength',
        'PrependDutToEro': 'prependDutToEro',
        'ReservationErrorTlv': 'reservationErrorTlv',
        'Rro': 'rro',
        'SendRro': 'sendRro',
        'TunnelIdsCount': 'tunnelIdsCount',
        'TunnelIdsStart': 'tunnelIdsStart',
    }

    def __init__(self, parent):
        super(Ingress, self).__init__(parent)

    @property
    def SenderRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.senderrange_15dfd9e6673a6986869f84e8c22d0879.SenderRange): An instance of the SenderRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.senderrange_15dfd9e6673a6986869f84e8c22d0879 import SenderRange
        return SenderRange(self)

    @property
    def EnableEro(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableEro'])
    @EnableEro.setter
    def EnableEro(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableEro'], value)

    @property
    def Ero(self):
        """
        Returns
        -------
        - list(dict(arg1:str[ip | as],arg2:str,arg3:number,arg4:bool)): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ero'])
    @Ero.setter
    def Ero(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ero'], value)

    @property
    def PrefixLength(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrefixLength'])
    @PrefixLength.setter
    def PrefixLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PrefixLength'], value)

    @property
    def PrependDutToEro(self):
        """
        Returns
        -------
        - str(none | prependLoose | prependStrict): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrependDutToEro'])
    @PrependDutToEro.setter
    def PrependDutToEro(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PrependDutToEro'], value)

    @property
    def ReservationErrorTlv(self):
        """
        Returns
        -------
        - list(dict(arg1:number,arg2:number,arg3:str)): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReservationErrorTlv'])
    @ReservationErrorTlv.setter
    def ReservationErrorTlv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReservationErrorTlv'], value)

    @property
    def Rro(self):
        """
        Returns
        -------
        - list(dict(arg1:str[ip | label],arg2:str,arg3:bool,arg4:bool,arg5:number,arg6:bool,arg7:bool,arg8:bool)): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Rro'])
    @Rro.setter
    def Rro(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Rro'], value)

    @property
    def SendRro(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendRro'])
    @SendRro.setter
    def SendRro(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendRro'], value)

    @property
    def TunnelIdsCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelIdsCount'])
    @TunnelIdsCount.setter
    def TunnelIdsCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TunnelIdsCount'], value)

    @property
    def TunnelIdsStart(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelIdsStart'])
    @TunnelIdsStart.setter
    def TunnelIdsStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TunnelIdsStart'], value)

    def update(self, EnableEro=None, Ero=None, PrefixLength=None, PrependDutToEro=None, ReservationErrorTlv=None, Rro=None, SendRro=None, TunnelIdsCount=None, TunnelIdsStart=None):
        """Updates ingress resource on the server.

        Args
        ----
        - EnableEro (bool): 
        - Ero (list(dict(arg1:str[ip | as],arg2:str,arg3:number,arg4:bool))): 
        - PrefixLength (number): 
        - PrependDutToEro (str(none | prependLoose | prependStrict)): 
        - ReservationErrorTlv (list(dict(arg1:number,arg2:number,arg3:str))): 
        - Rro (list(dict(arg1:str[ip | label],arg2:str,arg3:bool,arg4:bool,arg5:number,arg6:bool,arg7:bool,arg8:bool))): 
        - SendRro (bool): 
        - TunnelIdsCount (number): 
        - TunnelIdsStart (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
