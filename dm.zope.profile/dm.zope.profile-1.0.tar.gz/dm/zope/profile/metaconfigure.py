# Copyright (C) 2020 by Dr. Dieter Maurer; see LICENSE.txt for details
"""ZCML directives for ``profiler`` controluration."""
from zope.interface import Interface
from zope.schema import NativeStringLine, Choice

from .interfaces import IProfileControl, IStatsControl, control_fields
from .profiler import Control, profiler


class IElement(Interface):
  name = Choice(
    title=u"sequence name",
    values=("include", "exclude", "sort_by", "restrictions"),
    description=u"tells the controluration attribute targeted by this element",
    )

  value = NativeStringLine(
    title=u"value",
    )


class IProfilerConfig(Interface):
  timer = IProfileControl["timer"]
  type = IStatsControl["type"]
  strip_dirs = IStatsControl["strip_dirs"]
  

class ProfilerConfig(object):
  default_allowed_attributes = '__call__'

  def __init__(self, _context, timer, type, strip_dirs):
    self._context = _context
    c = self.control = Control()
    c.include = set()
    c.exclude = set()
    c.sort_by = []
    c.restrictions = []
    c.timer = timer
    c.type = type
    c.strip_dirs = strip_dirs

  def element(self, _context, name, value=None):
    add = "add" if name in ("include", "exclude") else "append"
    getattr(getattr(self.control, name), add)(value)

  def __call__(self):
    # verify the values
    c = self.control
    for f in control_fields:
      fn = f.__name__
      __traceback_info__ = fn
      f.validate(getattr(c, fn))
    self._context.action(
      discriminator=("dm.zope.profile",),
      callable=apply_control, args=(c,))


def apply_control(control):
  for f in control_fields:
    fn = f.__name__
    setattr(Control, fn, getattr(control, fn))
  profiler.reset()
