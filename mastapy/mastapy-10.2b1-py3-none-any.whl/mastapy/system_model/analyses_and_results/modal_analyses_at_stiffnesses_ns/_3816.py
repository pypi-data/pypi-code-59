'''_3816.py

PartToPartShearCouplingHalfModalAnalysesAtStiffnesses
'''


from mastapy.system_model.part_model.couplings import _2140
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6177
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns import _3774
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_MODAL_ANALYSES_AT_STIFFNESSES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtStiffnessesNS', 'PartToPartShearCouplingHalfModalAnalysesAtStiffnesses')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingHalfModalAnalysesAtStiffnesses',)


class PartToPartShearCouplingHalfModalAnalysesAtStiffnesses(_3774.CouplingHalfModalAnalysesAtStiffnesses):
    '''PartToPartShearCouplingHalfModalAnalysesAtStiffnesses

    This is a mastapy class.
    '''

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_MODAL_ANALYSES_AT_STIFFNESSES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingHalfModalAnalysesAtStiffnesses.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2140.PartToPartShearCouplingHalf':
        '''PartToPartShearCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2140.PartToPartShearCouplingHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6177.PartToPartShearCouplingHalfLoadCase':
        '''PartToPartShearCouplingHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6177.PartToPartShearCouplingHalfLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
