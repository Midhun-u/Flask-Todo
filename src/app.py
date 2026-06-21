from flask import Flask

# Main app instance
app = Flask(__name__)

@app.route("/")
def index():
    return {"success": True, "status": "Running", "status_code": 200}

if __name__ == "__main__":
    app.run(debug=True)