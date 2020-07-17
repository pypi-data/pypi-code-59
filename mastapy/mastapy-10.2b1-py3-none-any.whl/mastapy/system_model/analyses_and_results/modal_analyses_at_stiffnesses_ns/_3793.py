'''_3793.py

GuideDxfModelModalAnalysesAtStiffnesses
'''


from mastapy.system_model.part_model import _2013
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6144
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns import _3761
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_MODAL_ANALYSES_AT_STIFFNESSES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtStiffnessesNS', 'GuideDxfModelModalAnalysesAtStiffnesses')


__docformat__ = 'restructuredtext en'
__all__ = ('GuideDxfModelModalAnalysesAtStiffnesses',)


class GuideDxfModelModalAnalysesAtStiffnesses(_3761.ComponentModalAnalysesAtStiffnesses):
    '''GuideDxfModelModalAnalysesAtStiffnesses

    This is a mastapy class.
    '''

    TYPE = _GUIDE_DXF_MODEL_MODAL_ANALYSES_AT_STIFFNESSES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GuideDxfModelModalAnalysesAtStiffnesses.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2013.GuideDxfModel':
        '''GuideDxfModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2013.GuideDxfModel)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6144.GuideDxfModelLoadCase':
        '''GuideDxfModelLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6144.GuideDxfModelLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
