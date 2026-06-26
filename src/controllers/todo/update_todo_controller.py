from models.todo_model import TodoModel
from flask import request

def update_todo_controller(todo_id: str):

    auth_user = request.user
    body: dict[str, any] = request.get_json()

    if not auth_user:
        return {"success": False, "error": "User is missing", "status_code": 403}, 403

    if not body:
        return {"success": False, "error": "Update fields are required", "status_code": 400}, 400

    

    return {"success": True}