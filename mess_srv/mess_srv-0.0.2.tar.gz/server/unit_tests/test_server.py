"""Тестирование обработки входящих запросов сервером"""

import unittest


from server.data.msg_keys import ERROR, ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, TEXT_MSG
from common.msg_response import RESPONSE


class TestServer(unittest.TestCase):
    """Тестирования функций сервера"""
    dict_error = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }

    dict_no_error = {
        RESPONSE: 200
    }

    def test_no_error(self):
        """Прием корректного запроса"""
        self.assertEqual(answer_to_client({
            ACTION: PRESENCE,
            TIME: 1.1,
            USER: {ACCOUNT_NAME: 'Guest'}
        }), self.dict_no_error)

    def test_wrong_username(self):
        """Ошибка если имя пользователя в запросе не Guest"""
        self.assertEqual(answer_to_client({
            ACTION: PRESENCE,
            TIME: 1.1,
            USER: {ACCOUNT_NAME: 'Guest1'},
            TEXT_MSG: 'Здесь когда-то будет сообщение'
        }), self.dict_error)

    def test_no_action(self):
        """Ошибка если в запросе отсутствует поле Action"""
        self.assertEqual(answer_to_client({
            TIME: 1.1,
            USER: {ACCOUNT_NAME: 'Guest'},
            TEXT_MSG: 'Здесь когда-то будет сообщение'
        }), self.dict_error)


if __name__ == '__main__':
    unittest.main()
