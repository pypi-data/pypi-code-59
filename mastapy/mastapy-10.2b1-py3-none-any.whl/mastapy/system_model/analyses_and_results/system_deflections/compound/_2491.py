'''_2491.py

WormGearSetCompoundSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model.gears import _2108
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.worm import _177
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2489, _2490, _2426
from mastapy.system_model.analyses_and_results.system_deflections import _2359
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'WormGearSetCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetCompoundSystemDeflection',)


class WormGearSetCompoundSystemDeflection(_2426.GearSetCompoundSystemDeflection):
    '''WormGearSetCompoundSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2108.WormGearSet':
        '''WormGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2108.WormGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_2108.WormGearSet':
        '''WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2108.WormGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def worm_gear_set_rating(self) -> '_177.WormGearSetDutyCycleRating':
        '''WormGearSetDutyCycleRating: 'WormGearSetRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_177.WormGearSetDutyCycleRating)(self.wrapped.WormGearSetRating) if self.wrapped.WormGearSetRating else None

    @property
    def worm_gears_compound_system_deflection(self) -> 'List[_2489.WormGearCompoundSystemDeflection]':
        '''List[WormGearCompoundSystemDeflection]: 'WormGearsCompoundSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearsCompoundSystemDeflection, constructor.new(_2489.WormGearCompoundSystemDeflection))
        return value

    @property
    def worm_meshes_compound_system_deflection(self) -> 'List[_2490.WormGearMeshCompoundSystemDeflection]':
        '''List[WormGearMeshCompoundSystemDeflection]: 'WormMeshesCompoundSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormMeshesCompoundSystemDeflection, constructor.new(_2490.WormGearMeshCompoundSystemDeflection))
        return value

    @property
    def load_case_analyses_ready(self) -> 'List[_2359.WormGearSetSystemDeflection]':
        '''List[WormGearSetSystemDeflection]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_2359.WormGearSetSystemDeflection))
        return value

    @property
    def assembly_system_deflection_load_cases(self) -> 'List[_2359.WormGearSetSystemDeflection]':
        '''List[WormGearSetSystemDeflection]: 'AssemblySystemDeflectionLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySystemDeflectionLoadCases, constructor.new(_2359.WormGearSetSystemDeflection))
        return value
