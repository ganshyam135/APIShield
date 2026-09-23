from app.db.database import get_api_keys_collection


class APIKeyRepository:

    async def create(self, document: dict):
        collection = get_api_keys_collection()

        result = await collection.insert_one(document)

        return result


api_key_repository = APIKeyRepository()