from flask import request
from models.todo_model import TodoModel

def get_todo_controller(todo_id: str):
   
    auth_user: dict[str, any] = request.user

    if not auth_user:
        return {"success": False, "error": "User is missing", "status_code": 403}, 403

    todo_model = TodoModel()
    todo = todo_model.get_todo_by_id_and_user_id(todo_id, auth_user.get("id"))

    return {"success": True, "todo": todo, "status_code": 200}