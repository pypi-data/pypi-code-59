# -*- coding: utf-8 -*-

from collections import namedtuple

import fast_tracker.core.trace_node

from fast_tracker.core.node_mixin import GenericNodeMixin
from fast_tracker.core.metric import TimeMetric

_SolrNode = namedtuple('_SolrNode',
                       ['library', 'command', 'children', 'start_time', 'end_time',
                        'duration', 'exclusive', 'guid', 'is_async', 'agent_attributes',
                        'user_attributes', ])


class SolrNode(_SolrNode, GenericNodeMixin):

    @property
    def name(self):
        return 'SolrClient/%s/%s' % (self.library, self.command)

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
