from flask import Flask
from db import init_db
from api import drone_api

init_db()
app = Flask(__name__)
app.register_blueprint(drone_api)

if __name__ == "__main__":
    app.run(port=5000, debug=True)