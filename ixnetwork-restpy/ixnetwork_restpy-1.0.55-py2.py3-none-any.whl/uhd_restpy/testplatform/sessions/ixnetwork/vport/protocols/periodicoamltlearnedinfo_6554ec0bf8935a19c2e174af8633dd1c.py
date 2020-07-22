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


class PeriodicOamLtLearnedInfo(Base):
    """
    The PeriodicOamLtLearnedInfo class encapsulates a list of periodicOamLtLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the PeriodicOamLtLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'periodicOamLtLearnedInfo'
    _SDM_ATT_MAP = {
        'AverageHopCount': 'averageHopCount',
        'CVlan': 'cVlan',
        'CompleteReplyCount': 'completeReplyCount',
        'DstMacAddress': 'dstMacAddress',
        'LtmSentCount': 'ltmSentCount',
        'MdLevel': 'mdLevel',
        'NoReplyCount': 'noReplyCount',
        'PartialReplyCount': 'partialReplyCount',
        'RecentHopCount': 'recentHopCount',
        'RecentHops': 'recentHops',
        'RecentReplyStatus': 'recentReplyStatus',
        'SVlan': 'sVlan',
        'SrcMacAddress': 'srcMacAddress',
    }

    def __init__(self, parent):
        super(PeriodicOamLtLearnedInfo, self).__init__(parent)

    @property
    def LtLearnedHop(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.ltlearnedhop_57462a3f529f62632b3fd3cbe879b821.LtLearnedHop): An instance of the LtLearnedHop class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.ltlearnedhop_57462a3f529f62632b3fd3cbe879b821 import LtLearnedHop
        return LtLearnedHop(self)

    @property
    def AverageHopCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AverageHopCount'])

    @property
    def CVlan(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CVlan'])

    @property
    def CompleteReplyCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CompleteReplyCount'])

    @property
    def DstMacAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DstMacAddress'])

    @property
    def LtmSentCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LtmSentCount'])

    @property
    def MdLevel(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MdLevel'])

    @property
    def NoReplyCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoReplyCount'])

    @property
    def PartialReplyCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PartialReplyCount'])

    @property
    def RecentHopCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RecentHopCount'])

    @property
    def RecentHops(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RecentHops'])

    @property
    def RecentReplyStatus(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RecentReplyStatus'])

    @property
    def SVlan(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SVlan'])

    @property
    def SrcMacAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SrcMacAddress'])

    def find(self, AverageHopCount=None, CVlan=None, CompleteReplyCount=None, DstMacAddress=None, LtmSentCount=None, MdLevel=None, NoReplyCount=None, PartialReplyCount=None, RecentHopCount=None, RecentHops=None, RecentReplyStatus=None, SVlan=None, SrcMacAddress=None):
        """Finds and retrieves periodicOamLtLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve periodicOamLtLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all periodicOamLtLearnedInfo resources from the server.

        Args
        ----
        - AverageHopCount (number): 
        - CVlan (str): 
        - CompleteReplyCount (number): 
        - DstMacAddress (str): 
        - LtmSentCount (number): 
        - MdLevel (number): 
        - NoReplyCount (number): 
        - PartialReplyCount (number): 
        - RecentHopCount (number): 
        - RecentHops (str): 
        - RecentReplyStatus (str): 
        - SVlan (str): 
        - SrcMacAddress (str): 

        Returns
        -------
        - self: This instance with matching periodicOamLtLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of periodicOamLtLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the periodicOamLtLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
