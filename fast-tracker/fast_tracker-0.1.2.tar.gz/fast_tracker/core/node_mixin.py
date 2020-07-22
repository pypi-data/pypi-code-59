# -*- coding: utf-8 -*-
"""
混入设计模式
"""
from enum import Enum

import fast_tracker.core.attribute as attribute
from fast_tracker.core.attribute_filter import (DST_SPAN_EVENTS, DST_TRANSACTION_SEGMENTS)


class SpanType(Enum):
    """span类型"""
    Entry = 0 # 入口
    Exit = 1 # 外部调用
    Local = 2 # 本地调用

class SpanLayerAtrr(Enum):
    """
    span所属层的属性
    """
    Local = 0 # 本地
    DB = 1 # 数据库
    RPC = 2 # RPC框架
    HTTP = 3 # http调用
    MQ = 4 # 中间件
    CACHE = 5 # 缓存


class GenericNodeMixin(object):
    @property
    def processed_user_attributes(self):
        if hasattr(self, '_processed_user_attributes'):
            return self._processed_user_attributes
        self._processed_user_attributes = u_attrs = {}
        for k, v in self.user_attributes.items():
            k, v = attribute.process_user_attribute(k, v)
            u_attrs[k] = v
        return u_attrs

    def get_trace_segment_params(self, settings, params=None):
        _params = attribute.resolve_agent_attributes(
            self.agent_attributes,
            settings.attribute_filter,
            DST_TRANSACTION_SEGMENTS)

        if params:
            _params.update(params)

        _params.update(attribute.resolve_user_attributes(
            self.processed_user_attributes,
            settings.attribute_filter,
            DST_TRANSACTION_SEGMENTS))

        _params['exclusive_duration_millis'] = 1000.0 * self.exclusive
        return _params

    def span_event(
            self, settings, base_attrs=None, parent_guid=None):
        i_attrs = base_attrs and base_attrs.copy() or {}
        i_attrs['t'] = SpanType.Exit.value
        i_attrs['o'] = self.name # 操作名称
        i_attrs['s'] = self.guid # span_id
        i_attrs['d'] = int(self.duration * 1000)
        i_attrs['ts'] = int(self.start_time * 1000)
        i_attrs['te'] = int(self.end_time * 1000)
        i_attrs['y'] = SpanLayerAtrr.HTTP.value

        if parent_guid:
            i_attrs['p'] = parent_guid
        else:
            i_attrs['t'] = SpanType.Entry.value

        a_attrs = attribute.resolve_agent_attributes(
            self.agent_attributes,
            settings.attribute_filter,
            DST_SPAN_EVENTS)

        u_attrs = attribute.resolve_user_attributes(
            self.processed_user_attributes,
            settings.attribute_filter,
            DST_SPAN_EVENTS)
        a_attrs.update(u_attrs)
        return i_attrs, a_attrs

    def span_events(self,
                    settings, base_attrs=None, parent_guid=None):

        yield self.span_event(
            settings,
            base_attrs=base_attrs,
            parent_guid=parent_guid)

        for child in self.children:
            for event in child.span_events(
                    settings,
                    base_attrs=base_attrs,
                    parent_guid=self.guid):
                yield event


class DatastoreNodeMixin(GenericNodeMixin):

    @property
    def name(self):
        product = self.product
        target = self.target
        operation = self.operation or 'other'

        if target:
            name = 'Datastore/statement/%s/%s/%s' % (product, target,
                                                     operation)
        else:
            name = 'Datastore/operation/%s/%s' % (product, operation)

        return name

    @property
    def db_instance(self):
        if hasattr(self, '_db_instance'):
            return self._db_instance

        db_instance_attr = None
        if self.database_name:
            _, db_instance_attr = attribute.process_user_attribute(
                'db_instance', self.database_name)
        self._db_instance = db_instance_attr
        return db_instance_attr

    def span_event(self, *args, **kwargs):
        i_attrs, a_attrs = super(DatastoreNodeMixin, self).span_event(*args, **kwargs)
        if hasattr(self, 'dbapi2_module'):
            component = getattr(self.dbapi2_module, '__name__', None)
            if component is None:
                component = getattr(self.dbapi2_module, '__file__', None)
            if component is None:
                component = str(self.dbapi2_module)
        else:
            component = self.product or self.target
        i_attrs['c'] = component
        i_attrs['y'] = SpanLayerAtrr.DB.value

        if self.instance_hostname:
            _, a_attrs['db_hostname'] = attribute.process_user_attribute(
                'db_hostname', self.instance_hostname)
        else:
            a_attrs['db_hostname'] = 'Unknown'
        a_attrs['db_type'] = self.product or self.target
        a_attrs.update(self.agent_attributes)
        return i_attrs, a_attrs
