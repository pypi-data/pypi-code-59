from dataclasses import dataclass
from typing import List, Optional

from arcor2.data.common import Pose, StrEnum

from dataclasses_jsonschema import JsonSchemaMixin


@dataclass
class ScoredItem(JsonSchemaMixin):

    id: int
    item_pose: Pose
    search_score: float


@dataclass
class SearchOutput(JsonSchemaMixin):

    items: List[ScoredItem]
    container_pose: Pose


@dataclass
class GripperSetup(JsonSchemaMixin):

    pick_pose: Pose
    pick_speed: float
    pre_pick_opening: float
    pick_grip: float
    pick_force: float


@dataclass
class SearchVisualizationSetup(JsonSchemaMixin):

    container: bool
    space_selector: bool
    estimate: bool
    refine: bool


@dataclass
class SearchSaveInfo(JsonSchemaMixin):

    save_input: bool
    save_visualizations: bool
    path: Optional[str] = None


class LogLevel(StrEnum):

    TRACE: str = "trace"
    DEBUG: str = "debug"
    INFO: str = "info"
    WARN: str = "warn"
    ERROR: str = "error"
    FATAL: str = "fatal"


@dataclass
class SearchEngineParameters(JsonSchemaMixin):

    visualization_setup: Optional[SearchVisualizationSetup] = None
    search_data_save_info: Optional[SearchSaveInfo] = None
    search_log_level: Optional[LogLevel] = None
