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


class Ipv4mpls(Base):
    """
    The Ipv4mpls class encapsulates a list of ipv4mpls resources that are managed by the system.
    A list of resources can be retrieved from the server using the Ipv4mpls.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'ipv4mpls'
    _SDM_ATT_MAP = {
        'AsPath': 'asPath',
        'BlockOffset': 'blockOffset',
        'BlockSize': 'blockSize',
        'ControlWordEnabled': 'controlWordEnabled',
        'IpPrefix': 'ipPrefix',
        'LabelBase': 'labelBase',
        'LocalPreference': 'localPreference',
        'MaxLabel': 'maxLabel',
        'MultiExitDiscriminator': 'multiExitDiscriminator',
        'Neighbor': 'neighbor',
        'NextHop': 'nextHop',
        'OriginType': 'originType',
        'PrefixLength': 'prefixLength',
        'RouteDistinguisher': 'routeDistinguisher',
        'SeqDeliveryEnabled': 'seqDeliveryEnabled',
        'SiteId': 'siteId',
    }

    def __init__(self, parent):
        super(Ipv4mpls, self).__init__(parent)

    @property
    def AsPath(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AsPath'])

    @property
    def BlockOffset(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BlockOffset'])

    @property
    def BlockSize(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BlockSize'])

    @property
    def ControlWordEnabled(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ControlWordEnabled'])

    @property
    def IpPrefix(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpPrefix'])

    @property
    def LabelBase(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LabelBase'])

    @property
    def LocalPreference(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalPreference'])

    @property
    def MaxLabel(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxLabel'])

    @property
    def MultiExitDiscriminator(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MultiExitDiscriminator'])

    @property
    def Neighbor(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Neighbor'])

    @property
    def NextHop(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextHop'])

    @property
    def OriginType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OriginType'])

    @property
    def PrefixLength(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrefixLength'])

    @property
    def RouteDistinguisher(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteDistinguisher'])

    @property
    def SeqDeliveryEnabled(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SeqDeliveryEnabled'])

    @property
    def SiteId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SiteId'])

    def find(self, AsPath=None, BlockOffset=None, BlockSize=None, ControlWordEnabled=None, IpPrefix=None, LabelBase=None, LocalPreference=None, MaxLabel=None, MultiExitDiscriminator=None, Neighbor=None, NextHop=None, OriginType=None, PrefixLength=None, RouteDistinguisher=None, SeqDeliveryEnabled=None, SiteId=None):
        """Finds and retrieves ipv4mpls resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ipv4mpls resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ipv4mpls resources from the server.

        Args
        ----
        - AsPath (str): 
        - BlockOffset (number): 
        - BlockSize (number): 
        - ControlWordEnabled (bool): 
        - IpPrefix (str): 
        - LabelBase (number): 
        - LocalPreference (number): 
        - MaxLabel (number): 
        - MultiExitDiscriminator (number): 
        - Neighbor (str): 
        - NextHop (str): 
        - OriginType (str): 
        - PrefixLength (number): 
        - RouteDistinguisher (str): 
        - SeqDeliveryEnabled (bool): 
        - SiteId (number): 

        Returns
        -------
        - self: This instance with matching ipv4mpls resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ipv4mpls data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ipv4mpls resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
