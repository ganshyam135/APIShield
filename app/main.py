from fastapi import FastAPI

from app.api.health import router as health_router

app = FastAPI(
    title="APIShield",
    description="Backend-focused API management and observability platform.",
    version="0.1.0",
)

app.include_router(health_router)
