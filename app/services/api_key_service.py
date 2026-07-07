from app.utils.security import generate_api_key


class APIKeyService:
    def create_api_key(self, name: str):
        return {
            "id": 1,
            "name": name,
            "api_key": generate_api_key(),
        }