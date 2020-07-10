# coding: utf-8

"""
    Agilicus API

    Agilicus API endpoints  # noqa: E501

    The version of the OpenAPI document: 2020.07.09
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from agilicus_api.api_client import ApiClient
from agilicus_api.exceptions import (
    ApiTypeError,
    ApiValueError
)


class AuditsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_audits(self, **kwargs):  # noqa: E501
        """View audit records  # noqa: E501

        View audit records for any API  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_audits(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: limit the number of rows in the response
        :param str user_id: Query based on user id
        :param str dt_from: Search criteria from when the query happened. * Inclusive. * In UTC. * Supports human-friendly values such as \"now\", \"today\", \"now-1day\". 
        :param str dt_to: Search criteria until when the query happened. * Exclusive. * In UTC. * Supports human-friendly values such as \"now\", \"today\", \"now-1day\". 
        :param str action: the type of action which caused the log
        :param str target_id: The identifier for the target of the log (e.g. the jti of a created token). 
        :param str token_id: The id of the bearer token for which to find records.
        :param str api_name: The name of the API which generated the audit logs
        :param str target_resource_type: Filters the type of resource associated with the audit records.
        :param str org_id: Organisation Unique identifier
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ListAuditsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_audits_with_http_info(**kwargs)  # noqa: E501

    def list_audits_with_http_info(self, **kwargs):  # noqa: E501
        """View audit records  # noqa: E501

        View audit records for any API  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_audits_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: limit the number of rows in the response
        :param str user_id: Query based on user id
        :param str dt_from: Search criteria from when the query happened. * Inclusive. * In UTC. * Supports human-friendly values such as \"now\", \"today\", \"now-1day\". 
        :param str dt_to: Search criteria until when the query happened. * Exclusive. * In UTC. * Supports human-friendly values such as \"now\", \"today\", \"now-1day\". 
        :param str action: the type of action which caused the log
        :param str target_id: The identifier for the target of the log (e.g. the jti of a created token). 
        :param str token_id: The id of the bearer token for which to find records.
        :param str api_name: The name of the API which generated the audit logs
        :param str target_resource_type: Filters the type of resource associated with the audit records.
        :param str org_id: Organisation Unique identifier
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ListAuditsResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['limit', 'user_id', 'dt_from', 'dt_to', 'action', 'target_id', 'token_id', 'api_name', 'target_resource_type', 'org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_audits" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 500:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_audits`, must be a value less than or equal to `500`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_audits`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'user_id' in local_var_params and local_var_params['user_id'] is not None:  # noqa: E501
            query_params.append(('user_id', local_var_params['user_id']))  # noqa: E501
        if 'dt_from' in local_var_params and local_var_params['dt_from'] is not None:  # noqa: E501
            query_params.append(('dt_from', local_var_params['dt_from']))  # noqa: E501
        if 'dt_to' in local_var_params and local_var_params['dt_to'] is not None:  # noqa: E501
            query_params.append(('dt_to', local_var_params['dt_to']))  # noqa: E501
        if 'action' in local_var_params and local_var_params['action'] is not None:  # noqa: E501
            query_params.append(('action', local_var_params['action']))  # noqa: E501
        if 'target_id' in local_var_params and local_var_params['target_id'] is not None:  # noqa: E501
            query_params.append(('target_id', local_var_params['target_id']))  # noqa: E501
        if 'token_id' in local_var_params and local_var_params['token_id'] is not None:  # noqa: E501
            query_params.append(('token_id', local_var_params['token_id']))  # noqa: E501
        if 'api_name' in local_var_params and local_var_params['api_name'] is not None:  # noqa: E501
            query_params.append(('api_name', local_var_params['api_name']))  # noqa: E501
        if 'target_resource_type' in local_var_params and local_var_params['target_resource_type'] is not None:  # noqa: E501
            query_params.append(('target_resource_type', local_var_params['target_resource_type']))  # noqa: E501
        if 'org_id' in local_var_params and local_var_params['org_id'] is not None:  # noqa: E501
            query_params.append(('org_id', local_var_params['org_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['token-valid']  # noqa: E501

        return self.api_client.call_api(
            '/v1/audits', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListAuditsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_auth_records(self, **kwargs):  # noqa: E501
        """View authentication audit records  # noqa: E501

        View and search authentication audit records for different users and organisations in the system.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_auth_records(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: limit the number of rows in the response
        :param str user_id: Query based on user id
        :param str dt_from: Search criteria from when the query happened. * Inclusive. * In UTC. * Supports human-friendly values such as \"now\", \"today\", \"now-1day\". 
        :param str dt_to: Search criteria until when the query happened. * Exclusive. * In UTC. * Supports human-friendly values such as \"now\", \"today\", \"now-1day\". 
        :param str org_id: Organisation Unique identifier
        :param str session_id: The session formed when the user started to log in.
        :param str trace_id: The id representing the request that triggered the event
        :param str upstream_user_id: The id of the user from upstream
        :param str upstream_idp: The name of the upstream idp
        :param str login_org_id: The org id the user tried to log in to
        :param str source_ip: The source IP address of the client device logging in.
        :param str client_id: The oidc client id used to log in
        :param str event: The event which triggered the audit record
        :param str stage: The stage of a pipeline to query for
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ListAuthAuditsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_auth_records_with_http_info(**kwargs)  # noqa: E501

    def list_auth_records_with_http_info(self, **kwargs):  # noqa: E501
        """View authentication audit records  # noqa: E501

        View and search authentication audit records for different users and organisations in the system.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_auth_records_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: limit the number of rows in the response
        :param str user_id: Query based on user id
        :param str dt_from: Search criteria from when the query happened. * Inclusive. * In UTC. * Supports human-friendly values such as \"now\", \"today\", \"now-1day\". 
        :param str dt_to: Search criteria until when the query happened. * Exclusive. * In UTC. * Supports human-friendly values such as \"now\", \"today\", \"now-1day\". 
        :param str org_id: Organisation Unique identifier
        :param str session_id: The session formed when the user started to log in.
        :param str trace_id: The id representing the request that triggered the event
        :param str upstream_user_id: The id of the user from upstream
        :param str upstream_idp: The name of the upstream idp
        :param str login_org_id: The org id the user tried to log in to
        :param str source_ip: The source IP address of the client device logging in.
        :param str client_id: The oidc client id used to log in
        :param str event: The event which triggered the audit record
        :param str stage: The stage of a pipeline to query for
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ListAuthAuditsResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['limit', 'user_id', 'dt_from', 'dt_to', 'org_id', 'session_id', 'trace_id', 'upstream_user_id', 'upstream_idp', 'login_org_id', 'source_ip', 'client_id', 'event', 'stage']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_auth_records" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 500:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_auth_records`, must be a value less than or equal to `500`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_auth_records`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'user_id' in local_var_params and local_var_params['user_id'] is not None:  # noqa: E501
            query_params.append(('user_id', local_var_params['user_id']))  # noqa: E501
        if 'dt_from' in local_var_params and local_var_params['dt_from'] is not None:  # noqa: E501
            query_params.append(('dt_from', local_var_params['dt_from']))  # noqa: E501
        if 'dt_to' in local_var_params and local_var_params['dt_to'] is not None:  # noqa: E501
            query_params.append(('dt_to', local_var_params['dt_to']))  # noqa: E501
        if 'org_id' in local_var_params and local_var_params['org_id'] is not None:  # noqa: E501
            query_params.append(('org_id', local_var_params['org_id']))  # noqa: E501
        if 'session_id' in local_var_params and local_var_params['session_id'] is not None:  # noqa: E501
            query_params.append(('session_id', local_var_params['session_id']))  # noqa: E501
        if 'trace_id' in local_var_params and local_var_params['trace_id'] is not None:  # noqa: E501
            query_params.append(('trace_id', local_var_params['trace_id']))  # noqa: E501
        if 'upstream_user_id' in local_var_params and local_var_params['upstream_user_id'] is not None:  # noqa: E501
            query_params.append(('upstream_user_id', local_var_params['upstream_user_id']))  # noqa: E501
        if 'upstream_idp' in local_var_params and local_var_params['upstream_idp'] is not None:  # noqa: E501
            query_params.append(('upstream_idp', local_var_params['upstream_idp']))  # noqa: E501
        if 'login_org_id' in local_var_params and local_var_params['login_org_id'] is not None:  # noqa: E501
            query_params.append(('login_org_id', local_var_params['login_org_id']))  # noqa: E501
        if 'source_ip' in local_var_params and local_var_params['source_ip'] is not None:  # noqa: E501
            query_params.append(('source_ip', local_var_params['source_ip']))  # noqa: E501
        if 'client_id' in local_var_params and local_var_params['client_id'] is not None:  # noqa: E501
            query_params.append(('client_id', local_var_params['client_id']))  # noqa: E501
        if 'event' in local_var_params and local_var_params['event'] is not None:  # noqa: E501
            query_params.append(('event', local_var_params['event']))  # noqa: E501
        if 'stage' in local_var_params and local_var_params['stage'] is not None:  # noqa: E501
            query_params.append(('stage', local_var_params['stage']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['token-valid']  # noqa: E501

        return self.api_client.call_api(
            '/v1/auth_audits', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListAuthAuditsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
