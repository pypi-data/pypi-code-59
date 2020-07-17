'''_2341.py

StraightBevelPlanetGearSystemDeflection
'''


from mastapy.system_model.part_model.gears import _2105
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _3340
from mastapy.system_model.analyses_and_results.system_deflections import _2337
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'StraightBevelPlanetGearSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelPlanetGearSystemDeflection',)


class StraightBevelPlanetGearSystemDeflection(_2337.StraightBevelDiffGearSystemDeflection):
    '''StraightBevelPlanetGearSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelPlanetGearSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2105.StraightBevelPlanetGear':
        '''StraightBevelPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2105.StraightBevelPlanetGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def power_flow_results(self) -> '_3340.StraightBevelPlanetGearPowerFlow':
        '''StraightBevelPlanetGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3340.StraightBevelPlanetGearPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults else None
