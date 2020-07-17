'''_4726.py

BevelDifferentialGearModalAnalysis
'''


from mastapy.system_model.part_model.gears import _2071
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6077
from mastapy.system_model.analyses_and_results.system_deflections import _2236
from mastapy.system_model.analyses_and_results.modal_analyses import _4731
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'BevelDifferentialGearModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearModalAnalysis',)


class BevelDifferentialGearModalAnalysis(_4731.BevelGearModalAnalysis):
    '''BevelDifferentialGearModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2071.BevelDifferentialGear':
        '''BevelDifferentialGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2071.BevelDifferentialGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6077.BevelDifferentialGearLoadCase':
        '''BevelDifferentialGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6077.BevelDifferentialGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def system_deflection_results(self) -> '_2236.BevelDifferentialGearSystemDeflection':
        '''BevelDifferentialGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2236.BevelDifferentialGearSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
