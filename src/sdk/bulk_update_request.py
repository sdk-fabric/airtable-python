"""
bulk_update_request automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
from .record import Record
class BulkUpdateRequest(BaseModel):
    perform_upsert: Optional[List[str]] = Field(default=None, alias="performUpsert")
    return_fields_by_field_id: Optional[bool] = Field(default=None, alias="returnFieldsByFieldId")
    typecast: Optional[bool] = Field(default=None, alias="typecast")
    records: Optional[List[Record]] = Field(default=None, alias="records")
    pass
