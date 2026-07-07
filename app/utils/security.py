import secrets


def generate_api_key() -> str:
    return f"aps_live_{secrets.token_urlsafe(32)}"

#test
print(generate_api_key())