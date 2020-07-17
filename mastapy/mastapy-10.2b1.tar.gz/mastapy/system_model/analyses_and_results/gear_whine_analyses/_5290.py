'''_5290.py

ClutchGearWhineAnalysis
'''


from mastapy.system_model.part_model.couplings import _2130
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6089
from mastapy.system_model.analyses_and_results.system_deflections import _2246
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5307
from mastapy._internal.python_net import python_net_import

_CLUTCH_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'ClutchGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchGearWhineAnalysis',)


class ClutchGearWhineAnalysis(_5307.CouplingGearWhineAnalysis):
    '''ClutchGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _CLUTCH_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2130.Clutch':
        '''Clutch: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2130.Clutch)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6089.ClutchLoadCase':
        '''ClutchLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6089.ClutchLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def system_deflection_results(self) -> '_2246.ClutchSystemDeflection':
        '''ClutchSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2246.ClutchSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
