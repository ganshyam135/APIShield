from pydantic import BaseModel, Field
from datetime import datetime


class APIKeyCreateRequest(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=50,
        description="Friendly name for the API key",
    )

class APIKeyResponse(BaseModel):
    id: str
    name: str
    api_key: str

class APIKeyListItem(BaseModel):
    id: str
    name: str
    created_at: datetime
    last_used_at: datetime | None = None
    is_active: bool