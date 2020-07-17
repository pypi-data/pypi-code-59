'''_5315.py

CylindricalPlanetGearGearWhineAnalysis
'''


from mastapy.system_model.part_model.gears import _2083
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2277
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5312
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'CylindricalPlanetGearGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalPlanetGearGearWhineAnalysis',)


class CylindricalPlanetGearGearWhineAnalysis(_5312.CylindricalGearGearWhineAnalysis):
    '''CylindricalPlanetGearGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_PLANET_GEAR_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalPlanetGearGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2083.CylindricalPlanetGear':
        '''CylindricalPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2083.CylindricalPlanetGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def system_deflection_results(self) -> '_2277.CylindricalPlanetGearSystemDeflection':
        '''CylindricalPlanetGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2277.CylindricalPlanetGearSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
