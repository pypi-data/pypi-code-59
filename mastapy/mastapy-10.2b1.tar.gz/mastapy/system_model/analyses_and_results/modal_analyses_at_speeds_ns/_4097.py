'''_4097.py

TorqueConverterModalAnalysesAtSpeeds
'''


from mastapy.system_model.part_model.couplings import _2157
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6220
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _4020
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'TorqueConverterModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterModalAnalysesAtSpeeds',)


class TorqueConverterModalAnalysesAtSpeeds(_4020.CouplingModalAnalysesAtSpeeds):
    '''TorqueConverterModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2157.TorqueConverter':
        '''TorqueConverter: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2157.TorqueConverter)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6220.TorqueConverterLoadCase':
        '''TorqueConverterLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6220.TorqueConverterLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None
