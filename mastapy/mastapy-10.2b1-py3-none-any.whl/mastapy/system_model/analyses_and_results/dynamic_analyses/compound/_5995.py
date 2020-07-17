'''_5995.py

HypoidGearSetCompoundDynamicAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2091
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _5993, _5994, _5942
from mastapy.system_model.analyses_and_results.dynamic_analyses import _5874
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'HypoidGearSetCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetCompoundDynamicAnalysis',)


class HypoidGearSetCompoundDynamicAnalysis(_5942.AGMAGleasonConicalGearSetCompoundDynamicAnalysis):
    '''HypoidGearSetCompoundDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSetCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2091.HypoidGearSet':
        '''HypoidGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2091.HypoidGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_2091.HypoidGearSet':
        '''HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2091.HypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def hypoid_gears_compound_dynamic_analysis(self) -> 'List[_5993.HypoidGearCompoundDynamicAnalysis]':
        '''List[HypoidGearCompoundDynamicAnalysis]: 'HypoidGearsCompoundDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearsCompoundDynamicAnalysis, constructor.new(_5993.HypoidGearCompoundDynamicAnalysis))
        return value

    @property
    def hypoid_meshes_compound_dynamic_analysis(self) -> 'List[_5994.HypoidGearMeshCompoundDynamicAnalysis]':
        '''List[HypoidGearMeshCompoundDynamicAnalysis]: 'HypoidMeshesCompoundDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidMeshesCompoundDynamicAnalysis, constructor.new(_5994.HypoidGearMeshCompoundDynamicAnalysis))
        return value

    @property
    def load_case_analyses_ready(self) -> 'List[_5874.HypoidGearSetDynamicAnalysis]':
        '''List[HypoidGearSetDynamicAnalysis]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_5874.HypoidGearSetDynamicAnalysis))
        return value

    @property
    def assembly_dynamic_analysis_load_cases(self) -> 'List[_5874.HypoidGearSetDynamicAnalysis]':
        '''List[HypoidGearSetDynamicAnalysis]: 'AssemblyDynamicAnalysisLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyDynamicAnalysisLoadCases, constructor.new(_5874.HypoidGearSetDynamicAnalysis))
        return value
