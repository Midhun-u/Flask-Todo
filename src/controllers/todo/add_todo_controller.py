from flask import request
from models.todo_model import TodoModel

def add_todo_controller():

    body: dict[str, any] | None = request.get_json()
    auth_user: dict[str, any] = request.user

    if not auth_user:
        return {"success": False, "error": "User is missing", "status_code": 403}, 403
    
    if not body:
        return {"success": False, "error": "All fields are required", "status_code": 400}, 400

    task = body.get("task")

    if not task:
        return {"success": False, "error": "All fields are required", "status_code": 400}, 400

    if len(task.strip()) < 5 or len(task.strip()) > 100:
        return {"success": False, "error": "Invalid fields", "status_code": 400}, 400

    todo_model = TodoModel()
    new_todo: dict[str, any] = todo_model.add_todo(task=task, user_id=auth_user.get("id"))

    if not new_todo:
        return {"success": False, "error": "Unable to create todo", "status_code": 500}, 500

    return {"success": True, "message": "Todo is created", "new_todo": new_todo, "status_code": 201}, 201