"""Мессенджер. Серверная часть"""
import argparse
import configparser
import logging
import os
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from server.data.msg_keys import PORT
from server.config.cfg_path import INI_DIR
from server.config.cfg_srv_db import SrvDataBase
from server.gui.gui_main_window import MainWindow
from server.data.core import ServerBody
from server.data.decorators import Log

LOGGER = logging.getLogger('server')


@Log()
def arg_parser(port, ip_address):
    """Парсер аргументов"""
    LOGGER.debug('Инициализация парсера аргументов: %s', sys.argv)
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default=port, type=int, nargs='?')
    parser.add_argument('-a', default=ip_address, nargs='?')
    parser.add_argument('--no_gui', action='store_true')
    namespace = parser.parse_args(sys.argv[1:])
    listen_address = namespace.a
    listen_port = namespace.p
    gui_flag = namespace.no_gui
    LOGGER.debug('Аргументы успешно загружены')
    return listen_address, listen_port, gui_flag


@Log()
def config_load():
    """Парсер конфигурации"""
    config = configparser.ConfigParser()
    config_path = os.path.join(INI_DIR, f'server.ini')
    config.read(config_path)
    if 'SETTINGS' in config:
        return config
    else:
        config.add_section('SETTINGS')
        config.set('SETTINGS', 'port', str(PORT))
        config.set('SETTINGS', 'ip_addr', '')
        config.set('SETTINGS', 'db_path', '')
        config.set('SETTINGS', 'db_file', 'srv_db.db3')
        return config


@Log()
def main():
    """Основная функция"""
    config = config_load()
    listen_address, listen_port, gui_flag = arg_parser(
        config['SETTINGS']['port'], config['SETTINGS']['ip_addr'])
    database = SrvDataBase(
        os.path.join(
            config['SETTINGS']['db_path'],
            config['SETTINGS']['db_file']))
    server = ServerBody(listen_address, listen_port, database)
    server.daemon = True
    server.start()
    if gui_flag:
        while True:
            command = input('Для выключения сервера введите stop')
            if command == 'stop':
                server.running = False
                server.join()
                break
    else:
        server_app = QApplication(sys.argv)
        server_app.setAttribute(Qt.AA_DisableWindowContextHelpButton)
        main_window = MainWindow(database, server, config)
        server_app.exec_()
        server.running = False


if __name__ == '__main__':
    main()
