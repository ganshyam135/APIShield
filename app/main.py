from contextlib import asynccontextmanager

from fastapi import FastAPI

from motor.motor_asyncio import AsyncIOMotorClient

from app.api.health import router as health_router
from app.core.config import settings
from app.db import database


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Connecting to MongoDB...")

    database.client = AsyncIOMotorClient(settings.mongodb_url)
    database.database = database.client[settings.database_name]
    
    print("MongoDB Connected!")

    yield

    print("Closing MongoDB connection...")

    database.client.close()

    print("MongoDB Closed")


app = FastAPI(
    title=settings.app_name,
    description="Backend-focused API management and observability platform.",
    version=settings.app_version,
    lifespan=lifespan
)

app.include_router(health_router)
