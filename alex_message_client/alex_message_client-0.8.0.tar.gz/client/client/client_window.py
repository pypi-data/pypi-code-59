"""Модуль, открывающий рабочее окно клиентской части приложения 'Мессенджер'"""
import base64

from Crypto.Cipher import PKCS1_OAEP
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from PyQt5.QtWidgets import QMessageBox, QWidget, QLabel, QLineEdit, QPushButton, qApp, QMainWindow, QDialog

from common.variables import MESSAGE_TEXT, SENDER
from client.client_gui import Ui_MainWindow


class ClientWindow(QMainWindow):
    """
    Класс - основное окно пользователя.
    Содержит всю основную логику работы клиентского модуля.
    Конфигурация окна создана в QTDesigner и загружается из
    конвертированого файла client_gui.py
    """

    def __init__(self, database, transport, keys):
        super().__init__()

        self.database = database
        self.transport = transport

        self.decrypter = PKCS1_OAEP.new(keys)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.load_user_list()
        self.ui.mnu_exit.triggered.connect(self.close)

        self.ui.lstUser.doubleClicked.connect(self.user_list_click)
        self.ui.btn_sendMsg.clicked.connect(self.send_msg)
        self.messages = QMessageBox()
        self.current_chat = None

        self.show()

    def send_msg(self):
        """Метод отправки сообщения выбранному пользователю"""
        self.ui.statusbar.showMessage('Нажали кнопку отправки сообщения')
        self.ui.inputMsg.clear()

    def load_user_list(self):
        """Метод, заполняющий список пользователей в виджет QListView."""
        contacts_list = self.database.get_users()
        model = QStandardItemModel()
        self.ui.lstUser.setModel(model)
        for i in sorted(contacts_list):
            item = QStandardItem(i)
            item.setEditable(False)
            if i == self.transport.username:
                continue
            else:
                model.appendRow(item)
        self.ui.lstUser.setModel(model)

    def user_tab_clicked(self):
        """Метод, открывающий вкладку с выбранным пользователем, для обмена сообщениями."""
        self.ui.statusbar.showMessage(
            f'Выбрана вкладка {self.user_tab.objectName().title()}')
        print(self.ui.lstUser.currentIndex().data().capitalize() + 'Tab')

    # Функция обновляющяя контакт лист
    def clients_list_update(self):
        """Метод, обновляющий список контактов."""
        contacts_list = self.database.get_users()
        contacts_model = QStandardItemModel()
        for i in sorted(contacts_list):
            item = QStandardItem(i)
            item.setEditable(False)
            if i != self.transport.username:
                contacts_model.appendRow(item)
        self.ui.lstUser.setModel(contacts_model)

    # Слот приёма нового сообщений
    @pyqtSlot(dict)
    def message(self, message):
        """
        Слот обработчик поступаемых сообщений, выполняет дешифровку
        поступаемых сообщений и их сохранение в истории сообщений.
        Запрашивает пользователя если пришло сообщение не от текущего
        собеседника. При необходимости меняет собеседника.
        """
        # Получаем строку байтов
        encrypted_message = base64.b64decode(message[MESSAGE_TEXT])
        # Декодируем строку, при ошибке выдаём сообщение и завершаем функцию
        try:
            decrypted_message = self.decrypter.decrypt(encrypted_message)
        except (ValueError, TypeError):
            self.messages.warning(
                self, 'Ошибка', 'Не удалось декодировать сообщение.')
            return
        # Сохраняем сообщение в базу и обновляем историю сообщений или
        # открываем новый чат.
        self.database.save_message(
            self.current_chat,
            'in',
            decrypted_message.decode('utf8'))

        sender = message[SENDER]
        if sender == self.current_chat:
            self.history_list_update()
        else:
            # Проверим есть ли такой пользователь у нас в контактах:
            if self.database.check_contact(sender):
                # Если есть, спрашиваем и желании открыть с ним чат и открываем
                # при желании
                if self.messages.question(self, 'Новое сообщение',
                                          f'Получено новое сообщение от {sender}, открыть чат с ним?',
                                          QMessageBox.Yes,
                                          QMessageBox.No) == QMessageBox.Yes:
                    self.current_chat = sender
                    self.set_active_user()
            else:
                print('NO')
                # Раз нету,спрашиваем хотим ли добавить юзера в контакты.
                if self.messages.question(
                        self,
                        'Новое сообщение',
                        f'Получено новое сообщение от {sender}.\n Данного пользователя нет в вашем '
                        f'контакт-листе.\n Добавить в контакты и открыть чат с ним?',
                        QMessageBox.Yes,
                        QMessageBox.No) == QMessageBox.Yes:
                    self.add_contact(sender)
                    self.current_chat = sender
                    # Нужно заново сохранить сообщение, иначе оно будет потеряно,
                    # т.к. на момент предыдущего вызова контакта не было.
                    self.database.save_message(
                        self.current_chat, 'in', decrypted_message.decode('utf8'))
                    self.set_active_user()

    # Слот потери соединения
    # Выдаёт сообщение о ошибке и завершает работу приложения
    @pyqtSlot()
    def connection_lost(self):
        """
        Слот обработчик потери соеднинения с сервером.
        Выдаёт окно предупреждение и завершает работу приложения.
        """
        self.messages.warning(
            self,
            'Сбой соединения',
            'Потеряно соединение с сервером. ')
        self.close()

    @pyqtSlot()
    def sig_205(self):
        """Слот выполняющий обновление баз данных по команде сервера."""
        if self.current_chat and not self.database.check_user(
                self.current_chat):
            self.messages.warning(
                self,
                'Сочувствую',
                'К сожалению, собеседник был удалён с сервера.')
            self.set_disabled_input()
            self.current_chat = None
        self.clients_list_update()

    def make_connection(self, trans_obj):
        """Метод обеспечивающий соединение сигналов и слотов."""
        trans_obj.new_message.connect(self.message)
        trans_obj.connection_lost.connect(self.connection_lost)
        trans_obj.message_205.connect(self.sig_205)


class UserNameDialog(QDialog):
    """Класс реализующий стартовый диалог с запросом логина и пароля пользователя."""

    def __init__(self):
        super().__init__()

        self.ok_pressed = False

        self.setWindowTitle('Привет!')
        self.setFixedSize(175, 135)

        self.label = QLabel('Введите имя пользователя:', self)
        self.label.move(10, 10)
        self.label.setFixedSize(150, 10)

        self.client_name = QLineEdit(self)
        self.client_name.setFixedSize(154, 20)
        self.client_name.move(10, 30)

        self.btn_ok = QPushButton('Начать', self)
        self.btn_ok.move(10, 105)
        self.btn_ok.clicked.connect(self.click)

        self.btn_cancel = QPushButton('Выход', self)
        self.btn_cancel.move(90, 105)
        self.btn_cancel.clicked.connect(qApp.exit)

        self.label_passwd = QLabel('Введите пароль:', self)
        self.label_passwd.move(10, 55)
        self.label_passwd.setFixedSize(150, 15)

        self.client_passwd = QLineEdit(self)
        self.client_passwd.setFixedSize(154, 20)
        self.client_passwd.move(10, 75)
        self.client_passwd.setEchoMode(QLineEdit.Password)

        self.show()

    def click(self):
        """Метод обрабтчик кнопки подтверждения входа под учётной записью."""
        if self.client_name.text() and self.client_passwd.text():
            self.ok_pressed = True
            qApp.exit()
