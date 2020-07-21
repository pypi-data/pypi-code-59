class DeviceEngagedException(Exception):

    def __init__(self):
        super("Unable to Mark Device to 'Engaged'. Check for device State using `adb devices`. If it is offline, "
              "kill the adb server `adb kill-server` and try again.")
