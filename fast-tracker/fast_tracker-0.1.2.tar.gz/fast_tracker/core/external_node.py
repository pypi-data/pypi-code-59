# -*- coding: utf-8 -*-
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse

from collections import namedtuple

import fast_tracker.core.attribute as attribute
import fast_tracker.core.trace_node

from fast_tracker.core.node_mixin import GenericNodeMixin, SpanLayerAtrr, SpanType
from fast_tracker.core.metric import TimeMetric


_ExternalNode = namedtuple('_ExternalNode',
                           ['library', 'url', 'method', 'children', 'start_time', 'end_time',
                            'duration', 'exclusive', 'params', 'is_async', 'guid',
                            'agent_attributes', 'user_attributes'])


class ExternalNode(_ExternalNode, GenericNodeMixin):

    @property
    def details(self):
        if hasattr(self, '_details'):
            return self._details

        try:
            self._details = urlparse.urlparse(self.url or '')
        except Exception:
            self._details = urlparse.urlparse('http://unknown.url')

        return self._details

    @property
    def name(self):
        return 'External/%s/%s/%s' % (
            self.netloc, self.library, self.method or '')

    @property
    def url_with_path(self):
        details = self.details
        url = urlparse.urlunsplit((details.scheme, details.netloc,
                                   details.path, '', ''))
        return url

    @property
    def http_url(self):
        if hasattr(self, '_http_url'):
            return self._http_url

        _, url_attr = attribute.process_user_attribute(
            'http_url', self.url_with_path)
        self._http_url = url_attr
        return url_attr

    @property
    def netloc(self):
        hostname = self.details.hostname or 'unknown'

        try:
            scheme = self.details.scheme.lower()
            port = self.details.port
        except Exception:
            scheme = None
            port = None

        if (scheme, port) in (('http', 80), ('https', 443)):
            port = None

        netloc = port and ('%s:%s' % (hostname, port)) or hostname
        return netloc

    def trace_node(self, stats, root, connections):

        netloc = self.netloc

        method = self.method or ''

        if self.cross_process_id is None:
            name = 'External/%s/%s/%s' % (netloc, self.library, method)
        else:
            name = 'ExternalTransaction/%s/%s/%s' % (netloc, self.cross_process_id, self.external_txn_name)
        name = root.string_table.cache(name)
        start_time = fast_tracker.core.trace_node.node_start_time(root, self)
        end_time = fast_tracker.core.trace_node.node_end_time(root, self)
        children = []
        root.trace_node_count += 1
        self.agent_attributes['url'] = self.http_url
        params = self.get_trace_segment_params(root.settings, params=self.params)
        return fast_tracker.core.trace_node.TraceNode(start_time=start_time,  end_time=end_time, name=name,
                                                      params=params, children=children, label=None)

    def span_event(self, *args, **kwargs):
        i_attrs, a_attrs = super(ExternalNode, self).span_event(*args, **kwargs)
        i_attrs['t'] = SpanType.Exit.value
        i_attrs['y'] = SpanLayerAtrr.HTTP.value
        _, i_attrs['c'] = attribute.process_user_attribute('component', self.library)
        i_attrs['c'] = i_attrs['c'].title()
        
        if self.method:
            _, a_attrs['http_method'] = attribute.process_user_attribute(
                'http_method', self.method)
        a_attrs['url'] = self.http_url
        a_attrs['path'] = self.details.path
        return i_attrs, a_attrs
