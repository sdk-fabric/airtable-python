
# airtable-python

This [SDK](https://github.com/sdk-fabric/airtable-python) is managed by the [SDK Fabric](https://sdk-fabric.org/) project, a global infrastructure to
automatically generate SDKs for every API.

You can find more information about this SDK at [TypeHub](https://typehub.cloud/):
https://app.typehub.cloud/d/sdkfabric/airtable

## Usage

```python
from sdk.client import Client

client = Client.build("[access_token]")

# Retrieve the user's ID.
response = client.meta().get_whoami()

# List records in a table.
response = client.records().get_all("base_id", "table_id_or_name", "time_zone", "user_locale", 1, 1, "offset", "view", "sort", "filter_by_formula", "cell_format", "fields", True, "record_metadata")

# Retrieve a single record.
response = client.records().get("base_id", "table_id_or_name", "record_id")

# Creates multiple records.
response = client.records().create("base_id", "table_id_or_name", RecordCollection())

# Updates a single record.
response = client.records().replace("base_id", "table_id_or_name", "record_id", Record())

# Updates up to 10 records, or upserts them when performUpsert is set.
response = client.records().replace_all("base_id", "table_id_or_name", BulkUpdateRequest())

# Updates a single record.
response = client.records().update("base_id", "table_id_or_name", "record_id", Record())

# Updates up to 10 records, or upserts them when performUpsert is set.
response = client.records().update_all("base_id", "table_id_or_name", BulkUpdateRequest())

# Deletes a single record.
response = client.records().delete("base_id", "table_id_or_name", "record_id")

# Creates a new column and returns the schema for the newly created column.
response = client.fields().create("base_id", "table_id", Field())

# Updates the name and/or description of a field.
response = client.fields().update("base_id", "table_id", "column_id", Field())

# Creates a new table and returns the schema for the newly created table.
response = client.tables().create("base_id", Table())

# Updates the name and/or description of a table.
response = client.tables().update("base_id", "table_id_or_name", Table())

# Returns a list of comments for the record from newest to oldest.
response = client.comments().get_all("base_id", "table_id_or_name", "record_id")

# Creates a comment on a record.
response = client.comments().create("base_id", "table_id_or_name", "record_id", Comment())

# Updates a comment on a record.
response = client.comments().update("base_id", "table_id_or_name", "record_id", "row_comment_id", Comment())

# Deletes a comment from a record.
response = client.comments().delete("base_id", "table_id_or_name", "record_id", "row_comment_id")
```
