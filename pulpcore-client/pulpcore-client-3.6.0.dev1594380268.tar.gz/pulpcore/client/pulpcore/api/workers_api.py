# coding: utf-8

"""
    Pulp 3 API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pulpcore.client.pulpcore.api_client import ApiClient
from pulpcore.client.pulpcore.exceptions import (
    ApiTypeError,
    ApiValueError
)


class WorkersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list(self, **kwargs):  # noqa: E501
        """List workers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str ordering: Which field to use when ordering the results.
        :param str name:
        :param str name__in: Filter results where name is in a comma-separated list of values
        :param str last_heartbeat__lt: Filter results where last_heartbeat is less than value
        :param str last_heartbeat__lte: Filter results where last_heartbeat is less than or equal to value
        :param str last_heartbeat__gt: Filter results where last_heartbeat is greater than value
        :param str last_heartbeat__gte: Filter results where last_heartbeat is greater than or equal to value
        :param str last_heartbeat__range: Filter results where last_heartbeat is between two comma separated values
        :param str last_heartbeat: ISO 8601 formatted dates are supported
        :param str online:
        :param str missing:
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :param str fields: A list of fields to include in the response.
        :param str exclude_fields: A list of fields to exclude from the response.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_with_http_info(**kwargs)  # noqa: E501

    def list_with_http_info(self, **kwargs):  # noqa: E501
        """List workers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str ordering: Which field to use when ordering the results.
        :param str name:
        :param str name__in: Filter results where name is in a comma-separated list of values
        :param str last_heartbeat__lt: Filter results where last_heartbeat is less than value
        :param str last_heartbeat__lte: Filter results where last_heartbeat is less than or equal to value
        :param str last_heartbeat__gt: Filter results where last_heartbeat is greater than value
        :param str last_heartbeat__gte: Filter results where last_heartbeat is greater than or equal to value
        :param str last_heartbeat__range: Filter results where last_heartbeat is between two comma separated values
        :param str last_heartbeat: ISO 8601 formatted dates are supported
        :param str online:
        :param str missing:
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :param str fields: A list of fields to include in the response.
        :param str exclude_fields: A list of fields to exclude from the response.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse2009, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['ordering', 'name', 'name__in', 'last_heartbeat__lt', 'last_heartbeat__lte', 'last_heartbeat__gt', 'last_heartbeat__gte', 'last_heartbeat__range', 'last_heartbeat', 'online', 'missing', 'limit', 'offset', 'fields', 'exclude_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ordering' in local_var_params and local_var_params['ordering'] is not None:  # noqa: E501
            query_params.append(('ordering', local_var_params['ordering']))  # noqa: E501
        if 'name' in local_var_params and local_var_params['name'] is not None:  # noqa: E501
            query_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'name__in' in local_var_params and local_var_params['name__in'] is not None:  # noqa: E501
            query_params.append(('name__in', local_var_params['name__in']))  # noqa: E501
        if 'last_heartbeat__lt' in local_var_params and local_var_params['last_heartbeat__lt'] is not None:  # noqa: E501
            query_params.append(('last_heartbeat__lt', local_var_params['last_heartbeat__lt']))  # noqa: E501
        if 'last_heartbeat__lte' in local_var_params and local_var_params['last_heartbeat__lte'] is not None:  # noqa: E501
            query_params.append(('last_heartbeat__lte', local_var_params['last_heartbeat__lte']))  # noqa: E501
        if 'last_heartbeat__gt' in local_var_params and local_var_params['last_heartbeat__gt'] is not None:  # noqa: E501
            query_params.append(('last_heartbeat__gt', local_var_params['last_heartbeat__gt']))  # noqa: E501
        if 'last_heartbeat__gte' in local_var_params and local_var_params['last_heartbeat__gte'] is not None:  # noqa: E501
            query_params.append(('last_heartbeat__gte', local_var_params['last_heartbeat__gte']))  # noqa: E501
        if 'last_heartbeat__range' in local_var_params and local_var_params['last_heartbeat__range'] is not None:  # noqa: E501
            query_params.append(('last_heartbeat__range', local_var_params['last_heartbeat__range']))  # noqa: E501
        if 'last_heartbeat' in local_var_params and local_var_params['last_heartbeat'] is not None:  # noqa: E501
            query_params.append(('last_heartbeat', local_var_params['last_heartbeat']))  # noqa: E501
        if 'online' in local_var_params and local_var_params['online'] is not None:  # noqa: E501
            query_params.append(('online', local_var_params['online']))  # noqa: E501
        if 'missing' in local_var_params and local_var_params['missing'] is not None:  # noqa: E501
            query_params.append(('missing', local_var_params['missing']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
        if 'exclude_fields' in local_var_params and local_var_params['exclude_fields'] is not None:  # noqa: E501
            query_params.append(('exclude_fields', local_var_params['exclude_fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic']  # noqa: E501

        return self.api_client.call_api(
            '/pulp/api/v3/workers/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2009',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read(self, worker_href, **kwargs):  # noqa: E501
        """Inspect a worker  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read(worker_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str worker_href: URI of Worker. e.g.: /pulp/api/v3/workers/1/ (required)
        :param str fields: A list of fields to include in the response.
        :param str exclude_fields: A list of fields to exclude from the response.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Worker
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.read_with_http_info(worker_href, **kwargs)  # noqa: E501

    def read_with_http_info(self, worker_href, **kwargs):  # noqa: E501
        """Inspect a worker  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_with_http_info(worker_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str worker_href: URI of Worker. e.g.: /pulp/api/v3/workers/1/ (required)
        :param str fields: A list of fields to include in the response.
        :param str exclude_fields: A list of fields to exclude from the response.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Worker, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['worker_href', 'fields', 'exclude_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'worker_href' is set
        if self.api_client.client_side_validation and ('worker_href' not in local_var_params or  # noqa: E501
                                                        local_var_params['worker_href'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `worker_href` when calling `read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'worker_href' in local_var_params:
            path_params['worker_href'] = local_var_params['worker_href']  # noqa: E501

        query_params = []
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
        if 'exclude_fields' in local_var_params and local_var_params['exclude_fields'] is not None:  # noqa: E501
            query_params.append(('exclude_fields', local_var_params['exclude_fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic']  # noqa: E501

        return self.api_client.call_api(
            '{worker_href}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Worker',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
