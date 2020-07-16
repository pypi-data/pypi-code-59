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


class RouteRange(Base):
    """
    The RouteRange class encapsulates a list of routeRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the RouteRange.find() method.
    The list can be managed by using the RouteRange.add() and RouteRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'routeRange'
    _SDM_ATT_MAP = {
        'Bandwidth': 'bandwidth',
        'Delay': 'delay',
        'DestCount': 'destCount',
        'EnablePacking': 'enablePacking',
        'Enabled': 'enabled',
        'FirstRoute': 'firstRoute',
        'Flag': 'flag',
        'HopCount': 'hopCount',
        'Load': 'load',
        'Mask': 'mask',
        'Metric': 'metric',
        'Mtu': 'mtu',
        'NextHop': 'nextHop',
        'NomberOfRoutes': 'nomberOfRoutes',
        'NumberOfRoutes': 'numberOfRoutes',
        'OriginatingAs': 'originatingAs',
        'ProtocolId': 'protocolId',
        'Reliability': 'reliability',
        'RouteTag': 'routeTag',
        'Source': 'source',
        'Type': 'type',
    }

    def __init__(self, parent):
        super(RouteRange, self).__init__(parent)

    @property
    def Bandwidth(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Bandwidth'])
    @Bandwidth.setter
    def Bandwidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Bandwidth'], value)

    @property
    def Delay(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Delay'])
    @Delay.setter
    def Delay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Delay'], value)

    @property
    def DestCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DestCount'])
    @DestCount.setter
    def DestCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DestCount'], value)

    @property
    def EnablePacking(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePacking'])
    @EnablePacking.setter
    def EnablePacking(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePacking'], value)

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
    def FirstRoute(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FirstRoute'])
    @FirstRoute.setter
    def FirstRoute(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FirstRoute'], value)

    @property
    def Flag(self):
        """
        Returns
        -------
        - str(externalRoute | candidateDefault): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Flag'])
    @Flag.setter
    def Flag(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Flag'], value)

    @property
    def HopCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['HopCount'])
    @HopCount.setter
    def HopCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HopCount'], value)

    @property
    def Load(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Load'])
    @Load.setter
    def Load(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Load'], value)

    @property
    def Mask(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mask'])
    @Mask.setter
    def Mask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mask'], value)

    @property
    def Metric(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Metric'])
    @Metric.setter
    def Metric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Metric'], value)

    @property
    def Mtu(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mtu'])
    @Mtu.setter
    def Mtu(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mtu'], value)

    @property
    def NextHop(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextHop'])
    @NextHop.setter
    def NextHop(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NextHop'], value)

    @property
    def NomberOfRoutes(self):
        """DEPRECATED 
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NomberOfRoutes'])
    @NomberOfRoutes.setter
    def NomberOfRoutes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NomberOfRoutes'], value)

    @property
    def NumberOfRoutes(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfRoutes'])
    @NumberOfRoutes.setter
    def NumberOfRoutes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfRoutes'], value)

    @property
    def OriginatingAs(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OriginatingAs'])
    @OriginatingAs.setter
    def OriginatingAs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OriginatingAs'], value)

    @property
    def ProtocolId(self):
        """
        Returns
        -------
        - str(igrp | enhancedIgrp | static | rip | hello | ospf | isis | egp | bgp | idrp | connected): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolId'])
    @ProtocolId.setter
    def ProtocolId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProtocolId'], value)

    @property
    def Reliability(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Reliability'])
    @Reliability.setter
    def Reliability(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Reliability'], value)

    @property
    def RouteTag(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteTag'])
    @RouteTag.setter
    def RouteTag(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouteTag'], value)

    @property
    def Source(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Source'])
    @Source.setter
    def Source(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Source'], value)

    @property
    def Type(self):
        """
        Returns
        -------
        - str(external | internal): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])
    @Type.setter
    def Type(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Type'], value)

    def update(self, Bandwidth=None, Delay=None, DestCount=None, EnablePacking=None, Enabled=None, FirstRoute=None, Flag=None, HopCount=None, Load=None, Mask=None, Metric=None, Mtu=None, NextHop=None, NomberOfRoutes=None, NumberOfRoutes=None, OriginatingAs=None, ProtocolId=None, Reliability=None, RouteTag=None, Source=None, Type=None):
        """Updates routeRange resource on the server.

        Args
        ----
        - Bandwidth (number): 
        - Delay (number): 
        - DestCount (number): 
        - EnablePacking (bool): 
        - Enabled (bool): 
        - FirstRoute (str): 
        - Flag (str(externalRoute | candidateDefault)): 
        - HopCount (number): 
        - Load (number): 
        - Mask (number): 
        - Metric (number): 
        - Mtu (number): 
        - NextHop (str): 
        - NomberOfRoutes (number): 
        - NumberOfRoutes (number): 
        - OriginatingAs (number): 
        - ProtocolId (str(igrp | enhancedIgrp | static | rip | hello | ospf | isis | egp | bgp | idrp | connected)): 
        - Reliability (number): 
        - RouteTag (number): 
        - Source (str): 
        - Type (str(external | internal)): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Bandwidth=None, Delay=None, DestCount=None, EnablePacking=None, Enabled=None, FirstRoute=None, Flag=None, HopCount=None, Load=None, Mask=None, Metric=None, Mtu=None, NextHop=None, NomberOfRoutes=None, NumberOfRoutes=None, OriginatingAs=None, ProtocolId=None, Reliability=None, RouteTag=None, Source=None, Type=None):
        """Adds a new routeRange resource on the server and adds it to the container.

        Args
        ----
        - Bandwidth (number): 
        - Delay (number): 
        - DestCount (number): 
        - EnablePacking (bool): 
        - Enabled (bool): 
        - FirstRoute (str): 
        - Flag (str(externalRoute | candidateDefault)): 
        - HopCount (number): 
        - Load (number): 
        - Mask (number): 
        - Metric (number): 
        - Mtu (number): 
        - NextHop (str): 
        - NomberOfRoutes (number): 
        - NumberOfRoutes (number): 
        - OriginatingAs (number): 
        - ProtocolId (str(igrp | enhancedIgrp | static | rip | hello | ospf | isis | egp | bgp | idrp | connected)): 
        - Reliability (number): 
        - RouteTag (number): 
        - Source (str): 
        - Type (str(external | internal)): 

        Returns
        -------
        - self: This instance with all currently retrieved routeRange resources using find and the newly added routeRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained routeRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Bandwidth=None, Delay=None, DestCount=None, EnablePacking=None, Enabled=None, FirstRoute=None, Flag=None, HopCount=None, Load=None, Mask=None, Metric=None, Mtu=None, NextHop=None, NomberOfRoutes=None, NumberOfRoutes=None, OriginatingAs=None, ProtocolId=None, Reliability=None, RouteTag=None, Source=None, Type=None):
        """Finds and retrieves routeRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve routeRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all routeRange resources from the server.

        Args
        ----
        - Bandwidth (number): 
        - Delay (number): 
        - DestCount (number): 
        - EnablePacking (bool): 
        - Enabled (bool): 
        - FirstRoute (str): 
        - Flag (str(externalRoute | candidateDefault)): 
        - HopCount (number): 
        - Load (number): 
        - Mask (number): 
        - Metric (number): 
        - Mtu (number): 
        - NextHop (str): 
        - NomberOfRoutes (number): 
        - NumberOfRoutes (number): 
        - OriginatingAs (number): 
        - ProtocolId (str(igrp | enhancedIgrp | static | rip | hello | ospf | isis | egp | bgp | idrp | connected)): 
        - Reliability (number): 
        - RouteTag (number): 
        - Source (str): 
        - Type (str(external | internal)): 

        Returns
        -------
        - self: This instance with matching routeRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of routeRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the routeRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
