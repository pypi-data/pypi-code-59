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


class Flapping(Base):
    """
    The Flapping class encapsulates a required flapping resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'flapping'
    _SDM_ATT_MAP = {
        'DownTime': 'downTime',
        'EnablePartialFlap': 'enablePartialFlap',
        'Enabled': 'enabled',
        'RoutesToFlapFrom': 'routesToFlapFrom',
        'RoutesToFlapTo': 'routesToFlapTo',
        'UpTime': 'upTime',
    }

    def __init__(self, parent):
        super(Flapping, self).__init__(parent)

    @property
    def DownTime(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownTime'])
    @DownTime.setter
    def DownTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownTime'], value)

    @property
    def EnablePartialFlap(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePartialFlap'])
    @EnablePartialFlap.setter
    def EnablePartialFlap(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePartialFlap'], value)

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
    def RoutesToFlapFrom(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RoutesToFlapFrom'])
    @RoutesToFlapFrom.setter
    def RoutesToFlapFrom(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RoutesToFlapFrom'], value)

    @property
    def RoutesToFlapTo(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RoutesToFlapTo'])
    @RoutesToFlapTo.setter
    def RoutesToFlapTo(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RoutesToFlapTo'], value)

    @property
    def UpTime(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpTime'])
    @UpTime.setter
    def UpTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpTime'], value)

    def update(self, DownTime=None, EnablePartialFlap=None, Enabled=None, RoutesToFlapFrom=None, RoutesToFlapTo=None, UpTime=None):
        """Updates flapping resource on the server.

        Args
        ----
        - DownTime (number): 
        - EnablePartialFlap (bool): 
        - Enabled (bool): 
        - RoutesToFlapFrom (number): 
        - RoutesToFlapTo (number): 
        - UpTime (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
