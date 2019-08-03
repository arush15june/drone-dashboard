""" Simulated Drone """

import socket

import drone_pb2
import datetime
import calendar
import time

NEW_LINE = '\n'

def get_timestamp():
    """ Get UTC Timestamp. """

    return calendar.timegm(datetime.datetime.utcnow().utctimetuple())

def serialize_payload(uuid, latitude, longitude):
    """ Serilaized payload as protobuf binary """
    drone_state = drone_pb2.DroneState()
    drone_state.uuid = uuid
    drone_state.latitude = latitude
    drone_state.longitude = longitude
    drone_state.timestamp = int(get_timestamp())

    return drone_state.SerializeToString()
    
def connect(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    return client

def send_payload(client, payload):
    client.send(payload)

def close_connection(client):
    client.close()

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 18000
    UUID = '36520bf6-360a-4ed5-b2e8-a0afb0f37b88'
    
    client = connect(HOST, PORT)

    while True:
        latitude = 1.0
        longitude = 2.0
        payload = serialize_payload(UUID, latitude, longitude)
        print(payload)
        client.send(payload)
        time.sleep(1)