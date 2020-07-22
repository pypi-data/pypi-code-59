# -*- coding: utf-8 -*-

from collections import namedtuple

import fast_tracker.core.trace_node

from fast_tracker.common import system_info
from fast_tracker.core.node_mixin import DatastoreNodeMixin
from fast_tracker.core.metric import TimeMetric

_DatastoreNode = namedtuple('_DatastoreNode',
                            ['product', 'target', 'operation', 'children', 'start_time',
                             'end_time', 'duration', 'exclusive', 'host', 'port_path_or_id',
                             'database_name', 'is_async', 'guid', 'agent_attributes',
                             'user_attributes', ])


class DatastoreNode(_DatastoreNode, DatastoreNodeMixin):

    @property
    def instance_hostname(self):
        if self.host in system_info.LOCALHOST_EQUIVALENTS:
            hostname = system_info.gethostname()
        else:
            hostname = self.host
        return hostname

    def trace_node(self, stats, root, connections):
        name = root.string_table.cache(self.name)
        start_time = fast_tracker.core.trace_node.node_start_time(root, self)
        end_time = fast_tracker.core.trace_node.node_end_time(root, self)
        children = []
        root.trace_node_count += 1
        self.agent_attributes['db_port'] = self.port_path_or_id
        self.agent_attributes['db_type'] = self.product
        params = self.get_trace_segment_params(root.settings)
        ds_tracer_settings = stats.settings.datastore_tracer
        instance_enabled = ds_tracer_settings.instance_reporting.enabled
        if instance_enabled:
            if self.instance_hostname:
                params['host'] = self.instance_hostname
            if self.port_path_or_id:
                params['port_path_or_id'] = self.port_path_or_id
        return fast_tracker.core.trace_node.TraceNode(start_time=start_time,end_time=end_time, name=name,
                                                      params=params, children=children, label=None)
