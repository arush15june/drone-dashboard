""" 
    Wrapper for handling Drone state.

    dict{drone_state} ::
    {
        "curr_speed": 0.0,
        "is_moving": false,
        "latitude": "500.00",
        "longitude": "800.00",
        "timestamp": "2019-08-03T09:03:29.252741+00:00",
        "uuid": "97712291-957b-4c18-ad8d-1e0492d5d7ed"
    }
"""
from marshmallow import ValidationError

from models import DroneState
from schema import DroneStateSchema
from db import db_session

def serialize_drone_state(drone_state, *args, **kwargs):
    """
    Serialize a models.DroneState instance to a schema.DroneStateSchema. 
        
    :return schema.DroneStateSchema: Drone state schema.
    """
    return DroneStateSchema().dump(drone_state, **kwargs)

def load_drone_state_dict(data_dict, *args, **kwargs):
    """
    Load a dictionary to a schema.DroneStateSchema. 
        
    :return schema.DroneStateSchema: Drone state schema.
    """
    return DroneStateSchema().load(data_dict, **kwargs)

def get_all_drones():
    """ 
    Return list of all drones in database. 

    :return List[dict{drone_state}]: list of all drones
    """
    all_drones_state = DroneState.query.all()
    drone_state_schema = DroneStateSchema(many=True)
    return drone_state_schema.dump(all_drones_state).data
    
def get_drone_uuid(uuid):
    """
    Filter drone by UUID. 
    
    :return dict{drone_state}: drone state of uuid.
    """
    drone_state = DroneState.query.get(uuid)
    return serialize_drone_state(drone_state).data

def add_drone(data_dict, *args, **kwargs):
    """
    Add a drone to the database.
    
    :return dict{drone_state}: created drone state.
    """
    drone_state = load_drone_state_dict(data_dict, session=db_session)
    
    db_session.add(drone_state.data)
    db_session.commit()

    return drone_state.data

def update_drone(uuid, data_dict, *args, **kwargs):
    """ Update drone by UUID in database. """ 
    curr_speed = data_dict.pop('curr_speed', None)
    
    drone_instance = DroneState.query.get(uuid)
    if drone_instance is None:
        raise ValidationError(messages={'error': 'uuid not in database'})

    drone_state = load_drone_state_dict(data_dict, instance=drone_instance)
    if curr_speed is not None:
        drone_state.data.curr_speed = curr_speed
        
    db_session.commit()

    return drone_state.data


def delete_drone(uuid, *args, **kwargs):
    """ Delete UUID from drone database. """
    drone_instance = DroneState.query.get(uuid)
    if drone_instance is None:
        raise ValidationError(message={'error': 'uuid not in database'})
    
    db_session.delete(drone_instance)
    db_session.commit()
    
    return serialize_drone_state(drone_instance).data