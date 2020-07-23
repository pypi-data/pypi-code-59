import logging

import cx_Oracle

from .abstract import Abstract_DB
from soft_collect.config import settings as s

logger = logging.getLogger(__name__)


class Oracle(Abstract_DB):
    def select(self, sql):
        c = self.set_up_connection()

        yield from c.execute(sql)

    def fetch_all(self, sql):
        c = self.set_up_connection()

        return c.execute(sql).fetchall()

    def set_up_connection(self):
        logger.info(f"Creating connection to SQL Server in {s.ip}")
        connection = cx_Oracle.connect(
            s.user, s.password, f"{s.ip}/{s.base}", encoding="UTF-8", nencoding="UTF-8"
        )

        return connection.cursor()
