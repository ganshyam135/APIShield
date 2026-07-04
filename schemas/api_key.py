from pydantic import BaseModel, Field


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