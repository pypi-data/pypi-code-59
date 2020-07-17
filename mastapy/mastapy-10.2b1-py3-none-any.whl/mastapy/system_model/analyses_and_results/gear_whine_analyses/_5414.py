'''_5414.py

ZerolBevelGearGearWhineAnalysis
'''


from mastapy.system_model.part_model.gears import _2109
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6232
from mastapy.system_model.analyses_and_results.system_deflections import _2363
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5284
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'ZerolBevelGearGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearGearWhineAnalysis',)


class ZerolBevelGearGearWhineAnalysis(_5284.BevelGearGearWhineAnalysis):
    '''ZerolBevelGearGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _ZEROL_BEVEL_GEAR_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2109.ZerolBevelGear':
        '''ZerolBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2109.ZerolBevelGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6232.ZerolBevelGearLoadCase':
        '''ZerolBevelGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6232.ZerolBevelGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def system_deflection_results(self) -> '_2363.ZerolBevelGearSystemDeflection':
        '''ZerolBevelGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2363.ZerolBevelGearSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
