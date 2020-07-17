'''_4269.py

CVTPulleyModalAnalysisAtAStiffness
'''


from mastapy.system_model.part_model.couplings import _2138
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4313
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'CVTPulleyModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTPulleyModalAnalysisAtAStiffness',)


class CVTPulleyModalAnalysisAtAStiffness(_4313.PulleyModalAnalysisAtAStiffness):
    '''CVTPulleyModalAnalysisAtAStiffness

    This is a mastapy class.
    '''

    TYPE = _CVT_PULLEY_MODAL_ANALYSIS_AT_A_STIFFNESS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CVTPulleyModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2138.CVTPulley':
        '''CVTPulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2138.CVTPulley)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None
