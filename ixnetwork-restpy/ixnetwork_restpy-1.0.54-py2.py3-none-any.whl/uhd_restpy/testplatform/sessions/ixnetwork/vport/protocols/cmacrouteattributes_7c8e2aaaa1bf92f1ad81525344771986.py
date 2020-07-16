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


class CmacRouteAttributes(Base):
    """
    The CmacRouteAttributes class encapsulates a required cmacRouteAttributes resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'cmacRouteAttributes'
    _SDM_ATT_MAP = {
        'AggregatorAs': 'aggregatorAs',
        'AggregatorId': 'aggregatorId',
        'AsPath': 'asPath',
        'AsSetMode': 'asSetMode',
        'Cluster': 'cluster',
        'Community': 'community',
        'EnableAggregator': 'enableAggregator',
        'EnableAsPath': 'enableAsPath',
        'EnableAtomicAggregate': 'enableAtomicAggregate',
        'EnableCluster': 'enableCluster',
        'EnableCommunity': 'enableCommunity',
        'EnableLocalPref': 'enableLocalPref',
        'EnableMultiExit': 'enableMultiExit',
        'EnableNextHop': 'enableNextHop',
        'EnableOrigin': 'enableOrigin',
        'EnableOriginator': 'enableOriginator',
        'ExtendedCommunity': 'extendedCommunity',
        'LocalPref': 'localPref',
        'MultiExit': 'multiExit',
        'NextHop': 'nextHop',
        'NextHopIpType': 'nextHopIpType',
        'NextHopMode': 'nextHopMode',
        'Origin': 'origin',
        'OriginatorId': 'originatorId',
        'SetNextHop': 'setNextHop',
    }

    def __init__(self, parent):
        super(CmacRouteAttributes, self).__init__(parent)

    @property
    def AggregatorAs(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AggregatorAs'])
    @AggregatorAs.setter
    def AggregatorAs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AggregatorAs'], value)

    @property
    def AggregatorId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AggregatorId'])
    @AggregatorId.setter
    def AggregatorId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AggregatorId'], value)

    @property
    def AsPath(self):
        """
        Returns
        -------
        - list(dict(arg1:bool,arg2:str[unknown | asSet | asSequence | asConfedSet | asConfedSequence],arg3:list[number])): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AsPath'])
    @AsPath.setter
    def AsPath(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AsPath'], value)

    @property
    def AsSetMode(self):
        """
        Returns
        -------
        - str(includeAsSeq | includeAsSeqConf | includeAsSet | includeAsSetConf | noInclude | prependAs): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AsSetMode'])
    @AsSetMode.setter
    def AsSetMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AsSetMode'], value)

    @property
    def Cluster(self):
        """
        Returns
        -------
        - list(number): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Cluster'])
    @Cluster.setter
    def Cluster(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Cluster'], value)

    @property
    def Community(self):
        """
        Returns
        -------
        - list(number): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Community'])
    @Community.setter
    def Community(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Community'], value)

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
    def EnableAtomicAggregate(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAtomicAggregate'])
    @EnableAtomicAggregate.setter
    def EnableAtomicAggregate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAtomicAggregate'], value)

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
    def EnableMultiExit(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMultiExit'])
    @EnableMultiExit.setter
    def EnableMultiExit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMultiExit'], value)

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
    def ExtendedCommunity(self):
        """
        Returns
        -------
        - list(dict(arg1:str[decimal | hex | ip | ieeeFloat],arg2:str[decimal | hex | ip | ieeeFloat],arg3:str[twoOctetAs | ip | fourOctetAs | opaque | administratorAsTwoOctetLinkBw],arg4:str[routeTarget | origin | extendedBandwidthSubType],arg5:str)): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExtendedCommunity'])
    @ExtendedCommunity.setter
    def ExtendedCommunity(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExtendedCommunity'], value)

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
    def MultiExit(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MultiExit'])
    @MultiExit.setter
    def MultiExit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MultiExit'], value)

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
    def NextHopIpType(self):
        """
        Returns
        -------
        - str(ipv4 | ipv6): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextHopIpType'])
    @NextHopIpType.setter
    def NextHopIpType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NextHopIpType'], value)

    @property
    def NextHopMode(self):
        """
        Returns
        -------
        - str(fixed | incrementPerPeer): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextHopMode'])
    @NextHopMode.setter
    def NextHopMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NextHopMode'], value)

    @property
    def Origin(self):
        """
        Returns
        -------
        - str(igp | egp | incomplete): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Origin'])
    @Origin.setter
    def Origin(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Origin'], value)

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
    def SetNextHop(self):
        """
        Returns
        -------
        - str(manually | sameAsLocalIp): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetNextHop'])
    @SetNextHop.setter
    def SetNextHop(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetNextHop'], value)

    def update(self, AggregatorAs=None, AggregatorId=None, AsPath=None, AsSetMode=None, Cluster=None, Community=None, EnableAggregator=None, EnableAsPath=None, EnableAtomicAggregate=None, EnableCluster=None, EnableCommunity=None, EnableLocalPref=None, EnableMultiExit=None, EnableNextHop=None, EnableOrigin=None, EnableOriginator=None, ExtendedCommunity=None, LocalPref=None, MultiExit=None, NextHop=None, NextHopIpType=None, NextHopMode=None, Origin=None, OriginatorId=None, SetNextHop=None):
        """Updates cmacRouteAttributes resource on the server.

        Args
        ----
        - AggregatorAs (number): 
        - AggregatorId (str): 
        - AsPath (list(dict(arg1:bool,arg2:str[unknown | asSet | asSequence | asConfedSet | asConfedSequence],arg3:list[number]))): 
        - AsSetMode (str(includeAsSeq | includeAsSeqConf | includeAsSet | includeAsSetConf | noInclude | prependAs)): 
        - Cluster (list(number)): 
        - Community (list(number)): 
        - EnableAggregator (bool): 
        - EnableAsPath (bool): 
        - EnableAtomicAggregate (bool): 
        - EnableCluster (bool): 
        - EnableCommunity (bool): 
        - EnableLocalPref (bool): 
        - EnableMultiExit (bool): 
        - EnableNextHop (bool): 
        - EnableOrigin (bool): 
        - EnableOriginator (bool): 
        - ExtendedCommunity (list(dict(arg1:str[decimal | hex | ip | ieeeFloat],arg2:str[decimal | hex | ip | ieeeFloat],arg3:str[twoOctetAs | ip | fourOctetAs | opaque | administratorAsTwoOctetLinkBw],arg4:str[routeTarget | origin | extendedBandwidthSubType],arg5:str))): 
        - LocalPref (number): 
        - MultiExit (number): 
        - NextHop (str): 
        - NextHopIpType (str(ipv4 | ipv6)): 
        - NextHopMode (str(fixed | incrementPerPeer)): 
        - Origin (str(igp | egp | incomplete)): 
        - OriginatorId (str): 
        - SetNextHop (str(manually | sameAsLocalIp)): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
