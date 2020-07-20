# Copyright (C) 2020 by Dr. Dieter Maurer; see LICENSE.txt for details
from cProfile import Profile
from copy import deepcopy
from pstats import Stats
from re import compile
from sys import version_info

from zope.annotation.interfaces import IAnnotations
from zope.component import adapter
from zope.component.globalregistry import globalSiteManager
from zope.interface import implementer

from Acquisition import Implicit
from ZPublisher.interfaces import IPubStart, IPubEnd

from .interfaces import IProfileControl, IStatsControl

@implementer(IProfileControl, IStatsControl)
class Control(object):
  """used as singleton"""
  timer = "real time"
  include = set()
  exclude = set(("@@profile$",))
  type = "stats"
  strip_dirs = True
  sort_by = ["cumulative",]
  restrictions = ["100",]


COMPILED = frozenset(("timer", "include", "exclude", "restrictions"))


class Profile(Profile):
  """Profile associating top level function calls with the request.

  Request entries are marked with line number ``0``.
  """
  def __init__(self, request, timer):
    self.request = request
    args = (timer,) if timer is not None else ()
    super(Profile, self).__init__(*args)

  def create_stats(self):
    super(Profile, self).create_stats()
    stats = self.stats
    # determine top level calls
    tops = {}
    for key, kstats in stats.items():
      if kstats[0] > sum(cstats[0] for cstats in kstats[4].values()):
        tops[key] = (
          kstats[0] - sum(cstats[0] for cstats in kstats[4].values()),
          kstats[1] - sum(cstats[1] for cstats in kstats[4].values()),
          kstats[2] - sum(cstats[2] for cstats in kstats[4].values()),
          kstats[3] - sum(cstats[3] for cstats in kstats[4].values()),
          )
    # we cheat a bit with the times
    #  because we do not know how `cProfile` measures time internally
    re = ("<request>", 0, self.request)
    # add request entry
    stats[re] = (
      1, 1,
      sum(cstats[2] for cstats in tops.values()),
      sum(cstats[3] for cstats in tops.values()),
      {})
    # update top level calls
    for key, kstats in tops.items():
      stats[key][4][re] = kstats


class Profiler(Control, Implicit):
  enabled = False

  def __init__(self):
    self.update(clear=True, recompile=True)

  def update(self, clear=False, recompile=False, **kw):
    """update configuration."""
    for k, v in kw.items():
      if v != getattr(self, k, None):
        if k == "timer": clear = True
        if k in COMPILED: recompile = True
      setattr(self, k, v)
    if clear: self.clear()
    if recompile: self._recompile()

  def reset(self):
    """reset to default configuration."""
    self.update(**dict(i for i in Control.__dict__.items()
                       if i[0] in IProfileControl
                       or i[0] in IStatsControl))

  def clear(self):
    self.stats = MyStats()

  def enable(self):
    self.enabled = True
    registerHandler(self.start)
    registerHandler(self.stop)

  def disable(self):
    self.enabled = False
    unregisterHandler(self.start)
    unregisterHandler(self.stop)

  @adapter(IPubStart)
  def start(self, ev):
    request = ev.request
    if not self.enabled: return
    pi = request["PATH_INFO"]
    incs = self._include
    if incs and not any(inc(pi) for inc in incs): return
    if any(exc(pi) for exc in self._exclude): return
    prof = Profile(pi, self._timer)
    IAnnotations(request)[__name__] = prof
    prof.enable()

  @adapter(IPubEnd)
  def stop(self, ev):
    request = ev.request
    prof = IAnnotations(request).get(__name__)
    if prof is not None:
      prof.disable()
      self.stats.add(prof)

  def _recompile(self):
    self._timer = None if self.timer == "real time" else thread_time
    # `z3c.form` can turn collection values into ``None``
    self._include = [compile(x).search for x in self.include or ()]
    self._exclude = [compile(x).search for x in self.exclude or ()]
    val = IStatsControl["restrictions"].value_type._validate
    self._restrictions = [val(x) for x in self.restrictions or ()]

  def process_stats(self, type=None):
    if type is None: type = self.type
    stats = deepcopy(self.stats)
    stats.stream = StringIO()
    if self.strip_dirs: stats.strip_dirs()
    stats.sort_stats(*self.sort_by)
    getattr(stats, "print_" + type)(*self._restrictions)
    return stats.stream.getvalue()


try: from time import thread_time # 3.7+
except ImportError:
  try:
    from time import clock_gettime, CLOCK_THREAD_CPUTIME_ID # 3.3+
    def thread_time(): return clock_gettime(CLOCK_THREAD_CPUTIME_ID)
  except ImportError: # 2.7
    from os import times
    def thread_time():
      tms = times()
      return tms[0] + tms[1]

try: from cStringIO import StringIO # 2
except ImportError: # 2
  from io import StringIO


class MyStats(Stats):
  # ensure we can copy it
  def __init__(self, *args, **kw):
    Stats.__init__(self, *args, **kw)
    self.stream = None

  # work around bug in older Python versions
  def load_stats(self, arg):
    if arg is None: self.stats = {}; return
    Stats.load_stats(self, arg)


profiler = Profiler()

registerHandler = globalSiteManager.registerHandler
unregisterHandler = globalSiteManager.unregisterHandler
