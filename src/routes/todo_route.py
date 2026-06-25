from flask import Blueprint
from controllers.todo.add_todo_controller import add_todo_controller
from middlewares.auth import auth_middleware

# Todo Blueprint
todo_blueprint = Blueprint(name="todo", import_name=__name__, url_prefix="/api/v1/todo")

# Handling authorization
@todo_blueprint.before_request
def before_request(): 
    return auth_middleware()

# Route for adding todo
@todo_blueprint.post("/add-todo")
def add_todo():
    return add_todo_controller()