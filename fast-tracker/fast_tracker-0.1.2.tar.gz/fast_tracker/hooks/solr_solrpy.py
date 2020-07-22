# -*- coding: utf-8 -*-

import fast_tracker.api.solr_trace

def instrument(module):

    if hasattr(module.Solr, 'delete'):
        fast_tracker.api.solr_trace.wrap_solr_trace(
                module, 'Solr.delete', 'solrpy', 'delete')
    if hasattr(module.Solr, 'delete_many'):
        fast_tracker.api.solr_trace.wrap_solr_trace(
                module, 'Solr.delete_many', 'solrpy', 'delete')
    if hasattr(module.Solr, 'delete_query'):
        fast_tracker.api.solr_trace.wrap_solr_trace(
                module, 'Solr.delete_query', 'solrpy', 'delete')
    if hasattr(module.Solr, 'add'):
        fast_tracker.api.solr_trace.wrap_solr_trace(
                module, 'Solr.add', 'solrpy', 'add')
    if hasattr(module.Solr, 'add_many'):
        fast_tracker.api.solr_trace.wrap_solr_trace(
                module, 'Solr.add_many', 'solrpy', 'add')
    if hasattr(module.Solr, 'commit'):
        fast_tracker.api.solr_trace.wrap_solr_trace(
                module, 'Solr.commit', 'solrpy', 'commit')
    if hasattr(module.Solr, 'optimize'):
        fast_tracker.api.solr_trace.wrap_solr_trace(
                module, 'Solr.optimize', 'solrpy', 'optimize')

    if hasattr(module.SolrConnection, 'query'):
        fast_tracker.api.solr_trace.wrap_solr_trace(
                module, 'SolrConnection.query', 'solrpy', 'query')
    if hasattr(module.SolrConnection, 'raw_query'):
        fast_tracker.api.solr_trace.wrap_solr_trace(
                module, 'SolrConnection.raw_query', 'solrpy', 'query')

    if hasattr(module, 'SearchHandler'):
        fast_tracker.api.solr_trace.wrap_solr_trace(
                module, 'SearchHandler.__call__', 'solrpy', 'query')
