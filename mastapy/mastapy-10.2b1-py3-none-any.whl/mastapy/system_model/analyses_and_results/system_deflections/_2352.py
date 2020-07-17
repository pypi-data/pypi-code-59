'''_2352.py

TorqueConverterSystemDeflection
'''


from mastapy.system_model.part_model.couplings import _2157
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6220
from mastapy.system_model.analyses_and_results.power_flows import _3348
from mastapy.system_model.analyses_and_results.system_deflections import _2264
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'TorqueConverterSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterSystemDeflection',)


class TorqueConverterSystemDeflection(_2264.CouplingSystemDeflection):
    '''TorqueConverterSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterSystemDeflection.TYPE'):
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

    @property
    def power_flow_results(self) -> '_3348.TorqueConverterPowerFlow':
        '''TorqueConverterPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3348.TorqueConverterPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults else None
