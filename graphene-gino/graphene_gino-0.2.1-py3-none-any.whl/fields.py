import inspect
from functools import partial

import sqlalchemy
from graphene import (
    Argument,
    Connection,
    ConnectionField,
    Field,
    Int,
    List,
    String,
)
from sqlalchemy.orm.query import Query

from .filtering import FilterSet
from .registry import get_global_registry
from .utils import (
    TOTAL_FIELD,
    get_query,
)

FILTERS_FIELD = 'filters'
ORDER_BY_FIELD = 'order_by'
PAGE_FIELD = 'page'
PAGINATE_BY_FIELD = 'paginate_by'


class GinoConnection(Connection):

    count = Int()
    total = Int()

    def resolve_count(self, info, **args):
        return len(self.edges)

    def resolve_total(self, info, **args):
        if self.edges:
            result = getattr(self.edges[0].node, TOTAL_FIELD, None)
            if result is None:
                return len(self.edges)
            return result
        return 0

    class Meta:
        abstract = True


class GinoNodeField(Field):
    def __init__(self, type, *args, **kwargs):  # noqa: A002
        # TODO
        self.primary_key_name = self._meta.model.primary_key.columns.keys()[0]
        kwargs.update({
            self.primary_key_name: Int(),
        })
        super(GinoNodeField, self).__init__(
            type,
            *args,
            **kwargs,
        )

    async def node_resolver(self, resolver, root, info, **args):
        query = resolver(root, info, **args)
        if query is None:
            query = await self._type.get_node(info, args[self.primary_key_name])
        return query

    def get_resolver(self, parent_resolver):
        return super().get_resolver(partial(self.node_resolver, parent_resolver))


class GinoConnectionField(ConnectionField):
    def __init__(self, connection, registry=None, *args, **kwargs):  # noqa: A002
        kwargs.update({
            ORDER_BY_FIELD: Argument(List(String)),
            PAGE_FIELD: Argument(Int),
            PAGINATE_BY_FIELD: Argument(Int),
        })
        if not registry:
            registry = get_global_registry()

        if 'filters' in kwargs:
            self._filters = kwargs['filters']
        else:
            model = connection._meta.node._meta.model
            inspected_model = sqlalchemy.inspect(model)
            all_model_attrs = inspected_model.columns
            filter_set_name = '{0}DefaultFilterSet'.format(model.__name__)
            self._filters = registry.get_default_filter(filter_set_name)
            if not self._filters:
                filters_meta = type('Meta', (), {
                    'model': model,
                    'fields': {column.key: [...] for column in all_model_attrs},
                })
                self._filters = type('{0}DefaultFilterSet'.format(model.__name__), (FilterSet,), {
                    'Meta': filters_meta,
                })
                registry.register_default_filter(filter_set_name, self._filters)

        if self._filters:
            kwargs[FILTERS_FIELD] = Argument(self._filters)
        else:
            del kwargs['filters']

        super(GinoConnectionField, self).__init__(connection, *args, **kwargs)

    @property
    def model(self):
        return self.type._meta.node._meta.model

    async def _query_resolver(self, query, info, **args):
        if query is None:
            query = self.model
        filter_set = self.get_filter_set(info)
        filters = args.get(FILTERS_FIELD, {})
        order_by = args.get(ORDER_BY_FIELD, [])
        page = args.get(PAGE_FIELD, None)
        paginate_by = args.get(PAGINATE_BY_FIELD, None)
        query = await get_query(query, info, filter_set, filters, order_by, page, paginate_by)
        return query

    async def query_resolver(self, resolver, root, info, **args):
        query = resolver(root, info, **args)
        if inspect.isawaitable(query):
            return await query
        if query is None or isinstance(query, Query):
            query = await self._query_resolver(query, info, **args)
        return await query.gino.all()

    def get_resolver(self, parent_resolver):
        return super().get_resolver(partial(self.query_resolver, parent_resolver))

    def get_filter_set(self, info: 'ResolveInfo') -> 'FilterSet':  # noqa: F821
        """
        Get field filter set.
        Args:
            info: Graphene resolve info object.
        Returns:
            FilterSet class from field args.
        """
        return self._filters


class GinoListField(Field):
    def __init__(self, _type, *args, **kwargs):
        super(GinoListField, self).__init__(List(_type), *args, **kwargs)
