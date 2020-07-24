import datetime
from sync.base import BaseSync
from utils.loggerutils import logging
from classcard_dataclient.models import Class

logger = logging.getLogger(__name__)


class SectionSync(BaseSync):
    def __init__(self):
        super(SectionSync, self).__init__()
        now = datetime.datetime.now()
        self.offset = 300
        self.section_map = {}

    def extract_section(self):
        sql = "SELECT DPCODE1, DPNAME1 FROM BASE_CUSTDEPT ORDER BY DPCODE1"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        for row in rows:
            code, name = row[0], row[1]
            section = Class(name=name, number=code, school=self.school_id)
            self.section_map[code] = section

    def sync(self):
        self.extract_section()
        if not self.section_map:
            logger.info("没有班级信息")
            return
        for code, section in self.section_map.items():
            code, data = self.client.create_section(sections=section)
            if code:
                logger.error("Code: {}, Msg: {}".format(code, data))
        self.close_db()
