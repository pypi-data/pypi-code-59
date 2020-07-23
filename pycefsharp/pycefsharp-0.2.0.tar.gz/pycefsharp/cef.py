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
    def __init__(self, url:str, title:str = "pycefsharp", icon:str = None, geometry:list = [-1, -1, -1, -1]):
        super().__init__()

        self.__url = url
        self.__icon = os.path.join(__path__[0], "cef.ico") if icon == None else icon

        self.Icon = Icon(self.__icon)
        self.Text = title
        self.geometry = geometry

        self.Load += self.__OnLoad
        self.Shown += self.__OnShow
        self.FormClosed += self.__OnClose

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, new_url:str):
        self.__url = new_url
        self.__cef_browser_form.Load(self.__url)

    @property
    def icon(self) -> str:
        return self.__icon

    @property
    def title(self) -> str:
        return self.Text

    @property
    def geometry(self) -> list:
        return [
            self.Location.X, self.Location.Y,
            self.Size.Width, self.Size.Height
        ]

    @geometry.setter
    def geometry(self, new_geometry:list):
        if not new_geometry[0] == -1 or not new_geometry[1] == -1:
            self.Location = Point(new_geometry[0], new_geometry[1])
        else:
            self.StartPosition = WinForms.FormStartPosition.CenterScreen

        if not new_geometry[2] == -1 or not new_geometry[3] == -1:
            self.Size = Size(new_geometry[2], new_geometry[3])

    def __OnLoad(self, sender, ev):
        self.__cef_browser_form = Cef_Forms.ChromiumWebBrowser(self.__url)
        self.__cef_browser_form.Dock = WinForms.DockStyle.Fill
        self.Controls.Add(self.__cef_browser_form)

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
