# -*- coding: utf-8 -*-

import fast_tracker.api.solr_trace

def instrument(module):

    if hasattr(module.Solr, 'search'):
        fast_tracker.api.solr_trace.wrap_solr_trace(
                module, 'Solr.search', 'pysolr', 'query')
    if hasattr(module.Solr, 'more_like_this'):
        fast_tracker.api.solr_trace.wrap_solr_trace(
                module, 'Solr.more_like_this', 'pysolr', 'query')
    if hasattr(module.Solr, 'suggest_terms'):
        fast_tracker.api.solr_trace.wrap_solr_trace(
                module, 'Solr.suggest_terms', 'pysolr', 'query')
    if hasattr(module.Solr, 'add'):
        fast_tracker.api.solr_trace.wrap_solr_trace(
                module, 'Solr.add', 'pysolr', 'add')
    if hasattr(module.Solr, 'delete'):
        fast_tracker.api.solr_trace.wrap_solr_trace(
                module, 'Solr.delete', 'pysolr', 'delete')
    if hasattr(module.Solr, 'commit'):
        fast_tracker.api.solr_trace.wrap_solr_trace(
                module, 'Solr.commit', 'pysolr', 'commit')
    if hasattr(module.Solr, 'optimize'):
        fast_tracker.api.solr_trace.wrap_solr_trace(
                module, 'Solr.optimize', 'pysolr', 'optimize')
