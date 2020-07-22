# -*- coding: utf-8 -*-
"""
事物数据结构，事物是这个系统最终于的概念，每个Web 应用的Request请求或者非Web应用，都称为事物
"""


from collections import namedtuple
import random

import fast_tracker.core.error_collector
import fast_tracker.core.trace_node

from fast_tracker.core.metric import  TimeMetric
from fast_tracker.core.string_table import StringTable
from fast_tracker.core.attribute import (create_user_attributes,
                                     resolve_user_attributes, process_user_attribute)
from fast_tracker.core.attribute_filter import (DST_ERROR_COLLECTOR,
                                            DST_TRANSACTION_TRACER, DST_TRANSACTION_EVENTS, DST_SPAN_EVENTS)
from fast_tracker.core.node_mixin import SpanLayerAtrr, SpanType


_TransactionNode = namedtuple('_TransactionNode',
                              ['settings', 'path', 'type', 'group', 'base_name', 'name_for_metric',
                               'port', 'request_uri', 'queue_start', 'start_time',
                               'end_time', 'last_byte_time', 'response_time', 'total_time',
                               'duration', 'exclusive', 'root', 'errors', 'slow_sql',
                               'custom_events', 'suppress_apdex', 'custom_metrics', 'guid',
                               'cpu_time', 'suppress_transaction_trace', 'client_cross_process_id',
                               'referring_transaction_guid', 'record_tt', 'synthetics_resource_id',
                               'synthetics_job_id', 'synthetics_monitor_id', 'synthetics_header',
                               'is_part_of_cat', 'trip_id', 'path_hash', 'referring_path_hash',
                               'alternate_path_hashes', 'trace_intrinsics', 'agent_attributes',
                               'distributed_trace_intrinsics', 'user_attributes', 'priority',
                               'sampled', 'parent_transport_duration', 'parent_span', 'parent_type',
                               'parent_account', 'parent_app', 'parent_tx', 'parent_transport_type',
                               'root_span_guid', 'trace_id', 'loop_time', ])


class TransactionNode(_TransactionNode):
    """持有与交易根相对应的数据的类。 所有为交易记录的感兴趣的节点被保留为一棵树“children”属性中的结构。
    """

    def __new__(cls, *args, **kwargs):
        node = _TransactionNode.__new__(cls, *args, **kwargs)
        node.include_transaction_trace_request_uri = False
        return node

    def __hash__(self):
        return id(self)

    @property
    def string_table(self):
        result = getattr(self, '_string_table', None)
        if result is not None:
            return result
        self._string_table = StringTable()
        return self._string_table

    @property
    def name(self):
        return self.name_for_metric

    def error_details(self):

        if not self.errors:
            return

        for error in self.errors:
            params = {}
            params["stack_trace"] = error.stack_trace

            intrinsics = {'spanId': error.span_id}
            intrinsics.update(self.trace_intrinsics)
            params['intrinsics'] = intrinsics

            params['agentAttributes'] = {}
            for attr in self.agent_attributes:
                if attr.destinations & DST_ERROR_COLLECTOR:
                    params['agentAttributes'][attr.name] = attr.value

            params['userAttributes'] = {}
            for attr in self.user_attributes:
                if attr.destinations & DST_ERROR_COLLECTOR:
                    params['userAttributes'][attr.name] = attr.value

            err_attrs = create_user_attributes(error.custom_params,
                                               self.settings.attribute_filter)
            for attr in err_attrs:
                if attr.destinations & DST_ERROR_COLLECTOR:
                    params['userAttributes'][attr.name] = attr.value

            yield fast_tracker.core.error_collector.TracedError(
                start_time=error.timestamp,
                path=self.path,
                message=error.message,
                type=error.type,
                parameters=params)

    def transaction_trace(self, stats, limit, connections):

        self.trace_node_count = 0
        self.trace_node_limit = limit

        start_time = fast_tracker.core.trace_node.root_start_time(self)

        trace_node = self.root.trace_node(stats, self, connections)

        attributes = {}

        attributes['intrinsics'] = self.trace_intrinsics

        attributes['agentAttributes'] = {}
        for attr in self.agent_attributes:
            if attr.destinations & DST_TRANSACTION_TRACER:
                attributes['agentAttributes'][attr.name] = attr.value
                if attr.name == 'request.uri':
                    self.include_transaction_trace_request_uri = True

        attributes['userAttributes'] = {}
        for attr in self.user_attributes:
            if attr.destinations & DST_TRANSACTION_TRACER:
                attributes['userAttributes'][attr.name] = attr.value

        root = fast_tracker.core.trace_node.TraceNode(
            start_time=trace_node.start_time,
            end_time=trace_node.end_time,
            name='ROOT',
            params={},
            children=[trace_node],
            label=None)

        return fast_tracker.core.trace_node.RootNode(
            start_time=start_time,
            empty0={},
            empty1={},
            root=root,
            attributes=attributes)

    def slow_sql_nodes(self, stats):
        for item in self.slow_sql:
            yield item.slow_sql_node(stats, self)

    def transaction_event(self, stats_table):
        intrinsics = self.transaction_event_intrinsics(stats_table)

        user_attributes = {}
        for attr in self.user_attributes:
            if attr.destinations & DST_TRANSACTION_EVENTS:
                user_attributes[attr.name] = attr.value

        agent_attributes = {}
        for attr in self.agent_attributes:
            if attr.destinations & DST_TRANSACTION_EVENTS:
                agent_attributes[attr.name] = attr.value

        transaction_event = [intrinsics, user_attributes, agent_attributes]
        return transaction_event

    def transaction_event_intrinsics(self, stats_table):

        intrinsics = self._event_intrinsics(stats_table)

        intrinsics['type'] = 'Transaction'
        intrinsics['name'] = self.path
        intrinsics['totalTime'] = self.total_time

        def _add_if_not_empty(key, value):
            if value:
                intrinsics[key] = value

        if self.errors:
            intrinsics['error'] = True

        if self.path_hash:
            intrinsics['nr.guid'] = self.guid
            intrinsics['nr.tripId'] = self.trip_id
            intrinsics['nr.pathHash'] = self.path_hash

            _add_if_not_empty('nr.referringPathHash',
                              self.referring_path_hash)
            _add_if_not_empty('nr.alternatePathHashes',
                              ','.join(self.alternate_path_hashes))
            _add_if_not_empty('nr.referringTransactionGuid',
                              self.referring_transaction_guid)

        if self.synthetics_resource_id:
            intrinsics['nr.guid'] = self.guid

        if self.parent_tx:
            intrinsics['parentId'] = self.parent_tx

        if self.parent_span:
            intrinsics['parentSpanId'] = self.parent_span

        return intrinsics

    def error_events(self, stats_table):
        # TODO 暂时用不上
        errors = []
        for error in self.errors:

            intrinsics = self.error_event_intrinsics(error, stats_table)            
            agent_attributes = {}
            for attr in self.agent_attributes:
                if attr.destinations & DST_ERROR_COLLECTOR:
                    agent_attributes[attr.name] = attr.value

            user_attributes = {}
            for attr in self.user_attributes:
                if attr.destinations & DST_ERROR_COLLECTOR:
                    user_attributes[attr.name] = attr.value
           
            err_attrs = create_user_attributes(error.custom_params,
                                               self.settings.attribute_filter)
            for attr in err_attrs:
                if attr.destinations & DST_ERROR_COLLECTOR:
                    user_attributes[attr.name] = attr.value

            error_event = [intrinsics, user_attributes, agent_attributes]
            errors.append(error_event)

        return errors

    def error_event_intrinsics(self, error, stats_table):

        intrinsics = self._event_intrinsics(stats_table)

        intrinsics['type'] = "TransactionError"
        intrinsics['error.class'] = error.type
        intrinsics['error.message'] = error.message
        intrinsics['transactionName'] = self.path
        intrinsics['spanId'] = error.span_id

        intrinsics['nr.transactionGuid'] = self.guid
        if self.referring_transaction_guid:
            guid = self.referring_transaction_guid
            intrinsics['nr.referringTransactionGuid'] = guid

        return intrinsics

    def _event_intrinsics(self, stats_table):

        cache = getattr(self, '_event_intrinsics_cache', None)
        if cache is not None:
            return self._event_intrinsics_cache.copy()

        intrinsics = self.distributed_trace_intrinsics.copy()

        intrinsics['timestamp'] = int(1000.0 * self.start_time)
        intrinsics['duration'] = self.response_time

        if self.port:
            intrinsics['port'] = self.port
        def _add_call_time(source, target):
            if (source, '') in stats_table:
                call_time = stats_table[(source, '')].total_call_time
                if target in intrinsics:
                    intrinsics[target] += call_time
                else:
                    intrinsics[target] = call_time

        def _add_call_count(source, target):

            if (source, '') in stats_table:
                call_count = stats_table[(source, '')].call_count
                if target in intrinsics:
                    intrinsics[target] += call_count
                else:
                    intrinsics[target] = call_count

        _add_call_time('WebFrontend/QueueTime', 'queueDuration')

        _add_call_time('External/all', 'externalDuration')
        _add_call_time('Datastore/all', 'databaseDuration')
        _add_call_time('Memcache/all', 'memcacheDuration')

        _add_call_count('External/all', 'externalCallCount')
        _add_call_count('Datastore/all', 'databaseCallCount')

        if self.loop_time:
            intrinsics['eventLoopTime'] = self.loop_time
        _add_call_time('EventLoop/Wait/all', 'eventLoopWait')

        self._event_intrinsics_cache = intrinsics.copy()

        return intrinsics
    
    def error_trace(self):
        """
        错误的链路
        :return: 
        """
        if not self.errors:
            return None
        return [{'Timestamp': int(error.timestamp * 1000), 
                 'Data': {'event': 'error', 'error_kind': error.type, 
                          'message': error.message, 'stack': '\r\n '.join(error.stack_trace)}}
                for error in self.errors]
    
    def custom_details(self, root):
        """
        
        :param dict root: 
        :return: 
        """
        if not self.custom_events:
            return []
        pq = self.custom_events.pq
        if not pq:
            return []
        for event in pq:
            if event[-1] is None:
                continue
            intrinsics, attributes = event[-1]
            operation_name = ''
            span_type = root['t']
            span_layer = root['y']
            if 'operation_name' in attributes:
                operation_name = attributes.pop('operation_name')
            if 'span_type' in attributes:
                span_type = attributes.pop('span_type')
            if 'span_layer' in attributes:
                span_layer = attributes.pop('span_layer')
                
            
            yield {'id': self.trace_id, 
                   'c': intrinsics['type'], 
                   'ts':intrinsics['timestamp'],
                   'te': intrinsics['timestamp'],
                   'd':1,
                   'p': self.guid,
                   's': ('%032x' % random.getrandbits(128))[:16],
                   'er': 'False',
                   'o': operation_name or intrinsics['type'],
                   't': span_type,
                   'y': span_layer,
                   'g': attributes
                   }
            
        

    def span_events(self, settings):
        base_attrs = {
            'id': self.trace_id,
        }
        agent_attributes = {}
        for attr in self.agent_attributes:
            if attr.name in ('response.status', 'request.method', 'request.headers.host'):
                agent_attributes[attr.name] = attr.value
        
        entry_status_code = agent_attributes.get('response.status', '200')
        entry = {
            'id': self.trace_id,
            't': SpanType.Entry.value,
            's': self.guid , # span_id
            'd': int(self.duration * 1000),
            'ts':int(self.start_time * 1000),
            'te': int(self.end_time * 1000),
            'y': SpanLayerAtrr.HTTP.value,
            'c': self.base_name.split('.')[0].title() if self.base_name and isinstance(self.base_name, str) else 'Python',
            'o': self.request_uri,
            'er': 'False' if entry_status_code == '200' else 'True',
            'r': agent_attributes.get('request.headers.host', '').split(':')[0],
        }
        l = self.error_trace()
        custom_events = self.custom_details(entry)
        if l:
            entry['l'] = l
        entry['g'] = {'url': ''.join(['http://', agent_attributes.get('request.headers.host', ''), self.request_uri]),
                      'path': self.request_uri,
                      'http_method': agent_attributes.get('request.method', ''),
                      'status_code': entry_status_code}
    
        yield entry
        for event in self.root.span_events(
                settings,
                base_attrs,
                parent_guid=self.parent_span
        ):
            i_attr = event[0]
            a_attr = event[1]
            if not i_attr.get('i_f'):
                i_attr['g'] = a_attr
                i_attr['er'] = 'False' if a_attr.get('status_code') == '200' or entry_status_code else 'True'
                yield i_attr
        for event in custom_events:
            yield event