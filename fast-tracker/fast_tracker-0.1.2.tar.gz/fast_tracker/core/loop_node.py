#  -*- coding: utf-8 -*-
from collections import namedtuple

import fast_tracker.core.trace_node

from fast_tracker.core.node_mixin import GenericNodeMixin
from fast_tracker.core.metric import TimeMetric

_LoopNode = namedtuple('_LoopNode',
                       ['fetch_name', 'start_time', 'end_time', 'duration', 'guid'])


class LoopNode(_LoopNode, GenericNodeMixin):

    @property
    def exclusive(self):
        return self.duration

    @property
    def agent_attributes(self):
        return {}

    @property
    def children(self):
        return ()

    @property
    def name(self):
        return self.fetch_name()

    def trace_node(self, stats, root, connections):
        name = 'EventLoop/Wait/%s' % self.name
        name = root.string_table.cache(name)
        start_time = fast_tracker.core.trace_node.node_start_time(root, self)
        end_time = fast_tracker.core.trace_node.node_end_time(root, self)
        root.trace_node_count += 1
        children = []
        params = {
            'exclusive_duration_millis': 1000.0 * self.duration,
        }
        return fast_tracker.core.trace_node.TraceNode(start_time=start_time,end_time=end_time, name=name,
                                                      params=params, children=children, label=None)

    def span_event(self, *args, **kwargs):
        i_attrs, a_attrs = super(LoopNode, self).span_event(*args, **kwargs)
        i_attrs['o'] = 'EventLoop/Wait/%s' % self.name
        return i_attrs, a_attrs
