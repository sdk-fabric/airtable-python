"""
error automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union
from .error_details import ErrorDetails


class Error(BaseModel):
    error: Optional[ErrorDetails] = Field(default=None, alias="error")
    pass


