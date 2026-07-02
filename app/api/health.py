from fastapi import APIRouter
from datetime import datetime, UTC


router = APIRouter()


@router.get("/health")
async def health_check():
    return{
        "status": "healthy",
        "service": "APIShield",
        "version": "0.1.0",
        "timestamp": datetime.now(UTC).isoformat(),
    }
