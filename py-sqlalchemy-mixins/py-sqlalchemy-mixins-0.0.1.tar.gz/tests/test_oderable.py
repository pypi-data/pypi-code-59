from operator import add
from mixins.session import SessionMixin
from sqlalchemy.ext.declarative.api import declarative_base
from mixins.orderable import OrderableMixin
from mixins.crud import CRUDMixin
import unittest

import sqlalchemy as sa

from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import Session

Base = declarative_base()


class BaseModel(Base, SessionMixin):
    __abstract__ = True


class SampleModel(BaseModel, OrderableMixin):
    __tablename__ = "samples"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255))


def add_obj(obj, session):
    try:
        session.add(obj)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


class TestOrderableMixin(unittest.TestCase):

    def setUp(self) -> None:
        # setup a in memory sqlite db
        engine = create_engine('sqlite:///:memory:', echo=False)
        session = Session(engine)
        BaseModel.metadata.drop_all(engine)
        BaseModel.metadata.create_all(engine)
        BaseModel.set_session(session)
        self.session = session

    def add_obj(self, obj):
        return add_obj(obj, self.session)

    def test_default_index(self):
        self.add_obj(SampleModel())
        assert SampleModel.query.first().order_index == 0

    def test_index_increases(self):
        for i in range(10):
            self.add_obj(SampleModel())

        assert len(SampleModel.query.all()) == 10
        assert SampleModel.query.first().order_index == 0
        assert SampleModel.query.all()[-1].order_index == 9

    def test_move_down(self):
        for i in range(10):
            self.add_obj(SampleModel())

        # the current first has the lowest index
        first: SampleModel = SampleModel.query.first()
        assert first.order_index == 0
        # if we move it down - its index increases
        first.move_down()
        self.session.commit()
        assert first.order_index == 1

        for _ in range(10):
            first.move_down()
        
        self.session.commit()

        assert first.order_index == 9

    def test_move_up(self):
        for _ in range(10):
            self.add_obj(SampleModel())

        # get the obj with the current highest index
        last: SampleModel = SampleModel.query.all()[-1]
        assert last.order_index == 9

        # if we move it down - its index decreases
        last.move_up()
        self.session.commit()
        assert last.order_index == 8

        for _ in range(10):
            last.move_up()
        self.session.commit()
        assert last.order_index == 0

    def test_normalize(self):
        for _ in range(10):
            self.add_obj(SampleModel())

        # randomly mix their index
        all_ = SampleModel.query.all()

        # dont mess up their order - only make the indexes weird
        all_[1].order_index = 1
        all_[2].order_index = 22
        all_[3].order_index = 33
        all_[4].order_index = 45
        all_[5].order_index = 55
        all_[6].order_index = 62
        all_[7].order_index = 78
        all_[8].order_index = 79
        all_[9].order_index = 99

        self.session.commit()

        SampleModel.normalize()
        self.session.commit()

        # now query them again and make sure their indexes are normalized
        all_ = SampleModel.query.all()
        for i in range(10):
            assert all_[i].order_index == i

    def tearDown(self) -> None:
        # cleanup
        SampleModel.query.delete()
