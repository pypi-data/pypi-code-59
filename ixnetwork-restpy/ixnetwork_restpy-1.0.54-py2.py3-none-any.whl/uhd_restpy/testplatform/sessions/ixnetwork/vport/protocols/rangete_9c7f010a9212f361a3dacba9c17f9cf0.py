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


class RangeTe(Base):
    """
    The RangeTe class encapsulates a required rangeTe resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'rangeTe'
    _SDM_ATT_MAP = {
        'EnableRangeTe': 'enableRangeTe',
        'TeAdmGroup': 'teAdmGroup',
        'TeLinkMetric': 'teLinkMetric',
        'TeMaxBandWidth': 'teMaxBandWidth',
        'TeMaxReserveBandWidth': 'teMaxReserveBandWidth',
        'TeRouterId': 'teRouterId',
        'TeRouterIdIncrement': 'teRouterIdIncrement',
        'TeUnreservedBandWidth': 'teUnreservedBandWidth',
    }

    def __init__(self, parent):
        super(RangeTe, self).__init__(parent)

    @property
    def EnableRangeTe(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableRangeTe'])
    @EnableRangeTe.setter
    def EnableRangeTe(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableRangeTe'], value)

    @property
    def TeAdmGroup(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeAdmGroup'])
    @TeAdmGroup.setter
    def TeAdmGroup(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeAdmGroup'], value)

    @property
    def TeLinkMetric(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeLinkMetric'])
    @TeLinkMetric.setter
    def TeLinkMetric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeLinkMetric'], value)

    @property
    def TeMaxBandWidth(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeMaxBandWidth'])
    @TeMaxBandWidth.setter
    def TeMaxBandWidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeMaxBandWidth'], value)

    @property
    def TeMaxReserveBandWidth(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeMaxReserveBandWidth'])
    @TeMaxReserveBandWidth.setter
    def TeMaxReserveBandWidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeMaxReserveBandWidth'], value)

    @property
    def TeRouterId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeRouterId'])
    @TeRouterId.setter
    def TeRouterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeRouterId'], value)

    @property
    def TeRouterIdIncrement(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeRouterIdIncrement'])
    @TeRouterIdIncrement.setter
    def TeRouterIdIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeRouterIdIncrement'], value)

    @property
    def TeUnreservedBandWidth(self):
        """
        Returns
        -------
        - list(number): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeUnreservedBandWidth'])
    @TeUnreservedBandWidth.setter
    def TeUnreservedBandWidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeUnreservedBandWidth'], value)

    def update(self, EnableRangeTe=None, TeAdmGroup=None, TeLinkMetric=None, TeMaxBandWidth=None, TeMaxReserveBandWidth=None, TeRouterId=None, TeRouterIdIncrement=None, TeUnreservedBandWidth=None):
        """Updates rangeTe resource on the server.

        Args
        ----
        - EnableRangeTe (bool): 
        - TeAdmGroup (str): 
        - TeLinkMetric (number): 
        - TeMaxBandWidth (number): 
        - TeMaxReserveBandWidth (number): 
        - TeRouterId (str): 
        - TeRouterIdIncrement (str): 
        - TeUnreservedBandWidth (list(number)): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
