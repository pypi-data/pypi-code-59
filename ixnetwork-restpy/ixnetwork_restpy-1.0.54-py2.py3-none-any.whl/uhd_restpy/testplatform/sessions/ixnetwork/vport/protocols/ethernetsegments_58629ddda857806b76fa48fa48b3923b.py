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


class EthernetSegments(Base):
    """
    The EthernetSegments class encapsulates a list of ethernetSegments resources that are managed by the user.
    A list of resources can be retrieved from the server using the EthernetSegments.find() method.
    The list can be managed by using the EthernetSegments.add() and EthernetSegments.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ethernetSegments'
    _SDM_ATT_MAP = {
        'AutoConfigureEsImport': 'autoConfigureEsImport',
        'BMacPrefix': 'bMacPrefix',
        'BMacPrefixLength': 'bMacPrefixLength',
        'DfElectionMethod': 'dfElectionMethod',
        'DfElectionTimer': 'dfElectionTimer',
        'EnableActiveStandby': 'enableActiveStandby',
        'EnableRootLeaf': 'enableRootLeaf',
        'EnableSecondLabel': 'enableSecondLabel',
        'Enabled': 'enabled',
        'EsImport': 'esImport',
        'Esi': 'esi',
        'EsiLabel': 'esiLabel',
        'FirstLabel': 'firstLabel',
        'IncludeMacMobilityExtendedCommunity': 'includeMacMobilityExtendedCommunity',
        'SecondLabel': 'secondLabel',
        'SupportFastConvergence': 'supportFastConvergence',
        'SupportMultiHomedEsAutoDiscovery': 'supportMultiHomedEsAutoDiscovery',
        'TypeOfEthernetVpn': 'typeOfEthernetVpn',
        'UseSameSequenceNumber': 'useSameSequenceNumber',
    }

    def __init__(self, parent):
        super(EthernetSegments, self).__init__(parent)

    @property
    def AdBmacEsRouteAttributes(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.adbmacesrouteattributes_a27df43ab138bf74c352963245ee6679.AdBmacEsRouteAttributes): An instance of the AdBmacEsRouteAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.adbmacesrouteattributes_a27df43ab138bf74c352963245ee6679 import AdBmacEsRouteAttributes
        return AdBmacEsRouteAttributes(self)._select()

    @property
    def BMacMappedIp(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.bmacmappedip_06e61aa570d306aacd8b1eda4e867608.BMacMappedIp): An instance of the BMacMappedIp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.bmacmappedip_06e61aa570d306aacd8b1eda4e867608 import BMacMappedIp
        return BMacMappedIp(self)

    @property
    def Evi(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.evi_c3b57653c9c7077eb20eb9c9891f849c.Evi): An instance of the Evi class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.evi_c3b57653c9c7077eb20eb9c9891f849c import Evi
        return Evi(self)

    @property
    def AutoConfigureEsImport(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutoConfigureEsImport'])
    @AutoConfigureEsImport.setter
    def AutoConfigureEsImport(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AutoConfigureEsImport'], value)

    @property
    def BMacPrefix(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BMacPrefix'])
    @BMacPrefix.setter
    def BMacPrefix(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BMacPrefix'], value)

    @property
    def BMacPrefixLength(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BMacPrefixLength'])
    @BMacPrefixLength.setter
    def BMacPrefixLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BMacPrefixLength'], value)

    @property
    def DfElectionMethod(self):
        """
        Returns
        -------
        - str(serviceCarving): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DfElectionMethod'])
    @DfElectionMethod.setter
    def DfElectionMethod(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DfElectionMethod'], value)

    @property
    def DfElectionTimer(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DfElectionTimer'])
    @DfElectionTimer.setter
    def DfElectionTimer(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DfElectionTimer'], value)

    @property
    def EnableActiveStandby(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableActiveStandby'])
    @EnableActiveStandby.setter
    def EnableActiveStandby(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableActiveStandby'], value)

    @property
    def EnableRootLeaf(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableRootLeaf'])
    @EnableRootLeaf.setter
    def EnableRootLeaf(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableRootLeaf'], value)

    @property
    def EnableSecondLabel(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSecondLabel'])
    @EnableSecondLabel.setter
    def EnableSecondLabel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSecondLabel'], value)

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
    def EsImport(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EsImport'])
    @EsImport.setter
    def EsImport(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EsImport'], value)

    @property
    def Esi(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Esi'])
    @Esi.setter
    def Esi(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Esi'], value)

    @property
    def EsiLabel(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EsiLabel'])
    @EsiLabel.setter
    def EsiLabel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EsiLabel'], value)

    @property
    def FirstLabel(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FirstLabel'])
    @FirstLabel.setter
    def FirstLabel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FirstLabel'], value)

    @property
    def IncludeMacMobilityExtendedCommunity(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeMacMobilityExtendedCommunity'])
    @IncludeMacMobilityExtendedCommunity.setter
    def IncludeMacMobilityExtendedCommunity(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeMacMobilityExtendedCommunity'], value)

    @property
    def SecondLabel(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SecondLabel'])
    @SecondLabel.setter
    def SecondLabel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SecondLabel'], value)

    @property
    def SupportFastConvergence(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportFastConvergence'])
    @SupportFastConvergence.setter
    def SupportFastConvergence(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportFastConvergence'], value)

    @property
    def SupportMultiHomedEsAutoDiscovery(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportMultiHomedEsAutoDiscovery'])
    @SupportMultiHomedEsAutoDiscovery.setter
    def SupportMultiHomedEsAutoDiscovery(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportMultiHomedEsAutoDiscovery'], value)

    @property
    def TypeOfEthernetVpn(self):
        """
        Returns
        -------
        - str(evpn | pbbEvpn): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TypeOfEthernetVpn'])
    @TypeOfEthernetVpn.setter
    def TypeOfEthernetVpn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TypeOfEthernetVpn'], value)

    @property
    def UseSameSequenceNumber(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseSameSequenceNumber'])
    @UseSameSequenceNumber.setter
    def UseSameSequenceNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseSameSequenceNumber'], value)

    def update(self, AutoConfigureEsImport=None, BMacPrefix=None, BMacPrefixLength=None, DfElectionMethod=None, DfElectionTimer=None, EnableActiveStandby=None, EnableRootLeaf=None, EnableSecondLabel=None, Enabled=None, EsImport=None, Esi=None, EsiLabel=None, FirstLabel=None, IncludeMacMobilityExtendedCommunity=None, SecondLabel=None, SupportFastConvergence=None, SupportMultiHomedEsAutoDiscovery=None, TypeOfEthernetVpn=None, UseSameSequenceNumber=None):
        """Updates ethernetSegments resource on the server.

        Args
        ----
        - AutoConfigureEsImport (bool): 
        - BMacPrefix (str): 
        - BMacPrefixLength (number): 
        - DfElectionMethod (str(serviceCarving)): 
        - DfElectionTimer (number): 
        - EnableActiveStandby (bool): 
        - EnableRootLeaf (bool): 
        - EnableSecondLabel (bool): 
        - Enabled (bool): 
        - EsImport (str): 
        - Esi (str): 
        - EsiLabel (number): 
        - FirstLabel (number): 
        - IncludeMacMobilityExtendedCommunity (bool): 
        - SecondLabel (number): 
        - SupportFastConvergence (bool): 
        - SupportMultiHomedEsAutoDiscovery (bool): 
        - TypeOfEthernetVpn (str(evpn | pbbEvpn)): 
        - UseSameSequenceNumber (bool): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AutoConfigureEsImport=None, BMacPrefix=None, BMacPrefixLength=None, DfElectionMethod=None, DfElectionTimer=None, EnableActiveStandby=None, EnableRootLeaf=None, EnableSecondLabel=None, Enabled=None, EsImport=None, Esi=None, EsiLabel=None, FirstLabel=None, IncludeMacMobilityExtendedCommunity=None, SecondLabel=None, SupportFastConvergence=None, SupportMultiHomedEsAutoDiscovery=None, TypeOfEthernetVpn=None, UseSameSequenceNumber=None):
        """Adds a new ethernetSegments resource on the server and adds it to the container.

        Args
        ----
        - AutoConfigureEsImport (bool): 
        - BMacPrefix (str): 
        - BMacPrefixLength (number): 
        - DfElectionMethod (str(serviceCarving)): 
        - DfElectionTimer (number): 
        - EnableActiveStandby (bool): 
        - EnableRootLeaf (bool): 
        - EnableSecondLabel (bool): 
        - Enabled (bool): 
        - EsImport (str): 
        - Esi (str): 
        - EsiLabel (number): 
        - FirstLabel (number): 
        - IncludeMacMobilityExtendedCommunity (bool): 
        - SecondLabel (number): 
        - SupportFastConvergence (bool): 
        - SupportMultiHomedEsAutoDiscovery (bool): 
        - TypeOfEthernetVpn (str(evpn | pbbEvpn)): 
        - UseSameSequenceNumber (bool): 

        Returns
        -------
        - self: This instance with all currently retrieved ethernetSegments resources using find and the newly added ethernetSegments resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ethernetSegments resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AutoConfigureEsImport=None, BMacPrefix=None, BMacPrefixLength=None, DfElectionMethod=None, DfElectionTimer=None, EnableActiveStandby=None, EnableRootLeaf=None, EnableSecondLabel=None, Enabled=None, EsImport=None, Esi=None, EsiLabel=None, FirstLabel=None, IncludeMacMobilityExtendedCommunity=None, SecondLabel=None, SupportFastConvergence=None, SupportMultiHomedEsAutoDiscovery=None, TypeOfEthernetVpn=None, UseSameSequenceNumber=None):
        """Finds and retrieves ethernetSegments resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ethernetSegments resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ethernetSegments resources from the server.

        Args
        ----
        - AutoConfigureEsImport (bool): 
        - BMacPrefix (str): 
        - BMacPrefixLength (number): 
        - DfElectionMethod (str(serviceCarving)): 
        - DfElectionTimer (number): 
        - EnableActiveStandby (bool): 
        - EnableRootLeaf (bool): 
        - EnableSecondLabel (bool): 
        - Enabled (bool): 
        - EsImport (str): 
        - Esi (str): 
        - EsiLabel (number): 
        - FirstLabel (number): 
        - IncludeMacMobilityExtendedCommunity (bool): 
        - SecondLabel (number): 
        - SupportFastConvergence (bool): 
        - SupportMultiHomedEsAutoDiscovery (bool): 
        - TypeOfEthernetVpn (str(evpn | pbbEvpn)): 
        - UseSameSequenceNumber (bool): 

        Returns
        -------
        - self: This instance with matching ethernetSegments resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ethernetSegments data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ethernetSegments resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def FlushRemoteCmacForwardingTable(self):
        """Executes the flushRemoteCmacForwardingTable operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('flushRemoteCmacForwardingTable', payload=payload, response_object=None)
