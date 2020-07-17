'''_2305.py

MeasurementComponentSystemDeflection
'''


from mastapy.system_model.part_model import _2021
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6169
from mastapy.system_model.analyses_and_results.power_flows import _3305
from mastapy.system_model.analyses_and_results.system_deflections import _2357
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'MeasurementComponentSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementComponentSystemDeflection',)


class MeasurementComponentSystemDeflection(_2357.VirtualComponentSystemDeflection):
    '''MeasurementComponentSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _MEASUREMENT_COMPONENT_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MeasurementComponentSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2021.MeasurementComponent':
        '''MeasurementComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2021.MeasurementComponent)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6169.MeasurementComponentLoadCase':
        '''MeasurementComponentLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6169.MeasurementComponentLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def power_flow_results(self) -> '_3305.MeasurementComponentPowerFlow':
        '''MeasurementComponentPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3305.MeasurementComponentPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults else None
