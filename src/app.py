from flask import Flask
from routes.init import register_blueprints
from dotenv import load_dotenv
from os import getenv
from config.db import connect_to_database

# Main app instance
app = Flask(__name__)

# Routes
register_blueprints(app=app)
@app.route("/api/v1")
def index():
    return {"success": True, "status": "Running", "status_code": 200}

# Error handler
@app.errorhandler(500)
def error_handler(error):
    return {
        "success": False,
        "error": "Server error",
        "status_code": 500
    }, 500

if __name__ == "__main__":

    # Loading env
    load_dotenv()
    port = getenv("PORT") if getenv("PORT") else 5000

    # Connecting to the database
    connect_to_database()

    app.run(debug=False, port=port)