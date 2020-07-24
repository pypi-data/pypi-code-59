from business.action import upload_meeting_attendance
from utils.loggerutils import logging
from core.processor import Processor

logger = logging.getLogger(__name__)


class BusinessProcessor(Processor):
    KIND_FUNC = {"OpenConventioneerRecord": "upload_meeting_attendance"}

    @staticmethod
    def upload_meeting_attendance(*args, **kwargs):
        upload_meeting_attendance(*args, **kwargs)
