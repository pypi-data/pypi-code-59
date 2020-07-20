# Copyright (C) 2020 by Dr. Dieter Maurer; see LICENSE.txt for details
from unittest import TestCase

from zope.component.testing import PlacelessSetup
from zope.configuration.xmlconfig import file as load_control

from ...import profile
from ..interfaces import control_fields
from ..profiler import Control, profiler


class TestZcml(PlacelessSetup, TestCase):
  # Note: the test below does not change the default configuration
  #  otherwise, we would need to restore it to ensure test isolation
  def test_example_control(self):
    old = self.get_control()
    profiler.update(strip_dirs=False)
    load_control("example_config.zcml", profile)
    new = self.get_control()
    # the example recreates the default controluration and resets the profiler
    self.assertEqual(old, new)
    # but is not identical
    self.assertIsNot(old["include"], new["include"])
    

  def get_control(self):
    c = {}
    for f in control_fields:
      fn = f.__name__
      c[fn] = getattr(profiler, fn)
    return c
    
