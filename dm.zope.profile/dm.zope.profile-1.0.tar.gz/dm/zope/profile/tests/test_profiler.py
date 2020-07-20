# Copyright (C) 2020 by Dr. Dieter Maurer; see LICENSE.txt for details
from time import sleep
from unittest import TestCase

from zope.annotation.attribute import AttributeAnnotations
from zope.component import provideAdapter
from zope.component.testing import PlacelessSetup
from zope.event import notify
from ZPublisher.pubevents import PubStart, PubSuccess

from ..profiler import profiler


class Request(object):
  PATH_INFO = "PATH_INFO"

  def __getitem__(self, key):
    if key != "PATH_INFO": raise KeyError(key)
    return self.PATH_INFO


def process(): sleep(0.1)


class TestProfiler(PlacelessSetup, TestCase):
  def setUp(self):
    super(TestProfiler, self).setUp()
    provideAdapter(AttributeAnnotations, (None,))
    self.request = Request()

  def tearDown(self):
    profiler.clear()
    profiler.reset()
    if profiler.enabled: profiler.disable()
    super(TestProfiler, self).tearDown()

  def _request(self, enable=True):
    if enable and not profiler.enabled: profiler.enable()
    r = self.request
    notify(PubStart(r))
    process()
    notify(PubSuccess(r))

  def test_nothing_if_disabled(self):
    self._request(False)
    self.assertFalse(profiler.stats.stats)

  def test_something_if_enabled(self):
    self._request()
    self.assertTrue(profiler.stats.stats)

  def test_auto_clear(self):
    stats = profiler.stats
    # no change
    profiler.update(timer="real time")
    self.assertIs(stats, profiler.stats)
    # change
    profiler.update(timer="CPU time")
    self.assertIsNot(stats, profiler.stats)
    
  def test_include(self):
    # this tests ``_recompile``
    profiler.update(include=set(("UVW",)))
    self._request()
    self.assertFalse(profiler.stats.stats) # no match
    profiler.update(include=set(("UVW", "INFO")))
    self._request()
    self.assertTrue(profiler.stats.stats) # match
    
  def test_exclude(self):
    profiler.update(include=set(("INFO",)), exclude=set(("INFO",)))
    self._request()
    self.assertFalse(profiler.stats.stats) # exclude match

  def test_process(self):
    # we test only that we can call the methods
    # we trust that ``pStats.Stats`` does the right thing
    self._request()
    for type in "stats callers callees".split():
      self.assertTrue(profiler.process_stats(type))

  def test_sort(self):
    self._request()
    cum_sort = profiler.process_stats() # cumulative time
    profiler.update(sort_by=("time",)) # internal time
    self.assertNotEqual(cum_sort, profiler.process_stats())

  def test_strip_dirs(self):
    self._request()
    stripped = profiler.process_stats()
    profiler.update(strip_dirs=False)
    self.assertNotEqual(stripped, profiler.process_stats())

  def test_top_level(self):
    self._request()
    stats = profiler.process_stats("callees")
    sl = stats.split("\n")
    self.assertEqual(sl[4][:22], "<request>:0(PATH_INFO)")

  def test_combine(self):
    self._request()
    self.request.PATH_INFO = "REQUEST 2"
    self._request()
    stats = profiler.process_stats()
    self.assertIn("PATH_INFO", stats)
    self.assertIn("REQUEST 2", stats)

  def test_reset(self):
    profiler.update(strip_dirs=False)
    stats = profiler.stats
    profiler.reset()
    self.assertTrue(profiler.strip_dirs)
    self.assertIs(stats, profiler.stats) # no change
    profiler.update(timer="CPU time")
    stats = profiler.stats
    profiler.reset()
    self.assertEqual(profiler.timer, "real time")
    self.assertIsNot(stats, profiler.stats) # change
