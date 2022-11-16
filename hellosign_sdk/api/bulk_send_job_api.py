"""
    Dropbox Sign API

    Dropbox Sign v3 API  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Contact: apisupport@hellosign.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401
from metadict import MetaDict

from hellosign_sdk.api_client import ApiClient, ApiException, Endpoint as _Endpoint
from hellosign_sdk.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from hellosign_sdk.model.bulk_send_job_get_response import BulkSendJobGetResponse
from hellosign_sdk.model.bulk_send_job_list_response import BulkSendJobListResponse
from hellosign_sdk.model.error_response import ErrorResponse


class BulkSendJobApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.bulk_send_job_get_endpoint = _Endpoint(
            settings={
                'response_type': (BulkSendJobGetResponse,),
                'auth': [
                    'api_key',
                    'oauth2'
                ],
                'endpoint_path': '/bulk_send_job/{bulk_send_job_id}',
                'operation_id': 'bulk_send_job_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'bulk_send_job_id',
                ],
                'required': [
                    'bulk_send_job_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'bulk_send_job_id':
                        (str,),
                },
                'attribute_map': {
                    'bulk_send_job_id': 'bulk_send_job_id',
                },
                'location_map': {
                    'bulk_send_job_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.bulk_send_job_list_endpoint = _Endpoint(
            settings={
                'response_type': (BulkSendJobListResponse,),
                'auth': [
                    'api_key',
                    'oauth2'
                ],
                'endpoint_path': '/bulk_send_job/list',
                'operation_id': 'bulk_send_job_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'page_size',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'page_size':
                        (int,),
                },
                'attribute_map': {
                    'page': 'page',
                    'page_size': 'page_size',
                },
                'location_map': {
                    'page': 'query',
                    'page_size': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def bulk_send_job_get(
        self,
        bulk_send_job_id,
        **kwargs
    ):
        """Get Bulk Send Job  # noqa: E501

        Returns the status of the BulkSendJob and its SignatureRequests specified by the `bulk_send_job_id` parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.bulk_send_job_get(bulk_send_job_id, async_req=True)
        >>> result = thread.get()

        Args:
            bulk_send_job_id (str): The id of the BulkSendJob to retrieve.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            BulkSendJobGetResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['bulk_send_job_id'] = \
            bulk_send_job_id
        try:
            return self.bulk_send_job_get_endpoint.call_with_http_info(**kwargs)
        except ApiException as e:
            if e.status == 200:
                e.body = self.api_client.deserialize(
                    response=MetaDict({'data': e.body}),
                    response_type=[BulkSendJobGetResponse],
                    _check_type=True,
                )

                raise e
            range_code = "4XX"[0]
            range_code_left = int(f"{range_code}00")
            range_code_right = int(f"{range_code}99")

            if range_code_left <= e.status <= range_code_right:
                e.body = self.api_client.deserialize(
                    response=MetaDict({'data': e.body}),
                    response_type=[ErrorResponse],
                    _check_type=True,
                )

                raise e

    def bulk_send_job_list(
        self,
        **kwargs
    ):
        """List Bulk Send Jobs  # noqa: E501

        Returns a list of BulkSendJob that you can access.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.bulk_send_job_list(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): Which page number of the BulkSendJob List to return. Defaults to `1`.. [optional] if omitted the server will use the default value of 1
            page_size (int): Number of objects to be returned per page. Must be between `1` and `100`. Default is 20.. [optional] if omitted the server will use the default value of 20
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            BulkSendJobListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        try:
            return self.bulk_send_job_list_endpoint.call_with_http_info(**kwargs)
        except ApiException as e:
            if e.status == 200:
                e.body = self.api_client.deserialize(
                    response=MetaDict({'data': e.body}),
                    response_type=[BulkSendJobListResponse],
                    _check_type=True,
                )

                raise e
            range_code = "4XX"[0]
            range_code_left = int(f"{range_code}00")
            range_code_right = int(f"{range_code}99")

            if range_code_left <= e.status <= range_code_right:
                e.body = self.api_client.deserialize(
                    response=MetaDict({'data': e.body}),
                    response_type=[ErrorResponse],
                    _check_type=True,
                )

                raise e

