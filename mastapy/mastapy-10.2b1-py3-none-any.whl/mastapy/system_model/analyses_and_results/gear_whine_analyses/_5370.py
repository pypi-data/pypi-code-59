'''_5370.py

PlanetaryConnectionGearWhineAnalysis
'''


from mastapy.system_model.connections_and_sockets import _1863
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6179
from mastapy.system_model.analyses_and_results.system_deflections import _2314
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5382
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'PlanetaryConnectionGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetaryConnectionGearWhineAnalysis',)


class PlanetaryConnectionGearWhineAnalysis(_5382.ShaftToMountableComponentConnectionGearWhineAnalysis):
    '''PlanetaryConnectionGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _PLANETARY_CONNECTION_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PlanetaryConnectionGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def connection_design(self) -> '_1863.PlanetaryConnection':
        '''PlanetaryConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1863.PlanetaryConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_load_case(self) -> '_6179.PlanetaryConnectionLoadCase':
        '''PlanetaryConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6179.PlanetaryConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase else None

    @property
    def system_deflection_results(self) -> '_2314.PlanetaryConnectionSystemDeflection':
        '''PlanetaryConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2314.PlanetaryConnectionSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
