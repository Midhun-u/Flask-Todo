from routes.auth_route import auth_blueprint
from flask import Flask

def register_blueprints(app: Flask):
    app.register_blueprint(auth_blueprint)