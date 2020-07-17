'''_2717.py

StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft
'''


from typing import List

from mastapy.system_model.part_model.gears import _2102
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _2715, _2716, _2634
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _2595
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound', 'StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft',)


class StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft(_2634.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft):
    '''StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2102.StraightBevelDiffGearSet':
        '''StraightBevelDiffGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2102.StraightBevelDiffGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_2102.StraightBevelDiffGearSet':
        '''StraightBevelDiffGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2102.StraightBevelDiffGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def straight_bevel_diff_gears_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'List[_2715.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft]: 'StraightBevelDiffGearsCompoundSteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearsCompoundSteadyStateSynchronousResponseOnAShaft, constructor.new(_2715.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def straight_bevel_diff_meshes_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'List[_2716.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft]: 'StraightBevelDiffMeshesCompoundSteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffMeshesCompoundSteadyStateSynchronousResponseOnAShaft, constructor.new(_2716.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def load_case_analyses_ready(self) -> 'List[_2595.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft]':
        '''List[StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_2595.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def assembly_steady_state_synchronous_response_on_a_shaft_load_cases(self) -> 'List[_2595.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft]':
        '''List[StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft]: 'AssemblySteadyStateSynchronousResponseOnAShaftLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySteadyStateSynchronousResponseOnAShaftLoadCases, constructor.new(_2595.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft))
        return value
