""" 
    API Root

    /api
        /api/drones
            - POST: Create new drone.
            - GET: Get all drones.
        /api/drones/<uuid>
            - GET: Get selected drone.
            - PUT: Update selected drone.
            - DELETE: Delete Selected drone.
"""
from flask import Flask
from db import init_db
from api import drone_api
from flask_cors import CORS

init_db()

app = Flask(__name__)
cors = CORS(app, resources={r"/api": {"origins": "*"}})

app.register_blueprint(drone_api, url_prefix='/api')

if __name__ == "__main__":
    app.run(port=5000, debug=True)