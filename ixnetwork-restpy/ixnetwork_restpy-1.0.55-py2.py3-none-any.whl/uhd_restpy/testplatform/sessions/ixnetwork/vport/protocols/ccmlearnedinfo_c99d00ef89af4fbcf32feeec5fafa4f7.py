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


class CcmLearnedInfo(Base):
    """
    The CcmLearnedInfo class encapsulates a list of ccmLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the CcmLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'ccmLearnedInfo'
    _SDM_ATT_MAP = {
        'AllRmepDead': 'allRmepDead',
        'CVlan': 'cVlan',
        'CciInterval': 'cciInterval',
        'ErrCcmDefect': 'errCcmDefect',
        'ErrCcmDefectCount': 'errCcmDefectCount',
        'IfaceTlvDefectCount': 'ifaceTlvDefectCount',
        'MdLevel': 'mdLevel',
        'MdName': 'mdName',
        'MdNameFormat': 'mdNameFormat',
        'MepId': 'mepId',
        'MepMacAddress': 'mepMacAddress',
        'OutOfSequenceCcmCount': 'outOfSequenceCcmCount',
        'PortTlvDefectCount': 'portTlvDefectCount',
        'RdiRxCount': 'rdiRxCount',
        'RdiRxState': 'rdiRxState',
        'ReceivedAis': 'receivedAis',
        'ReceivedIfaceTlvDefect': 'receivedIfaceTlvDefect',
        'ReceivedPortTlvDefect': 'receivedPortTlvDefect',
        'ReceivedRdi': 'receivedRdi',
        'RemoteMepDefectCount': 'remoteMepDefectCount',
        'RmepCcmDefect': 'rmepCcmDefect',
        'SVlan': 'sVlan',
        'ShortMaName': 'shortMaName',
        'ShortMaNameFormat': 'shortMaNameFormat',
        'SomeRmepDefect': 'someRmepDefect',
    }

    def __init__(self, parent):
        super(CcmLearnedInfo, self).__init__(parent)

    @property
    def AllRmepDead(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AllRmepDead'])

    @property
    def CVlan(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CVlan'])

    @property
    def CciInterval(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CciInterval'])

    @property
    def ErrCcmDefect(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrCcmDefect'])

    @property
    def ErrCcmDefectCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrCcmDefectCount'])

    @property
    def IfaceTlvDefectCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IfaceTlvDefectCount'])

    @property
    def MdLevel(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MdLevel'])

    @property
    def MdName(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MdName'])

    @property
    def MdNameFormat(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MdNameFormat'])

    @property
    def MepId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MepId'])

    @property
    def MepMacAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MepMacAddress'])

    @property
    def OutOfSequenceCcmCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutOfSequenceCcmCount'])

    @property
    def PortTlvDefectCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortTlvDefectCount'])

    @property
    def RdiRxCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RdiRxCount'])

    @property
    def RdiRxState(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RdiRxState'])

    @property
    def ReceivedAis(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceivedAis'])

    @property
    def ReceivedIfaceTlvDefect(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceivedIfaceTlvDefect'])

    @property
    def ReceivedPortTlvDefect(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceivedPortTlvDefect'])

    @property
    def ReceivedRdi(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceivedRdi'])

    @property
    def RemoteMepDefectCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteMepDefectCount'])

    @property
    def RmepCcmDefect(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RmepCcmDefect'])

    @property
    def SVlan(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SVlan'])

    @property
    def ShortMaName(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShortMaName'])

    @property
    def ShortMaNameFormat(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShortMaNameFormat'])

    @property
    def SomeRmepDefect(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SomeRmepDefect'])

    def find(self, AllRmepDead=None, CVlan=None, CciInterval=None, ErrCcmDefect=None, ErrCcmDefectCount=None, IfaceTlvDefectCount=None, MdLevel=None, MdName=None, MdNameFormat=None, MepId=None, MepMacAddress=None, OutOfSequenceCcmCount=None, PortTlvDefectCount=None, RdiRxCount=None, RdiRxState=None, ReceivedAis=None, ReceivedIfaceTlvDefect=None, ReceivedPortTlvDefect=None, ReceivedRdi=None, RemoteMepDefectCount=None, RmepCcmDefect=None, SVlan=None, ShortMaName=None, ShortMaNameFormat=None, SomeRmepDefect=None):
        """Finds and retrieves ccmLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ccmLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ccmLearnedInfo resources from the server.

        Args
        ----
        - AllRmepDead (bool): 
        - CVlan (str): 
        - CciInterval (str): 
        - ErrCcmDefect (bool): 
        - ErrCcmDefectCount (number): 
        - IfaceTlvDefectCount (number): 
        - MdLevel (number): 
        - MdName (str): 
        - MdNameFormat (number): 
        - MepId (number): 
        - MepMacAddress (str): 
        - OutOfSequenceCcmCount (number): 
        - PortTlvDefectCount (number): 
        - RdiRxCount (number): 
        - RdiRxState (str): 
        - ReceivedAis (bool): 
        - ReceivedIfaceTlvDefect (bool): 
        - ReceivedPortTlvDefect (bool): 
        - ReceivedRdi (bool): 
        - RemoteMepDefectCount (number): 
        - RmepCcmDefect (bool): 
        - SVlan (str): 
        - ShortMaName (str): 
        - ShortMaNameFormat (number): 
        - SomeRmepDefect (bool): 

        Returns
        -------
        - self: This instance with matching ccmLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ccmLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ccmLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
