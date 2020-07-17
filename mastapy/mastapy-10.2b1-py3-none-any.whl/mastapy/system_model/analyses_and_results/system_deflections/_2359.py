'''_2359.py

WormGearSetSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model.gears import _2108
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6231
from mastapy.system_model.analyses_and_results.power_flows import _3355
from mastapy.gears.rating.worm import _178
from mastapy.system_model.analyses_and_results.system_deflections import _2360, _2358, _2286
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'WormGearSetSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetSystemDeflection',)


class WormGearSetSystemDeflection(_2286.GearSetSystemDeflection):
    '''WormGearSetSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_SET_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2108.WormGearSet':
        '''WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2108.WormGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6231.WormGearSetLoadCase':
        '''WormGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6231.WormGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def power_flow_results(self) -> '_3355.WormGearSetPowerFlow':
        '''WormGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3355.WormGearSetPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults else None

    @property
    def rating(self) -> '_178.WormGearSetRating':
        '''WormGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_178.WormGearSetRating)(self.wrapped.Rating) if self.wrapped.Rating else None

    @property
    def component_detailed_analysis(self) -> '_178.WormGearSetRating':
        '''WormGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_178.WormGearSetRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def worm_gears_system_deflection(self) -> 'List[_2360.WormGearSystemDeflection]':
        '''List[WormGearSystemDeflection]: 'WormGearsSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearsSystemDeflection, constructor.new(_2360.WormGearSystemDeflection))
        return value

    @property
    def worm_meshes_system_deflection(self) -> 'List[_2358.WormGearMeshSystemDeflection]':
        '''List[WormGearMeshSystemDeflection]: 'WormMeshesSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormMeshesSystemDeflection, constructor.new(_2358.WormGearMeshSystemDeflection))
        return value
