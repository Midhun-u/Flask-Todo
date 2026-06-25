from flask import request
from utils.auth_protected_routes import auth_protected_routes
from jwt import decode
from os import getenv
from dotenv import load_dotenv
from models.user_model import UserModel

# Function for handling authorization
def auth_middleware():
    
    path = request.path
    is_protected = False
    
    for protected_route in auth_protected_routes:
        if protected_route in path:
            is_protected = True
            break

    if is_protected:
        authorization = request.headers.get("Authorization")
        
        if not authorization:
            return {"success": False, "error": "Unauthorized user", "status_code": 401}, 401

        auth_token = authorization.split(" ")[1]
        
        if not auth_token:
            return {"success": False, "error": "Unauthorized user", "status_code": 401}, 401

        load_dotenv()

        jwt_secret = getenv("JWT_SECRET")

        try:     
            decoded_data = decode(jwt=auth_token, key=jwt_secret, algorithms="HS256")

            if not decoded_data:
                return {"success": False, "error": "Unauthorized user", "status_code": 401}, 401

            user_model = UserModel()
            user = user_model.get_user_by_id(decoded_data.get("id"))

            if not user:
                return {"success": False, "error": "Invalid user", "status_code": 403}, 403

            user_dict: dict[str, any] = user.dict()
            user_dict.pop("password")

            request.user = user_dict

        except Exception as exception:
            return {"success": False, "error": "Invalid token", "status_code": 403}, 403