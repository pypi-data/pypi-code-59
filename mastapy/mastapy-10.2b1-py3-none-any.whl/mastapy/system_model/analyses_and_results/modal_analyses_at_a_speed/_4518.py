'''_4518.py

DatumModalAnalysisAtASpeed
'''


from mastapy.system_model.part_model import _2008
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6119
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _4496
from mastapy._internal.python_net import python_net_import

_DATUM_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'DatumModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('DatumModalAnalysisAtASpeed',)


class DatumModalAnalysisAtASpeed(_4496.ComponentModalAnalysisAtASpeed):
    '''DatumModalAnalysisAtASpeed

    This is a mastapy class.
    '''

    TYPE = _DATUM_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DatumModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2008.Datum':
        '''Datum: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2008.Datum)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6119.DatumLoadCase':
        '''DatumLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6119.DatumLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
