import React, { useState, useEffect } from 'react';
import MapGL, {Marker } from 'react-map-gl'
import 'mapbox-gl/dist/mapbox-gl.css'
import { haversineDistance } from './Util'
import useInterval from '@use-it/interval';

import {
    GetDrone
} from './API'
import { FaRegDotCircle } from 'react-icons/fa'
require('dotenv').config()

const MAPBOX_TOKEN = 'pk.eyJ1IjoiYmF0dGVyeWNoYXJnZXIiLCJhIjoiY2sxdXAxMWV1MGQ1ZDNucXVtcGo4emlobSJ9.inK45HvAdqwtHdbMsbNdOw'

const markerStyle = {
    color: '#FFFFFF',
}
const MarkerIcon = FaRegDotCircle

const mapBoxMapStyle = "mapbox://styles/mapbox/dark-v9"

export default function Map({ match }) {
    let uuid = match.params.uuid
    
    const [markerOptions, setMarkerOptions] = useState({
        latitude: 0,
        longitude: 0
    })

    const [viewport, setViewPort ] = useState({
        width: "100%",
        height: 800,
        latitude: 0,
        longitude: 0,
        zoom: 16
    })

    useInterval(async () => {
        let data = await GetDrone(uuid)
        let latitude = data['latitude']
        let longitude = data['longitude']
        setMarkerOptions({
            latitude: latitude,
            longitude: longitude
        })

        let distance = haversineDistance(viewport.longitude, viewport.latitude, longitude, latitude)
        console.log(distance, viewport.latitude, viewport.longitude, latitude, longitude)
        if( distance > 10) {
            setViewPort({
                ...viewport,
                latitude: data['latitude'],
                longitude: data['longitude'],
                zoom: 16
            })
        }
        console.log(uuid, data, viewport, markerOptions)
    }, 500)

    const _onViewportChange = viewport => setViewPort({...viewport})
    
    return (
    <MapGL
    {...viewport}
    mapStyle={mapBoxMapStyle}
    onViewportChange={_onViewportChange}
    mapboxApiAccessToken={MAPBOX_TOKEN}
    >
        <Marker {...markerOptions}>
            <MarkerIcon style={markerStyle} />
            <p style={markerStyle}>{uuid}</p>
        </Marker>
    </MapGL>
    )
}