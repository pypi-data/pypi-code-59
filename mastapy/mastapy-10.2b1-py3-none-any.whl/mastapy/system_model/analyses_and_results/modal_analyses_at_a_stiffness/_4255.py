'''_4255.py

ConceptCouplingModalAnalysisAtAStiffness
'''


from mastapy.system_model.part_model.couplings import _2133
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6094
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4266
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'ConceptCouplingModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingModalAnalysisAtAStiffness',)


class ConceptCouplingModalAnalysisAtAStiffness(_4266.CouplingModalAnalysisAtAStiffness):
    '''ConceptCouplingModalAnalysisAtAStiffness

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_COUPLING_MODAL_ANALYSIS_AT_A_STIFFNESS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingModalAnalysisAtAStiffness.TYPE'):
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
