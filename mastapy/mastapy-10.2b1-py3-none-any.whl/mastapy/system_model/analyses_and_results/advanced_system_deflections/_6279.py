'''_6279.py

ConceptCouplingAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2133
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6094
from mastapy.system_model.analyses_and_results.system_deflections import _2252
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _6291
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'ConceptCouplingAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingAdvancedSystemDeflection',)


class ConceptCouplingAdvancedSystemDeflection(_6291.CouplingAdvancedSystemDeflection):
    '''ConceptCouplingAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_COUPLING_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2133.ConceptCoupling':
        '''ConceptCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2133.ConceptCoupling)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6094.ConceptCouplingLoadCase':
        '''ConceptCouplingLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6094.ConceptCouplingLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2252.ConceptCouplingSystemDeflection]':
        '''List[ConceptCouplingSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySystemDeflectionResults, constructor.new(_2252.ConceptCouplingSystemDeflection))
        return value
