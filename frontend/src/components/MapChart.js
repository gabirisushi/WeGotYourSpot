import React, { Component } from 'react';
import Map from 'pigeon-maps';
import Marker from 'pigeon-marker';

const providers = {
  osm: (x, y, z) => {
    const s = String.fromCharCode(97 +(x + y + z) % 3)
    return `https://${s}.tile.openstreetmap.org/${z}/${x}/${y}.png`
  }
}


class MapChart extends Component {
    constructor () {
      super()
      this.state = {
          center: [48.69429, 9.1866],
          zoom: 14,
          provider: 'osm',
          metaWheelZoom: false,
          twoFingerDrag: false,
          animate: true,
          zoomSnap: true,
          mouseEvents: true,
          touchEvents: true,
          minZoom: 1,
          maxZoom: 18,
          dragAnchor: [48.8565, 2.3475],
          markers: [],
          currentPosition: {},
          count: {}
      }
    }

    componentDidMount() {
        let newCenter = []
        newCenter.push(this.props.destination.latitude)
        newCenter.push(this.props.destination.longitude)
        this.setState({
            currentPosition : this.props.destination,
            markers : this.props.parkings,
            center: newCenter
          });
    }

    zoomIn() {
        this.setState({
            zoom: Math.min(this.state.zoom + 1, 18)
        })
    }

    zoomOut()  {
        this.setState({
            zoom: Math.max(this.state.zoom - 1, 1)
        })
    }

    handleClick({ event, latLng, pixel }) {
        console.log('Map clicked!', latLng, pixel)
    }

    createMap() {
        const { center, zoom, provider, animate, metaWheelZoom, zoomSnap, mouseEvents, touchEvents, markers } = this.state
        return (
        <div style={{padding: '50px',margin: '0 auto'}}>
            <Map
                limitBounds='edge'
                center={center}
                zoom={zoom}
                provider={providers[provider]}
                dprs={[1, 2]}
                onClick={this.handleClick}
                animate={animate}
                metaWheelZoom={metaWheelZoom}
                zoomSnap={zoomSnap}
                mouseEvents={mouseEvents}
                touchEvents={touchEvents}
                defaultWidth={900}
                height={600}
                boxClassname="pigeon-filters">
                {
                    markers.map((marker) => (
                        <Marker anchor={[marker.latitude, marker.longitude]} payload={1} onClick={({ event, anchor, payload }) => {this.props.showParkingInfo(marker)}} />
                ))}
                {
                  <Marker anchor={[this.state.currentPosition.latitude, this.state.currentPosition.longitude]} payload={1} onClick={({ event, anchor, payload }) => {}} />
                }
            </Map>
          </div>
        );
    }

    render() {
        return (
        <div>
            {this.createMap()}
        </div>);
    }
}

export default MapChart;
