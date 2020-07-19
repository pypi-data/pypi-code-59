from mixins.crud import CRUDMixin


import unittest

import sqlalchemy as sa

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class BaseModel(CRUDMixin):
    __abstract__ = True


class SampleModel(BaseModel):
    __tablename__ = "samples"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255))


class TestWithRealDatabase(unittest.TestCase):
    def setUp(self) -> None:
        # setup ORM to communicate with a sqlite db
        engine = create_engine('sqlite:///:memory:', echo=False)
        session = Session(engine)
        BaseModel.metadata.drop_all(engine)
        BaseModel.metadata.create_all(engine)
        BaseModel.set_session(session)

    def test_create(self):
        some_model = SampleModel.create(name="Test")
        assert some_model
        # check that the primary key was set
        assert some_model.id
        assert some_model.name == "Test"

        # can we query i by asking for the first element?
        model = SampleModel.first()
        assert model
        assert model.id == some_model.id

        # can we get it by it's id
        SampleModel.get(model.id).name == "Test"

    def test_create_multiple(self):
        a = SampleModel.create(name="Test A")
        b = SampleModel.create(name="Test B")
        c = SampleModel.create(name="Test C")

        # are there really 3 items ?
        assert SampleModel.all() == [a, b, c]
        # and can we get different ones ?
        assert SampleModel.first().id == a.id
        assert SampleModel.get(c.id).name == "Test C"

        # can we delete a single one?
        b.delete()
        # was it really deleted ?
        assert SampleModel.all() == [a, c]
        # can we delted the other ones atr once?
        SampleModel.destroy([a.id, c.id])
        assert SampleModel.all() == []

    def test_update_and_persist(self):
        a = SampleModel.create(name="Test A")
        # that the old way
        a.name = "I was updated!"
        a.id = 1234567
        a.save()

        assert SampleModel.first().name == "I was updated!"
        assert SampleModel.first().id == 1234567

        # shortcut
        a.update(name="I like cheeeeese!", id=99999)
        assert SampleModel.first().name == "I like cheeeeese!"
        assert SampleModel.first().id == 99999
