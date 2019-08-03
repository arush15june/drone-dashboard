import datetime
import uuid

from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean

from db import Base

def generate_uuid():
    """ 
    Get a random UUID 
    
    :return str: Randomly generated UUID string.
    """
    return str(uuid.uuid4())

class DroneState(Base):
    __tablename__ = 'drones'
    uuid = Column(String(36), primary_key=True, default=generate_uuid)
    latitude = Column(Float())
    longitude = Column(Float())
    timestamp = Column(DateTime(), default=datetime.datetime.utcnow)
    curr_speed = Column(Float(), default=0.0)
    is_moving = Column(Boolean(), default=False)

    def __repr__(self):
        return f'<DroneState {self.uuid} speed: {self.curr_speed} moving: {self.is_moving}>'