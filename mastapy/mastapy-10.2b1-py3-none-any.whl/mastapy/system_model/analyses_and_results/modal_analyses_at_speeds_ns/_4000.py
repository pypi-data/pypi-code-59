'''_4000.py

BoltedJointModalAnalysesAtSpeeds
'''


from mastapy.system_model.part_model import _2003
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6085
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _4076
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'BoltedJointModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltedJointModalAnalysesAtSpeeds',)


class BoltedJointModalAnalysesAtSpeeds(_4076.SpecialisedAssemblyModalAnalysesAtSpeeds):
    '''BoltedJointModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _BOLTED_JOINT_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BoltedJointModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2003.BoltedJoint':
        '''BoltedJoint: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2003.BoltedJoint)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6085.BoltedJointLoadCase':
        '''BoltedJointLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6085.BoltedJointLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None
