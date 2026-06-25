from flask import request
from utils.auth_protected_routes import auth_protected_routes
from jwt import decode
from os import getenv
from dotenv import load_dotenv

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
            user = decode(jwt=auth_token, key=jwt_secret, algorithms="HS256")
            if user:
                request.user = user
            else:
                return {"success": False, "error": "Unauthorized user", "status_code": 401}, 401
        except Exception as exception:
            return {"success": False, "error": "Invalid token", "status_code": 403}, 403