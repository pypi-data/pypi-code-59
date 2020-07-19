import datetime
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime, Text
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.sql import default_comparator
from server.config.cfg_path import ROOT_DIR


class SrvDataBase:
    # Описание серверного хранилища данных
    class UsersAll:
        # Все пользователи
        def __init__(self, username, pass_hash):
            self.name = username
            self.last_session = datetime.datetime.now()
            self.pass_hash = pass_hash
            self.pubkey = None
            self.id = None

    class UsersActive:
        # Активные пользователи
        def __init__(self, user_id, ip_address, port, login_time):
            self.user = user_id
            self.ip_address = ip_address
            self.port = port
            self.login_time = login_time
            self.id = None

    class UsersLoginHistory:
        # История входов
        def __init__(self, name, date, ip, port):
            self.id = None
            self.name = name
            self.date_time = date
            self.ip = ip
            self.port = port

    class UsersContacts:
        # Контакты
        def __init__(self, user, contact):
            self.id = None
            self.user = user
            self.contact = contact

    class UsersHistory:
        # История действий пользователя
        def __init__(self, user):
            self.id = None
            self.user = user
            self.sent = 0
            self.accepted = 0

    def __init__(self, path):
        # Указываем директорию для хранения файлов БД
        self.db_engine = create_engine(f'sqlite:///{ROOT_DIR}/{path}',
                                       echo=False,
                                       pool_recycle=7200,
                                       connect_args={'check_same_thread': False})
        self.metadata = MetaData()

        users_table = Table('Users',
                            self.metadata,
                            Column('id', Integer, primary_key=True),
                            Column('name', String, unique=True),
                            Column('last_session', DateTime),
                            Column('pass_hash', String),
                            Column('pubkey', Text)
                            )

        active_users_table = Table('Active_users',
                                   self.metadata,
                                   Column('id', Integer, primary_key=True),
                                   Column('user', ForeignKey('Users.id'), unique=True),
                                   Column('ip_address', String),
                                   Column('port', Integer),
                                   Column('login_time', DateTime)
                                   )

        user_login_history = Table('Login_history',
                                   self.metadata,
                                   Column('id', Integer, primary_key=True),
                                   Column('name', ForeignKey('Users.id')),
                                   Column('date_time', DateTime),
                                   Column('ip', String),
                                   Column('port', String)
                                   )

        users_contacts = Table('Contacts',
                               self.metadata,
                               Column('id', Integer, primary_key=True),
                               Column('user', ForeignKey('Users.id')),
                               Column('contact', ForeignKey('Users.id'))
                               )

        users_history_table = Table('History', self.metadata,
                                    Column('id', Integer, primary_key=True),
                                    Column('user', ForeignKey('Users.id')),
                                    Column('sent', Integer),
                                    Column('accepted', Integer)
                                    )

        self.metadata.create_all(self.db_engine)

        mapper(self.UsersAll, users_table)
        mapper(self.UsersActive, active_users_table)
        mapper(self.UsersLoginHistory, user_login_history)
        mapper(self.UsersContacts, users_contacts)
        mapper(self.UsersHistory, users_history_table)

        Session = sessionmaker(bind=self.db_engine)
        self.session = Session()

        self.session.query(self.UsersActive).delete()
        self.session.commit()

    def user_login(self, username, ip_address, port, key):
        rez = self.session.query(self.UsersAll).filter_by(name=username)
        if rez.count():
            user = rez.first()
            user.last_login = datetime.datetime.now()
            if user.pubkey != key:
                user.pubkey = key
            else:
                raise ValueError('Пользователь не зарегистрирован.')

            new_active_user = self.UsersActive(user.id, ip_address, port, datetime.datetime.now())
            self.session.add(new_active_user)

            history = self.UsersLoginHistory(user.id, datetime.datetime.now(), ip_address, port)
            self.session.add(history)

            self.session.commit()

    def user_add(self, name, pass_hash):
        user_row = self.UsersAll(name, pass_hash)
        self.session.add(user_row)
        self.session.commit()
        history_row = self.UsersHistory(user_row.id)
        self.session.add(history_row)
        self.session.commit()

    def user_remove(self, name):
        user = self.session.query(self.UsersAll).filter_by(name=name).first()
        self.session.query(self.UsersActive).filter_by(user=user.id).delete()
        self.session.query(self.UsersLoginHistory).filter_by(name=user.id).delete()
        self.session.query(self.UsersContacts).filter_by(user=user.id).delete()
        self.session.query(self.UsersContacts).filter_by(contact=user.id).delete()
        self.session.query(self.UsersHistory).filter_by(user=user.id).delete()
        self.session.query(self.UsersAll).filter_by(name=name).delete()
        self.session.commit()

    def user_get_hash(self, name):
        user = self.session.query(self.UsersAll).filter_by(name=name).first()
        return user.pass_hash

    # Функция возвращает публичный ключ пользователя
    def get_pubkey(self, name):
        user = self.session.query(self.UsersAll).filter_by(name=name).first()
        return user.pubkey

    def user_check(self, name):
        if self.session.query(self.UsersAll).filter_by(name=name).count():
            return True
        else:
            return False

    def user_logout(self, username):
        user = self.session.query(self.UsersAll).filter_by(name=username).first()
        self.session.query(self.UsersActive).filter_by(user=user.id).delete()
        self.session.commit()

    def process_message(self, sender, recipient):
        sender = self.session.query(self.UsersAll).filter_by(name=sender).first().id
        recipient = self.session.query(self.UsersAll).filter_by(name=recipient).first().id

        sender_row = self.session.query(self.UsersHistory).filter_by(user=sender).first()
        sender_row.sent += 1

        recipient_row = self.session.query(self.UsersHistory).filter_by(user=recipient).first()
        recipient_row.accepted += 1

        self.session.commit()

    def contact_add(self, user, contact):
        user = self.session.query(self.UsersAll).filter_by(name=user).first()
        contact = self.session.query(self.UsersAll).filter_by(name=contact).first()

        if not contact or self.session.query(self.UsersContacts).filter_by(user=user.id, contact=contact.id).count():
            return

        contact_row = self.UsersContacts(user.id, contact.id)
        self.session.add(contact_row)
        self.session.commit()

    def contact_remove(self, user, contact):
        user = self.session.query(self.UsersAll).filter_by(name=user).first()
        contact = self.session.query(self.UsersAll).filter_by(name=contact).first()

        if not contact:
            return

        self.session.query(self.UsersContacts).filter(
            self.UsersContacts.user == user.id,
            self.UsersContacts.contact == contact.id
        ).delete()

        self.session.commit()

    def users_list(self):
        query = self.session.query(
            self.UsersAll.name,
            self.UsersAll.last_session
        )
        return query.all()

    def active_users_list(self):
        query = self.session.query(
            self.UsersAll.name,
            self.UsersActive.ip_address,
            self.UsersActive.port,
            self.UsersActive.login_time
        ).join(self.UsersAll)
        return query.all()

    def login_history(self, username=None):
        query = self.session.query(self.UsersAll.name,
                                   self.UsersLoginHistory.date_time,
                                   self.UsersLoginHistory.ip,
                                   self.UsersLoginHistory.port
                                   ).join(self.UsersAll)
        if username:
            query = query.filter(self.UsersAll.name == username)
        return query.all()

    def get_contacts(self, username):
        user = self.session.query(self.UsersAll).filter_by(name=username).one()
        query = self.session.query(
            self.UsersContacts,
            self.UsersAll.name
        ).filter_by(user=user.id).join(self.UsersAll,
                                       self.UsersContacts.contact == self.UsersAll.id
                                       )
        return [contact[1] for contact in query.all()]

    def message_history(self):
        query = self.session.query(
            self.UsersAll.name,
            self.UsersAll.last_session,
            self.UsersHistory.sent,
            self.UsersHistory.accepted
        ).join(self.UsersAll)
        return query.all()


if __name__ == '__main__':
    db = SrvDataBase('../srv_database/srv_db.db3')
    db.user_login('user_1', '192.168.1.4', 8888, 111)
    db.user_login('user_2', '192.168.1.5', 7777, 222)
    print('---------')
    print(f'Список активных юзеров\n'
          f'{db.active_users_list()}')
    print('---------')
    db.process_message('user_1', 'user_2')
    print(db.message_history())
