"""Ключи используемых действий"""

# Сетевые настройки по умолчанию
IP_ADDRESS = '127.0.0.1'
PORT = 7777
MAX_CONNECTIONS = 5
PACKAGE_LENGTH = 10240

# Кодировка проекта
ENCODING = 'utf-8'

# Действия с контактами
ADD_CONTACT = 'add'
REMOVE_CONTACT = 'remove'
GET_CONTACTS = 'get_contacts'

# Public Keys
PUBLIC_KEY = 'pubkey'
PUBLIC_KEY_REQUEST = 'pubkey_need'

# Основные ключи
ACCOUNT_NAME = 'account_name'
ACTION = 'action'
DATA = 'bin'
ERROR = 'error'
EXIT = 'exit'
LIST_INFO = 'data_list'
MSG = 'message'
PRESENCE = 'presence'
TEXT_MSG = 'text'
TIME = 'time'
USER = 'user'
USERS_REQUEST = 'get_users'

# Отправитель, получатель
DESTINATION = 'to'
SENDER = 'from'

# Коды ответов
RESPONSE = 'response'
RESP_200 = {RESPONSE: 200}
RESP_202 = {RESPONSE: 202, LIST_INFO: None}
RESP_205 = {RESPONSE: 205}
RESP_400 = {RESPONSE: 400, ERROR: None}
RESP_511 = {RESPONSE: 511, DATA: None}
