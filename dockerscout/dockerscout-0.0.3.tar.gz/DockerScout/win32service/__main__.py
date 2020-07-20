"""
Windows Service Integration
"""
import sys
import win32serviceutil, servicemanager

from DockerScout.win32service.service import DockerScoutService, ensure_wintypes_path


if __name__ == '__main__':
    ensure_wintypes_path()
    #if len(sys.argv) == 1:
    #    servicemanager.Initialize()
    #    servicemanager.PrepareToHostSingle(DockerScoutService)
    #    servicemanager.StartServiceCtrlDispatcher()
    #    return

    win32serviceutil.HandleCommandLine(DockerScoutService, argv=list(sys.argv))
