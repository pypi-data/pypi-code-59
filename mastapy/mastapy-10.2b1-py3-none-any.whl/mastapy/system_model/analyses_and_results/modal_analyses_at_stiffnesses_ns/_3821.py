'''_3821.py

PointLoadModalAnalysesAtStiffnesses
'''


from mastapy.system_model.part_model import _2029
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6185
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns import _3855
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_MODAL_ANALYSES_AT_STIFFNESSES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtStiffnessesNS', 'PointLoadModalAnalysesAtStiffnesses')


__docformat__ = 'restructuredtext en'
__all__ = ('PointLoadModalAnalysesAtStiffnesses',)


class PointLoadModalAnalysesAtStiffnesses(_3855.VirtualComponentModalAnalysesAtStiffnesses):
    '''PointLoadModalAnalysesAtStiffnesses

    This is a mastapy class.
    '''

    TYPE = _POINT_LOAD_MODAL_ANALYSES_AT_STIFFNESSES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PointLoadModalAnalysesAtStiffnesses.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2029.PointLoad':
        '''PointLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2029.PointLoad)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6185.PointLoadLoadCase':
        '''PointLoadLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6185.PointLoadLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
