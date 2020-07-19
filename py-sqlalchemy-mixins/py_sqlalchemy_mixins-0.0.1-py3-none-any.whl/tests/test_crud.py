import typing
from tests import MockSession
import unittest

import sqlalchemy as sa

from mixins.crud import CRUDMixin


class SampleModel(CRUDMixin):
    __tablename__ = "sample"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255))


class MockQuery(object):

    def __init__(self, mock_session=None):
        self.mock_session: typing.Optional[MockSession] = mock_session

    def all(self) -> typing.List:
        if self.mock_session:
            return self.mock_session.objects
        return []

    def get(self, _id) -> typing.Optional[object]:
        if self.mock_session:
            for obj in self.mock_session.objects:
                try:
                    if obj.id == _id:
                        return obj
                except KeyError:
                    continue
        return None

    def first(self) -> typing.Optional[object]:
        if self.mock_session and self.mock_session.objects:
            return self.mock_session.objects[0]
        return None


class TestCrud(unittest.TestCase):

    def setUp(self) -> None:
        # create a fake session
        self.session: MockSession = MockSession()
        # create fake queries
        self.mock_query = MockQuery(self.session)
        SampleModel.set_session(self.session)
        SampleModel.query = self.mock_query

    def test_repr(self):
        model = SampleModel()
        assert repr(model) == "<SampleModel>"

    def test_create(self):
        instance = SampleModel.create()
        assert instance
        assert self.session.commit_called
        assert self.session.add_called
        assert instance in self.session.objects

    def test_all(self):
        instance = SampleModel.create()
        assert instance in SampleModel.all()

    def test_get(self):
        instance = SampleModel.create(id=45)
        assert SampleModel.get(45) == instance

    def test_first(self):
        instance = SampleModel.create(id=45)
        SampleModel.create()
        SampleModel.create()
        SampleModel.create()

        assert SampleModel.first() == instance

    def test_delete(self):
        assert not self.session.delete_called
        SampleModel.create(id=45).delete()
        assert self.session.delete_called

    def test_destroy(self):
        assert not self.session.delete_called
        a = SampleModel.create(id=46)
        b = SampleModel.create(id=47)
        c = SampleModel.create(id=48)
        d = SampleModel.create(id=49)
        SampleModel.destroy([46, 47, 48, 49])
        assert self.session.delete_called
        assert self.session.deleted_objects
        assert len(self.session.deleted_objects) == 4
        assert self.session.deleted_objects == [a, b, c, d]

    def test_save(self):
        instance = SampleModel.create(id=45)
        self.session.add_called = False
        instance.id = 23456
        assert not self.session.add_called
        instance.save()
        assert self.session.add_called

    def test_clone(self):
        instance = SampleModel.create(id=45, name="Hey")
        assert instance.name == "Hey"

        clone = instance.clone()
        assert clone != instance

        assert clone.id != instance.id
        assert clone.name == instance.name
