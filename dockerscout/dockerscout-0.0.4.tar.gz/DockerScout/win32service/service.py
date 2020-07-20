import socket
import os
import sys
import servicemanager
import win32service
import win32serviceutil

from DockerScout.monitor import ImageScanner, run


def ensure_wintypes_path():
    import site
    sites = site.getsitepackages()

    pywin32_system32 = "pywin32_system32"
    for item in sites:
        if item.lower().endswith("site-packages"):
            addpath = os.path.join(item, pywin32_system32)
            if os.path.isdir(addpath):
                append_system_path(addpath)


def append_system_path(addpath):
    # borrowed from https://stackoverflow.com/a/21452408/148415
    import winreg as reg

    # read the value
    # use this if you need to modify the system variable and if you have admin privileges
    key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment', 0, reg.KEY_ALL_ACCESS)
    value, _ = reg.QueryValueEx(key, 'PATH')

    if addpath in value:
        return

    # modify it
    value = value + os.pathsep + addpath

    # write it back
    reg.SetValueEx(key, 'PATH', 0, reg.REG_EXPAND_SZ, value)
    reg.CloseKey(key)


class DockerScoutService(win32serviceutil.ServiceFramework):
    _svc_name_ = "DockerScout"
    _svc_display_name_ = "Docker Scout"
    _svc_description_ = "Clean up unused docker images"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        servicemanager.LogInfoMsg("New Instance {}".format(self._svc_display_name_))

        socket.setdefaulttimeout(60)

    def info(self, msg):
        servicemanager.LogInfoMsg(msg)

    def SvcStop(self):
        servicemanager.LogInfoMsg("Stopping {}".format(self._svc_display_name_))
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.ReportServiceStatus(win32service.SERVICE_STOPPED)
        sys.exit(0)
        ImageScanner.getinstance().end = True

    def SvcDoRun(self):
        self.info("Starting {}".format(self._svc_display_name_))
        self.ReportServiceStatus(win32service.SERVICE_START_PENDING)
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        run([])
