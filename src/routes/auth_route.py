from flask import Blueprint
from controllers.auth.sign_controller import sign_controller
from controllers.auth.login_controller import login_controller

# Auth Blueprint
auth_blueprint = Blueprint("auth", __name__, url_prefix="/api/v1/auth")

# Route for signing
@auth_blueprint.post("/sign")
def sign():
    return sign_controller()

# Route for login
@auth_blueprint.post("/login")
def login(): 
    return login_controller()