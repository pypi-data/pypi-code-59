"""
Abel's logging system
"""
import logging
import logging.config
import os
import sys

from pathlib import Path


def configure_logger(name, log_path: Path = Path('../logs/test.log')) -> logging.Logger:
    """
    configures the logger
    :param name:
    :param log_path:
    :return:
    """

    log_path.parent.mkdir(parents=True, exist_ok=True)

    logging.config.dictConfig({
        'version': 1,
        'formatters': {
            'basic': {'format': '%(message)s'},
            'default': {'format': '%(asctime)s %(message)s', 'datefmt': '%H:%M:%S'},
            'detailed': {
                'format': '%(asctime)-8s %(name)-4s %(levelname)-7s %(message)s funcName:%(funcName)s',
                'datefmt': '%H:%M:%S'
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'basic',
                'stream': 'ext://sys.stdout'
            },
            'file': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'default',
                'filename': log_path,
                'backupCount': 0
            },
            'fullFile': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'detailed',
                'filename': os.path.splitext(str(log_path))[0] + '_full.log',
                'backupCount': 0
            },
            'root': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'detailed',
                'filename': os.path.splitext(str(log_path))[0] + '_root.log',
                'backupCount': 0
            },
        },
        'loggers': {
            name: {
                'level': 'INFO',
                'handlers': ['console', 'file', 'fullFile']
            },
            '': {
                'level': 'DEBUG',
                'handlers': ['root']
            }
        },
        'disable_existing_loggers': True
    })
    return logging.getLogger(name)


default_formatter = logging.Formatter('%(asctime)-8s %(name)-4s %(levelname)-7s %(message)s funcName:%(funcName)s',
                                      datefmt='%H:%M:%S')


def basic_config(level: str = "DEBUG", file='../logs/basicLog.log', mode='w') -> logging.Logger:
    """
    Just sets up the python logging module,
    By default will be set to INFO level
    :param mode: the file using mode
    :param file: the file location
    :param level: default logging.INFO
    :type level: logging
    """

    if not os.path.exists(os.path.dirname(file)):
        os.makedirs(os.path.dirname(file))
    logging.basicConfig(filename=file,
                        filemode=mode,
                        format='%(asctime)-8s %(name)-4s %(levelname)-7s %(message)s',
                        datefmt='%H:%M:%S',
                        level=level)

    return logging.getLogger()


def get_console_handler(logging_level=logging.INFO,
                        formatter=logging.Formatter('%(message)s'),
                        log_stream=sys.stdout) -> logging.StreamHandler:
    """
    Creates a console handler to redirect all logging to the console
    :param logging_level: Optional logging level (defaults to info and above)
    :param formatter: Optional format
    :param log_stream: Defaults to sys.stdout. If you want it go to a string buffer create one using
            log_stream_buffer = io.StringIO()
            logger.addHandler(log.get_console_handler(log_stream = log_stream_buffer)
    :return:
    """
    # print everything above info to console
    console_handler = logging.StreamHandler(log_stream)
    console_handler.setLevel(logging_level)
    console_handler.setFormatter(formatter)
    return console_handler


def get_file_handler(file_path, logging_level=logging.INFO, formatter=default_formatter,
                     mode='a') -> logging.FileHandler:
    """
    get's the file handler
    :param file_path:
    :param logging_level:
    :param formatter:
    :param mode:
    :return:
    """
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    file_handler = logging.FileHandler(file_path, mode=mode)
    file_handler.setLevel(logging_level)
    file_handler.setFormatter(formatter)
    return file_handler
