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


class RateControlParameters(Base):
    """
    The RateControlParameters class encapsulates a required rateControlParameters resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'rateControlParameters'
    _SDM_ATT_MAP = {
        'ArpRefreshInterval': 'arpRefreshInterval',
        'MaxRequestsPerBurst': 'maxRequestsPerBurst',
        'MaxRequestsPerSec': 'maxRequestsPerSec',
        'MinRetryInterval': 'minRetryInterval',
        'RetryCount': 'retryCount',
        'SendInBursts': 'sendInBursts',
        'SendRequestsAsFastAsPossible': 'sendRequestsAsFastAsPossible',
    }

    def __init__(self, parent):
        super(RateControlParameters, self).__init__(parent)

    @property
    def ArpRefreshInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpRefreshInterval'])
    @ArpRefreshInterval.setter
    def ArpRefreshInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpRefreshInterval'], value)

    @property
    def MaxRequestsPerBurst(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRequestsPerBurst'])
    @MaxRequestsPerBurst.setter
    def MaxRequestsPerBurst(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxRequestsPerBurst'], value)

    @property
    def MaxRequestsPerSec(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRequestsPerSec'])
    @MaxRequestsPerSec.setter
    def MaxRequestsPerSec(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxRequestsPerSec'], value)

    @property
    def MinRetryInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinRetryInterval'])
    @MinRetryInterval.setter
    def MinRetryInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinRetryInterval'], value)

    @property
    def RetryCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RetryCount'])
    @RetryCount.setter
    def RetryCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RetryCount'], value)

    @property
    def SendInBursts(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendInBursts'])
    @SendInBursts.setter
    def SendInBursts(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendInBursts'], value)

    @property
    def SendRequestsAsFastAsPossible(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendRequestsAsFastAsPossible'])
    @SendRequestsAsFastAsPossible.setter
    def SendRequestsAsFastAsPossible(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendRequestsAsFastAsPossible'], value)

    def update(self, ArpRefreshInterval=None, MaxRequestsPerBurst=None, MaxRequestsPerSec=None, MinRetryInterval=None, RetryCount=None, SendInBursts=None, SendRequestsAsFastAsPossible=None):
        """Updates rateControlParameters resource on the server.

        Args
        ----
        - ArpRefreshInterval (number): 
        - MaxRequestsPerBurst (number): 
        - MaxRequestsPerSec (number): 
        - MinRetryInterval (number): 
        - RetryCount (number): 
        - SendInBursts (bool): 
        - SendRequestsAsFastAsPossible (bool): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
