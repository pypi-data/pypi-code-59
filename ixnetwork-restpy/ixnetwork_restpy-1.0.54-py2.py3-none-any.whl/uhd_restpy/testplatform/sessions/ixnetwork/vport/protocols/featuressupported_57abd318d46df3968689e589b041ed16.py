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


class FeaturesSupported(Base):
    """
    The FeaturesSupported class encapsulates a required featuresSupported resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'featuresSupported'
    _SDM_ATT_MAP = {
        'ApplyActions': 'applyActions',
        'ApplyActionsMiss': 'applyActionsMiss',
        'ApplySetField': 'applySetField',
        'ApplySetFieldMiss': 'applySetFieldMiss',
        'Experimenter': 'experimenter',
        'ExperimenterMiss': 'experimenterMiss',
        'Instruction': 'instruction',
        'InstructionMiss': 'instructionMiss',
        'Match': 'match',
        'NextTable': 'nextTable',
        'NextTableMiss': 'nextTableMiss',
        'Wildcards': 'wildcards',
        'WriteActions': 'writeActions',
        'WriteActionsMiss': 'writeActionsMiss',
        'WriteSetField': 'writeSetField',
        'WriteSetFieldMiss': 'writeSetFieldMiss',
    }

    def __init__(self, parent):
        super(FeaturesSupported, self).__init__(parent)

    @property
    def ApplyActions(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApplyActions'])
    @ApplyActions.setter
    def ApplyActions(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ApplyActions'], value)

    @property
    def ApplyActionsMiss(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApplyActionsMiss'])
    @ApplyActionsMiss.setter
    def ApplyActionsMiss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ApplyActionsMiss'], value)

    @property
    def ApplySetField(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApplySetField'])
    @ApplySetField.setter
    def ApplySetField(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ApplySetField'], value)

    @property
    def ApplySetFieldMiss(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApplySetFieldMiss'])
    @ApplySetFieldMiss.setter
    def ApplySetFieldMiss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ApplySetFieldMiss'], value)

    @property
    def Experimenter(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Experimenter'])
    @Experimenter.setter
    def Experimenter(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Experimenter'], value)

    @property
    def ExperimenterMiss(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterMiss'])
    @ExperimenterMiss.setter
    def ExperimenterMiss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterMiss'], value)

    @property
    def Instruction(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Instruction'])
    @Instruction.setter
    def Instruction(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Instruction'], value)

    @property
    def InstructionMiss(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InstructionMiss'])
    @InstructionMiss.setter
    def InstructionMiss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InstructionMiss'], value)

    @property
    def Match(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Match'])
    @Match.setter
    def Match(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Match'], value)

    @property
    def NextTable(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextTable'])
    @NextTable.setter
    def NextTable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NextTable'], value)

    @property
    def NextTableMiss(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextTableMiss'])
    @NextTableMiss.setter
    def NextTableMiss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NextTableMiss'], value)

    @property
    def Wildcards(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Wildcards'])
    @Wildcards.setter
    def Wildcards(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Wildcards'], value)

    @property
    def WriteActions(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['WriteActions'])
    @WriteActions.setter
    def WriteActions(self, value):
        self._set_attribute(self._SDM_ATT_MAP['WriteActions'], value)

    @property
    def WriteActionsMiss(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['WriteActionsMiss'])
    @WriteActionsMiss.setter
    def WriteActionsMiss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['WriteActionsMiss'], value)

    @property
    def WriteSetField(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['WriteSetField'])
    @WriteSetField.setter
    def WriteSetField(self, value):
        self._set_attribute(self._SDM_ATT_MAP['WriteSetField'], value)

    @property
    def WriteSetFieldMiss(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['WriteSetFieldMiss'])
    @WriteSetFieldMiss.setter
    def WriteSetFieldMiss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['WriteSetFieldMiss'], value)

    def update(self, ApplyActions=None, ApplyActionsMiss=None, ApplySetField=None, ApplySetFieldMiss=None, Experimenter=None, ExperimenterMiss=None, Instruction=None, InstructionMiss=None, Match=None, NextTable=None, NextTableMiss=None, Wildcards=None, WriteActions=None, WriteActionsMiss=None, WriteSetField=None, WriteSetFieldMiss=None):
        """Updates featuresSupported resource on the server.

        Args
        ----
        - ApplyActions (bool): 
        - ApplyActionsMiss (bool): 
        - ApplySetField (bool): 
        - ApplySetFieldMiss (bool): 
        - Experimenter (bool): 
        - ExperimenterMiss (bool): 
        - Instruction (bool): 
        - InstructionMiss (bool): 
        - Match (bool): 
        - NextTable (bool): 
        - NextTableMiss (bool): 
        - Wildcards (bool): 
        - WriteActions (bool): 
        - WriteActionsMiss (bool): 
        - WriteSetField (bool): 
        - WriteSetFieldMiss (bool): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
