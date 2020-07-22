# coding:utf-8
import json
import logging
import socket
import datetime
import sys
import os
import logging.config
import threading

__all__ = ['MainLog', ]


def currentframe():
    """Return the frame object for the caller's stack frame."""
    try:
        raise Exception
    except:
        return sys.exc_info()[2].tb_frame.f_back


_srcfile = os.path.normcase(currentframe.__code__.co_filename)


class MainLog:

    _instance_lock = threading.Lock()
    log_levels = ['info', 'debug', 'warn', 'error']

    def __init__(self, app_name, prefix_path, when="D",  backup_count=3):
        if not os.path.exists(prefix_path):
            os.mkdir(prefix_path)
        self.prefix_path = prefix_path
        self.program_log_name = app_name + '-code'
        self.journal_log_name = app_name + '-info'
        self.host_name = socket.gethostname()
        self.generate_loggers(when, backup_count)

    def __new__(cls, *args, **kwargs):
        if not hasattr(MainLog, '_instance'):
            with MainLog._instance_lock:
                if not hasattr(MainLog, '_instance'):
                    MainLog._instance = object.__new__(cls)
        return MainLog._instance

    def generate_loggers(self, when, backup_count):
        pid = str(os.getpid())

        config_dict = dict()
        config_dict['version'] = 1
        config_dict['disable_existing_loggers'] = True
        handler_dict = dict()
        for level in self.log_levels:
            handler_dict[level] = dict()
            handler_dict[level]['class'] = 'logging.handlers.TimedRotatingFileHandler'
            handler_dict[level]['level'] = level.upper()
            if level == 'info':
                file_name = self.journal_log_name
            else:
                file_name = self.program_log_name
            handler_dict[level]['filename'] = os.path.join(self.prefix_path, '%s-%s.%s.log' % (file_name, level, pid))
            handler_dict[level]['when'] = when
            handler_dict[level]['backupCount'] = backup_count
            handler_dict[level]['interval'] = 1
        loggers_dict = dict()
        loggers_dict[self.program_log_name] = dict()
        loggers_dict[self.journal_log_name] = dict()
        loggers_dict[self.program_log_name]['handlers'] = ['debug', 'warn', 'error']
        loggers_dict[self.journal_log_name]['handlers'] = ['info']
        for logger in loggers_dict.keys():
            loggers_dict[logger]['level'] = 'DEBUG'
            loggers_dict[logger]['propagate'] = False
        config_dict['handlers'] = handler_dict
        config_dict['loggers'] = loggers_dict
        logging.config.dictConfig(config_dict)

    def program_model(self, log_level, message, extra=None):
        path_name, lineno, func_name, logger_module = self.get_current_location()
        data = {
            "app_name": self.program_log_name,  # 服务编号
            "logger": logger_module,  # 日志对象名
            "HOSTNAME": self.host_name,  # 主机名
            "log_time": self.date_log_time(),  # 时间
            "level": log_level,  # 日志界别
            "thread": threading.currentThread().ident,  # 线程编号
            "message": message,  # 消息
            "pathName": path_name,  # 打印日志位置
            "lineNo": lineno,  # 打印日志行号
            "funcName": func_name,  # 打印日志方法名
        }
        if isinstance(extra, dict):
            data.update(extra)
        return json.dumps(data, ensure_ascii=False)

    def journal_model(self, dialog_type, log_level='INFO', **kwargs):
        _, _, _, logger_module = self.get_current_location()
        data = {
            "app_name": self.journal_log_name,  # 服务编号
            "level": log_level,  # 日志界别
            "logger": logger_module,  # 日志对象名
            "log_time": self.date_log_time(),  # 时间
            "transaction_id": kwargs.get("transaction_id", ""),
            "dialog_type": dialog_type,
            "address": kwargs.get("address", ""),
            "fcode": kwargs.get("fcode", ""),
            "tcode": kwargs.get("tcode", ""),
            "method_code": kwargs.get("method_code", ""),
            "http_method": kwargs.get("http_method", ""),
            "request_time": kwargs.get("request_time", ""),
            "request_headers": kwargs.get("request_headers", ""),
            "request_payload": kwargs.get("request_payload", ""),
            "response_headers": kwargs.get("response_headers", ""),
            "response_payload": kwargs.get("response_payload", ""),
            "response_time": kwargs.get("response_time", ""),
            "response_code": kwargs.get("response_code", ""),
            "response_remark": kwargs.get("response_remark", ""),
            "http_status_code": kwargs.get("http_status_code", ""),
            "order_id": kwargs.get("order_id", ""),
            "account_type": kwargs.get("account_type", ""),
            "account_num": kwargs.get("account_num", ""),
            "province_code": kwargs.get("province_code", ""),
            "city_code": kwargs.get("city_code", ""),
            "key_type": kwargs.get("key_type", ""),
            "key_param": kwargs.get("key_param", ""),
            "total_time": kwargs.get("total_time", ""),
        }
        return json.dumps(data, ensure_ascii=False)

    def get_current_location(self):
        try:
            # 获取被调用位置的文件路径、行号、函数名
            path_name, lineno, func_name = self.find_caller()
        except ValueError:
            path_name, lineno, func_name = "(unknown file)", 0, "(unknown function)"
        try:
            filename = os.path.basename(path_name)
            logger_module = os.path.splitext(filename)[0]
        except (TypeError, ValueError, AttributeError):
            logger_module = "Unknown module"
        return path_name, lineno, func_name, logger_module

    @staticmethod
    def date_log_time():
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def find_caller():
        f = currentframe()
        if f is not None:
            f = f.f_back
        rv = "(unknown file)", 0, "(unknown function)"
        while hasattr(f, "f_code"):
            co = f.f_code
            filename = os.path.normcase(co.co_filename)
            if filename == _srcfile:
                f = f.f_back
                continue
            rv = (co.co_filename, f.f_lineno, co.co_name)
            break
        return rv

    def debug(self, msg, *args, **kwargs):
        message = self.program_model('DEBUG', msg, kwargs.get('extra'))
        logging.getLogger(self.program_log_name).debug(message, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        message = self.program_model('INFO', msg, kwargs.get('extra'))
        logging.getLogger(self.program_log_name).info(message, *args, **kwargs)

    def warn(self, msg, *args, **kwargs):
        message = self.program_model('WARN',  msg, kwargs.get('extra'))
        logging.getLogger(self.program_log_name).warn(message, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        message = self.program_model('ERROR', msg, kwargs.get('extra'))
        logging.getLogger(self.program_log_name).error(message, *args, **kwargs)

    def external(self, *args, **kwargs):
        message = self.journal_model('in', **kwargs)
        logging.getLogger(self.journal_log_name).info(message)

    def internal(self, *args, **kwargs):
        message = self.journal_model('out', **kwargs)
        logging.getLogger(self.journal_log_name).info(message)

    def exception(self, msg, *args, **kwargs):
        message = self.program_model('ERROR', msg, kwargs.get('extra'))
        logging.getLogger(self.program_log_name).error(message, *args, **kwargs)
