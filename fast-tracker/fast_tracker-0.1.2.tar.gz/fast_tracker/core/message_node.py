# -*- coding: utf-8 -*-
from collections import namedtuple

import fast_tracker.core.trace_node

from fast_tracker.core.node_mixin import GenericNodeMixin, SpanLayerAtrr
from fast_tracker.core.metric import TimeMetric

_MessageNode = namedtuple('_MessageNode',
                          ['library', 'operation', 'children', 'start_time',
                           'end_time', 'duration', 'exclusive', 'destination_name',
                           'destination_type', 'params', 'is_async', 'guid',
                           'agent_attributes', 'user_attributes'])


class MessageNode(_MessageNode, GenericNodeMixin):

    @property
    def name(self):
        name = 'MessageBroker/%s/%s/%s/Named/%s' % (self.library,
                                                    self.destination_type, self.operation, self.destination_name)
        return name

    def trace_node(self, stats, root, connections):
        name = root.string_table.cache(self.name)
        start_time = fast_tracker.core.trace_node.node_start_time(root, self)
        end_time = fast_tracker.core.trace_node.node_end_time(root, self)
        children = []
        root.trace_node_count += 1
        params = self.get_trace_segment_params(
            root.settings, params=self.params)
        return fast_tracker.core.trace_node.TraceNode(start_time=start_time, end_time=end_time, name=name,
                                                      params=params, children=children, label=None)
    
    def span_event(self, *args, **kwargs):
        i_attrs, a_attrs = super(MessageNode, self).span_event(*args, **kwargs)
        i_attrs['y'] = SpanLayerAtrr.MQ.value
        return i_attrs, a_attrs
