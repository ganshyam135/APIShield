from datetime import datetime, UTC

from app.utils.security import generate_api_key, hash_api_key
from app.repositories.api_key_repository import api_key_repository


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

        result = await api_key_repository.create(document)
        
        return {
            "id": str(result.inserted_id), 
            "name": name,
            "api_key": api_key,
        }
    
api_key_service = APIKeyService()

