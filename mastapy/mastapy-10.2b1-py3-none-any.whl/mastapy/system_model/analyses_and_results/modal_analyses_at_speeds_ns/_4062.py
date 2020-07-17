'''_4062.py

PartToPartShearCouplingModalAnalysesAtSpeeds
'''


from mastapy.system_model.part_model.couplings import _2139
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6178
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _4020
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'PartToPartShearCouplingModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingModalAnalysesAtSpeeds',)


class PartToPartShearCouplingModalAnalysesAtSpeeds(_4020.CouplingModalAnalysesAtSpeeds):
    '''PartToPartShearCouplingModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _PART_TO_PART_SHEAR_COUPLING_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2139.PartToPartShearCoupling':
        '''PartToPartShearCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2139.PartToPartShearCoupling)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6178.PartToPartShearCouplingLoadCase':
        '''PartToPartShearCouplingLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6178.PartToPartShearCouplingLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None
