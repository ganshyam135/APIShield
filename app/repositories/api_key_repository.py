from app.db.database import get_api_keys_collection


class APIKeyRepository:

    async def create(self, document: dict):
        collection = get_api_keys_collection()

        result = await collection.insert_one(document)

        return result

    async def list_all(
    self,
    skip: int = 0,
    limit: int = 10,
) -> list[dict]:
        collection = get_api_keys_collection()

        cursor = (
            collection.find({}, {"api_key_hash": 0})
            .sort("created_at", -1)
            .skip(skip)
            .limit(limit)
        )

        return await cursor.to_list(length=limit)


api_key_repository = APIKeyRepository()