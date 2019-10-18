""" Simulated Drone """

import sys
import csv
import os
import socket
import random
import datetime
import calendar
import time
import itertools

import drone_pb2

NEW_LINE = '\n'

def get_timestamp():
    """ 
    Get UTC Timestamp. 

    :return int: utc timestamp.
    """

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
    if len(sys.argv) <= 4:
        print("Usage: ./drone.py HOST UUID [random | static | csv]")
        sys.exit(1)

    def get_random_payload():
        """ Randomly generated device state. """
        speed = random.uniform(10.0, 15.0)
        lat, long = get_random_lat_long()

        return lat, long, speed
    
    def get_static_payload():
        return 1.0, 2.0, 10.0

    def get_csv_payload(csv_file):
        if csv_file is None:
            return None

        csvfile = open(csv_file)
        location_csv = csv.reader(csvfile, delimiter=',', quotechar='|')
        location_iterator = itertools.cycle(location_csv)
        
        def f():
            data = next(location_iterator)
            return float(data[1]), float(data[2]), float(data[3])
        
        return f

    HOST = sys.argv[1] 
    PORT = 18000
    UUID = sys.argv[2]
    MODE = sys.argv[3]

    try:
        csv_loc = sys.argv[4]
    except:
        csv_loc = None

    payload_method = {
        'random': get_random_payload,
        'static': get_static_payload,
        'csv': get_csv_payload(csv_loc)
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