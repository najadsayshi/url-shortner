from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class URL(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    original_url : str

    short_code : str = Field(index=True, unique=True)
    created_at : datetime = Field(default_factory=datetime.utcnow)
    expiry_at : Optional[datetime] = None
    click_count : int = Field(default=0)
    user_id : Optional[int] = None

