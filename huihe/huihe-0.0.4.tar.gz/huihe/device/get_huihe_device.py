from huihe.device.huiHeLight import HuiHeLight
from huihe.device.huiHeSwitch import HuiHeSwitch
from huihe.device.HuiHeIR import HuiHeIR
from huihe.device.HuiHeClimate import HuiHeClimate
from huihe.device.constant import SWITCH_OEM_MODEL,LIGHT_OEM_MODEL,HUMIDIFIER_OEM_MODEL,IRDEVICE_OEM_MODEL

def get_huihe_device(hass,data, api):
    dev_type = data["device"]["oem_model"]
    devices = []
    data=data["device"]
    if dev_type in LIGHT_OEM_MODEL:
        devices.append(HuiHeLight(hass,data, api))
    elif dev_type in HUMIDIFIER_OEM_MODEL:
        devices.append(HuiHeClimate(hass,data, api))
    elif dev_type in IRDEVICE_OEM_MODEL:
        devis_list = HuiHeIR(hass,data, api)
        for device in devis_list:
            devices.append(device)
    # elif dev_type == 'fan':
    #     devices.append(TuyaFanDevice(data, api))
    # elif dev_type == 'cover':
    #     devices.append(TuyaCover(data, api))
    # elif dev_type == 'lock':
    #     devices.append(TuyaLock(data, api))
    elif dev_type in SWITCH_OEM_MODEL:
        devices.append(HuiHeSwitch(hass,data, api))
    return devices



