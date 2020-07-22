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


class NetworkRange(Base):
    """
    The NetworkRange class encapsulates a list of networkRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the NetworkRange.find() method.
    The list can be managed by using the NetworkRange.add() and NetworkRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'networkRange'
    _SDM_ATT_MAP = {
        'EnableHostName': 'enableHostName',
        'Enabled': 'enabled',
        'EntryCol': 'entryCol',
        'EntryRow': 'entryRow',
        'GridNodeRoutes': 'gridNodeRoutes',
        'GridOutsideExLinks': 'gridOutsideExLinks',
        'GridOutsideLinks': 'gridOutsideLinks',
        'HostNamePrefix': 'hostNamePrefix',
        'InterfaceIps': 'interfaceIps',
        'InterfaceMetric': 'interfaceMetric',
        'Ipv6MtMetric': 'ipv6MtMetric',
        'LinkType': 'linkType',
        'NoOfCols': 'noOfCols',
        'NoOfRows': 'noOfRows',
        'RouterId': 'routerId',
        'RouterIdIncrement': 'routerIdIncrement',
        'TePaths': 'tePaths',
        'UseWideMetric': 'useWideMetric',
    }

    def __init__(self, parent):
        super(NetworkRange, self).__init__(parent)

    @property
    def EntryTe(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.entryte_9cd30e209352f3748008e607434e92a4.EntryTe): An instance of the EntryTe class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.entryte_9cd30e209352f3748008e607434e92a4 import EntryTe
        return EntryTe(self)._select()

    @property
    def RangeTe(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.rangete_9c7f010a9212f361a3dacba9c17f9cf0.RangeTe): An instance of the RangeTe class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.rangete_9c7f010a9212f361a3dacba9c17f9cf0 import RangeTe
        return RangeTe(self)._select()

    @property
    def EnableHostName(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableHostName'])
    @EnableHostName.setter
    def EnableHostName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableHostName'], value)

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
    def EntryCol(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EntryCol'])
    @EntryCol.setter
    def EntryCol(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EntryCol'], value)

    @property
    def EntryRow(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EntryRow'])
    @EntryRow.setter
    def EntryRow(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EntryRow'], value)

    @property
    def GridNodeRoutes(self):
        """
        Returns
        -------
        - list(dict(arg1:bool,arg2:str[ipAny | ipv4 | ipv6],arg3:str,arg4:number,arg5:number,arg6:number,arg7:number,arg8:bool,arg9:bool,arg10:number)): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['GridNodeRoutes'])
    @GridNodeRoutes.setter
    def GridNodeRoutes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GridNodeRoutes'], value)

    @property
    def GridOutsideExLinks(self):
        """
        Returns
        -------
        - list(dict(arg1:number,arg2:number,arg3:str,arg4:list[dict(arg1:str[ipAny | ipv4 | ipv6],arg2:str,arg3:number)],arg5:str,arg6:number,arg7:number,arg8:number,arg9:number,arg10:number,arg11:number,arg12:number,arg13:number,arg14:number,arg15:number,arg16:number)): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['GridOutsideExLinks'])
    @GridOutsideExLinks.setter
    def GridOutsideExLinks(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GridOutsideExLinks'], value)

    @property
    def GridOutsideLinks(self):
        """DEPRECATED 
        Returns
        -------
        - list(dict(arg1:number,arg2:number,arg3:str,arg4:str,arg5:number,arg6:number,arg7:number,arg8:number,arg9:number,arg10:number,arg11:number,arg12:number,arg13:number,arg14:number,arg15:number)): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['GridOutsideLinks'])
    @GridOutsideLinks.setter
    def GridOutsideLinks(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GridOutsideLinks'], value)

    @property
    def HostNamePrefix(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['HostNamePrefix'])
    @HostNamePrefix.setter
    def HostNamePrefix(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HostNamePrefix'], value)

    @property
    def InterfaceIps(self):
        """
        Returns
        -------
        - list(dict(arg1:str[ipAny | ipv4 | ipv6],arg2:str,arg3:number)): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceIps'])
    @InterfaceIps.setter
    def InterfaceIps(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceIps'], value)

    @property
    def InterfaceMetric(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceMetric'])
    @InterfaceMetric.setter
    def InterfaceMetric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceMetric'], value)

    @property
    def Ipv6MtMetric(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6MtMetric'])
    @Ipv6MtMetric.setter
    def Ipv6MtMetric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6MtMetric'], value)

    @property
    def LinkType(self):
        """
        Returns
        -------
        - str(pointToPoint | broadcast): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkType'])
    @LinkType.setter
    def LinkType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkType'], value)

    @property
    def NoOfCols(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfCols'])
    @NoOfCols.setter
    def NoOfCols(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfCols'], value)

    @property
    def NoOfRows(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfRows'])
    @NoOfRows.setter
    def NoOfRows(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfRows'], value)

    @property
    def RouterId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouterId'])
    @RouterId.setter
    def RouterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouterId'], value)

    @property
    def RouterIdIncrement(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouterIdIncrement'])
    @RouterIdIncrement.setter
    def RouterIdIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouterIdIncrement'], value)

    @property
    def TePaths(self):
        """
        Returns
        -------
        - list(dict(arg1:number,arg2:number,arg3:number,arg4:number,arg5:number,arg6:number,arg7:bool,arg8:str,arg9:number,arg10:number,arg11:number,arg12:number,arg13:number,arg14:number,arg15:number,arg16:number,arg17:number,arg18:number,arg19:number)): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TePaths'])
    @TePaths.setter
    def TePaths(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TePaths'], value)

    @property
    def UseWideMetric(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseWideMetric'])
    @UseWideMetric.setter
    def UseWideMetric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseWideMetric'], value)

    def update(self, EnableHostName=None, Enabled=None, EntryCol=None, EntryRow=None, GridNodeRoutes=None, GridOutsideExLinks=None, GridOutsideLinks=None, HostNamePrefix=None, InterfaceIps=None, InterfaceMetric=None, Ipv6MtMetric=None, LinkType=None, NoOfCols=None, NoOfRows=None, RouterId=None, RouterIdIncrement=None, TePaths=None, UseWideMetric=None):
        """Updates networkRange resource on the server.

        Args
        ----
        - EnableHostName (bool): 
        - Enabled (bool): 
        - EntryCol (number): 
        - EntryRow (number): 
        - GridNodeRoutes (list(dict(arg1:bool,arg2:str[ipAny | ipv4 | ipv6],arg3:str,arg4:number,arg5:number,arg6:number,arg7:number,arg8:bool,arg9:bool,arg10:number))): 
        - GridOutsideExLinks (list(dict(arg1:number,arg2:number,arg3:str,arg4:list[dict(arg1:str[ipAny | ipv4 | ipv6],arg2:str,arg3:number)],arg5:str,arg6:number,arg7:number,arg8:number,arg9:number,arg10:number,arg11:number,arg12:number,arg13:number,arg14:number,arg15:number,arg16:number))): 
        - GridOutsideLinks (list(dict(arg1:number,arg2:number,arg3:str,arg4:str,arg5:number,arg6:number,arg7:number,arg8:number,arg9:number,arg10:number,arg11:number,arg12:number,arg13:number,arg14:number,arg15:number))): 
        - HostNamePrefix (str): 
        - InterfaceIps (list(dict(arg1:str[ipAny | ipv4 | ipv6],arg2:str,arg3:number))): 
        - InterfaceMetric (number): 
        - Ipv6MtMetric (number): 
        - LinkType (str(pointToPoint | broadcast)): 
        - NoOfCols (number): 
        - NoOfRows (number): 
        - RouterId (str): 
        - RouterIdIncrement (str): 
        - TePaths (list(dict(arg1:number,arg2:number,arg3:number,arg4:number,arg5:number,arg6:number,arg7:bool,arg8:str,arg9:number,arg10:number,arg11:number,arg12:number,arg13:number,arg14:number,arg15:number,arg16:number,arg17:number,arg18:number,arg19:number))): 
        - UseWideMetric (bool): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, EnableHostName=None, Enabled=None, EntryCol=None, EntryRow=None, GridNodeRoutes=None, GridOutsideExLinks=None, GridOutsideLinks=None, HostNamePrefix=None, InterfaceIps=None, InterfaceMetric=None, Ipv6MtMetric=None, LinkType=None, NoOfCols=None, NoOfRows=None, RouterId=None, RouterIdIncrement=None, TePaths=None, UseWideMetric=None):
        """Adds a new networkRange resource on the server and adds it to the container.

        Args
        ----
        - EnableHostName (bool): 
        - Enabled (bool): 
        - EntryCol (number): 
        - EntryRow (number): 
        - GridNodeRoutes (list(dict(arg1:bool,arg2:str[ipAny | ipv4 | ipv6],arg3:str,arg4:number,arg5:number,arg6:number,arg7:number,arg8:bool,arg9:bool,arg10:number))): 
        - GridOutsideExLinks (list(dict(arg1:number,arg2:number,arg3:str,arg4:list[dict(arg1:str[ipAny | ipv4 | ipv6],arg2:str,arg3:number)],arg5:str,arg6:number,arg7:number,arg8:number,arg9:number,arg10:number,arg11:number,arg12:number,arg13:number,arg14:number,arg15:number,arg16:number))): 
        - GridOutsideLinks (list(dict(arg1:number,arg2:number,arg3:str,arg4:str,arg5:number,arg6:number,arg7:number,arg8:number,arg9:number,arg10:number,arg11:number,arg12:number,arg13:number,arg14:number,arg15:number))): 
        - HostNamePrefix (str): 
        - InterfaceIps (list(dict(arg1:str[ipAny | ipv4 | ipv6],arg2:str,arg3:number))): 
        - InterfaceMetric (number): 
        - Ipv6MtMetric (number): 
        - LinkType (str(pointToPoint | broadcast)): 
        - NoOfCols (number): 
        - NoOfRows (number): 
        - RouterId (str): 
        - RouterIdIncrement (str): 
        - TePaths (list(dict(arg1:number,arg2:number,arg3:number,arg4:number,arg5:number,arg6:number,arg7:bool,arg8:str,arg9:number,arg10:number,arg11:number,arg12:number,arg13:number,arg14:number,arg15:number,arg16:number,arg17:number,arg18:number,arg19:number))): 
        - UseWideMetric (bool): 

        Returns
        -------
        - self: This instance with all currently retrieved networkRange resources using find and the newly added networkRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained networkRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EnableHostName=None, Enabled=None, EntryCol=None, EntryRow=None, GridNodeRoutes=None, GridOutsideExLinks=None, GridOutsideLinks=None, HostNamePrefix=None, InterfaceIps=None, InterfaceMetric=None, Ipv6MtMetric=None, LinkType=None, NoOfCols=None, NoOfRows=None, RouterId=None, RouterIdIncrement=None, TePaths=None, UseWideMetric=None):
        """Finds and retrieves networkRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve networkRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all networkRange resources from the server.

        Args
        ----
        - EnableHostName (bool): 
        - Enabled (bool): 
        - EntryCol (number): 
        - EntryRow (number): 
        - GridNodeRoutes (list(dict(arg1:bool,arg2:str[ipAny | ipv4 | ipv6],arg3:str,arg4:number,arg5:number,arg6:number,arg7:number,arg8:bool,arg9:bool,arg10:number))): 
        - GridOutsideExLinks (list(dict(arg1:number,arg2:number,arg3:str,arg4:list[dict(arg1:str[ipAny | ipv4 | ipv6],arg2:str,arg3:number)],arg5:str,arg6:number,arg7:number,arg8:number,arg9:number,arg10:number,arg11:number,arg12:number,arg13:number,arg14:number,arg15:number,arg16:number))): 
        - GridOutsideLinks (list(dict(arg1:number,arg2:number,arg3:str,arg4:str,arg5:number,arg6:number,arg7:number,arg8:number,arg9:number,arg10:number,arg11:number,arg12:number,arg13:number,arg14:number,arg15:number))): 
        - HostNamePrefix (str): 
        - InterfaceIps (list(dict(arg1:str[ipAny | ipv4 | ipv6],arg2:str,arg3:number))): 
        - InterfaceMetric (number): 
        - Ipv6MtMetric (number): 
        - LinkType (str(pointToPoint | broadcast)): 
        - NoOfCols (number): 
        - NoOfRows (number): 
        - RouterId (str): 
        - RouterIdIncrement (str): 
        - TePaths (list(dict(arg1:number,arg2:number,arg3:number,arg4:number,arg5:number,arg6:number,arg7:bool,arg8:str,arg9:number,arg10:number,arg11:number,arg12:number,arg13:number,arg14:number,arg15:number,arg16:number,arg17:number,arg18:number,arg19:number))): 
        - UseWideMetric (bool): 

        Returns
        -------
        - self: This instance with matching networkRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of networkRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the networkRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
