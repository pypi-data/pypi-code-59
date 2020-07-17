'''_4287.py

HypoidGearSetModalAnalysisAtAStiffness
'''


from typing import List

from mastapy.system_model.part_model.gears import _2091
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6155
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4286, _4285, _4233
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'HypoidGearSetModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetModalAnalysisAtAStiffness',)


class HypoidGearSetModalAnalysisAtAStiffness(_4233.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness):
    '''HypoidGearSetModalAnalysisAtAStiffness

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSetModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2091.HypoidGearSet':
        '''HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2091.HypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6155.HypoidGearSetLoadCase':
        '''HypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6155.HypoidGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def hypoid_gears_modal_analysis_at_a_stiffness(self) -> 'List[_4286.HypoidGearModalAnalysisAtAStiffness]':
        '''List[HypoidGearModalAnalysisAtAStiffness]: 'HypoidGearsModalAnalysisAtAStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearsModalAnalysisAtAStiffness, constructor.new(_4286.HypoidGearModalAnalysisAtAStiffness))
        return value

    @property
    def hypoid_meshes_modal_analysis_at_a_stiffness(self) -> 'List[_4285.HypoidGearMeshModalAnalysisAtAStiffness]':
        '''List[HypoidGearMeshModalAnalysisAtAStiffness]: 'HypoidMeshesModalAnalysisAtAStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidMeshesModalAnalysisAtAStiffness, constructor.new(_4285.HypoidGearMeshModalAnalysisAtAStiffness))
        return value
