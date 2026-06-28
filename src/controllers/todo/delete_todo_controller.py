from flask import request
from models.todo_model import TodoModel

def delete_todo_controller(todo_id: str):

    auth_user: dict[str, any] = request.user

    if not auth_user:
        return {"success": False, "error": "User is missing", "status_code": 403}, 403

    todo_model = TodoModel()
    todo: dict[str, any] | None = todo_model.get_todo_by_id_and_user_id(todo_id, auth_user.get("id"))

    if not todo:
        return {"success": False, "error": "Todo is not found", "status_code": 404}, 404

    is_deleted: bool = todo_model.delete_todo_by_id_and_user_id(todo_id, auth_user.get("id"))

    if not is_deleted:
        return {"success": False, "error": "Unable to delete the todo", "status_code": 500}, 500

    return {"success": True, "message": "Todo is deleted", "status_code": 200}, 200