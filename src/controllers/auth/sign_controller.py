from flask import request, Response
from uuid import uuid4

def sign_controller():
    
    body: dict[str, any] = request.get_json()
    fullname = body.get("fullname")
    email = body.get("email")
    password = body.get("password")

    try:
        if not fullname or not email or not password:
            return {"success": False}

        if len(fullname) < 3 or len(fullname) > 30:
            return {"success": False, "error": "Invalid fields", "status_code": 400}, 400

        if len(password) < 6 or len(password) > 50:
            return {"success": False, "error": "Password should be 6 letters or above", "status_code": 400}, 400
        
        
        
    except KeyError:
        return {"success": False, "error": "Invalid fields", "status_code": 400}, 400

    return {"success": True}