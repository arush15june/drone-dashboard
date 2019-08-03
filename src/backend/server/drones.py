""" 
    Wrapper for handling Drone state.
"""
from models import DroneState
from schema import DroneStateSchema
from db import db_session

def get_all_drones():
    """ Return list of all drones in database. """
    all_drones = DroneState.query.all()
    drone_state_schema = DroneStateSchema(many=True)
    return drone_state_schema.dump(all_drones).data
    
def get_drone_uuid(uuid):
    """ Filter drone by UUID. """
    drone_state = DroneState.query.get(uuid)
    drone_state_schema = DroneStateSchema()
    return drone_state_schema.dump(drone_state).data