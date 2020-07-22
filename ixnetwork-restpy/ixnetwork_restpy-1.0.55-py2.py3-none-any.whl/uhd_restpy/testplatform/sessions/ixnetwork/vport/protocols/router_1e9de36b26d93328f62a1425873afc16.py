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
        'ActiveTime': 'activeTime',
        'AsNumber': 'asNumber',
        'DiscardLearnedRoutes': 'discardLearnedRoutes',
        'EigrpAddressFamily': 'eigrpAddressFamily',
        'EigrpMajorVersion': 'eigrpMajorVersion',
        'EigrpMinorVersion': 'eigrpMinorVersion',
        'EnablePiggyBack': 'enablePiggyBack',
        'Enabled': 'enabled',
        'IosMajorVersion': 'iosMajorVersion',
        'IosMinorVersion': 'iosMinorVersion',
        'IsRefreshComplete': 'isRefreshComplete',
        'K1': 'k1',
        'K2': 'k2',
        'K3': 'k3',
        'K4': 'k4',
        'K5': 'k5',
        'RouterId': 'routerId',
        'TrafficGroupId': 'trafficGroupId',
    }

    def __init__(self, parent):
        super(Router, self).__init__(parent)

    @property
    def Interface(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_ffc63882c65c19ba8c40e061d8180509.Interface): An instance of the Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_ffc63882c65c19ba8c40e061d8180509 import Interface
        return Interface(self)

    @property
    def LearnedRoute(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedroute_fb092a38c92327b22368d6fb71dd4dd6.LearnedRoute): An instance of the LearnedRoute class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedroute_fb092a38c92327b22368d6fb71dd4dd6 import LearnedRoute
        return LearnedRoute(self)

    @property
    def RouteRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.routerange_b3152d6492e8ce6060db5411a4f92fc0.RouteRange): An instance of the RouteRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.routerange_b3152d6492e8ce6060db5411a4f92fc0 import RouteRange
        return RouteRange(self)

    @property
    def ActiveTime(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActiveTime'])
    @ActiveTime.setter
    def ActiveTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ActiveTime'], value)

    @property
    def AsNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AsNumber'])
    @AsNumber.setter
    def AsNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AsNumber'], value)

    @property
    def DiscardLearnedRoutes(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DiscardLearnedRoutes'])
    @DiscardLearnedRoutes.setter
    def DiscardLearnedRoutes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DiscardLearnedRoutes'], value)

    @property
    def EigrpAddressFamily(self):
        """
        Returns
        -------
        - str(ipv4 | ipv6): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EigrpAddressFamily'])
    @EigrpAddressFamily.setter
    def EigrpAddressFamily(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EigrpAddressFamily'], value)

    @property
    def EigrpMajorVersion(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EigrpMajorVersion'])
    @EigrpMajorVersion.setter
    def EigrpMajorVersion(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EigrpMajorVersion'], value)

    @property
    def EigrpMinorVersion(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EigrpMinorVersion'])
    @EigrpMinorVersion.setter
    def EigrpMinorVersion(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EigrpMinorVersion'], value)

    @property
    def EnablePiggyBack(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePiggyBack'])
    @EnablePiggyBack.setter
    def EnablePiggyBack(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePiggyBack'], value)

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
    def IosMajorVersion(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IosMajorVersion'])
    @IosMajorVersion.setter
    def IosMajorVersion(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IosMajorVersion'], value)

    @property
    def IosMinorVersion(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IosMinorVersion'])
    @IosMinorVersion.setter
    def IosMinorVersion(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IosMinorVersion'], value)

    @property
    def IsRefreshComplete(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsRefreshComplete'])

    @property
    def K1(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['K1'])
    @K1.setter
    def K1(self, value):
        self._set_attribute(self._SDM_ATT_MAP['K1'], value)

    @property
    def K2(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['K2'])
    @K2.setter
    def K2(self, value):
        self._set_attribute(self._SDM_ATT_MAP['K2'], value)

    @property
    def K3(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['K3'])
    @K3.setter
    def K3(self, value):
        self._set_attribute(self._SDM_ATT_MAP['K3'], value)

    @property
    def K4(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['K4'])
    @K4.setter
    def K4(self, value):
        self._set_attribute(self._SDM_ATT_MAP['K4'], value)

    @property
    def K5(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['K5'])
    @K5.setter
    def K5(self, value):
        self._set_attribute(self._SDM_ATT_MAP['K5'], value)

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

    def update(self, ActiveTime=None, AsNumber=None, DiscardLearnedRoutes=None, EigrpAddressFamily=None, EigrpMajorVersion=None, EigrpMinorVersion=None, EnablePiggyBack=None, Enabled=None, IosMajorVersion=None, IosMinorVersion=None, K1=None, K2=None, K3=None, K4=None, K5=None, RouterId=None, TrafficGroupId=None):
        """Updates router resource on the server.

        Args
        ----
        - ActiveTime (number): 
        - AsNumber (number): 
        - DiscardLearnedRoutes (bool): 
        - EigrpAddressFamily (str(ipv4 | ipv6)): 
        - EigrpMajorVersion (number): 
        - EigrpMinorVersion (number): 
        - EnablePiggyBack (bool): 
        - Enabled (bool): 
        - IosMajorVersion (number): 
        - IosMinorVersion (number): 
        - K1 (number): 
        - K2 (number): 
        - K3 (number): 
        - K4 (number): 
        - K5 (number): 
        - RouterId (str): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ActiveTime=None, AsNumber=None, DiscardLearnedRoutes=None, EigrpAddressFamily=None, EigrpMajorVersion=None, EigrpMinorVersion=None, EnablePiggyBack=None, Enabled=None, IosMajorVersion=None, IosMinorVersion=None, K1=None, K2=None, K3=None, K4=None, K5=None, RouterId=None, TrafficGroupId=None):
        """Adds a new router resource on the server and adds it to the container.

        Args
        ----
        - ActiveTime (number): 
        - AsNumber (number): 
        - DiscardLearnedRoutes (bool): 
        - EigrpAddressFamily (str(ipv4 | ipv6)): 
        - EigrpMajorVersion (number): 
        - EigrpMinorVersion (number): 
        - EnablePiggyBack (bool): 
        - Enabled (bool): 
        - IosMajorVersion (number): 
        - IosMinorVersion (number): 
        - K1 (number): 
        - K2 (number): 
        - K3 (number): 
        - K4 (number): 
        - K5 (number): 
        - RouterId (str): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 

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

    def find(self, ActiveTime=None, AsNumber=None, DiscardLearnedRoutes=None, EigrpAddressFamily=None, EigrpMajorVersion=None, EigrpMinorVersion=None, EnablePiggyBack=None, Enabled=None, IosMajorVersion=None, IosMinorVersion=None, IsRefreshComplete=None, K1=None, K2=None, K3=None, K4=None, K5=None, RouterId=None, TrafficGroupId=None):
        """Finds and retrieves router resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve router resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all router resources from the server.

        Args
        ----
        - ActiveTime (number): 
        - AsNumber (number): 
        - DiscardLearnedRoutes (bool): 
        - EigrpAddressFamily (str(ipv4 | ipv6)): 
        - EigrpMajorVersion (number): 
        - EigrpMinorVersion (number): 
        - EnablePiggyBack (bool): 
        - Enabled (bool): 
        - IosMajorVersion (number): 
        - IosMinorVersion (number): 
        - IsRefreshComplete (number): 
        - K1 (number): 
        - K2 (number): 
        - K3 (number): 
        - K4 (number): 
        - K5 (number): 
        - RouterId (str): 
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): 

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

    def RefreshLearnedInfo(self):
        """Executes the refreshLearnedInfo operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshLearnedInfo', payload=payload, response_object=None)
