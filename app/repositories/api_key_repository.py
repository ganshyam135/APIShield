from app.db.database import get_api_keys_collection


class APIKeyRepository:

    async def create(self, document: dict):
        collection = get_api_keys_collection()

        result = await collection.insert_one(document)

        return result

    async def list_all(self) -> list[dict]:
        collection = get_api_keys_collection()

        cursor = collection.find(
            {},
            {"api_key_hash": 0},
        ).sort("created_at", -1)

        return await cursor.to_list(length=100)


api_key_repository = APIKeyRepository()