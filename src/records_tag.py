"""
RecordsTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List

from .record import Record
from .record_collection import RecordCollection

class RecordsTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    def get_all(self, base_id: str, table_id_or_name: str, time_zone: str, user_locale: str, page_size: int, max_records: int, offset: str, view: str, sort: str, filter_by_formula: str, cell_format: str, fields: str, return_fields_by_field_id: bool, record_metadata: str) -> RecordCollection:
        """
        List records in a table. Note that table names and table ids can be used interchangeably. We recommend using table IDs so you don&#039;t need to modify your API request when your table name changes.
        """
        try:
            path_params = {}
            path_params["baseId"] = base_id
            path_params["tableIdOrName"] = table_id_or_name

            query_params = {}
            query_params["timeZone"] = time_zone
            query_params["userLocale"] = user_locale
            query_params["pageSize"] = page_size
            query_params["maxRecords"] = max_records
            query_params["offset"] = offset
            query_params["view"] = view
            query_params["sort"] = sort
            query_params["filterByFormula"] = filter_by_formula
            query_params["cellFormat"] = cell_format
            query_params["fields"] = fields
            query_params["returnFieldsByFieldId"] = return_fields_by_field_id
            query_params["recordMetadata"] = record_metadata

            query_struct_names = []

            url = self.parser.url("/v0/:baseId/:tableIdOrName", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return RecordCollection.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def get(self, base_id: str, table_id_or_name: str, record_id: str) -> Record:
        """
        Retrieve a single record. Any &quot;empty&quot; fields (e.g. &quot;&quot;, [], or false) in the record will not be returned.
        """
        try:
            path_params = {}
            path_params["baseId"] = base_id
            path_params["tableIdOrName"] = table_id_or_name
            path_params["recordId"] = record_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/v0/:baseId/:tableIdOrName/:recordId", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return Record.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def replace(self, base_id: str, table_id_or_name: str, record_id: str, payload: Record) -> Record:
        """
        Updates a single record. Table names and table ids can be used interchangeably. We recommend using table IDs so you don&#039;t need to modify your API request when your table name changes.
        """
        try:
            path_params = {}
            path_params["baseId"] = base_id
            path_params["tableIdOrName"] = table_id_or_name
            path_params["recordId"] = record_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/v0/:baseId/:tableIdOrName/:recordId", path_params)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = self.http_client.put(url, headers=headers, params=self.parser.query(query_params, query_struct_names), json=payload.model_dump(by_alias=True))

            if response.status_code >= 200 and response.status_code < 300:
                return Record.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def update(self, base_id: str, table_id_or_name: str, record_id: str, payload: Record) -> Record:
        """
        Updates a single record. Table names and table ids can be used interchangeably. We recommend using table IDs so you don&#039;t need to modify your API request when your table name changes.
        """
        try:
            path_params = {}
            path_params["baseId"] = base_id
            path_params["tableIdOrName"] = table_id_or_name
            path_params["recordId"] = record_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/v0/:baseId/:tableIdOrName/:recordId", path_params)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = self.http_client.patch(url, headers=headers, params=self.parser.query(query_params, query_struct_names), json=payload.model_dump(by_alias=True))

            if response.status_code >= 200 and response.status_code < 300:
                return Record.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

