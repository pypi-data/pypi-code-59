# -*- coding: utf-8 -*-

import sys
from . import __path__
sys.path.append(__path__[0])

import clr
clr.AddReference("CefSharp")
clr.AddReference("CefSharp.Core")
clr.AddReference("CefSharp.WinForms")

import CefSharp
from CefSharp import Cef
import CefSharp.WinForms as Cef_Forms
