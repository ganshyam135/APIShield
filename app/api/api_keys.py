from fastapi import APIRouter, Query, HTTPException

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

@router.get("/{key_id}", response_model=APIKeyListItem)
async def get_api_key(key_id: str):
    api_key = await api_key_service.get_api_key(key_id)

    if api_key is None:
        raise HTTPException(
            status_code=404,
            detail="API key not found",
        )

    return api_key
