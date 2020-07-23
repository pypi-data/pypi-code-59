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

class CefView():
    def __init__(self, url:str, title:str = "pycefsharp", icon:str = None, geometry:list = [-1, -1, -1, -1]):
        self.__cef_form = WinForms.Form()
        self.__cef_form.StartPosition = WinForms.FormStartPosition.CenterScreen

        self.__cef_browser = None

        self.url = url
        self.title = title
        self.icon = os.path.join(__path__[0], "cef.ico") if icon == None else icon
        self.geometry = geometry

        self.__cef_form.Load += self.__on_load
        self.__cef_form.Shown += self.__on_show
        self.__cef_form.FormClosed += self.__on_close

    # attributes
    @property
    def _cef_form(self) -> WinForms.Form:
        return self.__cef_form

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, new_url:str):
        self.__url = new_url
        if not self.__cef_browser == None:
            self.__cef_browser.Load(self.__url)

    @property
    def icon(self) -> str:
        return self.__icon

    @icon.setter
    def icon(self, new_icon:str):
        self.__icon = new_icon
        self.__cef_form.Icon = Icon(self.__icon)

    @property
    def title(self) -> str:
        return self.__cef_form.Text
    
    @title.setter
    def title(self, new_title:str):
        self.__cef_form.Text = new_title

    @property
    def geometry(self) -> list:
        return [
            self.__cef_form.Location.X, self.__cef_form.Location.Y,
            self.__cef_form.Size.Width, self.__cef_form.Size.Height
        ]

    @geometry.setter
    def geometry(self, new_geometry:list):
        self.__cef_form.Size = Size(
            600 if new_geometry[2] == -1 else int(new_geometry[2]),
            400 if new_geometry[3] == -1 else int(new_geometry[3])
        )

        if new_geometry[0] == -1 or new_geometry[1] == -1:
            self.__to_center_screen()
        else:
            self.__cef_form.Location = Point(int(new_geometry[0]), int(new_geometry[1]))

    # events
    def __on_load(self, sender, ev):
        self.__cef_browser = Cef_Forms.ChromiumWebBrowser(self.__url)
        self.__cef_browser.Dock = WinForms.DockStyle.Fill
        self.__cef_form.Controls.Add(self.__cef_browser)

        self.on_load()

    def on_load(self):
        pass

    def __on_show(self, sender, ev):
        self.on_show()

    def on_show(self):
        pass

    def __on_close(self, sender, ev):
        self.on_close()

    def on_close(self):
        pass

    # functions
    def __to_center_screen(self):
        self.__cef_form.Location = Point(
            int((WinForms.Screen.PrimaryScreen.Bounds.Size.Width - self.__cef_form.Size.Width) / 2),
            int((WinForms.Screen.PrimaryScreen.Bounds.Size.Height - self.__cef_form.Size.Height) / 2)
        )

    def show(self):
        self.__cef_form.Show()

    def close(self):
        self.__cef_form.Close()

class CefApp():
    def __init__(self, settings:CefSettings = CefSettings()):
        settings.CachePath = os.path.join(__path__[0], "cefsharp", "gpu_cache")
        Cef.Initialize(settings)

    def Run(self, cefview:CefView):
        WinForms.Application.Run(cefview._cef_form)
