"""Основные действия с сообщениями"""
import json
import sys
import logging
from server.data.decorators import Log
from server.data.msg_keys import PACKAGE_LENGTH, ENCODING

if sys.argv[0].find('client') == -1:
    LOGGER = logging.getLogger('server')
else:
    LOGGER = logging.getLogger('client')


@Log()
def send_msg(sock, message):
    """
    Функция кодирует сообщение и отправляет его
    :param sock: сокет для передачи
    :param message: словарь для передачи
    :return: None
    """
    js_message = json.dumps(message)
    LOGGER.info('Вывод отправляемого сообщения js_message - %s', js_message)
    encoded_message = js_message.encode(ENCODING)
    LOGGER.info('Вывод отправляемого сообщения encoded_message - %s', encoded_message)
    sock.send(encoded_message)


@Log()
def get_msg(client):
    """
    Функция принимает сообщение и декодирует его
    :param client: сокет для перечачи данных
    :return: сообщение (словарь)
    """
    encoded_response = client.recv(PACKAGE_LENGTH)
    LOGGER.info('Вывод полученного сообщения encoded_message - %s', encoded_response)
    json_response = encoded_response.decode(ENCODING)
    LOGGER.info('Вывод полученного сообщения json_response - %s', json_response)
    response = json.loads(json_response)
    if isinstance(response, dict):
        LOGGER.debug('Сообщение обработано: %s', response)
        return response
    else:
        raise TypeError
