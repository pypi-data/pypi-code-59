# -*- coding: utf-8 -*-
from collections import namedtuple

import fast_tracker.core.trace_node

from fast_tracker.core.node_mixin import GenericNodeMixin
from fast_tracker.core.metric import TimeMetric

from fast_tracker.packages import six

_FunctionNode = namedtuple('_FunctionNode',
                           ['group', 'name', 'children', 'start_time', 'end_time',
                            'duration', 'exclusive', 'label', 'params', 'rollup',
                            'is_async', 'guid', 'agent_attributes', 'user_attributes'])


class FunctionNode(_FunctionNode, GenericNodeMixin):

    def trace_node(self, stats, root, connections):
        name = '%s/%s' % (self.group, self.name)
        name = root.string_table.cache(name)
        start_time = fast_tracker.core.trace_node.node_start_time(root, self)
        end_time = fast_tracker.core.trace_node.node_end_time(root, self)
        root.trace_node_count += 1
        children = []

        for child in self.children:
            if root.trace_node_count > root.trace_node_limit:
                break
            children.append(child.trace_node(stats, root, connections))
        params = self.get_trace_segment_params(
            root.settings, params=self.params)
        return fast_tracker.core.trace_node.TraceNode(start_time=start_time, end_time=end_time, name=name,
                                                      params=params, children=children, label=self.label)

    def span_event(self, *args, **kwargs):
        i_attrs, a_attrs = super(FunctionNode, self).span_event(*args, **kwargs)
        i_attrs['o'] = '%s/%s' % (self.group, self.name)
        i_attrs['i_f'] = True  # 是不是函数，暂时用不上函数级别跟踪
        return i_attrs, a_attrs
