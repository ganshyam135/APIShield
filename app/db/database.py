from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

client: AsyncIOMotorClient = None
database: AsyncIOMotorDatabase = None


def get_database() -> AsyncIOMotorDatabase:
    if database is None:
        raise RuntimeError("Database has not been initialized.")
    
    return database