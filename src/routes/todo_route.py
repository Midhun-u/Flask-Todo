from flask import Blueprint
from middlewares.auth import auth_middleware
from controllers.todo.add_todo_controller import add_todo_controller
from controllers.todo.get_user_todos_controller import get_user_todos_controller
from controllers.todo.get_todo_controller import get_todo_controller
from controllers.todo.update_todo_controller import update_todo_controller
from controllers.todo.delete_todo_controller import delete_todo_controller

# Todo Blueprint
todo_blueprint = Blueprint(name="todo", import_name=__name__, url_prefix="/api/v1/todo")

# Handling authorization
@todo_blueprint.before_request
def before_request(): 
    return auth_middleware()

# Route for adding todo
@todo_blueprint.post("/add-todo/")
def add_todo():
    return add_todo_controller()

# Route for getting all user todos
@todo_blueprint.get("/get-user-todos/")
def get_user_todos():
    return get_user_todos_controller()

# Route for getting specific user todo
@todo_blueprint.get("/get-todo/<string:todo_id>")
def get_todo(todo_id: str):
    return get_todo_controller(todo_id=todo_id)

# Route for updating todo
@todo_blueprint.patch("/update-todo/<string:todo_id>")
def update_todo(todo_id: str):
    return update_todo_controller(todo_id=todo_id)

# Route for deleting todo
@todo_blueprint.delete("/delete-todo/<string:todo_id>")
def delete_todo(todo_id: str):
    return delete_todo_controller(todo_id=todo_id)