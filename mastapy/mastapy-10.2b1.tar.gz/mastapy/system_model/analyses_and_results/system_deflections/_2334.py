'''_2334.py

SpringDamperSystemDeflection
'''


from mastapy.system_model.part_model.couplings import _2150
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6203
from mastapy.system_model.analyses_and_results.power_flows import _3333
from mastapy.system_model.analyses_and_results.system_deflections import _2264
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'SpringDamperSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperSystemDeflection',)


class SpringDamperSystemDeflection(_2264.CouplingSystemDeflection):
    '''SpringDamperSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _SPRING_DAMPER_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2150.SpringDamper':
        '''SpringDamper: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2150.SpringDamper)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6203.SpringDamperLoadCase':
        '''SpringDamperLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6203.SpringDamperLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def power_flow_results(self) -> '_3333.SpringDamperPowerFlow':
        '''SpringDamperPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3333.SpringDamperPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults else None
