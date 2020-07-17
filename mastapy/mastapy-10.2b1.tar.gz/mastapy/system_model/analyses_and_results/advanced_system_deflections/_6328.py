'''_6328.py

MeasurementComponentAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model import _2021
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6169
from mastapy.system_model.analyses_and_results.system_deflections import _2305
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _6374
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'MeasurementComponentAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementComponentAdvancedSystemDeflection',)


class MeasurementComponentAdvancedSystemDeflection(_6374.VirtualComponentAdvancedSystemDeflection):
    '''MeasurementComponentAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _MEASUREMENT_COMPONENT_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MeasurementComponentAdvancedSystemDeflection.TYPE'):
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
    def component_system_deflection_results(self) -> 'List[_2305.MeasurementComponentSystemDeflection]':
        '''List[MeasurementComponentSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentSystemDeflectionResults, constructor.new(_2305.MeasurementComponentSystemDeflection))
        return value
