""" Drone listener """

import datetime
import socket
import threading

import drone_pb2
from db import init_db, db_session
from models import DroneState
from schema import DroneStateSchema
import drones

NEW_LINE = '\n'

def parse_utc_timestamp(timestamp):
    return datetime.datetime.utcfromtimestamp(timestamp)

def parse_proto_message(data):
    return drone_pb2.DroneState().FromString(data)

def parse_drone_message(message_data):
    """ 
        Parse received protobuf binary messasge.
    """
    try:
        drone_data = parse_proto_message(message_data)
    except:
        print("INVALID DATA")
        return
    
    schema_data = {
        'latitude': drone_data.latitude,
        'longitude': drone_data.longitude,
        'data_timestamp': parse_utc_timestamp(drone_data.timestamp).isoformat(),
        'curr_speed': drone_data.curr_speed
    }

    drone = drones.update_drone(drone_data.uuid, schema_data)
    print(drone)

def connection_handler(client_socket):
    while True:
        try:
            recvd_data = client_socket.recv(1024)
            while NEW_LINE.encode() not in recvd_data:
                recvd_data += client_socket.recv(1024)
            
            parse_drone_message(recvd_data.rstrip())

        except ConnectionError:
            client_socket.close()
            print("Closing connection")
            break
            
def tcp_listener(host, port):
    """
    TCP Listener 
    
    :param host str: listener host.
    :param port int: port to listen on.
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    
    while True:
        client_sock, address = server.accept()
        print('Accepted connection from {}:{}'.format(address[0], address[1]))
        client_handler = threading.Thread(
            target=connection_handler,
            args=(client_sock,)  # without comma you'd get a... TypeError: handle_client_connection() argument after * must be a sequence, not _socketobject
        )
        client_handler.start()

if __name__ == "__main__":
    init_db()
    import signal, sys

    def handler(signum, frame):
        sys.exit(1)

    # Set the signal handler and a 5-second alarm
    signal.signal(signal.SIGINT, handler)

    HOST = '0.0.0.0'
    PORT = 18000

    tcp_listener(HOST, PORT)

    while True:
        pass