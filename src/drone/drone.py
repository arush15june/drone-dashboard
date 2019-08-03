""" Simulated Drone """

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
    """ Serilaized payload as protobuf binary """
    drone_state = drone_pb2.DroneState()
    drone_state.uuid = uuid
    drone_state.latitude = latitude
    drone_state.longitude = longitude
    drone_state.timestamp = int(get_timestamp())
    drone_state.curr_speed = speed

    return drone_state.SerializeToString()
    
def connect(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    return client

def send_payload(client, payload):
    client.send(payload)

def close_connection(client):
    client.close()

def get_random_lat_long():
    return (random.uniform(-90.0, 90.0), random.uniform(-90.0, 90.0))

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 18000
    UUID = '36520bf6-360a-4ed5-b2e8-a0afb0f37b88'
    
    client = connect(HOST, PORT)

    while True:
        latitude, longitude = get_random_lat_long()
        speed = random.uniform(10.0, 15.0)
        payload = serialize_payload(UUID, latitude, longitude, speed)
        print(payload)
        client.send(payload)
        time.sleep(1)