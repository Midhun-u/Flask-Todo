from flask import request
from models.todo_model import TodoModel

def get_user_todos_controller():

    page: int = int(request.args.get("page")) if request.args.get("page") else 1
    limit: int = int(request.args.get("limit")) if request.args.get("limit") else 10
    auth_user: dict[str, any] = request.user

    if not auth_user:
        return {"success": False, "error": "User is missing", "status_code": 403}, 403

    todo_model = TodoModel()

    todos: list[dict[str, any]] = todo_model.get_user_todos(auth_user.get("id"), page, limit)
    
    return {"success": True, "todos": todos, "page": page, "limit": limit}