'''_4093.py

SynchroniserModalAnalysesAtSpeeds
'''


from mastapy.system_model.part_model.couplings import _2152
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6214
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _4076
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'SynchroniserModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserModalAnalysesAtSpeeds',)


class SynchroniserModalAnalysesAtSpeeds(_4076.SpecialisedAssemblyModalAnalysesAtSpeeds):
    '''SynchroniserModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _SYNCHRONISER_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SynchroniserModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2152.Synchroniser':
        '''Synchroniser: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2152.Synchroniser)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6214.SynchroniserLoadCase':
        '''SynchroniserLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6214.SynchroniserLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None
