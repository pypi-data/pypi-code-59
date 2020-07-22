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


class Ipv4MulticastVpn(Base):
    """
    The Ipv4MulticastVpn class encapsulates a list of ipv4MulticastVpn resources that are managed by the system.
    A list of resources can be retrieved from the server using the Ipv4MulticastVpn.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'ipv4MulticastVpn'
    _SDM_ATT_MAP = {
        'AddressFamily': 'addressFamily',
        'AddressLength': 'addressLength',
        'CMcastRouteType': 'cMcastRouteType',
        'GroupAddress': 'groupAddress',
        'Neighbor': 'neighbor',
        'OpaqueLength': 'opaqueLength',
        'OriginatingRouter': 'originatingRouter',
        'RootAddress': 'rootAddress',
        'RouteDistinguisher': 'routeDistinguisher',
        'RouteKeyGroupAddress': 'routeKeyGroupAddress',
        'RouteKeyOriginatingRouter': 'routeKeyOriginatingRouter',
        'RouteKeyRouteDistinguisher': 'routeKeyRouteDistinguisher',
        'RouteKeyRsvpP2mpExtendedTunnelId': 'routeKeyRsvpP2mpExtendedTunnelId',
        'RouteKeyRsvpP2mpId': 'routeKeyRsvpP2mpId',
        'RouteKeyRsvpP2mpTunnelId': 'routeKeyRsvpP2mpTunnelId',
        'RouteKeySourceAddress': 'routeKeySourceAddress',
        'RouteKeyTunnelType': 'routeKeyTunnelType',
        'RouteKeyUpstreamLabel': 'routeKeyUpstreamLabel',
        'RouteType': 'routeType',
        'RsvpP2mpExtendedTunnelId': 'rsvpP2mpExtendedTunnelId',
        'RsvpP2mpId': 'rsvpP2mpId',
        'RsvpP2mpTunnelId': 'rsvpP2mpTunnelId',
        'SourceAddress': 'sourceAddress',
        'SourceAs': 'sourceAs',
        'TunnelType': 'tunnelType',
        'UpstreamLabel': 'upstreamLabel',
    }

    def __init__(self, parent):
        super(Ipv4MulticastVpn, self).__init__(parent)

    @property
    def OpaqueValueElement(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.opaquevalueelement_98265968d2cf9ade77b8757edf25c867.OpaqueValueElement): An instance of the OpaqueValueElement class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.opaquevalueelement_98265968d2cf9ade77b8757edf25c867 import OpaqueValueElement
        return OpaqueValueElement(self)

    @property
    def AddressFamily(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddressFamily'])

    @property
    def AddressLength(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddressLength'])

    @property
    def CMcastRouteType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CMcastRouteType'])

    @property
    def GroupAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupAddress'])

    @property
    def Neighbor(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Neighbor'])

    @property
    def OpaqueLength(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OpaqueLength'])

    @property
    def OriginatingRouter(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OriginatingRouter'])

    @property
    def RootAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RootAddress'])

    @property
    def RouteDistinguisher(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteDistinguisher'])

    @property
    def RouteKeyGroupAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteKeyGroupAddress'])

    @property
    def RouteKeyOriginatingRouter(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteKeyOriginatingRouter'])

    @property
    def RouteKeyRouteDistinguisher(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteKeyRouteDistinguisher'])

    @property
    def RouteKeyRsvpP2mpExtendedTunnelId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteKeyRsvpP2mpExtendedTunnelId'])

    @property
    def RouteKeyRsvpP2mpId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteKeyRsvpP2mpId'])

    @property
    def RouteKeyRsvpP2mpTunnelId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteKeyRsvpP2mpTunnelId'])

    @property
    def RouteKeySourceAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteKeySourceAddress'])

    @property
    def RouteKeyTunnelType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteKeyTunnelType'])

    @property
    def RouteKeyUpstreamLabel(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteKeyUpstreamLabel'])

    @property
    def RouteType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteType'])

    @property
    def RsvpP2mpExtendedTunnelId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RsvpP2mpExtendedTunnelId'])

    @property
    def RsvpP2mpId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RsvpP2mpId'])

    @property
    def RsvpP2mpTunnelId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RsvpP2mpTunnelId'])

    @property
    def SourceAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceAddress'])

    @property
    def SourceAs(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceAs'])

    @property
    def TunnelType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelType'])

    @property
    def UpstreamLabel(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamLabel'])

    def find(self, AddressFamily=None, AddressLength=None, CMcastRouteType=None, GroupAddress=None, Neighbor=None, OpaqueLength=None, OriginatingRouter=None, RootAddress=None, RouteDistinguisher=None, RouteKeyGroupAddress=None, RouteKeyOriginatingRouter=None, RouteKeyRouteDistinguisher=None, RouteKeyRsvpP2mpExtendedTunnelId=None, RouteKeyRsvpP2mpId=None, RouteKeyRsvpP2mpTunnelId=None, RouteKeySourceAddress=None, RouteKeyTunnelType=None, RouteKeyUpstreamLabel=None, RouteType=None, RsvpP2mpExtendedTunnelId=None, RsvpP2mpId=None, RsvpP2mpTunnelId=None, SourceAddress=None, SourceAs=None, TunnelType=None, UpstreamLabel=None):
        """Finds and retrieves ipv4MulticastVpn resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ipv4MulticastVpn resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ipv4MulticastVpn resources from the server.

        Args
        ----
        - AddressFamily (number): 
        - AddressLength (number): 
        - CMcastRouteType (str): 
        - GroupAddress (str): 
        - Neighbor (str): 
        - OpaqueLength (number): 
        - OriginatingRouter (str): 
        - RootAddress (str): 
        - RouteDistinguisher (str): 
        - RouteKeyGroupAddress (str): 
        - RouteKeyOriginatingRouter (str): 
        - RouteKeyRouteDistinguisher (str): 
        - RouteKeyRsvpP2mpExtendedTunnelId (str): 
        - RouteKeyRsvpP2mpId (number): 
        - RouteKeyRsvpP2mpTunnelId (number): 
        - RouteKeySourceAddress (str): 
        - RouteKeyTunnelType (str): 
        - RouteKeyUpstreamLabel (number): 
        - RouteType (str): 
        - RsvpP2mpExtendedTunnelId (str): 
        - RsvpP2mpId (number): 
        - RsvpP2mpTunnelId (number): 
        - SourceAddress (str): 
        - SourceAs (number): 
        - TunnelType (str): 
        - UpstreamLabel (number): 

        Returns
        -------
        - self: This instance with matching ipv4MulticastVpn resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ipv4MulticastVpn data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ipv4MulticastVpn resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
