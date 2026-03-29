from pydantic import BaseModel, HttpUrl
from typing import Optional

class URLCreate(BaseModel):
    original_url: HttpUrl
    custom_alias: Optional[str] = None