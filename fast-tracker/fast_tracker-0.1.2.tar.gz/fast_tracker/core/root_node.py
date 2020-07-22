# -*- coding: utf-8 -*-
"""
根节点
"""
from collections import namedtuple

import fast_tracker.core.trace_node
from fast_tracker.core.node_mixin import GenericNodeMixin, SpanType


_RootNode = namedtuple('_RootNode',
                       ['name', 'children', 'start_time', 'end_time', 'exclusive',
                        'duration', 'guid', 'agent_attributes', 'user_attributes',
                        'path', 'trusted_parent_span', 'tracing_vendors', ])


class RootNode(_RootNode, GenericNodeMixin):
    def span_event(self, *args, **kwargs):
        i_attrs, a_attrs = super(RootNode, self).span_event(*args, **kwargs)
        i_attrs['t'] = SpanType.Entry.value
        i_attrs['i_f'] = True # 是不是函数，暂时用不上函数级别跟踪
     
        return i_attrs, a_attrs

    def trace_node(self, stats, root, connections):
        name = self.path
        start_time = fast_tracker.core.trace_node.node_start_time(root, self)
        end_time = fast_tracker.core.trace_node.node_end_time(root, self)
        root.trace_node_count += 1
        children = []
        for child in self.children:
            if root.trace_node_count > root.trace_node_limit:
                break
            children.append(child.trace_node(stats, root, connections))
        params = self.get_trace_segment_params(root.settings)

        return fast_tracker.core.trace_node.TraceNode(
            start_time=start_time,
            end_time=end_time,
            name=name,
            params=params,
            children=children,
            label=None)
