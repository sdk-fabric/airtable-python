"""
error_details automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
class ErrorDetails(BaseModel):
    type: Optional[str] = Field(default=None, alias="type")
    message: Optional[str] = Field(default=None, alias="message")
    pass
