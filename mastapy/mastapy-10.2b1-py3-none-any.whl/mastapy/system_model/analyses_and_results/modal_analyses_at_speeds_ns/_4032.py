'''_4032.py

FaceGearModalAnalysesAtSpeeds
'''


from mastapy.system_model.part_model.gears import _2084
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6133
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _4036
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'FaceGearModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearModalAnalysesAtSpeeds',)


class FaceGearModalAnalysesAtSpeeds(_4036.GearModalAnalysesAtSpeeds):
    '''FaceGearModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2084.FaceGear':
        '''FaceGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2084.FaceGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6133.FaceGearLoadCase':
        '''FaceGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6133.FaceGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
