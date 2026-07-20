from datetime import datetime, UTC

from app.utils.security import generate_api_key, hash_api_key
from app.db.database import get_api_keys_collection


class APIKeyService:

    async def create_api_key(self, name: str):
        api_key = generate_api_key()

        api_key_hash = hash_api_key(api_key)

        document ={
            "name": name,
            "api_key_hash": api_key_hash,
            "created_at": datetime.now(UTC),
            "last_used_at": None,
            "is_active": True,
        }

        collection = get_api_keys_collection()

        result = await collection.insert_one(document)
        
        return {
            "id": 1,
            "name": name,
            "api_key": api_key,
            "key_hash": api_key_hash, #testing, will remove when connecting to MongoDB
        }
    
api_key_service = APIKeyService()

