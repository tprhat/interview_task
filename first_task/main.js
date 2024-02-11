import './style.css';
import {Feature, Map, View,} from 'ol';
import TileLayer from 'ol/layer/Tile';
import OSM from 'ol/source/OSM';
import {fromLonLat} from "ol/proj";
import {Polygon} from "ol/geom";
import {Vector} from "ol/layer";
import { Vector as Vector1 } from "ol/source";
import 'ol';



const map = new Map({
    target: 'map',
    layers: [
        new TileLayer({
            source: new OSM()
        }),
    ],
    view: new View({
        center: [0, 0],
        zoom: 2
    })
});


// Load and display the polygon from the JSON file
fetch('./polygon.json')
    .then(response => response.json())
    .then(polygonData => {
        // Convert the polygon coordinates to OpenLayers format
        var polygonCoordinates = polygonData.polygon.map(coord =>
            fromLonLat(coord)
        );

        // Create the polygon feature
        var polygonFeature = new Feature({
            geometry: new Polygon([polygonCoordinates])
        });

        // Create a vector layer to display the polygon
        var vectorLayer = new Vector({
            source: new Vector1({
                features: [polygonFeature]
            })
        });

        // Add the vector layer to the map
        map.addLayer(vectorLayer);

        // Fit the map view to the extent of the polygon
        map.getView().fit(polygonFeature.getGeometry().getExtent(), {
            padding: [50, 50, 50, 50]
        });
    })
    .catch(error => console.error('Error fetching JSON:', error));