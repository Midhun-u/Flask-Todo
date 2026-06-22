from flask import Blueprint
from controllers.auth.sign_controller import sign_controller

# Auth Blueprint
auth_blueprint = Blueprint("auth", __name__, url_prefix="/api/v1/auth")

# Route for signing
@auth_blueprint.post("/sign")
def sign():
    return sign_controller()