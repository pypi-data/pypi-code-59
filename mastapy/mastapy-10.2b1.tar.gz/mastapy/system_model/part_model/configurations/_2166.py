'''_2166.py

BearingDetailSelection
'''


from mastapy.system_model.part_model.configurations import _2168
from mastapy.system_model.part_model import _2000
from mastapy.bearings.bearing_designs import _1744
from mastapy._internal.python_net import python_net_import

_BEARING_DETAIL_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Configurations', 'BearingDetailSelection')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingDetailSelection',)


class BearingDetailSelection(_2168.PartDetailSelection['_2000.Bearing', '_1744.BearingDesign']):
    '''BearingDetailSelection

    This is a mastapy class.
    '''

    TYPE = _BEARING_DETAIL_SELECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BearingDetailSelection.TYPE'):
        super().__init__(instance_to_wrap)
