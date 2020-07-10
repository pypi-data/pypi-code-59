# -*- coding: utf-8 -*-

import logging
import os
from os import makedirs

from enhancements.config import ExtendedConfigParser
from enhancements.modules import ModuleParserPlugin


class LogModule(ModuleParserPlugin):

    LOGFILE = None

    def __init__(self, cmdargs=None, namespace=None):
        super().__init__(cmdargs, namespace)

        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG if self.args.debug else logging.INFO)

        logformatter = logging.Formatter('%(asctime)s [%(levelname)s]  %(message)s')
        logformatter_debug = logging.Formatter('%(asctime)s [%(filename)s:%(lineno)s - %(funcName)s() - %(threadName)s] [%(levelname)s]  %(message)s')
        for handler in root_logger.handlers:
            handler.setFormatter(logformatter_debug if self.args.debug else logformatter)

        logging.debug("loading LogModule")

        if self.args.logfile:
            try:
                if hasattr(self.args, 'nolog') and not self.args.nolog and self.create_log_dir(self.args.logfile):
                    logfile_handler = logging.FileHandler(self.args.logfile)
                    logfile_handler.setFormatter(logformatter)
                    root_logger.addHandler(logfile_handler)
                else:
                    logging.warning("logging to file disabled!")
            except (IOError, PermissionError) as error:
                logging.error(error)

    @classmethod
    def parser_arguments(cls):
        cls.PARSER.add_argument(
            '-d',
            '--debug',
            dest='debug',
            default=False,
            action='store_true',
            help='More verbose output of status information'
        )
        cls.PARSER.add_argument(
            '--logfile',
            dest='logfile',
            default=cls.LOGFILE,
            help='path to logfile'
        )
        if cls.LOGFILE:
            cls.PARSER.add_argument(
                '--no-logfile',
                dest='nolog',
                default=False,
                action='store_true',
                help='Disable logging to file'
            )

    @staticmethod
    def create_log_dir(logfile):
        usefilelogger = True
        logpath = os.path.dirname(logfile)
        if not os.path.exists(logpath):
            usefilelogger = False
            logging.warning("Log directory %s does not exist!", logpath)
            makedirs(logpath, exist_ok=True)
            logging.info("log directory %s created", logpath)
            usefilelogger = True
        return usefilelogger


class ConfigModule(ModuleParserPlugin):

    CONFIGFILE = None
    BASEPACKAGE = None

    def __init__(self, cmdargs=None, namespace=None):
        super().__init__(cmdargs, namespace)
        if not self.args.config.configfiles and self.CONFIGFILE:
            self.args.config.append(self.CONFIGFILE)

    @classmethod
    def parser_arguments(cls):
        cls.PARSER.add_argument(
            '-c',
            '--config',
            dest='config',
            default=ExtendedConfigParser(package=cls.BASEPACKAGE),
            action="append",
            help='path to configuration file'
        )
