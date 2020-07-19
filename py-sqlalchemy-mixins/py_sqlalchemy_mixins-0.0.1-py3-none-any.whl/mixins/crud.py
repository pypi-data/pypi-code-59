from sqlalchemy.ext.declarative.api import declarative_base
from mixins.session import SessionMixin
import typing

Base = declarative_base()

class BaseModelMixin(Base, SessionMixin):
    __abstract__ = True
    pass


class CRUDMixin(BaseModelMixin):
    __abstract__ = True

    def __repr__(self):
        return f"<{self.__class__.__name__}>"

    @classmethod
    def create(cls, **kwargs):
        """
        Creates the object and saves it.
        """
        instance = cls(**kwargs)
        return instance.save()

    @classmethod
    def all(cls):
        """
        Get all instances for that model class.
        """
        return cls.query.all()

    @classmethod
    def get(cls, _id):
        """
        Get the instance with the given id.
        """
        return cls.query.get(_id)

    @classmethod
    def first(cls):
        """
        Get the first instance for that model class.
        """
        return cls.query.first()

    @classmethod
    def destroy(cls, ids: typing.List):
        """
        Delete the records with the given ids.
        """
        with cls.get_session():
            for pk in ids:
                cls.get(pk).delete()

    def update(self, **kwargs):
        """
        Update a instance and saves it on success.
        """
        for name in kwargs.keys():
            try:
                setattr(self, name, kwargs[name])
            except AttributeError as e:
                raise KeyError("Attribute '{}' doesn't exist".format(name)) from e
        self.save()

    def save(self):
        """
        Saves the object to the database.
        """
        with self.get_session() as session:
            session.add(self)
        return self

    def delete(self):
        """
        Delete the object from the database.
        """
        with self.get_session() as session:
            session.delete(self)
        return None

    def clone(self, **kwargs):
        """Clone an arbitrary sqlalchemy model object without its primary key values."""
        with self.get_session() as session:
            table = self.__table__
            non_pk_columns = [k for k in table.columns.keys() if k not in table.primary_key]
            data = {c: getattr(self, c) for c in non_pk_columns}
            data.update(kwargs)
            clone = self.__class__(**data)
            session.add(clone)
        return clone
