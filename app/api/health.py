from fastapi import APIRouter, Depends


from datetime import datetime, UTC

from app.core.config import Settings
from app.core.dependencies import get_settings


router = APIRouter()


@router.get("/health")
async def health_check(
    settings: Settings = Depends(get_settings)
):
    return{
        "status": "healthy",
        "service": "APIShield",
        "version": "0.1.0",
        "timestamp": datetime.now(UTC).isoformat(),
    }
