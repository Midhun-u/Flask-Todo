import re
from flask import request, Response
from models.user_model import UserModel
from utils.hash_password import hash_password
from utils.generate_auth_token import generate_auth_token

def sign_controller():
    
    body: dict[str, any] = request.get_json()
    fullname = body.get("fullname")
    email = body.get("email")
    password = body.get("password")

    try:
        if not fullname.strip() or not email.strip() or not password.strip():
            return {"success": False}

        if len(fullname.strip()) < 3 or len(fullname.strip()) > 30:
            return {"success": False, "error": "Invalid fields", "status_code": 400}, 400

        # Checking email format
        match = re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)
        if not match:
            return {"success": False, "error": "Invalid fields", "status_code": 400}, 400

        if len(password.strip()) < 6 or len(password.strip()) > 50:
            return {"success": False, "error": "Password should be 6 letters or above", "status_code": 400}, 400
        
    except KeyError:
        return {"success": False, "error": "Invalid fields", "status_code": 400}, 400

    
    user_model = UserModel()
    
    # Checking if email is already registered
    user = user_model.get_user_by_email(email=email.strip())
    if user:
        return {"success": False, "error": "Email is already registered", "status_code": 409}, 409

    # Hashing password
    hashed_password = hash_password(password=password.strip())

    new_user = user_model.add_user(fullname=fullname.strip(), email=email.strip(), password=hashed_password.strip())
    new_user.pop("password")
    
    if new_user:
        auth_token = generate_auth_token(new_user)
        return {"success": True, "message": "User is created", "user": new_user, "auth_token": auth_token, "status_code": 201}, 201

    return {"success": True, "error": "Unable to create user", "status_code": 400}, 400