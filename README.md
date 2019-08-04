# Drone Dashboard Assignment

Real Time Dashboard for Drones

## Architecture

Technical Decisions and simulation assumptions for the assignment.

### Backend
- REST API built with Flask.
    - Use the REST API to add new drones and list all existing ones.
    - Used by the frontend to poll for drones in the database.
- Temporary SQLite database from storing drone data.
- Automated Tests with unittest.
- Mark drones not moving if they have been sending data 
but have not moved over 1 meter in the last 10 seconds.
- Application served via gunicorn.
- Handle every drone uniquely by its UUID.
- Background TCP Server to handle messages from drones.
    - Concurrently handle messages from multiple clients.
    - The server parses protobuf serialized messages from the drone.
    As cellular connections are expensive, the aim should
    be to reduce the amount of data transferred, protobuf 
    allows that by reducing the size of the mesasge transmitted 
    over the network.
    - The rudimentary TCP server was a decision for the assignment,
    it should be replaced with a full fledged message broker like RabbitMQ,
    and listen for messages over AMQP and MQTT to create a very efficient messaging architecture.
    - Having the drone message worker be seperated from the server allows to work on the REST API
    seperately from the handler itself, thus the worker could be kept running to make sure messages
    are not missed, even if the API Server is down.
- Simplistic self documenting code.


### Drone
- Unique UUID4 (acc to RFC 4122) associcated with every drone.
- Reports latitude, longitude and current speed as its state.
- Decision for the assignment: Connects over TCP to the drone server.
    - to be replaced with an MQTT or AMQP client
- Communication:
    - transmits messages serializing with protobuf to reduce size of the data transmitted (compared to JSON/XML/plaintext)
- Simulation:
    - random data
      - send random latitude, longitudes, speeds every few seconds.
    - static data
      - simulate stopped drone.

### Frontend
- Written in React using React-Bootstrap
  - Lists all drones and polls the REST API every 2 seconds (default).
  - Allows creation of new drones.
  - Displays all drones as a table.

## Documentation

### Tests
```
docker-compose -f docker-compose.test.yml up
```

### Container
- Start NGINX and Flask App.
```
docker-compose up
```
- Serves the frontend on 0.0.0.0:2800 and starts the listener on 0.0.0.0:18000

### REST API
| Endpoint | Method | Description |
|---------|-----|----|
| /drones | GET | Get state of all drones in database.|
| /drones | POST | Create new drone in database.|
| /drones/\<string:uuid> | PUT | Update state of drone by UUID.|
| /drones/\<string:uuid> | GET | Get State of drone by UUID.|
| /drones/\<string:uuid> | DELETE | Delete drone by UUID.|

### Drone
- requires python3
```python
pip install -r src/drone/requirements.txt
python src/drone/drone.py HOST UUID MODE<random/static> 
```
- random movement
```python
python src/drone/drone.py HOST UUID random
```
Sends random latitude, longtiude and current speed to the server

- static movement
```python
python src/drone/drone.py HOST UUID static
```
send static movement to the server.

- Use random movement to intialize moving state of drone.
- Use static movement to simulate non moving state of drone (switches state in 10 seconds).

### Usage
    - Initialize docker-compose.
    - Add a new drone (via 0.0.0.0:2800 frontend).
    - Start drone simulation for specific drone UUID.