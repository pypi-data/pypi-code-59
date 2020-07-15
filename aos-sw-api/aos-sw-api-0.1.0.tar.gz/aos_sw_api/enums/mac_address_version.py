from enum import Enum


class MacAddressVersionEnum(str, Enum):
    MAV_EUI_48 = "MAV_EUI_48"
    MAV_EUI_64 = "MAV_EUI_64"
