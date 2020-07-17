'''_3860.py

ZerolBevelGearModalAnalysesAtStiffnesses
'''


from mastapy.system_model.part_model.gears import _2109
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6232
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns import _3753
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MODAL_ANALYSES_AT_STIFFNESSES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtStiffnessesNS', 'ZerolBevelGearModalAnalysesAtStiffnesses')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearModalAnalysesAtStiffnesses',)


class ZerolBevelGearModalAnalysesAtStiffnesses(_3753.BevelGearModalAnalysesAtStiffnesses):
    '''ZerolBevelGearModalAnalysesAtStiffnesses

    This is a mastapy class.
    '''

    TYPE = _ZEROL_BEVEL_GEAR_MODAL_ANALYSES_AT_STIFFNESSES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearModalAnalysesAtStiffnesses.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2109.ZerolBevelGear':
        '''ZerolBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2109.ZerolBevelGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6232.ZerolBevelGearLoadCase':
        '''ZerolBevelGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6232.ZerolBevelGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
