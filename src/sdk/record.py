"""
record automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
class Record(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    created_time: Optional[str] = Field(default=None, alias="createdTime")
    fields: Optional[Dict[str, Any]] = Field(default=None, alias="fields")
    pass