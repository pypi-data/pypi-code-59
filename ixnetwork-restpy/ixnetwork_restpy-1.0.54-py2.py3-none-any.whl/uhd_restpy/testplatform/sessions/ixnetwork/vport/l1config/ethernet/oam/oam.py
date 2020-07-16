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


class Oam(Base):
    """
    The Oam class encapsulates a required oam resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'oam'
    _SDM_ATT_MAP = {
        'EnableTlvOption': 'enableTlvOption',
        'Enabled': 'enabled',
        'IdleTimer': 'idleTimer',
        'LinkEvents': 'linkEvents',
        'Loopback': 'loopback',
        'MacAddress': 'macAddress',
        'MaxOAMPDUSize': 'maxOAMPDUSize',
        'OrganizationUniqueIdentifier': 'organizationUniqueIdentifier',
        'TlvType': 'tlvType',
        'TlvValue': 'tlvValue',
        'VendorSpecificInformation': 'vendorSpecificInformation',
    }

    def __init__(self, parent):
        super(Oam, self).__init__(parent)

    @property
    def EnableTlvOption(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableTlvOption'])
    @EnableTlvOption.setter
    def EnableTlvOption(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableTlvOption'], value)

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
    def IdleTimer(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IdleTimer'])
    @IdleTimer.setter
    def IdleTimer(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IdleTimer'], value)

    @property
    def LinkEvents(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkEvents'])
    @LinkEvents.setter
    def LinkEvents(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkEvents'], value)

    @property
    def Loopback(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Loopback'])
    @Loopback.setter
    def Loopback(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Loopback'], value)

    @property
    def MacAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MacAddress'])
    @MacAddress.setter
    def MacAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MacAddress'], value)

    @property
    def MaxOAMPDUSize(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxOAMPDUSize'])
    @MaxOAMPDUSize.setter
    def MaxOAMPDUSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxOAMPDUSize'], value)

    @property
    def OrganizationUniqueIdentifier(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OrganizationUniqueIdentifier'])
    @OrganizationUniqueIdentifier.setter
    def OrganizationUniqueIdentifier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OrganizationUniqueIdentifier'], value)

    @property
    def TlvType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TlvType'])
    @TlvType.setter
    def TlvType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TlvType'], value)

    @property
    def TlvValue(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TlvValue'])
    @TlvValue.setter
    def TlvValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TlvValue'], value)

    @property
    def VendorSpecificInformation(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VendorSpecificInformation'])
    @VendorSpecificInformation.setter
    def VendorSpecificInformation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VendorSpecificInformation'], value)

    def update(self, EnableTlvOption=None, Enabled=None, IdleTimer=None, LinkEvents=None, Loopback=None, MacAddress=None, MaxOAMPDUSize=None, OrganizationUniqueIdentifier=None, TlvType=None, TlvValue=None, VendorSpecificInformation=None):
        """Updates oam resource on the server.

        Args
        ----
        - EnableTlvOption (bool): 
        - Enabled (bool): 
        - IdleTimer (number): 
        - LinkEvents (bool): 
        - Loopback (bool): 
        - MacAddress (str): 
        - MaxOAMPDUSize (number): 
        - OrganizationUniqueIdentifier (str): 
        - TlvType (str): 
        - TlvValue (str): 
        - VendorSpecificInformation (str): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
