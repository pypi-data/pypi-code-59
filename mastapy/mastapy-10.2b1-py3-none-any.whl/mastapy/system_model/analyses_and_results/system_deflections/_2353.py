'''_2353.py

TorqueConverterTurbineSystemDeflection
'''


from mastapy.system_model.part_model.couplings import _2160
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6222
from mastapy.system_model.analyses_and_results.power_flows import _3350
from mastapy.system_model.analyses_and_results.system_deflections import _2263
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'TorqueConverterTurbineSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterTurbineSystemDeflection',)


class TorqueConverterTurbineSystemDeflection(_2263.CouplingHalfSystemDeflection):
    '''TorqueConverterTurbineSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_TURBINE_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterTurbineSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2160.TorqueConverterTurbine':
        '''TorqueConverterTurbine: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2160.TorqueConverterTurbine)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6222.TorqueConverterTurbineLoadCase':
        '''TorqueConverterTurbineLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6222.TorqueConverterTurbineLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def power_flow_results(self) -> '_3350.TorqueConverterTurbinePowerFlow':
        '''TorqueConverterTurbinePowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3350.TorqueConverterTurbinePowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults else None
