# Copyright (C) 2020 by Dr. Dieter Maurer; see LICENSE.txt for details
from zope.component import adapter, getMultiAdapter
from zope.interface import directlyProvides, implementer
from zope.schema import Bool
from zope.schema.interfaces import ICollection, INativeStringLine

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from z3c.form.browser.multi import MultiWidget
from z3c.form.button import buttonAndHandler
from z3c.form.interfaces import IFormLayer, IFieldWidget, HIDDEN_MODE, \
     NOT_CHANGED
from z3c.form.field import Fields, Field
from z3c.form.form import Form, EditForm
from z3c.form.util import changedField
from z3c.form.widget import Widget, FieldWidget

from dm.reuse import rebindFunction

from .interfaces import IProfileControl, IStatsControl
from .profiler import profiler


class ILayer(IFormLayer):
  """our layer -- used to override ``z3c`` registrations."""


def applyChangesViaUpdate(form, content, data):
  changes = {}; values = {}
  for name, field in form.fields.items():
    # If the field is not in the data, then go on to the next one
    try:
      newValue = data[name]
    except KeyError:
      continue
    # If the value is NOT_CHANGED, ignore it, since the widget/converter
    # sent a strong message not to do so.
    if newValue is NOT_CHANGED:
      continue
    if changedField(field.field, newValue, context=content):
      # Only update the data, if it is different
      values[name] = newValue
      changes.setdefault(field.interface, []).append(name)
  if values: content.update(**values)
  return changes

class EditForm(EditForm):
    applyChanges = rebindFunction(
      EditForm.applyChanges,
      applyChanges=applyChangesViaUpdate
      )

class ProfileForm(EditForm):
  form_name = "Profiler"
  prefix = "profiler"
  fields = Fields(IProfileControl)

  def summary(self):
    return (profiler.enabled and "enabled" or "disabled") \
           + " " + profiler.timer


class StatsForm(EditForm):
  form_name = "Statistics"
  prefix = "stats"
  fields = Fields(IStatsControl)


class IntegrationForm(EditForm):
  template = ViewPageTemplateFile("profile.pt")
  prefix = "form"
  fields = Fields()

  def __init__(self, context, request):
    directlyProvides(request, ILayer)
    super(IntegrationForm, self).__init__(profiler.__of__(context), request)
    self.subforms = []

  def update(self):
    self.add_subform(ProfileForm)
    self.add_subform(StatsForm)
    for sf in self.subforms: sf.update()
    super(IntegrationForm, self).update()

  def add_subform(self, factory):
    sf = factory(self.context, self.request)
    self.fields += Fields(Field(Bool(default=False), sf.form_name, mode=HIDDEN_MODE))
    self.subforms.append(sf)

  def process_stats(self):
    return profiler.process_stats()

  @buttonAndHandler(u"Update")
  def upd(self, action): pass

  @buttonAndHandler(u"Enable", condition=lambda unused: not profiler.enabled)
  def enable(self, action): profiler.enable(); self.refreshActions = True

  @buttonAndHandler(u"Disable", condition=lambda unused: profiler.enabled)
  def disable(self, action): profiler.disable(); self.refreshActions = True

  @buttonAndHandler(u"Reset")
  def reset(self, action):
    profiler.reset()
    for f in self.subforms:
      f.ignoreRequest = True
      f.updateWidgets()

  @buttonAndHandler(u"Clear")
  def clear(self, action): profiler.clear()

  def combined_status(self):
    for f in [self] + self.subforms:
      if f.status: return f.status
    return

  def combined_errors(self):
    errs = []
    for f in [self] + self.subforms: errs.extend(getattr(f, "errors", ()))
    return errs


@adapter(ICollection, ILayer)
@implementer(IFieldWidget)
def collection_2_field_widget(field, request):
  return getMultiAdapter((field, field.value_type, request))


@adapter(ICollection, INativeStringLine, ILayer)
@implementer(IFieldWidget)
def collection_str_2_field_widget(field, value_type, request):
  return FieldWidget(field, MultiWidget(request))

