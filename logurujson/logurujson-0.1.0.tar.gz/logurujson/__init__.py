from __future__ import annotations

import loguru
from loguru import logger
import json
from datetime import datetime, timezone

logger.remove()


def serialize(record: loguru.Record):
    subset = dict(
        timestamp=datetime.fromtimestamp(record["time"].timestamp(), tz=timezone.utc)
        .isoformat()
        .replace("+00:00", "Z"),
        level=record["level"].name,
    )
    if isinstance(record["message"], dict):
        subset = {**record["message"], **subset}
    else:
        subset["message"] = record["message"]
    return json.dumps(subset)


def sink(message: loguru.Message):
    seralized = serialize(message.record)
    print(seralized)


logger.add(sink)
