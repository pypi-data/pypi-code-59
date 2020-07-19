"""Декораторы"""
import sys
import traceback
import inspect
import logging
import socket

if sys.argv[0].find('client') == -1:
    LOGGER = logging.getLogger('server')
else:
    LOGGER = logging.getLogger('client')


def log(function):
    """Функция-декоратор"""

    def log_save(*args, **kwargs):
        LOGGER.debug(
            'Произведен вызов функции %s c параметрами %s, %s',
            function.__name__,
            args,
            kwargs)
        LOGGER.debug(
            'Вызов из функции %s > %s',
            traceback.format_stack()[0].strip().split()[-1],
            inspect.stack()[1][3])
        LOGGER.debug(
            'Модуль - %s', function.__module__)
        return function(*args, **kwargs)

    return log_save


class Log:
    def __call__(self, function):
        def log_decorate(*args, **kwargs):
            """Обертка"""
            result = function(*args, **kwargs)
            LOGGER.debug(
                'Произведен вызов функции %s c параметрами %s, %s',
                function.__name__,
                args,
                kwargs)
            LOGGER.debug(
                'Вызов из функции %s > %s',
                traceback.format_stack()[0].strip().split()[-1],
                inspect.stack()[1][3])
            LOGGER.debug(
                'Модуль - %s', function.__module__)
            return result

        return log_decorate


@Log()
def login_required(func):
    """
    Декоратор, проверяющий, что клиент авторизован на сервере.
    Проверяет, что передаваемый объект сокета находится в
    списке авторизованных клиентов.
    За исключением передачи словаря-запроса
    на авторизацию. Если клиент не авторизован,
    генерирует исключение TypeError
    """

    def checker(*args, **kwargs):
        from server.data.core import ServerBody
        from server.data.msg_keys import ACTION, PRESENCE
        if isinstance(args[0], ServerBody):
            found = False
            for arg in args:
                if isinstance(arg, socket.socket):
                    for client in args[0].names:
                        if args[0].names[client] == arg:
                            found = True
            for arg in args:
                if isinstance(arg, dict):
                    if ACTION in arg and arg[ACTION] == PRESENCE:
                        found = True
            if not found:
                raise TypeError
        return func(*args, **kwargs)

    return checker
