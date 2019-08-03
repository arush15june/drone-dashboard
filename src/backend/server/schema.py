from marshmallow_sqlalchemy import ModelSchema
from models import DroneState
from db import db_session

class DroneStateSchema(ModelSchema):
    """ Serializer for DroneState model. """
    class Meta:
        model = DroneState
        sqla_session = db_session