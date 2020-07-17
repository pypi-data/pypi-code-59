'''_2778.py

CVTPulleySteadyStateSynchronousResponseAtASpeed
'''


from mastapy.system_model.part_model.couplings import _2138
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _2821
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'CVTPulleySteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTPulleySteadyStateSynchronousResponseAtASpeed',)


class CVTPulleySteadyStateSynchronousResponseAtASpeed(_2821.PulleySteadyStateSynchronousResponseAtASpeed):
    '''CVTPulleySteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    '''

    TYPE = _CVT_PULLEY_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CVTPulleySteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2138.CVTPulley':
        '''CVTPulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2138.CVTPulley)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None
