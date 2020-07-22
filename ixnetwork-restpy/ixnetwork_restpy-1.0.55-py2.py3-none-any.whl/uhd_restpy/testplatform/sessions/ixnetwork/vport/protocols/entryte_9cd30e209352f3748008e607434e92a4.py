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


class EntryTe(Base):
    """
    The EntryTe class encapsulates a required entryTe resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'entryTe'
    _SDM_ATT_MAP = {
        'EnableEntryTe': 'enableEntryTe',
        'EteAdmGroup': 'eteAdmGroup',
        'EteLinkMetric': 'eteLinkMetric',
        'EteMaxBandWidth': 'eteMaxBandWidth',
        'EteMaxReserveBandWidth': 'eteMaxReserveBandWidth',
        'EteRouterId': 'eteRouterId',
        'EteRouterIdIncrement': 'eteRouterIdIncrement',
        'EteUnreservedBandWidth': 'eteUnreservedBandWidth',
    }

    def __init__(self, parent):
        super(EntryTe, self).__init__(parent)

    @property
    def EnableEntryTe(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableEntryTe'])
    @EnableEntryTe.setter
    def EnableEntryTe(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableEntryTe'], value)

    @property
    def EteAdmGroup(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EteAdmGroup'])
    @EteAdmGroup.setter
    def EteAdmGroup(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EteAdmGroup'], value)

    @property
    def EteLinkMetric(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EteLinkMetric'])
    @EteLinkMetric.setter
    def EteLinkMetric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EteLinkMetric'], value)

    @property
    def EteMaxBandWidth(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EteMaxBandWidth'])
    @EteMaxBandWidth.setter
    def EteMaxBandWidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EteMaxBandWidth'], value)

    @property
    def EteMaxReserveBandWidth(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EteMaxReserveBandWidth'])
    @EteMaxReserveBandWidth.setter
    def EteMaxReserveBandWidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EteMaxReserveBandWidth'], value)

    @property
    def EteRouterId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EteRouterId'])
    @EteRouterId.setter
    def EteRouterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EteRouterId'], value)

    @property
    def EteRouterIdIncrement(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EteRouterIdIncrement'])
    @EteRouterIdIncrement.setter
    def EteRouterIdIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EteRouterIdIncrement'], value)

    @property
    def EteUnreservedBandWidth(self):
        """
        Returns
        -------
        - list(number): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EteUnreservedBandWidth'])
    @EteUnreservedBandWidth.setter
    def EteUnreservedBandWidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EteUnreservedBandWidth'], value)

    def update(self, EnableEntryTe=None, EteAdmGroup=None, EteLinkMetric=None, EteMaxBandWidth=None, EteMaxReserveBandWidth=None, EteRouterId=None, EteRouterIdIncrement=None, EteUnreservedBandWidth=None):
        """Updates entryTe resource on the server.

        Args
        ----
        - EnableEntryTe (bool): 
        - EteAdmGroup (str): 
        - EteLinkMetric (number): 
        - EteMaxBandWidth (number): 
        - EteMaxReserveBandWidth (number): 
        - EteRouterId (str): 
        - EteRouterIdIncrement (str): 
        - EteUnreservedBandWidth (list(number)): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
