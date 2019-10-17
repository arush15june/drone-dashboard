const HOST = 'http://localhost'
const PORT = ':5000'
const URL = HOST+PORT

const DRONES_API = '/api/drones'

/* 
  Get list of all drones.
*/
async function GetDrones() {
    let req = await fetch(URL+DRONES_API)
    let req_json = await req.json()
    
    return req_json
}

/* 
Add a new drone to database.
*/
async function AddDrone() {
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
    Fetch information of single drone.
*/
async function GetDrone(uuid) {
    let req = await fetch(URL+DRONES_API+`/${uuid}`)
    let req_json = await req.json()
    
    return req_json
}
  
export {
    HOST,
    PORT,
    URL,
    DRONES_API,
    GetDrones,
    GetDrone,
    AddDrone
}