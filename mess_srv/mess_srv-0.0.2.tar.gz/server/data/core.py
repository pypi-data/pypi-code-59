import threading
import logging
import select
import socket
import json
import hmac
import binascii
import os

from server.data.decorators import Log
from server.data.descript import Port
from server.data.msg_actions import get_msg, send_msg
from server.data.msg_keys import EXIT, GET_CONTACTS, LIST_INFO, ADD_CONTACT, \
    REMOVE_CONTACT, USERS_REQUEST, PUBLIC_KEY_REQUEST, DESTINATION, SENDER, PRESENCE, \
    ACTION, TIME, USER, MSG, TEXT_MSG, ERROR, ACCOUNT_NAME, DATA, PUBLIC_KEY, MAX_CONNECTIONS, RESP_200, RESP_400, \
    RESP_202, RESP_511, RESPONSE, RESP_205

LOGGER = logging.getLogger('server')


@Log()
class ServerBody(threading.Thread):
    port = Port()

    def __init__(self, listen_address, listen_port, database):
        self.addr = listen_address
        self.port = listen_port
        self.database = database
        self.transport = None
        self.clients = []
        self.listen_sockets = None
        self.error_sockets = None
        self.running = True
        self.names = dict()
        super().__init__()

    def run(self):
        self.sock_init()

        while self.running:
            try:
                client, client_address = self.transport.accept()
            except OSError:
                pass
            else:
                LOGGER.info('Установлено соединение с клиентом %s', client_address)
                client.settimeout(5)
                self.clients.append(client)

            recv_data_lst = []
            send_data_lst = []
            err_lst = []

            try:
                if self.clients:
                    recv_data_lst, self.listen_sockets, self.error_sockets = select.select(
                        self.clients, self.clients, [], 0)
            except OSError as error:
                LOGGER.error('Возникла ошибка в работе сокета: %s', error.errno)

            if recv_data_lst:
                for client_msg in recv_data_lst:
                    try:
                        self.process_client_message(get_msg(client_msg), client_msg)
                    except (OSError, json.JSONDecodeError, TypeError) as error:
                        LOGGER.debug('Получение данных из исключения клиента', exc_info=error)
                        self.remove_client(client_msg)

    def remove_client(self, client):
        LOGGER.info('Клиент %s отключился от сервера', client.getpeername())
        for name in self.names:
            if self.names[name] == client:
                self.database.user_logout(name)
                del self.names[name]
                break
        self.clients.remove(client)
        client.close()

    def sock_init(self):
        LOGGER.info('Сервер успешно запущен: %s:%s', self.addr, self.port)

        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.bind((self.addr, self.port))
        transport.settimeout(0.5)

        self.transport = transport
        self.transport.listen(MAX_CONNECTIONS)

    def process_message(self, msg):
        if msg[DESTINATION] in self.names and self.names[msg[DESTINATION]] in self.listen_sockets:
            try:
                send_msg(self.names[msg[DESTINATION]], msg)
                LOGGER.info('Сообщение от %s отправлено %s', msg[SENDER], msg[DESTINATION])
            except OSError:
                self.remove_client(msg[DESTINATION])
        elif msg[DESTINATION] in self.names and self.names[msg[DESTINATION]] not in self.listen_sockets:
            LOGGER.error('Не удалось установить связь с клиентом %s', msg[DESTINATION])
            self.remove_client(self.names[msg[DESTINATION]])
        else:
            LOGGER.error('Пользователь %s не зарегистрирован на сервере', msg[DESTINATION])

    # @login_required
    def process_client_message(self, msg, client):
        LOGGER.debug('Формируется ответ на входящее сообщение: %s', msg)

        if ACTION in msg and msg[ACTION] == PRESENCE and TIME in msg and USER in msg:
            self.auth_user(msg, client)

        elif ACTION in msg and msg[ACTION] == MSG and DESTINATION in msg and TIME in msg \
                and SENDER in msg and TEXT_MSG in msg and self.names[msg[SENDER]] == client:
            if msg[DESTINATION] in self.names:
                self.database.process_message(msg[SENDER], msg[DESTINATION])
                self.process_message(msg)
                try:
                    send_msg(client, RESP_200)
                except OSError:
                    self.remove_client(client)
            else:
                response = RESP_400
                response[ERROR] = 'Пользователь не зарегистрирован на сервере'
                try:
                    send_msg(client, response)
                except OSError:
                    pass
            return
        # Выход клиента
        elif ACTION in msg and msg[ACTION] == EXIT and ACCOUNT_NAME in msg \
                and self.names[msg[ACCOUNT_NAME]] == client:
            self.remove_client(client)
        # Запрос списка контактов
        elif ACTION in msg and msg[ACTION] == GET_CONTACTS and USER in msg and \
                self.names[msg[USER]] == client:
            response = RESP_202
            response[LIST_INFO] = self.database.get_contacts(msg[USER])
            try:
                send_msg(client, response)
            except OSError:
                self.remove_client(client)
        # Добавление контакта
        elif ACTION in msg and msg[ACTION] == ADD_CONTACT and ACCOUNT_NAME in msg and USER in msg \
                and self.names[msg[USER]] == client:
            self.database.contact_add(msg[USER], msg[ACCOUNT_NAME])
            try:
                send_msg(client, RESP_200)
            except OSError:
                self.remove_client(client)
        # Удаление контакта
        elif ACTION in msg and msg[ACTION] == REMOVE_CONTACT and ACCOUNT_NAME in msg \
                and USER in msg and self.names[msg[USER]] == client:
            self.database.contact_remove(msg[USER], msg[ACCOUNT_NAME])
            try:
                send_msg(client, RESP_200)
            except OSError:
                self.remove_client(client)
        # Запрос известных пользователей
        elif ACTION in msg and msg[ACTION] == USERS_REQUEST and ACCOUNT_NAME in msg \
                and self.names[msg[ACCOUNT_NAME]] == client:
            response = RESP_202
            response[LIST_INFO] = [user[0] for user in self.database.users_list()]
            try:
                send_msg(client, response)
            except OSError:
                self.remove_client(client)
        # Запрос публичного ключа
        elif ACTION in msg and msg[ACTION] == PUBLIC_KEY_REQUEST and ACCOUNT_NAME in msg:
            response = RESP_511
            response[DATA] = self.database.get_pubkey(msg[ACCOUNT_NAME])
            if response[DATA]:
                try:
                    send_msg(client, response)
                except OSError:
                    self.remove_client(client)
            else:
                response = RESP_400
                response[ERROR] = 'Публичный ключ для данного пользователя отсутствует'
                try:
                    send_msg(client, response)
                except OSError:
                    self.remove_client(client)
        # Bad Request
        else:
            response = RESP_400
            response[ERROR] = 'Запрос некорректен'
            try:
                send_msg(client, response)
            except OSError:
                self.remove_client(client)

    def auth_user(self, message, sock):
        LOGGER.debug('Инициализация процесса авторизации для %s', message[USER])
        if message[USER][ACCOUNT_NAME] in self.names.keys():
            response = RESP_400
            response[ERROR] = 'Имя пользователя уже занято'
            try:
                LOGGER.debug('Имя пользователя занято. отправка %s', response)
                send_msg(sock, response)
            except OSError:
                LOGGER.debug('OS Error')
                pass
            self.clients.remove(sock)
            sock.close()
        elif not self.database.user_check(message[USER][ACCOUNT_NAME]):
            response = RESP_400
            response[ERROR] = 'Пользователь не зарегистрирован'
            try:
                LOGGER.debug('Пользователь не зарегистрирован. Отправка %s', response)
                send_msg(sock, response)
            except OSError:
                pass
            self.clients.remove(sock)
            sock.close()
        else:
            LOGGER.debug('Имя пользователя указано верно, начинается проверка пароля')
            msg_auth = RESP_511
            random_str = binascii.hexlify(os.urandom(64))
            msg_auth[DATA] = random_str.decode('ascii')
            hash = hmac.new(self.database.user_get_hash(message[USER][ACCOUNT_NAME]), random_str, 'MD5')
            digest = hash.digest()
            LOGGER.debug('Авторизация... %s', msg_auth)
            try:
                send_msg(sock, msg_auth)
                ans = get_msg(sock)
            except OSError as error:
                LOGGER.debug('Ошибка в данных авторизации:', exc_info=error)
                sock.close()
                return
            client_digest = binascii.a2b_base64(ans[DATA])

            if RESPONSE in ans and ans[RESPONSE] == 511 and hmac.compare_digest(digest, client_digest):
                self.names[message[USER][ACCOUNT_NAME]] = sock
                client_ip, client_port = sock.getpeername()
                try:
                    send_msg(sock, RESP_200)
                except OSError:
                    self.remove_client(message[USER][ACCOUNT_NAME])
                self.database.user_login(
                    message[USER][ACCOUNT_NAME],
                    client_ip,
                    client_port,
                    message[USER][PUBLIC_KEY])
            else:
                response = RESP_400
                response[ERROR] = 'Неверный пароль.'
                try:
                    send_msg(sock, response)
                except OSError:
                    pass
                self.clients.remove(sock)
                sock.close()

    def service_update_lists(self):
        for client in self.names:
            try:
                send_msg(self.names[client], RESP_205)
            except OSError:
                self.remove_client(self.names[client])
