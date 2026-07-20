from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, AsyncIOMotorCollection

client: AsyncIOMotorClient = None
database: AsyncIOMotorDatabase = None


def get_database() -> AsyncIOMotorDatabase:
    if database is None:
        raise RuntimeError("Database has not been initialized.")
    
    return database

def get_api_keys_collection() -> AsyncIOMotorCollection:
    db = get_database()
    return db["api_keys"]