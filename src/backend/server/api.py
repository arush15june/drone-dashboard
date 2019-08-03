''' 
    REST API for handling drone state requests.
'''

import logging
from flask import Blueprint, render_template, abort, Response, jsonify

import drones

drone_api = Blueprint('drone', __name__)

@drone_api.route('/drones')
def drones_route():
    """ Return serialized list of all Drones. """
    all_drones_data = drones.get_all_drones()
    return jsonify(all_drones_data)

@drone_api.route('/drones/<string:uuid>')
def drone_uuid(uuid):
    """ Return serialized list of all Drones. """
    drone_data = drones.get_drone_uuid(uuid)
    return jsonify(drone_data)