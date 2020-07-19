"""Конфигурация для серверного логгера"""
import os
import sys
import logging.handlers
from datetime import datetime

from server.config.cfg_path import LOG_DIR

LOGGING_LEVEL = logging.DEBUG

SRV_FORMATTER = logging.Formatter('%(asctime)s %(levelname)-8s %(filename)-15s %(message)s')

DATE = datetime.today().strftime("%Y-%m-%d")

LOG_PATH = os.path.join(LOG_DIR, f'server_{DATE}.log')

STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(SRV_FORMATTER)
STREAM_HANDLER.setLevel(LOGGING_LEVEL)

LOG_FILE = logging.handlers.TimedRotatingFileHandler(LOG_PATH,
                                                     encoding='utf8',
                                                     interval=1,
                                                     when='D')
LOG_FILE.setFormatter(SRV_FORMATTER)

SRV_LOGGER = logging.getLogger('server')
SRV_LOGGER.addHandler(STREAM_HANDLER)
SRV_LOGGER.addHandler(LOG_FILE)
SRV_LOGGER.setLevel(LOGGING_LEVEL)

if __name__ == '__main__':
    SRV_LOGGER.critical('Критическая ошибка')
    SRV_LOGGER.error('Ошибка')
    SRV_LOGGER.debug('Отладочная информация')
    SRV_LOGGER.info('Информационное сообщение')
