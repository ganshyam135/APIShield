from fastapi import APIRouter

from app.schemas.api_key import (
    APIKeyCreateRequest,
    APIKeyResponse,
)

from app.services.api_key_service import api_key_service

router = APIRouter(
    prefix="/api-keys",
    tags=["API Keys"],
)

@router.post("", response_model=APIKeyResponse, status_code=201)
async def create_api_key(request: APIKeyCreateRequest):
    return await api_key_service.create_api_key(request.name)
