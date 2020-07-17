'''_2856.py

WormGearSetSteadyStateSynchronousResponseAtASpeed
'''


from typing import List

from mastapy.system_model.part_model.gears import _2108
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6231
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _2857, _2855, _2791
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'WormGearSetSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetSteadyStateSynchronousResponseAtASpeed',)


class WormGearSetSteadyStateSynchronousResponseAtASpeed(_2791.GearSetSteadyStateSynchronousResponseAtASpeed):
    '''WormGearSetSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2108.WormGearSet':
        '''WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2108.WormGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6231.WormGearSetLoadCase':
        '''WormGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6231.WormGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def worm_gears_steady_state_synchronous_response_at_a_speed(self) -> 'List[_2857.WormGearSteadyStateSynchronousResponseAtASpeed]':
        '''List[WormGearSteadyStateSynchronousResponseAtASpeed]: 'WormGearsSteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearsSteadyStateSynchronousResponseAtASpeed, constructor.new(_2857.WormGearSteadyStateSynchronousResponseAtASpeed))
        return value

    @property
    def worm_meshes_steady_state_synchronous_response_at_a_speed(self) -> 'List[_2855.WormGearMeshSteadyStateSynchronousResponseAtASpeed]':
        '''List[WormGearMeshSteadyStateSynchronousResponseAtASpeed]: 'WormMeshesSteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormMeshesSteadyStateSynchronousResponseAtASpeed, constructor.new(_2855.WormGearMeshSteadyStateSynchronousResponseAtASpeed))
        return value
