from jwt import encode, decode
from dotenv import load_dotenv
from os import getenv

load_dotenv()

def generate_auth_token(user: dict[str, any]): 
    
    jwt_secret_key = getenv("JWT_SECRET")
    
    if not jwt_secret_key: 
        raise ValueError("JWT secret key is missing")

    auth_token = encode(user, jwt_secret_key, algorithm="HS256")
    return auth_token