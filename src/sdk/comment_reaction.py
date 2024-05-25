"""
comment_reaction automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
from .comment_author import CommentAuthor
class CommentReaction(BaseModel):
    emoji: Optional[str] = Field(default=None, alias="emoji")
    reacting_user: Optional[CommentAuthor] = Field(default=None, alias="reactingUser")
    pass