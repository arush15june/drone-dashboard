from math import radians, cos, sin, asin, sqrt
import datetime
import uuid

from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
def generate_uuid():
    """ 
    Get a random UUID 
    
    :return str: Randomly generated UUID string.
    """
    return str(uuid.uuid4())


def haversine(lat1, lon1, lat2, lon2):
    """
    Distance between two latitude and longitude points in kilometers.

    :return float: distance in kilometers.
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

class DroneState(Base):
    """
    :param uuid str: UUID of Drone.
    :param latitude float: Last received latitude.
    :param longitude float: Last received longitude.
    :param data_timestamp datetime.datetime: Most recent timestamp of drone transmitting.
    :param move_timestamp datetime.datetime: Most recent timestamp of drone moving.
    :param curr_speed float: current speed of drone.
    :param is_moving bool: is the drone moving or not.
    """
    __tablename__ = 'drones'
    uuid = Column(String(36), primary_key=True, default=generate_uuid)
    latitude = Column(Float(), default=0.0)
    longitude = Column(Float(), default=0.0)
    data_timestamp = Column(DateTime(), default=datetime.datetime.utcnow)
    move_timestamp = Column(DateTime(), default=datetime.datetime.utcnow)
    curr_speed = Column(Float(), default=0.0)
    is_moving = Column(Boolean(), default=False)

    def _diff_distance(self, latitude, longitude):
        """ 
        Calculate distance between instance's coordinates and passed coordinates.

        :param latitude float: latitude of coord.
        :param longitude float: longitude of coord.
        
        :return float: distance in meters.
        """
        distance = haversine(self.latitude, self.longitude, latitude, longitude)*1000.0
        return distance
    
    def _diff_timestamp(self):
        """ 
        Calculate difference in seconds between move timestamp and data timestamp.

        :return float: total difference in seconds between data and move timestamps
        """
        tdelta = (self.data_timestamp - self.move_timestamp)

        return tdelta.total_seconds()

    def set_is_moving(self, latitude, longitude):
        """ 
        Set self.is_moving based on data_timestamp and move_timestamp
        
        :param latitude float: latitude of coord.
        :param longitude float: longitude of coord.
        """
        self.is_moving = True
        move_tdelta = self._diff_timestamp()
        diff_distance = self._diff_distance(latitude, longitude)

        if move_tdelta >= 10.0:
            if diff_distance <= 1.0:
                self.is_moving = False
            else:
                self.move_timestamp = self.data_timestamp

    def __repr__(self):
        return f'<DroneState {self.uuid} speed: {self.curr_speed} moving: {self.is_moving}>'