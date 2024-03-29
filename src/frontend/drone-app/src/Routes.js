import React from "react";
import { Route } from "react-router-dom";
import Drones from './Drones';
import Map from './Map'

export default function ReactRouter() {
    return (
        <React.Fragment>
            <Route exact path="/" component={Drones} />
            <Route exact path="/drones" component={Drones} />
            <Route exact path="/drones/:uuid" component={Map} />
        </React.Fragment>
    );
}