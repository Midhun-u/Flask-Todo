from flask import Flask
from routes.init import register_blueprints
from dotenv import load_dotenv
from os import getenv

# Main app instance
app = Flask(__name__)

# Routes
register_blueprints(app=app)

@app.route("/api/v1")
def index():
    return {"success": True, "status": "Running", "status_code": 200}

if __name__ == "__main__":

    # Loading env
    load_dotenv()
    
    port = getenv("PORT") if getenv("PORT") else 5000
    app.run(debug=True, port=port)