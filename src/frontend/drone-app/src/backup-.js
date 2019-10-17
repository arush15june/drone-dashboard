import React, { useState, useEffect } from 'react';
import DeckGL from '@deck.gl/react';
import {LineLayer} from '@deck.gl/layers';
import {StaticMap} from 'react-map-gl';
import {IconLayer} from '@deck.gl/layers';

import {
    GetDrone
} from './API'
require('dotenv').config()

export default function Map({ match }) {
    let uuid = match.params.uuid

    const [markerOptions, setMarkerOptions] = useState({
        latitude: 0,
        longitude: 0
    })

    const [viewstate, setViewState ] = useState({
        longitude: 0,
        latitude: 0,
        zoom: 2,
        pitch: 0,
        bearing: 0
    })

    const [lineLayerData, setLineLayerData] = useState([
        {sourcePosition: [0, 0], targetPosition: [0, 0]}
    ])

    useEffect(() => {
        const interval = setInterval(async () => {
            let data = await GetDrone(uuid)
            let latitude = data['latitude']
            let longitude = data['longitude']
            setMarkerOptions({
                latitude: latitude,
                longitude: longitude
            })
            setViewState({
                ...viewstate,
                latitude: latitude,
                longitude: longitude
            })
            const lastTargetPosition = lineLayerData[lineLayerData.length - 1].targetPosition
            let newLineData = {
                sourcePosition: [markerOptions.latitude, markerOptions.longitude],
                targetPosition: lastTargetPosition
            }
            lineLayerData.push(newLineData)
            console.log(uuid, data, viewstate, markerOptions)
        }, 1000)
        return () => clearInterval(interval);
    }, [])
    
    useEffect(() => {
        
    }, [markerOptions])

    const mapStyle = 'mapbox://styles/mapbox/dark-v9'

    return (
        <DeckGL
        {...viewstate}
        initialViewState={viewstate}
        controller={{dragRotate: false}}
        
      >
        <StaticMap
            reuseMaps
            mapStyle={mapStyle}
            preventStyleDiffing={true}
        />
      </DeckGL>
    )
}