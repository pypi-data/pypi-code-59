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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class TestParameters(Base):
    """
    The TestParameters class encapsulates a required testParameters resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'testParameters'
    _SDM_ATT_MAP = {
        'TestCategory': 'testCategory',
        'TestDUTName': 'testDUTName',
        'TestHighlights': 'testHighlights',
        'TestId': 'testId',
        'TestName': 'testName',
        'TestObjectives': 'testObjectives',
        'TesterName': 'testerName',
    }

    def __init__(self, parent):
        super(TestParameters, self).__init__(parent)

    @property
    def TestCategory(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TestCategory'])
    @TestCategory.setter
    def TestCategory(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TestCategory'], value)

    @property
    def TestDUTName(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TestDUTName'])
    @TestDUTName.setter
    def TestDUTName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TestDUTName'], value)

    @property
    def TestHighlights(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TestHighlights'])
    @TestHighlights.setter
    def TestHighlights(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TestHighlights'], value)

    @property
    def TestId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TestId'])

    @property
    def TestName(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TestName'])
    @TestName.setter
    def TestName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TestName'], value)

    @property
    def TestObjectives(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TestObjectives'])
    @TestObjectives.setter
    def TestObjectives(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TestObjectives'], value)

    @property
    def TesterName(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TesterName'])
    @TesterName.setter
    def TesterName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TesterName'], value)

    def update(self, TestCategory=None, TestDUTName=None, TestHighlights=None, TestName=None, TestObjectives=None, TesterName=None):
        """Updates testParameters resource on the server.

        Args
        ----
        - TestCategory (str): 
        - TestDUTName (str): 
        - TestHighlights (str): 
        - TestName (str): 
        - TestObjectives (str): 
        - TesterName (str): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
