from contextlib import asynccontextmanager

from fastapi import FastAPI

from motor.motor_asyncio import AsyncIOMotorClient

from app.api.health import router as health_router
from app.core.config import settings
from app.db import database
from app.core.logging import logger
from app.api.api_keys import router as api_key_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Connecting to MongoDB...")

    database.client = AsyncIOMotorClient(settings.mongodb_url)
    database.database = database.client[settings.database_name]
    
    logger.info("MongoDB Connected!")

    yield

    logger.info("Closing MongoDB connection...")

    database.client.close()

    logger.info("MongoDB Closed")


app = FastAPI(
    title=settings.app_name,
    description="Backend-focused API management and observability platform.",
    version=settings.app_version,
    lifespan=lifespan
)

app.include_router(health_router)
app.include_router(api_key_router)


