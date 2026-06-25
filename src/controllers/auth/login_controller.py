import re
from flask import request
from models.user_model import UserModel
from utils.check_password import check_password
from utils.generate_auth_token import generate_auth_token

def login_controller(): 
    
    body: dict[str, any] = request.get_json()

    if not body:
        return {"success": False, "error":  "All fields are required", "status_code": 400}, 400

    email = body.get("email")
    password = body.get("password")
    
    try:
        if not email or not password:
            return {"success": False, "error": "All fields are required", "status_code": 400}, 400

        # Checking email format
        match = re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)
        if not match:
            return {"success": False, "error": "Invalid fields", "status_code": 400}, 400

        if len(password.strip()) < 6 or len(password.strip()) > 50:
            return {"success": False, "error": "Password should be 6 letters or above", "status_code": 400}, 400
    except KeyError:
        return {"success": False, "error": "All fields are required", "status_code": 400}, 400

    user_model = UserModel()

    # Checking if user registered or not
    user = user_model.get_user_by_email(email=email.strip())
    
    if not user:
        return {"success": False, "error": "Email or password is incorrect", "status_code": 400}, 400

    # Checking password
    is_password_correct = check_password(password=password.strip(), hashed_password=user.password)

    if not is_password_correct:
        return {"success": False, "error": "Email or password is incorrect", "status_code": 400}, 400

    # Generating auth token
    user_dict: dict[str, any] = user.dict()
    user_dict.pop("password")
    user_dict.pop("created_at")
    auth_token = generate_auth_token(user=user_dict)
    
    return {"success": True, "message": "Login success", "auth_token": auth_token, "status_code": 200}, 200