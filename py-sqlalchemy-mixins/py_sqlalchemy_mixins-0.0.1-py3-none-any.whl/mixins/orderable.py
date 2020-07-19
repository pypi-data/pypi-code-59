from sqlalchemy import func, Column, Integer
from sqlalchemy.engine.default import DefaultExecutionContext
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.selectable import Select
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.result import RowProxy


def default_order_index(context: DefaultExecutionContext) -> int:
    """
    Get the current highest index
    """
    if context:
        engine: Engine = context.engine
        try:
            query: Select = select([func.max(1, func.max(context.current_column.table.c.order_index) + 1)])
            r: RowProxy = engine.execute(query).fetchone()
            i: int = int(r[0])
            return i
        except (TypeError, IndexError):
            return 0
    else:
        return 0


class OrderableMixin(object):
    """
    Mixin to make database models comparable.
    --
    The highest object has the lowest index (e.g. ZERO (0))

    The lowest object has the highest index (.e.g INF (9999999999))

    """

    order_index = Column(Integer,
                         default=default_order_index,
                         index=True)

    @classmethod
    def normalize(cls) -> None:
        """ Normalize all order indexes """

        for idx, item in enumerate(cls.query.order_by(cls.order_index).all()):
            item.order_index = idx

    def move_up(self) -> None:
        """ Move the database object one up -> decreases index by one"""
        if self.order_index == 0:
            return

        # get all items ordered by their index
        items = self.query.order_by(self.__class__.order_index).all()
        idx = items.index(self)

        # swap with item above
        above = items[idx - 1]
        above.order_index, self.order_index = idx, above.order_index

    def move_down(self) -> None:
        """ Move the database object one down -> increases index by on"""

        # get all items ordered by their index
        items = self.query.order_by(self.__class__.order_index).all()
        idx = items.index(self)

        # if item is last do nothing
        if idx == len(items) - 1:
            return

        # swap with item below
        below = items[idx + 1]
        below.order_index, self.order_index = idx, below.order_index
