import React, { useState, useEffect } from 'react';
import MapGL, {Marker } from 'react-map-gl'
import 'mapbox-gl/dist/mapbox-gl.css'
import { haversineDistance } from './Util'

import {
    GetDrone
} from './API'
import { FaRegDotCircle } from 'react-icons/fa'
require('dotenv').config()

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
        zoom: 2
    })

    useEffect(() => {
        const interval = setInterval(async () => {
            let data = await GetDrone(uuid)
            let latitude = data['latitude']
            let longitude = data['longitude']
            setMarkerOptions({
                latitude: latitude,
                longitude: longitude
            })
            if(haversineDistance(viewport.longitude, viewport.latitude, longitude, latitude) > 10) {
                setViewPort({
                    ...viewport,
                    latitude: data['latitude'],
                    longitude: data['longitude'],
                })
            }
            console.log(uuid, data, viewport, markerOptions)
        }, 500)
        return () => clearInterval(interval);
    }, [])

    const _onViewportChange = viewport => setViewPort({...viewport})
    
    return (
    <MapGL
    {...viewport}
    mapStyle={mapBoxMapStyle}
    onViewportChange={_onViewportChange}
    >
        <Marker {...markerOptions}>
            <MarkerIcon style={markerStyle} />
        </Marker>
    </MapGL>
    )
}