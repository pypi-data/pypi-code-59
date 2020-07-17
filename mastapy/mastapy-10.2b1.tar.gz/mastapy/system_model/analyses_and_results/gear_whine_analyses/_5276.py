'''_5276.py

BearingGearWhineAnalysis
'''


from typing import List

from mastapy.bearings.bearing_results.rolling import _1693
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2000
from mastapy.system_model.analyses_and_results.static_loads import _6074
from mastapy.system_model.analyses_and_results.system_deflections import _2231
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5305
from mastapy._internal.python_net import python_net_import

_BEARING_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'BearingGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingGearWhineAnalysis',)


class BearingGearWhineAnalysis(_5305.ConnectorGearWhineAnalysis):
    '''BearingGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _BEARING_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BearingGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def rolling_bearing_speed_results(self) -> '_1693.RollingBearingSpeedResults':
        '''RollingBearingSpeedResults: 'RollingBearingSpeedResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1693.RollingBearingSpeedResults)(self.wrapped.RollingBearingSpeedResults) if self.wrapped.RollingBearingSpeedResults else None

    @property
    def component_design(self) -> '_2000.Bearing':
        '''Bearing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2000.Bearing)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6074.BearingLoadCase':
        '''BearingLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6074.BearingLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def system_deflection_results(self) -> '_2231.BearingSystemDeflection':
        '''BearingSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2231.BearingSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None

    @property
    def planetaries(self) -> 'List[BearingGearWhineAnalysis]':
        '''List[BearingGearWhineAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(BearingGearWhineAnalysis))
        return value
