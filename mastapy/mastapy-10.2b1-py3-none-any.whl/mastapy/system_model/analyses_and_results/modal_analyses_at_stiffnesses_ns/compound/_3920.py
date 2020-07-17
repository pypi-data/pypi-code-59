'''_3920.py

ImportedFEComponentCompoundModalAnalysesAtStiffnesses
'''


from typing import List

from mastapy.system_model.part_model import _2016
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns import _3797
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns.compound import _3863
from mastapy._internal.python_net import python_net_import

_IMPORTED_FE_COMPONENT_COMPOUND_MODAL_ANALYSES_AT_STIFFNESSES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtStiffnessesNS.Compound', 'ImportedFEComponentCompoundModalAnalysesAtStiffnesses')


__docformat__ = 'restructuredtext en'
__all__ = ('ImportedFEComponentCompoundModalAnalysesAtStiffnesses',)


class ImportedFEComponentCompoundModalAnalysesAtStiffnesses(_3863.AbstractShaftOrHousingCompoundModalAnalysesAtStiffnesses):
    '''ImportedFEComponentCompoundModalAnalysesAtStiffnesses

    This is a mastapy class.
    '''

    TYPE = _IMPORTED_FE_COMPONENT_COMPOUND_MODAL_ANALYSES_AT_STIFFNESSES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ImportedFEComponentCompoundModalAnalysesAtStiffnesses.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2016.ImportedFEComponent':
        '''ImportedFEComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2016.ImportedFEComponent)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def load_case_analyses_ready(self) -> 'List[_3797.ImportedFEComponentModalAnalysesAtStiffnesses]':
        '''List[ImportedFEComponentModalAnalysesAtStiffnesses]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_3797.ImportedFEComponentModalAnalysesAtStiffnesses))
        return value

    @property
    def component_modal_analyses_at_stiffnesses_load_cases(self) -> 'List[_3797.ImportedFEComponentModalAnalysesAtStiffnesses]':
        '''List[ImportedFEComponentModalAnalysesAtStiffnesses]: 'ComponentModalAnalysesAtStiffnessesLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentModalAnalysesAtStiffnessesLoadCases, constructor.new(_3797.ImportedFEComponentModalAnalysesAtStiffnesses))
        return value

    @property
    def planetaries(self) -> 'List[ImportedFEComponentCompoundModalAnalysesAtStiffnesses]':
        '''List[ImportedFEComponentCompoundModalAnalysesAtStiffnesses]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(ImportedFEComponentCompoundModalAnalysesAtStiffnesses))
        return value
