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


class LmiStatusLearnedInfo(Base):
    """
    The LmiStatusLearnedInfo class encapsulates a list of lmiStatusLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the LmiStatusLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'lmiStatusLearnedInfo'
    _SDM_ATT_MAP = {
        'DataInstance': 'dataInstance',
        'DuplicatedIe': 'duplicatedIe',
        'InvalidEvcReferenceId': 'invalidEvcReferenceId',
        'InvalidMandatoryIe': 'invalidMandatoryIe',
        'InvalidMsgType': 'invalidMsgType',
        'InvalidNonMandatoryIe': 'invalidNonMandatoryIe',
        'InvalidProtocolVersion': 'invalidProtocolVersion',
        'LmiStatus': 'lmiStatus',
        'MandatoryIeMissing': 'mandatoryIeMissing',
        'OutOfSequenceIe': 'outOfSequenceIe',
        'ProtocolVersion': 'protocolVersion',
        'ReceiveSequenceNumber': 'receiveSequenceNumber',
        'SendSequenceNumber': 'sendSequenceNumber',
        'ShortMsgCounter': 'shortMsgCounter',
        'UnexpectedIe': 'unexpectedIe',
        'UnrecognizedIe': 'unrecognizedIe',
    }

    def __init__(self, parent):
        super(LmiStatusLearnedInfo, self).__init__(parent)

    @property
    def DataInstance(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataInstance'])

    @property
    def DuplicatedIe(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DuplicatedIe'])

    @property
    def InvalidEvcReferenceId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InvalidEvcReferenceId'])

    @property
    def InvalidMandatoryIe(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InvalidMandatoryIe'])

    @property
    def InvalidMsgType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InvalidMsgType'])

    @property
    def InvalidNonMandatoryIe(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InvalidNonMandatoryIe'])

    @property
    def InvalidProtocolVersion(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InvalidProtocolVersion'])

    @property
    def LmiStatus(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LmiStatus'])

    @property
    def MandatoryIeMissing(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MandatoryIeMissing'])

    @property
    def OutOfSequenceIe(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutOfSequenceIe'])

    @property
    def ProtocolVersion(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolVersion'])

    @property
    def ReceiveSequenceNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceiveSequenceNumber'])

    @property
    def SendSequenceNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendSequenceNumber'])

    @property
    def ShortMsgCounter(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShortMsgCounter'])

    @property
    def UnexpectedIe(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UnexpectedIe'])

    @property
    def UnrecognizedIe(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UnrecognizedIe'])

    def find(self, DataInstance=None, DuplicatedIe=None, InvalidEvcReferenceId=None, InvalidMandatoryIe=None, InvalidMsgType=None, InvalidNonMandatoryIe=None, InvalidProtocolVersion=None, LmiStatus=None, MandatoryIeMissing=None, OutOfSequenceIe=None, ProtocolVersion=None, ReceiveSequenceNumber=None, SendSequenceNumber=None, ShortMsgCounter=None, UnexpectedIe=None, UnrecognizedIe=None):
        """Finds and retrieves lmiStatusLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve lmiStatusLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all lmiStatusLearnedInfo resources from the server.

        Args
        ----
        - DataInstance (number): 
        - DuplicatedIe (str): 
        - InvalidEvcReferenceId (str): 
        - InvalidMandatoryIe (str): 
        - InvalidMsgType (str): 
        - InvalidNonMandatoryIe (str): 
        - InvalidProtocolVersion (str): 
        - LmiStatus (str): 
        - MandatoryIeMissing (str): 
        - OutOfSequenceIe (str): 
        - ProtocolVersion (number): 
        - ReceiveSequenceNumber (number): 
        - SendSequenceNumber (number): 
        - ShortMsgCounter (number): 
        - UnexpectedIe (str): 
        - UnrecognizedIe (str): 

        Returns
        -------
        - self: This instance with matching lmiStatusLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of lmiStatusLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the lmiStatusLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
