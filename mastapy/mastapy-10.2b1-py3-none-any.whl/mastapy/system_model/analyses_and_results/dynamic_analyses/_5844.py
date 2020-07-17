'''_5844.py

ConceptGearSetDynamicAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2078
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6097
from mastapy.system_model.analyses_and_results.dynamic_analyses import _5842, _5843, _5870
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'ConceptGearSetDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetDynamicAnalysis',)


class ConceptGearSetDynamicAnalysis(_5870.GearSetDynamicAnalysis):
    '''ConceptGearSetDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_GEAR_SET_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearSetDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2078.ConceptGearSet':
        '''ConceptGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2078.ConceptGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6097.ConceptGearSetLoadCase':
        '''ConceptGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6097.ConceptGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def concept_gears_dynamic_analysis(self) -> 'List[_5842.ConceptGearDynamicAnalysis]':
        '''List[ConceptGearDynamicAnalysis]: 'ConceptGearsDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearsDynamicAnalysis, constructor.new(_5842.ConceptGearDynamicAnalysis))
        return value

    @property
    def concept_meshes_dynamic_analysis(self) -> 'List[_5843.ConceptGearMeshDynamicAnalysis]':
        '''List[ConceptGearMeshDynamicAnalysis]: 'ConceptMeshesDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptMeshesDynamicAnalysis, constructor.new(_5843.ConceptGearMeshDynamicAnalysis))
        return value
