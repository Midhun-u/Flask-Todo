from flask import Blueprint
from controllers.auth.sign_controller import sign_controller
from controllers.auth.login_controller import login_controller
from controllers.auth.get_profile_controller import get_profile_controller
from middlewares.auth import auth_middleware

# Auth Blueprint
auth_blueprint = Blueprint(name="auth", import_name=__name__, url_prefix="/api/v1/auth")

# Handling authorization
@auth_blueprint.before_request
def before_request():
    return auth_middleware()

# Route for signing
@auth_blueprint.post("/sign/")
def sign():
    return sign_controller()

# Route for login
@auth_blueprint.post("/login/")
def login(): 
    return login_controller()

# Route for getting user profile
@auth_blueprint.get("/get-profile/")
def get_profile():
    return get_profile_controller()