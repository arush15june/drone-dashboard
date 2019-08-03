# Drone Dashboard Assignment

Real Time Dashboard for Drones

## Architecture

Technical Decisions and simulation assumptions for the assignment.

### Backend
    - REST API
    - In Memory SQLite Database for storing drone state.
### Drone
    - unique UUID (acc to RFC 4122) associcated with every drone.
    - Reports latitude and longitude as its state.
    - Communication:
    
### Frontend

## Documentation

### Container
```docker-commpose up```

### REST API
| Endpoint | Method | Description |
|---------|-----|----|
| /drones | GET | Get State of All Drones In Database.|