import time
from datetime import datetime

date_format = time.strftime('%a %b %d %H:%M:%S %Z %Y', time.localtime(time.time()))
strftime = datetime.strftime(datetime.now(), date_format)

# date_format1 = datetime.strptime("2010 05 20", '%a %b %d').now()
# cus_date = datetime.strptime("24052010", "%d%M%Y")

if __name__ == '__main__':
    print(datetime.now().isoformat())


class Scenario(object):
    id: None
    scenarioName: str
    dataRowNumber: int
    dataRow: int
    location: str
    tags: list
    startTime: datetime
    buildId: str
    deviceId: str
    status: str
    completed: bool
    endTime: datetime
    timeTaken: int
    scenarioTimeline: str
    steps: str
    failedOn: list
    stacktrace: str
    activity: str
    featureName: str
    featureFileName: str

    def __init__(self):
        self.id = None
        self.scenarioName = str()
        self.dataRowNumber = int()
        self.dataRow = int()
        self.location = str()
        self.tags = list()
        self.startTime = datetime.now().isoformat()
        self.buildId = str()
        self.deviceId = str()
        self.status = str()
        self.completed = bool()
        self.endTime = datetime.now().isoformat()
        self.timeTaken = int()
        self.scenarioTimeline = str()
        self.steps = str()
        self.failedOn = list()
        self.stacktrace = str()
        self.activity = str()
        self.featureName = str()
        self.featureFileName = str()
