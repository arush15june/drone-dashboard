import React from 'react';

import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Button from 'react-bootstrap/Button'
import Table from 'react-bootstrap/Table'
import Spinner from 'react-bootstrap/Spinner'

const HOST = ''
const PORT = '' 
const URL = HOST+PORT

const DRONES_API = '/api/drones'

/* 
  Get list of all drones.
*/
async function get_drones() {
  let req = await fetch(URL+DRONES_API)
  let req_json = await req.json()
  
  return req_json
}

/* 
  Add a new drone to database.
*/
async function add_drone() {
  let req = await fetch(URL+DRONES_API, {
    'method': 'POST',
    'body': JSON.stringify({}),
    'headers': {
      'Content-Type': 'application/json'
    }
  })
  
  let req_json = await req.json()
  
  return req_json
}

/* 
  Generate a table row from drone_state json.
*/
function generate_table_row(drone_json) {
  let uuid = drone_json['uuid']
  let latitude = drone_json['latitude']
  let longitude = drone_json['longitude']
  let data_timestamp = drone_json['data_timestamp']
  let speed = drone_json['curr_speed']
  let moving = drone_json['is_moving']
  let move_timestamp = drone_json['move_timestamp']
  
  return (
    <React.Fragment>
    <tr>
      <td>{uuid}</td>
      <td>{latitude.toFixed(3)}</td>
      <td>{longitude.toFixed(3)}</td>
      <td>{data_timestamp}</td>
      <td>{speed.toFixed(3)}</td>
      <td>{moving ? '✓' : '✖'}</td>
      <td>{move_timestamp}</td>
    </tr> 
    </React.Fragment>
  )
}
/* 
    Drones
*/
class Drones extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      drone_list: [],
      update: 2*1000, // Update Frequency. 2 seconds.
      spinner: false
    }
    this.droneListUpdateHandler = this.droneListUpdateHandler.bind(this)
    this.addButtonHandler = this.addButtonHandler.bind(this)
  }

  toggleSpinner() {
    this.setState({
      spinner: !this.state.spinner
    })
  }
  
  /* 
    Button handler to add a new drone.
  */
  async addButtonHandler() {
    this.toggleSpinner()
    let add_req = await add_drone()
    this.toggleSpinner()
    if (add_req.uuid != null) {
      console.log('Drone Created')
    }
  }
  
  /* 
    Update the drone table.
  */
  async droneListUpdateHandler() {
    let all_drones = await get_drones()
    all_drones = all_drones.map(generate_table_row);
    
    this.setState({
      drone_list: all_drones
    })
  }
  

  componentDidMount() {
    this.timer = setInterval(this.droneListUpdateHandler, this.state.update)
  }
  render() {
      return (
        <Container>
          <Row>
            <Col>
              <Button disabled={this.state.spinner} onClick={this.addButtonHandler}>{this.state.spinner ?
            <Spinner
              as="span"
              animation="grow"
              size="sm"
              role="status"
              aria-hidden="true" 
            />: <React.Fragment></React.Fragment>} Add Drone</Button>
            </Col>
          </Row>
          <Row>
            <Col>
              <Table responsive='xl'>
                <thead>
                  <tr>
                    <th>UUID</th>
                    <th>Latitude</th>
                    <th>Longitude</th>
                    <th>Data Timestamp</th>
                    <th>Speed (m/s)</th>
                    <th>Moving</th>
                    <th>Move Timestamp</th>
                  </tr>
                </thead>
                {this.state.drone_list.length > 0 ? this.state.drone_list : <React.Fragment></React.Fragment>}
              </Table>
            </Col>
          </Row>
        </Container>      
      )
  } 
}

export default Drones;