'''_6273.py

BoltedJointAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model import _2003
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6085
from mastapy.system_model.analyses_and_results.system_deflections import _2242
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _6348
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'BoltedJointAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltedJointAdvancedSystemDeflection',)


class BoltedJointAdvancedSystemDeflection(_6348.SpecialisedAssemblyAdvancedSystemDeflection):
    '''BoltedJointAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _BOLTED_JOINT_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BoltedJointAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2003.BoltedJoint':
        '''BoltedJoint: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2003.BoltedJoint)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6085.BoltedJointLoadCase':
        '''BoltedJointLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6085.BoltedJointLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2242.BoltedJointSystemDeflection]':
        '''List[BoltedJointSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySystemDeflectionResults, constructor.new(_2242.BoltedJointSystemDeflection))
        return value
