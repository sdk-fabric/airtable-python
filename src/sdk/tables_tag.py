"""
TablesTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List

from .error_exception import ErrorException
from .table import Table

class TablesTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    def create(self, base_id: str, payload: Table) -> Table:
        """
        Creates a new table and returns the schema for the newly created table.
        """
        try:
            path_params = {}
            path_params["baseId"] = base_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/v0/meta/bases/:baseId/tables", path_params)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = self.http_client.post(url, headers=headers, params=self.parser.query(query_params, query_struct_names), json=payload.model_dump(by_alias=True))

            if response.status_code >= 200 and response.status_code < 300:
                return Table.model_validate_json(json_data=response.content)

            if response.status_code == 400:
                raise ErrorException(response.content)
            if response.status_code == 403:
                raise ErrorException(response.content)
            if response.status_code == 404:
                raise ErrorException(response.content)
            if response.status_code == 500:
                raise ErrorException(response.content)

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def update(self, base_id: str, table_id_or_name: str, payload: Table) -> Table:
        try:
            path_params = {}
            path_params["baseId"] = base_id
            path_params["tableIdOrName"] = table_id_or_name

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/v0/meta/bases/:baseId/tables/:tableIdOrName", path_params)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = self.http_client.patch(url, headers=headers, params=self.parser.query(query_params, query_struct_names), json=payload.model_dump(by_alias=True))

            if response.status_code >= 200 and response.status_code < 300:
                return Table.model_validate_json(json_data=response.content)

            if response.status_code == 400:
                raise ErrorException(response.content)
            if response.status_code == 403:
                raise ErrorException(response.content)
            if response.status_code == 404:
                raise ErrorException(response.content)
            if response.status_code == 500:
                raise ErrorException(response.content)

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))


