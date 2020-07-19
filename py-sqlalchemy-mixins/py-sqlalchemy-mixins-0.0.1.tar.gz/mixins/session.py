from contextlib import contextmanager


class SessionNotSetError(Exception):
    pass


class classproperty(object):
    """
    taken from http://stackoverflow.com/a/13624858
    """

    def __init__(self, fget):
        self.fget = fget

    def __get__(self, owner_self, owner_cls):
        return self.fget(owner_cls)


class SessionMixin:
    _session = None

    @classmethod
    def set_session(cls, session):
        cls._session = session

    @classproperty
    def session(cls):
        if cls._session is None:
            raise SessionNotSetError("You need to set a session first")
        return cls._session

    @classmethod
    @contextmanager
    def get_session(cls):
        session = cls.session
        try:
            yield session
        except Exception as e:
            session.rollback()
            raise e
        else:
            session.commit()

    @classproperty
    def query(cls):
        return cls.session.query(cls)
