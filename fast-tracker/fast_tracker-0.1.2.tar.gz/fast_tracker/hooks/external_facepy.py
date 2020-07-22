# -*- coding: utf-8 -*-

import fast_tracker.api.external_trace


def instrument(module):

    def url_query(graph_obj, method, path, *args, **kwargs):
        return '/'.join([graph_obj.url, path])

    fast_tracker.api.external_trace.wrap_external_trace(
            module, 'GraphAPI._query', 'facepy', url_query)