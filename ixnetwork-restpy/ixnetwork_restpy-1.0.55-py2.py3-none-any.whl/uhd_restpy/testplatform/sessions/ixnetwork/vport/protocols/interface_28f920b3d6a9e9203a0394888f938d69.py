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


class Interface(Base):
    """
    The Interface class encapsulates a list of interface resources that are managed by the user.
    A list of resources can be retrieved from the server using the Interface.find() method.
    The list can be managed by using the Interface.add() and Interface.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'interface'
    _SDM_ATT_MAP = {
        'BfdCvType': 'bfdCvType',
        'BfdDiscriminatorEnd': 'bfdDiscriminatorEnd',
        'BfdDiscriminatorStart': 'bfdDiscriminatorStart',
        'ControlChannel': 'controlChannel',
        'DestinationAddressIpv4': 'destinationAddressIpv4',
        'DownStreamAddressType': 'downStreamAddressType',
        'DownStreamInterfaceAddress': 'downStreamInterfaceAddress',
        'DownStreamIpAddress': 'downStreamIpAddress',
        'EchoRequestInterval': 'echoRequestInterval',
        'EchoResponseTimeout': 'echoResponseTimeout',
        'EnableDownStreamMappingTlv': 'enableDownStreamMappingTlv',
        'EnableDsIflag': 'enableDsIflag',
        'EnableDsNflag': 'enableDsNflag',
        'EnableFecValidation': 'enableFecValidation',
        'EnablePeriodicPing': 'enablePeriodicPing',
        'Enabled': 'enabled',
        'FlapTxIntervals': 'flapTxIntervals',
        'IncludePadTlv': 'includePadTlv',
        'IncludeVendorEnterpriseNumberTlv': 'includeVendorEnterpriseNumberTlv',
        'Interfaces': 'interfaces',
        'MinRxInterval': 'minRxInterval',
        'Multiplier': 'multiplier',
        'PadTlvFirstOctet': 'padTlvFirstOctet',
        'PadTlvLength': 'padTlvLength',
        'ReplyMode': 'replyMode',
        'TxInterval': 'txInterval',
        'VendorEnterpriseNumber': 'vendorEnterpriseNumber',
    }

    def __init__(self, parent):
        super(Interface, self).__init__(parent)

    @property
    def BfdCvType(self):
        """
        Returns
        -------
        - str(bfdCvTypeIpUdp | bfdCvTypePwAch): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BfdCvType'])
    @BfdCvType.setter
    def BfdCvType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BfdCvType'], value)

    @property
    def BfdDiscriminatorEnd(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BfdDiscriminatorEnd'])
    @BfdDiscriminatorEnd.setter
    def BfdDiscriminatorEnd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BfdDiscriminatorEnd'], value)

    @property
    def BfdDiscriminatorStart(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BfdDiscriminatorStart'])
    @BfdDiscriminatorStart.setter
    def BfdDiscriminatorStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BfdDiscriminatorStart'], value)

    @property
    def ControlChannel(self):
        """
        Returns
        -------
        - str(controlChannelRouterAlert | controlChannelPwAch): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ControlChannel'])
    @ControlChannel.setter
    def ControlChannel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ControlChannel'], value)

    @property
    def DestinationAddressIpv4(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DestinationAddressIpv4'])
    @DestinationAddressIpv4.setter
    def DestinationAddressIpv4(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DestinationAddressIpv4'], value)

    @property
    def DownStreamAddressType(self):
        """
        Returns
        -------
        - str(ipv4Numbered | ipv4UnNumbered | ipv6Numbered | ipv6UnNumbered): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownStreamAddressType'])
    @DownStreamAddressType.setter
    def DownStreamAddressType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownStreamAddressType'], value)

    @property
    def DownStreamInterfaceAddress(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownStreamInterfaceAddress'])
    @DownStreamInterfaceAddress.setter
    def DownStreamInterfaceAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownStreamInterfaceAddress'], value)

    @property
    def DownStreamIpAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownStreamIpAddress'])
    @DownStreamIpAddress.setter
    def DownStreamIpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownStreamIpAddress'], value)

    @property
    def EchoRequestInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EchoRequestInterval'])
    @EchoRequestInterval.setter
    def EchoRequestInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EchoRequestInterval'], value)

    @property
    def EchoResponseTimeout(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EchoResponseTimeout'])
    @EchoResponseTimeout.setter
    def EchoResponseTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EchoResponseTimeout'], value)

    @property
    def EnableDownStreamMappingTlv(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDownStreamMappingTlv'])
    @EnableDownStreamMappingTlv.setter
    def EnableDownStreamMappingTlv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableDownStreamMappingTlv'], value)

    @property
    def EnableDsIflag(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDsIflag'])
    @EnableDsIflag.setter
    def EnableDsIflag(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableDsIflag'], value)

    @property
    def EnableDsNflag(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDsNflag'])
    @EnableDsNflag.setter
    def EnableDsNflag(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableDsNflag'], value)

    @property
    def EnableFecValidation(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableFecValidation'])
    @EnableFecValidation.setter
    def EnableFecValidation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableFecValidation'], value)

    @property
    def EnablePeriodicPing(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePeriodicPing'])
    @EnablePeriodicPing.setter
    def EnablePeriodicPing(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePeriodicPing'], value)

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
    def FlapTxIntervals(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlapTxIntervals'])
    @FlapTxIntervals.setter
    def FlapTxIntervals(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlapTxIntervals'], value)

    @property
    def IncludePadTlv(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludePadTlv'])
    @IncludePadTlv.setter
    def IncludePadTlv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludePadTlv'], value)

    @property
    def IncludeVendorEnterpriseNumberTlv(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeVendorEnterpriseNumberTlv'])
    @IncludeVendorEnterpriseNumberTlv.setter
    def IncludeVendorEnterpriseNumberTlv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeVendorEnterpriseNumberTlv'], value)

    @property
    def Interfaces(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Interfaces'])
    @Interfaces.setter
    def Interfaces(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Interfaces'], value)

    @property
    def MinRxInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinRxInterval'])
    @MinRxInterval.setter
    def MinRxInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinRxInterval'], value)

    @property
    def Multiplier(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Multiplier'])
    @Multiplier.setter
    def Multiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Multiplier'], value)

    @property
    def PadTlvFirstOctet(self):
        """
        Returns
        -------
        - str(dropPadTlvFromReply | copyPadTlvToReply): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PadTlvFirstOctet'])
    @PadTlvFirstOctet.setter
    def PadTlvFirstOctet(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PadTlvFirstOctet'], value)

    @property
    def PadTlvLength(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PadTlvLength'])
    @PadTlvLength.setter
    def PadTlvLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PadTlvLength'], value)

    @property
    def ReplyMode(self):
        """
        Returns
        -------
        - str(doNotReply | replyViaIpv4Ipv6UdpPacket | replyViaIpv4Ipv6UdpPacketWithRouterAlert | replyViaApplicationLevelControlChannel): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReplyMode'])
    @ReplyMode.setter
    def ReplyMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReplyMode'], value)

    @property
    def TxInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxInterval'])
    @TxInterval.setter
    def TxInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TxInterval'], value)

    @property
    def VendorEnterpriseNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VendorEnterpriseNumber'])
    @VendorEnterpriseNumber.setter
    def VendorEnterpriseNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VendorEnterpriseNumber'], value)

    def update(self, BfdCvType=None, BfdDiscriminatorEnd=None, BfdDiscriminatorStart=None, ControlChannel=None, DestinationAddressIpv4=None, DownStreamAddressType=None, DownStreamInterfaceAddress=None, DownStreamIpAddress=None, EchoRequestInterval=None, EchoResponseTimeout=None, EnableDownStreamMappingTlv=None, EnableDsIflag=None, EnableDsNflag=None, EnableFecValidation=None, EnablePeriodicPing=None, Enabled=None, FlapTxIntervals=None, IncludePadTlv=None, IncludeVendorEnterpriseNumberTlv=None, Interfaces=None, MinRxInterval=None, Multiplier=None, PadTlvFirstOctet=None, PadTlvLength=None, ReplyMode=None, TxInterval=None, VendorEnterpriseNumber=None):
        """Updates interface resource on the server.

        Args
        ----
        - BfdCvType (str(bfdCvTypeIpUdp | bfdCvTypePwAch)): 
        - BfdDiscriminatorEnd (number): 
        - BfdDiscriminatorStart (number): 
        - ControlChannel (str(controlChannelRouterAlert | controlChannelPwAch)): 
        - DestinationAddressIpv4 (str): 
        - DownStreamAddressType (str(ipv4Numbered | ipv4UnNumbered | ipv6Numbered | ipv6UnNumbered)): 
        - DownStreamInterfaceAddress (number): 
        - DownStreamIpAddress (str): 
        - EchoRequestInterval (number): 
        - EchoResponseTimeout (number): 
        - EnableDownStreamMappingTlv (bool): 
        - EnableDsIflag (bool): 
        - EnableDsNflag (bool): 
        - EnableFecValidation (bool): 
        - EnablePeriodicPing (bool): 
        - Enabled (bool): 
        - FlapTxIntervals (number): 
        - IncludePadTlv (bool): 
        - IncludeVendorEnterpriseNumberTlv (bool): 
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - MinRxInterval (number): 
        - Multiplier (number): 
        - PadTlvFirstOctet (str(dropPadTlvFromReply | copyPadTlvToReply)): 
        - PadTlvLength (number): 
        - ReplyMode (str(doNotReply | replyViaIpv4Ipv6UdpPacket | replyViaIpv4Ipv6UdpPacketWithRouterAlert | replyViaApplicationLevelControlChannel)): 
        - TxInterval (number): 
        - VendorEnterpriseNumber (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, BfdCvType=None, BfdDiscriminatorEnd=None, BfdDiscriminatorStart=None, ControlChannel=None, DestinationAddressIpv4=None, DownStreamAddressType=None, DownStreamInterfaceAddress=None, DownStreamIpAddress=None, EchoRequestInterval=None, EchoResponseTimeout=None, EnableDownStreamMappingTlv=None, EnableDsIflag=None, EnableDsNflag=None, EnableFecValidation=None, EnablePeriodicPing=None, Enabled=None, FlapTxIntervals=None, IncludePadTlv=None, IncludeVendorEnterpriseNumberTlv=None, Interfaces=None, MinRxInterval=None, Multiplier=None, PadTlvFirstOctet=None, PadTlvLength=None, ReplyMode=None, TxInterval=None, VendorEnterpriseNumber=None):
        """Adds a new interface resource on the server and adds it to the container.

        Args
        ----
        - BfdCvType (str(bfdCvTypeIpUdp | bfdCvTypePwAch)): 
        - BfdDiscriminatorEnd (number): 
        - BfdDiscriminatorStart (number): 
        - ControlChannel (str(controlChannelRouterAlert | controlChannelPwAch)): 
        - DestinationAddressIpv4 (str): 
        - DownStreamAddressType (str(ipv4Numbered | ipv4UnNumbered | ipv6Numbered | ipv6UnNumbered)): 
        - DownStreamInterfaceAddress (number): 
        - DownStreamIpAddress (str): 
        - EchoRequestInterval (number): 
        - EchoResponseTimeout (number): 
        - EnableDownStreamMappingTlv (bool): 
        - EnableDsIflag (bool): 
        - EnableDsNflag (bool): 
        - EnableFecValidation (bool): 
        - EnablePeriodicPing (bool): 
        - Enabled (bool): 
        - FlapTxIntervals (number): 
        - IncludePadTlv (bool): 
        - IncludeVendorEnterpriseNumberTlv (bool): 
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - MinRxInterval (number): 
        - Multiplier (number): 
        - PadTlvFirstOctet (str(dropPadTlvFromReply | copyPadTlvToReply)): 
        - PadTlvLength (number): 
        - ReplyMode (str(doNotReply | replyViaIpv4Ipv6UdpPacket | replyViaIpv4Ipv6UdpPacketWithRouterAlert | replyViaApplicationLevelControlChannel)): 
        - TxInterval (number): 
        - VendorEnterpriseNumber (number): 

        Returns
        -------
        - self: This instance with all currently retrieved interface resources using find and the newly added interface resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained interface resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, BfdCvType=None, BfdDiscriminatorEnd=None, BfdDiscriminatorStart=None, ControlChannel=None, DestinationAddressIpv4=None, DownStreamAddressType=None, DownStreamInterfaceAddress=None, DownStreamIpAddress=None, EchoRequestInterval=None, EchoResponseTimeout=None, EnableDownStreamMappingTlv=None, EnableDsIflag=None, EnableDsNflag=None, EnableFecValidation=None, EnablePeriodicPing=None, Enabled=None, FlapTxIntervals=None, IncludePadTlv=None, IncludeVendorEnterpriseNumberTlv=None, Interfaces=None, MinRxInterval=None, Multiplier=None, PadTlvFirstOctet=None, PadTlvLength=None, ReplyMode=None, TxInterval=None, VendorEnterpriseNumber=None):
        """Finds and retrieves interface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve interface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all interface resources from the server.

        Args
        ----
        - BfdCvType (str(bfdCvTypeIpUdp | bfdCvTypePwAch)): 
        - BfdDiscriminatorEnd (number): 
        - BfdDiscriminatorStart (number): 
        - ControlChannel (str(controlChannelRouterAlert | controlChannelPwAch)): 
        - DestinationAddressIpv4 (str): 
        - DownStreamAddressType (str(ipv4Numbered | ipv4UnNumbered | ipv6Numbered | ipv6UnNumbered)): 
        - DownStreamInterfaceAddress (number): 
        - DownStreamIpAddress (str): 
        - EchoRequestInterval (number): 
        - EchoResponseTimeout (number): 
        - EnableDownStreamMappingTlv (bool): 
        - EnableDsIflag (bool): 
        - EnableDsNflag (bool): 
        - EnableFecValidation (bool): 
        - EnablePeriodicPing (bool): 
        - Enabled (bool): 
        - FlapTxIntervals (number): 
        - IncludePadTlv (bool): 
        - IncludeVendorEnterpriseNumberTlv (bool): 
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - MinRxInterval (number): 
        - Multiplier (number): 
        - PadTlvFirstOctet (str(dropPadTlvFromReply | copyPadTlvToReply)): 
        - PadTlvLength (number): 
        - ReplyMode (str(doNotReply | replyViaIpv4Ipv6UdpPacket | replyViaIpv4Ipv6UdpPacketWithRouterAlert | replyViaApplicationLevelControlChannel)): 
        - TxInterval (number): 
        - VendorEnterpriseNumber (number): 

        Returns
        -------
        - self: This instance with matching interface resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of interface data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the interface resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
