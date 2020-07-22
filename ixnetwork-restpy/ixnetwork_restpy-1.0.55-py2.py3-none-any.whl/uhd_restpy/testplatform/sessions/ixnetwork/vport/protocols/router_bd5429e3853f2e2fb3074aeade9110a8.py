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


class Router(Base):
    """
    The Router class encapsulates a list of router resources that are managed by the user.
    A list of resources can be retrieved from the server using the Router.find() method.
    The list can be managed by using the Router.add() and Router.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'router'
    _SDM_ATT_MAP = {
        'EnableBfdMplsLearnedLsp': 'enableBfdMplsLearnedLsp',
        'EnableFilterFec': 'enableFilterFec',
        'EnableGracefulRestart': 'enableGracefulRestart',
        'EnableLspPingLearnedLsp': 'enableLspPingLearnedLsp',
        'EnableOverrideRbit': 'enableOverrideRbit',
        'EnableP2mpCapabilty': 'enableP2mpCapabilty',
        'EnablePduRateControl': 'enablePduRateControl',
        'EnableVcFecs': 'enableVcFecs',
        'EnableVcGroupMatch': 'enableVcGroupMatch',
        'Enabled': 'enabled',
        'InterPduGap': 'interPduGap',
        'IsBgpAdVplsLearnedInfoRefreshed': 'isBgpAdVplsLearnedInfoRefreshed',
        'ReconnectTime': 'reconnectTime',
        'RecoveryTime': 'recoveryTime',
        'RouterId': 'routerId',
        'TrafficGroupId': 'trafficGroupId',
        'TransportAddress': 'transportAddress',
        'UseTransportAddress': 'useTransportAddress',
    }

    def __init__(self, parent):
        super(Router, self).__init__(parent)

    @property
    def AdvFecRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.advfecrange_85d230f184c02b04f16549a52d46b4e2.AdvFecRange): An instance of the AdvFecRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.advfecrange_85d230f184c02b04f16549a52d46b4e2 import AdvFecRange
        return AdvFecRange(self)

    @property
    def IncludeIpFecRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.includeipfecrange_ff1ca9aefa3af035939d64a848d99e20.IncludeIpFecRange): An instance of the IncludeIpFecRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.includeipfecrange_ff1ca9aefa3af035939d64a848d99e20 import IncludeIpFecRange
        return IncludeIpFecRange(self)

    @property
    def Interface(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_a3e17ed11f3921214534d3e120a5a3d5.Interface): An instance of the Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_a3e17ed11f3921214534d3e120a5a3d5 import Interface
        return Interface(self)

    @property
    def L2Interface(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.l2interface_0a1b536650cf4a71368d9255d6ed3f51.L2Interface): An instance of the L2Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.l2interface_0a1b536650cf4a71368d9255d6ed3f51 import L2Interface
        return L2Interface(self)

    @property
    def LearnedBgpAdVplsLabels(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedbgpadvplslabels_74e67f73772aa5a610553add2c6922f5.LearnedBgpAdVplsLabels): An instance of the LearnedBgpAdVplsLabels class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedbgpadvplslabels_74e67f73772aa5a610553add2c6922f5 import LearnedBgpAdVplsLabels
        return LearnedBgpAdVplsLabels(self)

    @property
    def MulticastLeafRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.multicastleafrange_e6ee173e2068e696fa8b5a3b5e7641dc.MulticastLeafRange): An instance of the MulticastLeafRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.multicastleafrange_e6ee173e2068e696fa8b5a3b5e7641dc import MulticastLeafRange
        return MulticastLeafRange(self)

    @property
    def MulticastRootRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.multicastrootrange_c1c512e6d5798827e5dff8e609c5b5dc.MulticastRootRange): An instance of the MulticastRootRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.multicastrootrange_c1c512e6d5798827e5dff8e609c5b5dc import MulticastRootRange
        return MulticastRootRange(self)

    @property
    def ReqFecRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.reqfecrange_76a822569ee9b581335576defc7ada6a.ReqFecRange): An instance of the ReqFecRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.reqfecrange_76a822569ee9b581335576defc7ada6a import ReqFecRange
        return ReqFecRange(self)

    @property
    def EnableBfdMplsLearnedLsp(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableBfdMplsLearnedLsp'])
    @EnableBfdMplsLearnedLsp.setter
    def EnableBfdMplsLearnedLsp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableBfdMplsLearnedLsp'], value)

    @property
    def EnableFilterFec(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableFilterFec'])
    @EnableFilterFec.setter
    def EnableFilterFec(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableFilterFec'], value)

    @property
    def EnableGracefulRestart(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableGracefulRestart'])
    @EnableGracefulRestart.setter
    def EnableGracefulRestart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableGracefulRestart'], value)

    @property
    def EnableLspPingLearnedLsp(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLspPingLearnedLsp'])
    @EnableLspPingLearnedLsp.setter
    def EnableLspPingLearnedLsp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLspPingLearnedLsp'], value)

    @property
    def EnableOverrideRbit(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableOverrideRbit'])
    @EnableOverrideRbit.setter
    def EnableOverrideRbit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableOverrideRbit'], value)

    @property
    def EnableP2mpCapabilty(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableP2mpCapabilty'])
    @EnableP2mpCapabilty.setter
    def EnableP2mpCapabilty(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableP2mpCapabilty'], value)

    @property
    def EnablePduRateControl(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePduRateControl'])
    @EnablePduRateControl.setter
    def EnablePduRateControl(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePduRateControl'], value)

    @property
    def EnableVcFecs(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableVcFecs'])
    @EnableVcFecs.setter
    def EnableVcFecs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableVcFecs'], value)

    @property
    def EnableVcGroupMatch(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableVcGroupMatch'])
    @EnableVcGroupMatch.setter
    def EnableVcGroupMatch(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableVcGroupMatch'], value)

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
    def InterPduGap(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterPduGap'])
    @InterPduGap.setter
    def InterPduGap(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterPduGap'], value)

    @property
    def IsBgpAdVplsLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsBgpAdVplsLearnedInfoRefreshed'])

    @property
    def ReconnectTime(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReconnectTime'])
    @ReconnectTime.setter
    def ReconnectTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReconnectTime'], value)

    @property
    def RecoveryTime(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RecoveryTime'])
    @RecoveryTime.setter
    def RecoveryTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RecoveryTime'], value)

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
    def TrafficGroupId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficGroupId'])
    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficGroupId'], value)

    @property
    def TransportAddress(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransportAddress'])
    @TransportAddress.setter
    def TransportAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TransportAddress'], value)

    @property
    def UseTransportAddress(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseTransportAddress'])
    @UseTransportAddress.setter
    def UseTransportAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseTransportAddress'], value)

    def update(self, EnableBfdMplsLearnedLsp=None, EnableFilterFec=None, EnableGracefulRestart=None, EnableLspPingLearnedLsp=None, EnableOverrideRbit=None, EnableP2mpCapabilty=None, EnablePduRateControl=None, EnableVcFecs=None, EnableVcGroupMatch=None, Enabled=None, InterPduGap=None, ReconnectTime=None, RecoveryTime=None, RouterId=None, TrafficGroupId=None, TransportAddress=None, UseTransportAddress=None):
        """Updates router resource on the server.

        Args
        ----
        - EnableBfdMplsLearnedLsp (bool): 
        - EnableFilterFec (bool): 
        - EnableGracefulRestart (bool): 
        - EnableLspPingLearnedLsp (bool): 
        - EnableOverrideRbit (bool): 
        - EnableP2mpCapabilty (bool): 
        - EnablePduRateControl (bool): 
        - EnableVcFecs (bool): 
        - EnableVcGroupMatch (bool): 
        - Enabled (bool): 
        - InterPduGap (number): 
        - ReconnectTime (number): 
        - RecoveryTime (number): 
        - RouterId (str): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 
        - TransportAddress (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - UseTransportAddress (bool): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, EnableBfdMplsLearnedLsp=None, EnableFilterFec=None, EnableGracefulRestart=None, EnableLspPingLearnedLsp=None, EnableOverrideRbit=None, EnableP2mpCapabilty=None, EnablePduRateControl=None, EnableVcFecs=None, EnableVcGroupMatch=None, Enabled=None, InterPduGap=None, ReconnectTime=None, RecoveryTime=None, RouterId=None, TrafficGroupId=None, TransportAddress=None, UseTransportAddress=None):
        """Adds a new router resource on the server and adds it to the container.

        Args
        ----
        - EnableBfdMplsLearnedLsp (bool): 
        - EnableFilterFec (bool): 
        - EnableGracefulRestart (bool): 
        - EnableLspPingLearnedLsp (bool): 
        - EnableOverrideRbit (bool): 
        - EnableP2mpCapabilty (bool): 
        - EnablePduRateControl (bool): 
        - EnableVcFecs (bool): 
        - EnableVcGroupMatch (bool): 
        - Enabled (bool): 
        - InterPduGap (number): 
        - ReconnectTime (number): 
        - RecoveryTime (number): 
        - RouterId (str): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 
        - TransportAddress (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - UseTransportAddress (bool): 

        Returns
        -------
        - self: This instance with all currently retrieved router resources using find and the newly added router resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained router resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EnableBfdMplsLearnedLsp=None, EnableFilterFec=None, EnableGracefulRestart=None, EnableLspPingLearnedLsp=None, EnableOverrideRbit=None, EnableP2mpCapabilty=None, EnablePduRateControl=None, EnableVcFecs=None, EnableVcGroupMatch=None, Enabled=None, InterPduGap=None, IsBgpAdVplsLearnedInfoRefreshed=None, ReconnectTime=None, RecoveryTime=None, RouterId=None, TrafficGroupId=None, TransportAddress=None, UseTransportAddress=None):
        """Finds and retrieves router resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve router resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all router resources from the server.

        Args
        ----
        - EnableBfdMplsLearnedLsp (bool): 
        - EnableFilterFec (bool): 
        - EnableGracefulRestart (bool): 
        - EnableLspPingLearnedLsp (bool): 
        - EnableOverrideRbit (bool): 
        - EnableP2mpCapabilty (bool): 
        - EnablePduRateControl (bool): 
        - EnableVcFecs (bool): 
        - EnableVcGroupMatch (bool): 
        - Enabled (bool): 
        - InterPduGap (number): 
        - IsBgpAdVplsLearnedInfoRefreshed (bool): 
        - ReconnectTime (number): 
        - RecoveryTime (number): 
        - RouterId (str): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 
        - TransportAddress (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - UseTransportAddress (bool): 

        Returns
        -------
        - self: This instance with matching router resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of router data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the router resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def RefreshBgpAdVplsLearnedInfo(self):
        """Executes the refreshBgpAdVplsLearnedInfo operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshBgpAdVplsLearnedInfo', payload=payload, response_object=None)
