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


class UmhSelectionRouteRange(Base):
    """
    The UmhSelectionRouteRange class encapsulates a list of umhSelectionRouteRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the UmhSelectionRouteRange.find() method.
    The list can be managed by using the UmhSelectionRouteRange.add() and UmhSelectionRouteRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'umhSelectionRouteRange'
    _SDM_ATT_MAP = {
        'AggregatorAsNumber': 'aggregatorAsNumber',
        'AggregatorIdIncrementMode': 'aggregatorIdIncrementMode',
        'AggregatorIpAddress': 'aggregatorIpAddress',
        'DistinguisherAsNumber': 'distinguisherAsNumber',
        'DistinguisherAsNumberStep': 'distinguisherAsNumberStep',
        'DistinguisherAsNumberStepAcrossVrfs': 'distinguisherAsNumberStepAcrossVrfs',
        'DistinguisherAssignedNumber': 'distinguisherAssignedNumber',
        'DistinguisherAssignedNumberStep': 'distinguisherAssignedNumberStep',
        'DistinguisherAssignedNumberStepAcrossVrfs': 'distinguisherAssignedNumberStepAcrossVrfs',
        'DistinguisherCount': 'distinguisherCount',
        'DistinguisherCountPerVrf': 'distinguisherCountPerVrf',
        'DistinguisherIpAddress': 'distinguisherIpAddress',
        'DistinguisherIpAddressStep': 'distinguisherIpAddressStep',
        'DistinguisherIpAddressStepAcrossVrfs': 'distinguisherIpAddressStepAcrossVrfs',
        'DistinguisherMode': 'distinguisherMode',
        'DistinguisherStep': 'distinguisherStep',
        'DistinguisherType': 'distinguisherType',
        'EnableAggregator': 'enableAggregator',
        'EnableAsPath': 'enableAsPath',
        'EnableAtomicAggregator': 'enableAtomicAggregator',
        'EnableCluster': 'enableCluster',
        'EnableCommunity': 'enableCommunity',
        'EnableGenerateUniqueRoutes': 'enableGenerateUniqueRoutes',
        'EnableLocalPref': 'enableLocalPref',
        'EnableMed': 'enableMed',
        'EnableNextHop': 'enableNextHop',
        'EnableOrigin': 'enableOrigin',
        'EnableOriginator': 'enableOriginator',
        'EnableUseTraditionalNlri': 'enableUseTraditionalNlri',
        'Enabled': 'enabled',
        'FirstRoute': 'firstRoute',
        'IncludeSourceAsExtendedCommunityPresent': 'includeSourceAsExtendedCommunityPresent',
        'IncludeVrfRouteImportExtendedCommunityPresent': 'includeVrfRouteImportExtendedCommunityPresent',
        'IpType': 'ipType',
        'LocalPref': 'localPref',
        'MaskWidth': 'maskWidth',
        'MaskWidthTo': 'maskWidthTo',
        'Med': 'med',
        'NextHopIpAddress': 'nextHopIpAddress',
        'NextHopMode': 'nextHopMode',
        'NextHopSetMode': 'nextHopSetMode',
        'OriginProtocol': 'originProtocol',
        'OriginatorId': 'originatorId',
        'PackingFrom': 'packingFrom',
        'PackingTo': 'packingTo',
        'RouteCountPerVrfs': 'routeCountPerVrfs',
        'RouteStepAcrossVrfs': 'routeStepAcrossVrfs',
        'Step': 'step',
    }

    def __init__(self, parent):
        super(UmhSelectionRouteRange, self).__init__(parent)

    @property
    def AsSegment(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.assegment_77023b63251dc6667bdf6c21a3e43b82.AsSegment): An instance of the AsSegment class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.assegment_77023b63251dc6667bdf6c21a3e43b82 import AsSegment
        return AsSegment(self)._select()

    @property
    def Cluster(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.cluster_d68b61bb2cd5e48de06e56c1bb4b9cfb.Cluster): An instance of the Cluster class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.cluster_d68b61bb2cd5e48de06e56c1bb4b9cfb import Cluster
        return Cluster(self)._select()

    @property
    def Community(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.community_46f6c2c27e8a80b9e728ca3a28276bc2.Community): An instance of the Community class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.community_46f6c2c27e8a80b9e728ca3a28276bc2 import Community
        return Community(self)._select()

    @property
    def ExtendedCommunity(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.extendedcommunity_9dbd9a94c067c10769a25642ca9a2116.ExtendedCommunity): An instance of the ExtendedCommunity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.extendedcommunity_9dbd9a94c067c10769a25642ca9a2116 import ExtendedCommunity
        return ExtendedCommunity(self)._select()

    @property
    def Flapping(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.flapping_14ce629a4dbc4bd9b20c8fe1dc2a1e04.Flapping): An instance of the Flapping class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.flapping_14ce629a4dbc4bd9b20c8fe1dc2a1e04 import Flapping
        return Flapping(self)._select()

    @property
    def LabelSpace(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.labelspace_6d08c054aa4a79300972f72fa46e7edd.LabelSpace): An instance of the LabelSpace class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.labelspace_6d08c054aa4a79300972f72fa46e7edd import LabelSpace
        return LabelSpace(self)._select()

    @property
    def AggregatorAsNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AggregatorAsNumber'])
    @AggregatorAsNumber.setter
    def AggregatorAsNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AggregatorAsNumber'], value)

    @property
    def AggregatorIdIncrementMode(self):
        """
        Returns
        -------
        - str(fixed | increment): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AggregatorIdIncrementMode'])
    @AggregatorIdIncrementMode.setter
    def AggregatorIdIncrementMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AggregatorIdIncrementMode'], value)

    @property
    def AggregatorIpAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AggregatorIpAddress'])
    @AggregatorIpAddress.setter
    def AggregatorIpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AggregatorIpAddress'], value)

    @property
    def DistinguisherAsNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DistinguisherAsNumber'])
    @DistinguisherAsNumber.setter
    def DistinguisherAsNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DistinguisherAsNumber'], value)

    @property
    def DistinguisherAsNumberStep(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DistinguisherAsNumberStep'])
    @DistinguisherAsNumberStep.setter
    def DistinguisherAsNumberStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DistinguisherAsNumberStep'], value)

    @property
    def DistinguisherAsNumberStepAcrossVrfs(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DistinguisherAsNumberStepAcrossVrfs'])
    @DistinguisherAsNumberStepAcrossVrfs.setter
    def DistinguisherAsNumberStepAcrossVrfs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DistinguisherAsNumberStepAcrossVrfs'], value)

    @property
    def DistinguisherAssignedNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DistinguisherAssignedNumber'])
    @DistinguisherAssignedNumber.setter
    def DistinguisherAssignedNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DistinguisherAssignedNumber'], value)

    @property
    def DistinguisherAssignedNumberStep(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DistinguisherAssignedNumberStep'])
    @DistinguisherAssignedNumberStep.setter
    def DistinguisherAssignedNumberStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DistinguisherAssignedNumberStep'], value)

    @property
    def DistinguisherAssignedNumberStepAcrossVrfs(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DistinguisherAssignedNumberStepAcrossVrfs'])
    @DistinguisherAssignedNumberStepAcrossVrfs.setter
    def DistinguisherAssignedNumberStepAcrossVrfs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DistinguisherAssignedNumberStepAcrossVrfs'], value)

    @property
    def DistinguisherCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DistinguisherCount'])
    @DistinguisherCount.setter
    def DistinguisherCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DistinguisherCount'], value)

    @property
    def DistinguisherCountPerVrf(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DistinguisherCountPerVrf'])
    @DistinguisherCountPerVrf.setter
    def DistinguisherCountPerVrf(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DistinguisherCountPerVrf'], value)

    @property
    def DistinguisherIpAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DistinguisherIpAddress'])
    @DistinguisherIpAddress.setter
    def DistinguisherIpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DistinguisherIpAddress'], value)

    @property
    def DistinguisherIpAddressStep(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DistinguisherIpAddressStep'])
    @DistinguisherIpAddressStep.setter
    def DistinguisherIpAddressStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DistinguisherIpAddressStep'], value)

    @property
    def DistinguisherIpAddressStepAcrossVrfs(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DistinguisherIpAddressStepAcrossVrfs'])
    @DistinguisherIpAddressStepAcrossVrfs.setter
    def DistinguisherIpAddressStepAcrossVrfs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DistinguisherIpAddressStepAcrossVrfs'], value)

    @property
    def DistinguisherMode(self):
        """
        Returns
        -------
        - str(global | local): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DistinguisherMode'])
    @DistinguisherMode.setter
    def DistinguisherMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DistinguisherMode'], value)

    @property
    def DistinguisherStep(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DistinguisherStep'])
    @DistinguisherStep.setter
    def DistinguisherStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DistinguisherStep'], value)

    @property
    def DistinguisherType(self):
        """
        Returns
        -------
        - str(as | ip | asNumber2): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DistinguisherType'])
    @DistinguisherType.setter
    def DistinguisherType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DistinguisherType'], value)

    @property
    def EnableAggregator(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAggregator'])
    @EnableAggregator.setter
    def EnableAggregator(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAggregator'], value)

    @property
    def EnableAsPath(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAsPath'])
    @EnableAsPath.setter
    def EnableAsPath(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAsPath'], value)

    @property
    def EnableAtomicAggregator(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAtomicAggregator'])
    @EnableAtomicAggregator.setter
    def EnableAtomicAggregator(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAtomicAggregator'], value)

    @property
    def EnableCluster(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableCluster'])
    @EnableCluster.setter
    def EnableCluster(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableCluster'], value)

    @property
    def EnableCommunity(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableCommunity'])
    @EnableCommunity.setter
    def EnableCommunity(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableCommunity'], value)

    @property
    def EnableGenerateUniqueRoutes(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableGenerateUniqueRoutes'])
    @EnableGenerateUniqueRoutes.setter
    def EnableGenerateUniqueRoutes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableGenerateUniqueRoutes'], value)

    @property
    def EnableLocalPref(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLocalPref'])
    @EnableLocalPref.setter
    def EnableLocalPref(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLocalPref'], value)

    @property
    def EnableMed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMed'])
    @EnableMed.setter
    def EnableMed(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMed'], value)

    @property
    def EnableNextHop(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableNextHop'])
    @EnableNextHop.setter
    def EnableNextHop(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableNextHop'], value)

    @property
    def EnableOrigin(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableOrigin'])
    @EnableOrigin.setter
    def EnableOrigin(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableOrigin'], value)

    @property
    def EnableOriginator(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableOriginator'])
    @EnableOriginator.setter
    def EnableOriginator(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableOriginator'], value)

    @property
    def EnableUseTraditionalNlri(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableUseTraditionalNlri'])
    @EnableUseTraditionalNlri.setter
    def EnableUseTraditionalNlri(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableUseTraditionalNlri'], value)

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
    def IncludeSourceAsExtendedCommunityPresent(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeSourceAsExtendedCommunityPresent'])
    @IncludeSourceAsExtendedCommunityPresent.setter
    def IncludeSourceAsExtendedCommunityPresent(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeSourceAsExtendedCommunityPresent'], value)

    @property
    def IncludeVrfRouteImportExtendedCommunityPresent(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeVrfRouteImportExtendedCommunityPresent'])
    @IncludeVrfRouteImportExtendedCommunityPresent.setter
    def IncludeVrfRouteImportExtendedCommunityPresent(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeVrfRouteImportExtendedCommunityPresent'], value)

    @property
    def IpType(self):
        """
        Returns
        -------
        - str(ipAny | ipv4 | ipv6): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpType'])
    @IpType.setter
    def IpType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpType'], value)

    @property
    def LocalPref(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalPref'])
    @LocalPref.setter
    def LocalPref(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LocalPref'], value)

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
    def MaskWidthTo(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaskWidthTo'])
    @MaskWidthTo.setter
    def MaskWidthTo(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaskWidthTo'], value)

    @property
    def Med(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Med'])
    @Med.setter
    def Med(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Med'], value)

    @property
    def NextHopIpAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextHopIpAddress'])
    @NextHopIpAddress.setter
    def NextHopIpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NextHopIpAddress'], value)

    @property
    def NextHopMode(self):
        """
        Returns
        -------
        - str(nextHopIncrement | fixed | incrementPerPrefix): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextHopMode'])
    @NextHopMode.setter
    def NextHopMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NextHopMode'], value)

    @property
    def NextHopSetMode(self):
        """
        Returns
        -------
        - str(sameAsLocalIp | setManually): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextHopSetMode'])
    @NextHopSetMode.setter
    def NextHopSetMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NextHopSetMode'], value)

    @property
    def OriginProtocol(self):
        """
        Returns
        -------
        - str(igp | egp | incomplete): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OriginProtocol'])
    @OriginProtocol.setter
    def OriginProtocol(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OriginProtocol'], value)

    @property
    def OriginatorId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OriginatorId'])
    @OriginatorId.setter
    def OriginatorId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OriginatorId'], value)

    @property
    def PackingFrom(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PackingFrom'])
    @PackingFrom.setter
    def PackingFrom(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PackingFrom'], value)

    @property
    def PackingTo(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PackingTo'])
    @PackingTo.setter
    def PackingTo(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PackingTo'], value)

    @property
    def RouteCountPerVrfs(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteCountPerVrfs'])
    @RouteCountPerVrfs.setter
    def RouteCountPerVrfs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouteCountPerVrfs'], value)

    @property
    def RouteStepAcrossVrfs(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteStepAcrossVrfs'])
    @RouteStepAcrossVrfs.setter
    def RouteStepAcrossVrfs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouteStepAcrossVrfs'], value)

    @property
    def Step(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step'])
    @Step.setter
    def Step(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step'], value)

    def update(self, AggregatorAsNumber=None, AggregatorIdIncrementMode=None, AggregatorIpAddress=None, DistinguisherAsNumber=None, DistinguisherAsNumberStep=None, DistinguisherAsNumberStepAcrossVrfs=None, DistinguisherAssignedNumber=None, DistinguisherAssignedNumberStep=None, DistinguisherAssignedNumberStepAcrossVrfs=None, DistinguisherCount=None, DistinguisherCountPerVrf=None, DistinguisherIpAddress=None, DistinguisherIpAddressStep=None, DistinguisherIpAddressStepAcrossVrfs=None, DistinguisherMode=None, DistinguisherStep=None, DistinguisherType=None, EnableAggregator=None, EnableAsPath=None, EnableAtomicAggregator=None, EnableCluster=None, EnableCommunity=None, EnableGenerateUniqueRoutes=None, EnableLocalPref=None, EnableMed=None, EnableNextHop=None, EnableOrigin=None, EnableOriginator=None, EnableUseTraditionalNlri=None, Enabled=None, FirstRoute=None, IncludeSourceAsExtendedCommunityPresent=None, IncludeVrfRouteImportExtendedCommunityPresent=None, IpType=None, LocalPref=None, MaskWidth=None, MaskWidthTo=None, Med=None, NextHopIpAddress=None, NextHopMode=None, NextHopSetMode=None, OriginProtocol=None, OriginatorId=None, PackingFrom=None, PackingTo=None, RouteCountPerVrfs=None, RouteStepAcrossVrfs=None, Step=None):
        """Updates umhSelectionRouteRange resource on the server.

        Args
        ----
        - AggregatorAsNumber (number): 
        - AggregatorIdIncrementMode (str(fixed | increment)): 
        - AggregatorIpAddress (str): 
        - DistinguisherAsNumber (number): 
        - DistinguisherAsNumberStep (number): 
        - DistinguisherAsNumberStepAcrossVrfs (number): 
        - DistinguisherAssignedNumber (number): 
        - DistinguisherAssignedNumberStep (number): 
        - DistinguisherAssignedNumberStepAcrossVrfs (number): 
        - DistinguisherCount (number): 
        - DistinguisherCountPerVrf (number): 
        - DistinguisherIpAddress (str): 
        - DistinguisherIpAddressStep (str): 
        - DistinguisherIpAddressStepAcrossVrfs (str): 
        - DistinguisherMode (str(global | local)): 
        - DistinguisherStep (number): 
        - DistinguisherType (str(as | ip | asNumber2)): 
        - EnableAggregator (bool): 
        - EnableAsPath (bool): 
        - EnableAtomicAggregator (bool): 
        - EnableCluster (bool): 
        - EnableCommunity (bool): 
        - EnableGenerateUniqueRoutes (bool): 
        - EnableLocalPref (bool): 
        - EnableMed (bool): 
        - EnableNextHop (bool): 
        - EnableOrigin (bool): 
        - EnableOriginator (bool): 
        - EnableUseTraditionalNlri (bool): 
        - Enabled (bool): 
        - FirstRoute (str): 
        - IncludeSourceAsExtendedCommunityPresent (bool): 
        - IncludeVrfRouteImportExtendedCommunityPresent (bool): 
        - IpType (str(ipAny | ipv4 | ipv6)): 
        - LocalPref (number): 
        - MaskWidth (number): 
        - MaskWidthTo (number): 
        - Med (number): 
        - NextHopIpAddress (str): 
        - NextHopMode (str(nextHopIncrement | fixed | incrementPerPrefix)): 
        - NextHopSetMode (str(sameAsLocalIp | setManually)): 
        - OriginProtocol (str(igp | egp | incomplete)): 
        - OriginatorId (str): 
        - PackingFrom (number): 
        - PackingTo (number): 
        - RouteCountPerVrfs (number): 
        - RouteStepAcrossVrfs (str): 
        - Step (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AggregatorAsNumber=None, AggregatorIdIncrementMode=None, AggregatorIpAddress=None, DistinguisherAsNumber=None, DistinguisherAsNumberStep=None, DistinguisherAsNumberStepAcrossVrfs=None, DistinguisherAssignedNumber=None, DistinguisherAssignedNumberStep=None, DistinguisherAssignedNumberStepAcrossVrfs=None, DistinguisherCount=None, DistinguisherCountPerVrf=None, DistinguisherIpAddress=None, DistinguisherIpAddressStep=None, DistinguisherIpAddressStepAcrossVrfs=None, DistinguisherMode=None, DistinguisherStep=None, DistinguisherType=None, EnableAggregator=None, EnableAsPath=None, EnableAtomicAggregator=None, EnableCluster=None, EnableCommunity=None, EnableGenerateUniqueRoutes=None, EnableLocalPref=None, EnableMed=None, EnableNextHop=None, EnableOrigin=None, EnableOriginator=None, EnableUseTraditionalNlri=None, Enabled=None, FirstRoute=None, IncludeSourceAsExtendedCommunityPresent=None, IncludeVrfRouteImportExtendedCommunityPresent=None, IpType=None, LocalPref=None, MaskWidth=None, MaskWidthTo=None, Med=None, NextHopIpAddress=None, NextHopMode=None, NextHopSetMode=None, OriginProtocol=None, OriginatorId=None, PackingFrom=None, PackingTo=None, RouteCountPerVrfs=None, RouteStepAcrossVrfs=None, Step=None):
        """Adds a new umhSelectionRouteRange resource on the server and adds it to the container.

        Args
        ----
        - AggregatorAsNumber (number): 
        - AggregatorIdIncrementMode (str(fixed | increment)): 
        - AggregatorIpAddress (str): 
        - DistinguisherAsNumber (number): 
        - DistinguisherAsNumberStep (number): 
        - DistinguisherAsNumberStepAcrossVrfs (number): 
        - DistinguisherAssignedNumber (number): 
        - DistinguisherAssignedNumberStep (number): 
        - DistinguisherAssignedNumberStepAcrossVrfs (number): 
        - DistinguisherCount (number): 
        - DistinguisherCountPerVrf (number): 
        - DistinguisherIpAddress (str): 
        - DistinguisherIpAddressStep (str): 
        - DistinguisherIpAddressStepAcrossVrfs (str): 
        - DistinguisherMode (str(global | local)): 
        - DistinguisherStep (number): 
        - DistinguisherType (str(as | ip | asNumber2)): 
        - EnableAggregator (bool): 
        - EnableAsPath (bool): 
        - EnableAtomicAggregator (bool): 
        - EnableCluster (bool): 
        - EnableCommunity (bool): 
        - EnableGenerateUniqueRoutes (bool): 
        - EnableLocalPref (bool): 
        - EnableMed (bool): 
        - EnableNextHop (bool): 
        - EnableOrigin (bool): 
        - EnableOriginator (bool): 
        - EnableUseTraditionalNlri (bool): 
        - Enabled (bool): 
        - FirstRoute (str): 
        - IncludeSourceAsExtendedCommunityPresent (bool): 
        - IncludeVrfRouteImportExtendedCommunityPresent (bool): 
        - IpType (str(ipAny | ipv4 | ipv6)): 
        - LocalPref (number): 
        - MaskWidth (number): 
        - MaskWidthTo (number): 
        - Med (number): 
        - NextHopIpAddress (str): 
        - NextHopMode (str(nextHopIncrement | fixed | incrementPerPrefix)): 
        - NextHopSetMode (str(sameAsLocalIp | setManually)): 
        - OriginProtocol (str(igp | egp | incomplete)): 
        - OriginatorId (str): 
        - PackingFrom (number): 
        - PackingTo (number): 
        - RouteCountPerVrfs (number): 
        - RouteStepAcrossVrfs (str): 
        - Step (number): 

        Returns
        -------
        - self: This instance with all currently retrieved umhSelectionRouteRange resources using find and the newly added umhSelectionRouteRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained umhSelectionRouteRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AggregatorAsNumber=None, AggregatorIdIncrementMode=None, AggregatorIpAddress=None, DistinguisherAsNumber=None, DistinguisherAsNumberStep=None, DistinguisherAsNumberStepAcrossVrfs=None, DistinguisherAssignedNumber=None, DistinguisherAssignedNumberStep=None, DistinguisherAssignedNumberStepAcrossVrfs=None, DistinguisherCount=None, DistinguisherCountPerVrf=None, DistinguisherIpAddress=None, DistinguisherIpAddressStep=None, DistinguisherIpAddressStepAcrossVrfs=None, DistinguisherMode=None, DistinguisherStep=None, DistinguisherType=None, EnableAggregator=None, EnableAsPath=None, EnableAtomicAggregator=None, EnableCluster=None, EnableCommunity=None, EnableGenerateUniqueRoutes=None, EnableLocalPref=None, EnableMed=None, EnableNextHop=None, EnableOrigin=None, EnableOriginator=None, EnableUseTraditionalNlri=None, Enabled=None, FirstRoute=None, IncludeSourceAsExtendedCommunityPresent=None, IncludeVrfRouteImportExtendedCommunityPresent=None, IpType=None, LocalPref=None, MaskWidth=None, MaskWidthTo=None, Med=None, NextHopIpAddress=None, NextHopMode=None, NextHopSetMode=None, OriginProtocol=None, OriginatorId=None, PackingFrom=None, PackingTo=None, RouteCountPerVrfs=None, RouteStepAcrossVrfs=None, Step=None):
        """Finds and retrieves umhSelectionRouteRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve umhSelectionRouteRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all umhSelectionRouteRange resources from the server.

        Args
        ----
        - AggregatorAsNumber (number): 
        - AggregatorIdIncrementMode (str(fixed | increment)): 
        - AggregatorIpAddress (str): 
        - DistinguisherAsNumber (number): 
        - DistinguisherAsNumberStep (number): 
        - DistinguisherAsNumberStepAcrossVrfs (number): 
        - DistinguisherAssignedNumber (number): 
        - DistinguisherAssignedNumberStep (number): 
        - DistinguisherAssignedNumberStepAcrossVrfs (number): 
        - DistinguisherCount (number): 
        - DistinguisherCountPerVrf (number): 
        - DistinguisherIpAddress (str): 
        - DistinguisherIpAddressStep (str): 
        - DistinguisherIpAddressStepAcrossVrfs (str): 
        - DistinguisherMode (str(global | local)): 
        - DistinguisherStep (number): 
        - DistinguisherType (str(as | ip | asNumber2)): 
        - EnableAggregator (bool): 
        - EnableAsPath (bool): 
        - EnableAtomicAggregator (bool): 
        - EnableCluster (bool): 
        - EnableCommunity (bool): 
        - EnableGenerateUniqueRoutes (bool): 
        - EnableLocalPref (bool): 
        - EnableMed (bool): 
        - EnableNextHop (bool): 
        - EnableOrigin (bool): 
        - EnableOriginator (bool): 
        - EnableUseTraditionalNlri (bool): 
        - Enabled (bool): 
        - FirstRoute (str): 
        - IncludeSourceAsExtendedCommunityPresent (bool): 
        - IncludeVrfRouteImportExtendedCommunityPresent (bool): 
        - IpType (str(ipAny | ipv4 | ipv6)): 
        - LocalPref (number): 
        - MaskWidth (number): 
        - MaskWidthTo (number): 
        - Med (number): 
        - NextHopIpAddress (str): 
        - NextHopMode (str(nextHopIncrement | fixed | incrementPerPrefix)): 
        - NextHopSetMode (str(sameAsLocalIp | setManually)): 
        - OriginProtocol (str(igp | egp | incomplete)): 
        - OriginatorId (str): 
        - PackingFrom (number): 
        - PackingTo (number): 
        - RouteCountPerVrfs (number): 
        - RouteStepAcrossVrfs (str): 
        - Step (number): 

        Returns
        -------
        - self: This instance with matching umhSelectionRouteRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of umhSelectionRouteRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the umhSelectionRouteRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
