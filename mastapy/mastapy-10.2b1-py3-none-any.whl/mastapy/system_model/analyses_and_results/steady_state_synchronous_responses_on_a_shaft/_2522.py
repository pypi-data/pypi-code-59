'''_2522.py

ConceptCouplingSteadyStateSynchronousResponseOnAShaft
'''


from mastapy.system_model.part_model.couplings import _2133
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6094
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _2533
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'ConceptCouplingSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingSteadyStateSynchronousResponseOnAShaft',)


class ConceptCouplingSteadyStateSynchronousResponseOnAShaft(_2533.CouplingSteadyStateSynchronousResponseOnAShaft):
    '''ConceptCouplingSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2133.ConceptCoupling':
        '''ConceptCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2133.ConceptCoupling)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6094.ConceptCouplingLoadCase':
        '''ConceptCouplingLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6094.ConceptCouplingLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None
