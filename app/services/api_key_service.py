from app.utils.security import generate_api_key, hash_api_key


class APIKeyService:

    def create_api_key(self, name: str):
        api_key = generate_api_key()

        api_key_hash = hash_api_key(api_key)
        
        return {
            "id": 1,
            "name": name,
            "api_key": api_key,
            "key_hash": api_key_hash, #testing, will remove when connecting to MongoDB
        }
    
api_key_service = APIKeyService()

