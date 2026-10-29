from fastapi import APIRouter, Query

from typing import Annotated

from app.schemas.api_key import (
    APIKeyCreateRequest,
    APIKeyResponse,
    APIKeyListItem,
)

from app.services.api_key_service import api_key_service

router = APIRouter(
    prefix="/api-keys",
    tags=["API Keys"],
)

@router.post("", response_model=APIKeyResponse, status_code=201)
async def create_api_key(request: APIKeyCreateRequest):
    return await api_key_service.create_api_key(request.name)

@router.get("", response_model=list[APIKeyListItem])
async def list_api_keys(
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=100)] = 10,
):
    return await api_key_service.list_api_keys(
        skip=skip,
        limit=limit,
    )
