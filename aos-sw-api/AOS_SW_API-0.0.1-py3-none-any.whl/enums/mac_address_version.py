from enum import Enum


class MacAddressVersion(str, Enum):
    MAV_EUI_48 = "MAV_EUI_48"
    MAV_EUI_64 = "MAV_EUI_64"
