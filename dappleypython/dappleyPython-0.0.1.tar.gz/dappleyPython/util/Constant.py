import math

ADDRESS_CHECKSUM_LENGTH = 4
CHARSET_UTF_8 = "UTF-8"
COIN_SCALE = 9
COIN_DW = math.pow(10, 9)

TxTypeDefault = 0
TxTypeNormal = 1
TxTypeContract = 2
TxTypeCoinbase = 3
TxTypeGasReward = 4
TxTypeGasChange = 5
TxTypeReward = 6
