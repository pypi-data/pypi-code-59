'''_4072.py

RootAssemblyModalAnalysesAtSpeeds
'''


from mastapy.system_model.part_model import _2032
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _4083, _3988
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'RootAssemblyModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyModalAnalysesAtSpeeds',)


class RootAssemblyModalAnalysesAtSpeeds(_3988.AssemblyModalAnalysesAtSpeeds):
    '''RootAssemblyModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _ROOT_ASSEMBLY_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RootAssemblyModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2032.RootAssembly':
        '''RootAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2032.RootAssembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def modal_analyses_at_speeds_inputs(self) -> '_4083.StabilityAnalysis':
        '''StabilityAnalysis: 'ModalAnalysesAtSpeedsInputs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_4083.StabilityAnalysis)(self.wrapped.ModalAnalysesAtSpeedsInputs) if self.wrapped.ModalAnalysesAtSpeedsInputs else None
