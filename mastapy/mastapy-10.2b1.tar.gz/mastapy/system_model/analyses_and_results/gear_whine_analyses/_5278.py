'''_5278.py

BeltDriveGearWhineAnalysis
'''


from mastapy.system_model.part_model.couplings import _2128
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6076
from mastapy.system_model.analyses_and_results.system_deflections import _2233
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5384
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'BeltDriveGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BeltDriveGearWhineAnalysis',)


class BeltDriveGearWhineAnalysis(_5384.SpecialisedAssemblyGearWhineAnalysis):
    '''BeltDriveGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _BELT_DRIVE_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BeltDriveGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2128.BeltDrive':
        '''BeltDrive: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2128.BeltDrive)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6076.BeltDriveLoadCase':
        '''BeltDriveLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6076.BeltDriveLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def system_deflection_results(self) -> '_2233.BeltDriveSystemDeflection':
        '''BeltDriveSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2233.BeltDriveSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
