import time
import datetime
class IOTInternal(object):
  def __init__(self, internal):
    self.internal = internal
  def get_id(self):
    return self.internal['id']

class IOTDevice(IOTInternal):
  def __init__(self, internal):
    super().__init__(internal)
    self.data = None

class IOTDataField(IOTInternal):
  def __init__(self, internal):
    super().__init__(internal)
  def get_unit(self):
    return self.internal

class IOTDataEntries(object):
  def __init__(self, data, device, field):
    self.data = data
    self.field = field
    self.device = device
  def get_data(self):
    X = []
    Y = []
    T = []
    for x in self.data:
      Y.append(x["value"])
      X.append(x["independent"])
      t = time.mktime(datetime.datetime.strptime(x['created_at'], "%Y-%m-%dT%H:%M:%S.%fZ").timetuple())
      T.append(t)
    return {"X" : X, "Y" : Y, "T" : T}

  def get_unit(self):
    return self.field.get_unit();
