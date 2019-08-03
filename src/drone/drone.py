""" Simulated Drone """

import sys
import socket
import random
import datetime
import calendar
import time

import drone_pb2

NEW_LINE = '\n'

def get_timestamp():
    """ Get UTC Timestamp. """

    return calendar.timegm(datetime.datetime.utcnow().utctimetuple())

def serialize_payload(uuid, latitude, longitude, speed):
    """ 
    Serilaized payload as protobuf binary 
    
    :param uuid str: drone uuid
    :param latitude float: latitude degrees
    :param latitude float: longitude degrees
    :param speed float: current speed of drone.

    :return bytes: serialized payload
    """
    drone_state = drone_pb2.DroneState()
    drone_state.uuid = uuid
    drone_state.latitude = latitude
    drone_state.longitude = longitude
    drone_state.timestamp = int(get_timestamp())
    drone_state.curr_speed = speed

    return drone_state.SerializeToString()
    
def connect(host, port):
    """
    Connect to server. 
    
    :param host str: client hostname
    :param port int: client port

    :return client socket.socket: connected socket.
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    return client

def send_payload(client, payload):
    """ 
    Send payload via socket.

    :param client socket: connected socket object.
    :param payload bytes: payload bytestream.
    """
    client.send(payload)

def close_connection(client):
    """ 
    Close socket. 
    
    :param client socket: socket object.
    """
    client.close()

def get_random_lat_long():
    """ 
    Return a tuple with random latitude and longitudes. 

    :param tuple(float, float): latitude, longitude
    """
    return (random.uniform(-90.0, 90.0), random.uniform(-90.0, 90.0))

if __name__ == "__main__":
    def get_random_payload():
        """ Randomly generated device state. """
        speed = random.uniform(10.0, 15.0)
        lat, long = get_random_lat_long()

        return lat, long, speed
    
    def get_static_payload():
        return 1.0, 2.0, 10.0

    HOST = '127.0.0.1'
    PORT = 18000
    UUID = sys.argv[1]
    MODE = sys.argv[2]

    payload_method = {
        'random': get_random_payload,
        'static': get_static_payload
    }

    if MODE not in payload_method:
        print('INVALID MODE!')
        sys.exit(1)
    
    client = connect(HOST, PORT)

    while True:
        latitude, longitude, speed = payload_method[MODE]()
        payload = serialize_payload(UUID, latitude, longitude, speed)
        print('Transmitting state')
        print(f'UUID: {UUID} lat: {latitude} long: {longitude} speed: {speed}')
        client.send(payload)
        time.sleep(1)