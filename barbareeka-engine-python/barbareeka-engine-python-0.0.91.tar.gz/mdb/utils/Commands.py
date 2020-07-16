import enum


class Commands(object):
    class AndroidCommands(enum.Enum):
        LIST_ALL_DEVICES = "adb devices -l"
        ADB_HEADER = "List of devices attached"
        GET_CPU_INFO = "adb -s {} shell dumpsys cpuinfo {}"
        CPU_REGEX = "([0-9]+(\\.[0-9]+)?%)\\s+(user)\\s+(\\+)\\s+([0-9]+(\\.[0-9]+)?%)\\s+(kernel)(.*)"
        GET_DEVICE_MODEL = "adb -s {} shell getprop ro.product.model"
        GET_DEVICE_OS = "adb -s %s shell getprop ro.build.version.release"

    class Instruments(enum.Enum):
        LIST_ALL_DEVICES = "instruments -s devices | grep 'iPhone'"
        SIMULATOR_UDID_PATTERN = "[a-zA-Z0-9-]{36}"
