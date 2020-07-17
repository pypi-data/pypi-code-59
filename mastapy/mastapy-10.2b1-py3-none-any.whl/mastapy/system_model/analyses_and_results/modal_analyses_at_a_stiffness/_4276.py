'''_4276.py

ExternalCADModelModalAnalysisAtAStiffness
'''


from mastapy.system_model.part_model import _2011
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6132
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4252
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'ExternalCADModelModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('ExternalCADModelModalAnalysisAtAStiffness',)


class ExternalCADModelModalAnalysisAtAStiffness(_4252.ComponentModalAnalysisAtAStiffness):
    '''ExternalCADModelModalAnalysisAtAStiffness

    This is a mastapy class.
    '''

    TYPE = _EXTERNAL_CAD_MODEL_MODAL_ANALYSIS_AT_A_STIFFNESS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ExternalCADModelModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2011.ExternalCADModel':
        '''ExternalCADModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2011.ExternalCADModel)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6132.ExternalCADModelLoadCase':
        '''ExternalCADModelLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6132.ExternalCADModelLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
