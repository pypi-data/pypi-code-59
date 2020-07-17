'''_3846.py

SynchroniserHalfModalAnalysesAtStiffnesses
'''


from mastapy.system_model.part_model.couplings import _2154
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6213
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns import _3848
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_MODAL_ANALYSES_AT_STIFFNESSES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtStiffnessesNS', 'SynchroniserHalfModalAnalysesAtStiffnesses')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserHalfModalAnalysesAtStiffnesses',)


class SynchroniserHalfModalAnalysesAtStiffnesses(_3848.SynchroniserPartModalAnalysesAtStiffnesses):
    '''SynchroniserHalfModalAnalysesAtStiffnesses

    This is a mastapy class.
    '''

    TYPE = _SYNCHRONISER_HALF_MODAL_ANALYSES_AT_STIFFNESSES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SynchroniserHalfModalAnalysesAtStiffnesses.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2154.SynchroniserHalf':
        '''SynchroniserHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2154.SynchroniserHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6213.SynchroniserHalfLoadCase':
        '''SynchroniserHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6213.SynchroniserHalfLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
