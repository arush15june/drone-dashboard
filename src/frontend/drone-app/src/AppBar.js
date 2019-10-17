import React from 'react'
import Navbar from 'react-bootstrap/Navbar'
import { Link } from 'react-router-dom'

export default function AppBar(props) {
  return (
    <React.Fragment>
      <Navbar bg="dark">
        <Navbar.Brand><Link to={'/'}>Dronesy</Link></Navbar.Brand>
      </Navbar>
    </React.Fragment>
  )
}