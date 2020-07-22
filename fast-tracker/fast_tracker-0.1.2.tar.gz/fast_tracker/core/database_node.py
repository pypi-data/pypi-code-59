# -*- coding: utf-8 -*-
from collections import namedtuple

import fast_tracker.core.attribute as attribute
import fast_tracker.core.trace_node

from fast_tracker.common import system_info
from fast_tracker.core.database_utils import sql_statement, explain_plan
from fast_tracker.core.node_mixin import DatastoreNodeMixin
from fast_tracker.core.metric import TimeMetric

_SlowSqlNode = namedtuple('_SlowSqlNode',
                          ['duration', 'path', 'request_uri', 'sql', 'sql_format',
                           'metric', 'dbapi2_module', 'stack_trace', 'connect_params',
                           'cursor_params', 'sql_parameters', 'execute_params',
                           'host', 'port_path_or_id', 'database_name', 'params'])


class SlowSqlNode(_SlowSqlNode):

    def __new__(cls, *args, **kwargs):
        node = _SlowSqlNode.__new__(cls, *args, **kwargs)
        node.statement = sql_statement(node.sql, node.dbapi2_module)
        return node

    @property
    def formatted(self):
        return self.statement.formatted(self.sql_format)

    @property
    def identifier(self):
        return self.statement.identifier


_DatabaseNode = namedtuple('_DatabaseNode',
                           ['dbapi2_module', 'sql', 'children', 'start_time', 'end_time',
                            'duration', 'exclusive', 'stack_trace', 'sql_format',
                            'connect_params', 'cursor_params', 'sql_parameters',
                            'execute_params', 'host', 'port_path_or_id', 'database_name',
                            'is_async', 'guid', 'agent_attributes', 'user_attributes'])


class DatabaseNode(_DatabaseNode, DatastoreNodeMixin):

    def __new__(cls, *args, **kwargs):
        node = _DatabaseNode.__new__(cls, *args, **kwargs)
        node.statement = sql_statement(node.sql, node.dbapi2_module)
        return node

    @property
    def product(self):
        return self.dbapi2_module and self.dbapi2_module._nr_database_product

    @property
    def instance_hostname(self):
        #  获取数据库实例的hostname
        if self.host in system_info.LOCALHOST_EQUIVALENTS:
            hostname = system_info.gethostname()
        else:
            hostname = self.host
        return hostname

    @property
    def operation(self):
        return self.statement.operation

    @property
    def target(self):
        # 获取操作目标的表
        return self.statement.target

    @property
    def formatted(self):
        return self.statement.formatted(self.sql_format)

    def explain_plan(self, connections):
        return explain_plan(connections, self.statement, self.connect_params,
                            self.cursor_params, self.sql_parameters, self.execute_params,
                            self.sql_format)

    def slow_sql_node(self, stats, root):
        """

        :param  stats:
        :param  fast_tracker.api.transaction.Transaction root:
        :return:
        """
        product = self.product
        operation = self.operation or 'other'
        target = self.target

        if target:
            name = 'Datastore/statement/%s/%s/%s' % (product, target,
                                                     operation)
        else:
            name = 'Datastore/operation/%s/%s' % (product, operation)

        request_uri = ''
        if root.type == 'WebTransaction':
            request_uri = root.request_uri

        params = None
        if root.distributed_trace_intrinsics:
            params = root.distributed_trace_intrinsics.copy()

        return SlowSqlNode(duration=self.duration, path=root.path,
                           request_uri=request_uri, sql=self.sql,
                           sql_format=self.sql_format, metric=name,
                           dbapi2_module=self.dbapi2_module,
                           stack_trace=self.stack_trace,
                           connect_params=self.connect_params,
                           cursor_params=self.cursor_params,
                           sql_parameters=self.sql_parameters,
                           execute_params=self.execute_params,
                           host=self.instance_hostname,
                           port_path_or_id=self.port_path_or_id,
                           database_name=self.database_name,
                           params=params)

    def trace_node(self, stats, root, connections):
        name = root.string_table.cache(self.name)

        start_time = fast_tracker.core.trace_node.node_start_time(root, self)
        end_time = fast_tracker.core.trace_node.node_end_time(root, self)

        children = []

        root.trace_node_count += 1

        sql = self.formatted

        self.agent_attributes['db_instance'] = self.db_instance
    
        if sql:
            limit = root.settings.agent_limits.sql_query_length_maximum
            self.agent_attributes['db_statement'] = sql[:limit]

        params = self.get_trace_segment_params(root.settings)

        if self.host:
            params['host'] = self.instance_hostname

        if self.port_path_or_id:
            params['port_path_or_id'] = self.port_path_or_id

        sql = params.get('db_statement')
        if sql:
            params['db_statement'] = root.string_table.cache(sql)

            if self.stack_trace:
                params['backtrace'] = [root.string_table.cache(x) for x in
                                       self.stack_trace]

            if getattr(self, 'generate_explain_plan', None):
                explain_plan_data = self.explain_plan(connections)
                if explain_plan_data:
                    params['explain_plan'] = explain_plan_data

        return fast_tracker.core.trace_node.TraceNode(start_time=start_time,
                                                      end_time=end_time, name=name, params=params, children=children,
                                                      label=None)

    def span_event(self, *args, **kwargs):
        sql = self.formatted
        if sql:
            _, sql = attribute.process_user_attribute(
                'db_statement', sql, max_length=2000, ending='...') 

        self.agent_attributes['db_statement'] = sql
        self.agent_attributes['db_port'] = self.port_path_or_id
        return super(DatabaseNode, self).span_event(*args, **kwargs)
