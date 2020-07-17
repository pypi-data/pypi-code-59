'''_6354.py

SpringDamperHalfAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2151
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6202
from mastapy.system_model.analyses_and_results.system_deflections import _2333
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _6293
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'SpringDamperHalfAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperHalfAdvancedSystemDeflection',)


class SpringDamperHalfAdvancedSystemDeflection(_6293.CouplingHalfAdvancedSystemDeflection):
    '''SpringDamperHalfAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _SPRING_DAMPER_HALF_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperHalfAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2151.SpringDamperHalf':
        '''SpringDamperHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2151.SpringDamperHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6202.SpringDamperHalfLoadCase':
        '''SpringDamperHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6202.SpringDamperHalfLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def component_system_deflection_results(self) -> 'List[_2333.SpringDamperHalfSystemDeflection]':
        '''List[SpringDamperHalfSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentSystemDeflectionResults, constructor.new(_2333.SpringDamperHalfSystemDeflection))
        return value
