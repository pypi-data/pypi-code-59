class DeviceReleaseException(Exception):

    def __init__(self, udid: str):
        super("Cannot release device with udid {}".format(udid))
