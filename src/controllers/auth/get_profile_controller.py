from flask import request
from models.user_model import UserModel

def get_profile_controller():
    
    auth_user: dict[str, any] | None = request.user

    if not auth_user:
        return {"success": False, "error": "User is missing", "status_code": 403}, 403

    user_model = UserModel()

    user = user_model.get_user_by_id(auth_user.get("id"))
    user_dict: dict[str, any] | None = user.dict()
    user_dict.pop("password")
    
    return {"success": True, "user": user_dict, "status_code": 200}, 200