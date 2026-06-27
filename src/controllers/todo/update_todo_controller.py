from models.todo_model import TodoModel
from flask import request

def update_todo_controller(todo_id: str):

    auth_user: dict[str, any] | None = request.user
    body: dict[str, any] = request.get_json()
    protected_fields = {"id", "created_at", "user_id"}

    if not auth_user:
        return {"success": False, "error": "User is missing", "status_code": 403}, 403

    if not body:
        return {"success": False, "error": "Update fields are required", "status_code": 400}, 400

    for protected_field in protected_fields:
        if protected_field in body:
            return {"success": False, "error": "These fields are not editable", "status_code": 403}, 403

    todo_model = TodoModel()
    todo: dict[str, any] | None = todo_model.get_todo_by_id_and_user_id(todo_id, auth_user.get('id'))

    if not todo:
        return {"success": False, "error": "Todo is not found", "status_code": 404}, 404

    updated_todo = todo_model.update_todo_by_id_and_user_id(todo_id, auth_user.get("id"), body)
    if not updated_todo:
        return {"success": False, "error": "Unable to update the todo", "status_code": 500}, 500

    return {"success": True, "todo": updated_todo, "status_code": 200}, 200