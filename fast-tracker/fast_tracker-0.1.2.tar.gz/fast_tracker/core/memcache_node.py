#  -*- coding: utf-8 -*-
from collections import namedtuple

import fast_tracker.core.trace_node

from fast_tracker.core.node_mixin import GenericNodeMixin, SpanLayerAtrr
from fast_tracker.core.metric import TimeMetric

_MemcacheNode = namedtuple('_MemcacheNode',
        ['command', 'children', 'start_time', 'end_time', 'duration',
        'exclusive', 'is_async', 'guid', 'agent_attributes', 'user_attributes'])


class MemcacheNode(_MemcacheNode, GenericNodeMixin):

    @property
    def name(self):
        return 'Memcache/%s' % self.command

    def trace_node(self, stats, root, connections):
        name = root.string_table.cache(self.name)

        start_time = fast_tracker.core.trace_node.node_start_time(root, self)
        end_time = fast_tracker.core.trace_node.node_end_time(root, self)

        children = []

        root.trace_node_count += 1

        # Agent attributes
        params = self.get_trace_segment_params(root.settings)

        return fast_tracker.core.trace_node.TraceNode(start_time=start_time, end_time=end_time, name=name,
                                                      params=params, children=children, label=None)

    def span_event(self, *args, **kwargs):
        i_attrs, a_attrs = super(MemcacheNode, self).span_event(*args, **kwargs)
        i_attrs['y'] = SpanLayerAtrr.CACHE.value
        return i_attrs, a_attrs
