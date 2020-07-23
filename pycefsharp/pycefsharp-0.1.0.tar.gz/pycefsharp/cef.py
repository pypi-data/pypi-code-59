# -*- coding: utf-8 -*-

import os
import logging
from .cefsharp import Cef, Cef_Forms
from . import __path__

import clr
clr.AddReference("System.Windows.Forms")
import System.Windows.Forms as WinForms
from System.Drawing import Icon, Size, Point


class CefSettings(Cef_Forms.CefSettings):
    def __init__(self):
        super().__init__()

class CefView(WinForms.Form):
    def __init__(self, url:str, title:str = "pycefsharp", icon:str = None, geometry:tuple = (-1, -1, -1, -1)):
        super().__init__()

        self.__url = url

        if icon == None:
            icon = os.path.join(__path__[0], "cef.ico")

        self.Icon = Icon(icon)
        self.Text = title

        if not geometry[0] == -1 or not geometry[1] == -1:
            self.Location = Point(geometry[0], geometry[1])
        else:
            self.StartPosition = WinForms.FormStartPosition.CenterScreen

        if not geometry[2] == -1 or not geometry[3] == -1:
            self.Size = Size(geometry[2], geometry[3])

        self.Load += self.__OnLoad
        self.Shown += self.__OnShow
        self.FormClosed += self.__OnClose

    def __OnLoad(self, sender, ev):
        logging.info(self.__url)
        view = Cef_Forms.ChromiumWebBrowser(self.__url)
        view.Dock = WinForms.DockStyle.Fill
        self.Controls.Add(view)

        self.OnLoad(sender, ev)

    def OnLoad(self, sender, ev):
        pass

    def __OnShow(self, sender, ev):
        self.OnShow(sender, ev)

    def OnShow(self, sender, ev):
        pass

    def __OnClose(self, sender, ev):
        self.OnClose(sender, ev)

    def OnClose(self, sender, ev):
        pass

class CefApp():
    def __init__(self, settings:CefSettings = CefSettings()):
        settings.CachePath = os.path.join(__path__[0], "cefsharp", "gpu_cache")
        Cef.Initialize(settings)

    def Run(self, cefview:CefView):
        WinForms.Application.Run(cefview)
