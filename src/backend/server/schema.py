from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from models import DroneState
from db import db_session

class DroneStateSchema(ModelSchema):
    """ Serializer for DroneState model. """
    uuid = fields.String(dump_only=True)
    is_moving = fields.Boolean(dump_only=True)
    curr_speed = fields.Float(dump_only=True)
    move_timestamp = fields.DateTime(dump_only=True)
    
    class Meta:
        model = DroneState
        sqla_session = db_session