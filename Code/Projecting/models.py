from datetime import datetime
from enum import Enum

from pydantic import BaseModel, HttpUrl


class Author(BaseModel):
    login: str
    avatar_url: HttpUrl


class Release(BaseModel):
    name: str
    draft: bool = False
    tag_name: str
    html_url: HttpUrl
    author: Author
    created_at: datetime
    published_at: datetime = None
    body: str


class Body(BaseModel):
    action: str
    release: Release
