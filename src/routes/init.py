from routes.auth_route import auth_blueprint
from flask import Flask
from routes.todo_route import todo_blueprint

def register_blueprints(app: Flask):
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(todo_blueprint)