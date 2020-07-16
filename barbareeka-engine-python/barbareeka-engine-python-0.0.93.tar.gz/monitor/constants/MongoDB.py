import enum


class MongoDB(enum.Enum):
    pass


KEY_SCENARIOS_SCENARIO_NAME = "scenarioName"
QUERY_AND = "$and"
DATABASE_NAME = "optimus"
COLLECTION_SCENARIOS = "scenarios"
KEY_SCENARIOS_DEVICE_UDID = "deviceUdid"

KEY_SCENARIOS_START_TIME = "startTime"
ID = "_id"

STATUS_AVAILABLE = "Available"
STATUS_ENGAGED = "Engaged"
STATUS_PASSED = "passed"
