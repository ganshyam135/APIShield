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

    async def list_api_keys(
    self,
    skip: int = 0,
    limit: int = 10,
) -> list[dict]:
        documents = await api_key_repository.list_all(
            skip=skip,
            limit=limit,
        )

        return [
            {
                "id": str(document["_id"]),
                "name": document["name"],
                "created_at": document["created_at"],
                "last_used_at": document["last_used_at"],
                "is_active": document["is_active"],
            }
            for document in documents
        ]

    async def get_api_key(self, key_id: str) -> dict | None:
        document = await api_key_repository.get_by_id(key_id)

        if document is None:
            return None

        return {
            "id": str(document["_id"]),
            "name": document["name"],
            "created_at": document["created_at"],
            "last_used_at": document["last_used_at"],
            "is_active": document["is_active"],
        }
    
api_key_service = APIKeyService()

