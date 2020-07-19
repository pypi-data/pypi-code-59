import logging
import sys

if sys.argv[0].find('client') == -1:
    LOGGER = logging.getLogger('server')
else:
    LOGGER = logging.getLogger('client')


class Port:
    """Дескриптор проверки корректности порта"""
    def __set__(self, instance, port):
        if not 1023 < port < 65536:
            LOGGER.critical(
                'Попытка запуска сервера с указанием неподходящего порта %s.',
                port)
            raise TypeError('Некорректный номер порта')
        instance.__dict__[self.name] = port

    def __set_name__(self, owner, name):
        self.name = name
