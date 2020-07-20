# Copyright (C) 2020 by Dr. Dieter Maurer; see LICENSE.txt for details
from zope.interface import Interface
from zope.schema import Bool, Choice, Set, List, NativeStringLine, \
     ValidationError, getFieldsInOrder


class InvalidRegularExpression(ValidationError):
  __doc__ = "The regular expression is invalid"


class RegularExpression(NativeStringLine):
  def _validate(self, value):
    super(RegularExpression, self)._validate(value)
    from re import error, compile
    try: compile(value)
    except error as e:
      raise InvalidRegularExpression(str(e)).with_field_and_value(self, value)



class IProfileControl(Interface):
  timer = Choice(title=u"Timer",
                 values=("real time", "CPU time"),
                 default="real time",
                 )

  include = Set(
    title=u"URLs to profile",
    description=u"If not empty, a request is profiled only if at least "
    "one of the regular expressions matches its `PATH_INFO` (in search mode)",
    value_type=RegularExpression(),
    required=False,
    )

  exclude = Set(
    title=u"URLs not to profile",
    description=u"Do not profile if one of these regular expressions "
    "matches the requests `PATH_INFO` (in search mode)",
    value_type=RegularExpression(),
    required=False,
    )


class InvalidRestriction(ValidationError):
  __doc__ = "neither an integer nor a float between 0 and 1 nor a regular expression"

class Restriction(NativeStringLine):
  def _validate(self, value):
    super(Restriction, self)._validate(value)
    value = value.strip()
    try: return int(value)
    except ValueError: pass
    try:
      fl = float(value)
      if (0 < fl < 1): return fl
      raise InvalidRestriction("a float must be between 0 and 1").with_field_and_value(self, value)
    except ValueError:
      from re import compile, error
      try: return compile(value)
      except error: raise InvalidRestriction("invalid regular expression").with_field_and_value



class IStatsControl(Interface):
  type = Choice(
    title=u"type",
    description=u"evaluation type",
    values=("stats", "callees", "callers",),
    required=True,
    )

  strip_dirs = Bool(
    title=u"strip dirs",
    description=u"remove leading path information from file names?",
    default=True,
    )

  sort_by = List(
    title=u"sort by",
    description=u"A sequence of sort keys. See the documentation of Python's "
    u"`pstats` module for the meaning of those keys.",
    value_type=Choice(
      values=("cumulative", "time", "calls", "pcalls", "filename", "line", "name", "nfl", "stdname",),
      ),
    required=False,
    )

  restrictions = List(
    title=u"restrictions",
    description=u"a restriction can be an integer, a 0 < float < 1, or a regular expression. "
    u"an integer limits the number of entries shown, "
    u"a float the relative part of shown entries with respect to all entries,"
    u"a regular expression restricts to entries with stdname matched (in search "
    u"mode) by the expression",
    required=False,
    value_type=Restriction(),
    )


class IControl(IProfileControl, IStatsControl):
  """all control parameters"""


control_fields = [i[1] for i in getFieldsInOrder(IControl)]
