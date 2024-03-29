''' 
    REST API for handling drone state requests.
'''

import logging

from flask import request, Blueprint, render_template, abort, Response, jsonify
from marshmallow import ValidationError

import drones
from schema import DroneStateSchema

drone_api = Blueprint('drones', __name__)

@drone_api.route('/drones')
def drones_route():
    """
    Return serialized list of all Drones. 
    
    :return List[dict{drones.drone_state}]: list of all drones.
    """
    all_drones_data = drones.get_all_drones()
    return jsonify(all_drones_data)

@drone_api.route('/drones', methods=['POST'])
def drone_post():
    """
    Create a new drone.
    
    :return dict{drones.drone_state}: new drone state.
    """
    data_json = request.get_json()
    try:
        drone_state = drones.add_drone(data_json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    print(drone_state)

    return jsonify(drones.serialize_drone_state(drone_state).data), 201

@drone_api.route('/drones/<string:uuid>')
def drone_get(uuid):
    """
    Return drone data selected by UUID 

    :return dict{drone_state}: state of drone uuid.
    """
    drone_data = drones.get_drone_uuid(uuid)
    return jsonify(drone_data)

@drone_api.route('/drones/<string:uuid>', methods=['PUT'])
def drone_put(uuid):
    """
    Manipulate drone data selected by UUID 

    :return dict{drone_state}: state of updated drone uuid.
    """
    data_json = request.get_json()
    try:
        drone_state = drones.update_drone(uuid, data_json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    return jsonify(drones.serialize_drone_state(drone_state).data), 202

@drone_api.route('/drones/<string:uuid>', methods=['DELETE'])
def drone_delete(uuid):
    """
    Delete drone selected by UUID. 

    :return dict{drone_state}: state of deleted drone uuid.
    """
    try:
        drone_state = drones.delete_drone(uuid)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    return jsonify(drones.serialize_drone_state(drone_state).data), 202
