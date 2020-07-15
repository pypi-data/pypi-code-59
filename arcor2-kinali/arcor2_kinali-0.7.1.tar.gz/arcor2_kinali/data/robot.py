from dataclasses import dataclass
from typing import List

from arcor2.data.common import Joint, Orientation, Pose, Position, StrEnum

from dataclasses_jsonschema import JsonSchemaMixin


class MoveTypeEnum(StrEnum):

    AVOID_COLLISIONS: str = "AvoidCollisions"
    LINE: str = "Line"
    SIMPLE: str = "Simple"


@dataclass
class MoveRelativeParameters(JsonSchemaMixin):

    pose: Pose
    position: Position  # relative position
    orientation: Orientation  # relative orientation


@dataclass
class MoveRelativeJointsParameters(JsonSchemaMixin):

    joints: List[Joint]
    position: Position  # relative position
    orientation: Orientation  # relative orientation
