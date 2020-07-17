'''_6332.py

PartToPartShearCouplingAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2139
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6178
from mastapy.system_model.analyses_and_results.system_deflections import _2313
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _6291
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'PartToPartShearCouplingAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingAdvancedSystemDeflection',)


class PartToPartShearCouplingAdvancedSystemDeflection(_6291.CouplingAdvancedSystemDeflection):
    '''PartToPartShearCouplingAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _PART_TO_PART_SHEAR_COUPLING_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingAdvancedSystemDeflection.TYPE'):
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

    @property
    def assembly_system_deflection_results(self) -> 'List[_2313.PartToPartShearCouplingSystemDeflection]':
        '''List[PartToPartShearCouplingSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySystemDeflectionResults, constructor.new(_2313.PartToPartShearCouplingSystemDeflection))
        return value
