"""
FieldsTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List
from typing import Dict
from typing import Any
from urllib.parse import parse_qs

from .error_exception import ErrorException
from .field import Field

class FieldsTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    def create(self, base_id: str, table_id: str, payload: Field) -> Field:
        """
        Creates a new column and returns the schema for the newly created column.
        """
        try:
            path_params = {}
            path_params['baseId'] = base_id
            path_params['tableId'] = table_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/v0/meta/bases/:baseId/tables/:tableId/fields', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)

            options['json'] = payload.model_dump(by_alias=True)

            options['headers']['Content-Type'] = 'application/json'

            response = self.http_client.request('POST', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = Field.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode == 400:
                data = Error.model_validate_json(json_data=response.content)

                raise ErrorException(data)

            if statusCode == 403:
                data = Error.model_validate_json(json_data=response.content)

                raise ErrorException(data)

            if statusCode == 404:
                data = Error.model_validate_json(json_data=response.content)

                raise ErrorException(data)

            if statusCode == 500:
                data = Error.model_validate_json(json_data=response.content)

                raise ErrorException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))

    def update(self, base_id: str, table_id: str, column_id: str, payload: Field) -> Field:
        """
        Updates the name and/or description of a field. At least one of name or description must be specified.
        """
        try:
            path_params = {}
            path_params['baseId'] = base_id
            path_params['tableId'] = table_id
            path_params['columnId'] = column_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/v0/meta/bases/:baseId/tables/:tableId/fields/:columnId', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)

            options['json'] = payload.model_dump(by_alias=True)

            options['headers']['Content-Type'] = 'application/json'

            response = self.http_client.request('PATCH', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = Field.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode == 400:
                data = Error.model_validate_json(json_data=response.content)

                raise ErrorException(data)

            if statusCode == 403:
                data = Error.model_validate_json(json_data=response.content)

                raise ErrorException(data)

            if statusCode == 404:
                data = Error.model_validate_json(json_data=response.content)

                raise ErrorException(data)

            if statusCode == 500:
                data = Error.model_validate_json(json_data=response.content)

                raise ErrorException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))



