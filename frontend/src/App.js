import React, { Component } from 'react';
import './App.css';
import Network from './Network';
import { Form, Row, Button } from 'react-bootstrap';
import moment from 'moment'
import MapChart from './components/MapChart'

//map appid = reTU0kpxabMj6wk9exvq appkey = Agrxvfl82lkHM6XgXorj1YelSxPjnxePo-VamUV00Dw
//rest appid = txZF8JGv1FuLW8AXL4Kp appkey = z3aMphCKMa11sXSvf_ObiR0t776OShwmtfHgMNrpMxE
const DEMO_DESTINATION = {"latitude":52.49868925, "longitude":13.37485757}
const DEMO_PARKINGS = [
                      { id: 1, "latitude":52.51006, "longitude":13.3689744, "name": "Parkhaus Philharmonie APCOA", "free":12, "price":2},
                      { id :2, "latitude":52.5029838, "longitude":13.3738265, "name": "Parkhaus Gleisdreieck", "free":1 , "price":3}]

class App extends Component {
  constructor(){
    super()
    this.state = {
      "searched": false,
      "searchObj" : undefined
    }
  }

  handleSubmit(event) {
    event.preventDefault();
    let form = event.target.elements;
    let searchObject = {};
    searchObject.keyword = form.destination.value
    searchObject.destination = DEMO_DESTINATION
    searchObject.parkings = DEMO_PARKINGS
    searchObject.from = moment(form.from.value + ' ' + form.fromTime.value + ":00");
    searchObject.to = moment(form.to.value + ' ' + form.toTime.value + ":00");
    searchObject.type = {}
    searchObject.type.women = form.women.checked
    searchObject.type.family = form.family.checked
    searchObject.type.truck = form.truck.checked
    console.log(searchObject)
    // do some request to backend
    this.setState({
      searched: true,
      searchObj: searchObject
    });
  }

  showParkingInfo(parking) {
    alert(parking.name + " has " + parking.free + " free spots for " + parking.price + " per hour")
  }

  renderSearchField() {
    return (
      <div className="App">
       <Form onSubmit={this.handleSubmit.bind(this)}>
       <Row className="centered">
       <Form.Group size="lg" controlId="destination">
         <Form.Label>Your destination</Form.Label>
         <Form.Control type="text" placeholder="Where do you want to go?" />
       </Form.Group>
       &nbsp;&nbsp;&nbsp;
       <Form.Group controlId="from">
         <Form.Label>From</Form.Label>
         <Form.Control type="date" style={{width:'100%'}} />
       </Form.Group>
       <Form.Group controlId="fromTime">
         <Form.Label>Hour</Form.Label>
         <Form.Control type="text"  style={{width:'50px'}}/>
       </Form.Group>
       &nbsp;&nbsp;&nbsp;
       <Form.Group controlId="to">
         <Form.Label>To</Form.Label>
         <Form.Control type="date" style={{width:'100%'}} />
       </Form.Group>
       <Form.Group controlId="toTime">
         <Form.Label>Hour</Form.Label>
         <Form.Control type="text"  style={{width:'50px'}}/>
       </Form.Group>
       </Row>
       <Row className="centered">
         <Form.Check
           type="switch"
           id="women"
           label="women"
         />
         &nbsp;&nbsp;&nbsp;
         <Form.Check
           type="switch"
           label="family"
           id="family"
         />
         &nbsp;&nbsp;&nbsp;
         <Form.Check
           type="switch"
           label="truck"
           id="truck"
         />
       </Row>
       <Row className="centered">
         <Button type="submit">Go</Button>
       </Row>
       </Form>
      </div>
    );
  }

  render(){
    if (!this.state.searched) {
      return this.renderSearchField();
    } else {
      return (
        <MapChart
          destination={this.state.searchObj.destination}
          parkings={this.state.searchObj.parkings}
          showParkingInfo={this.showParkingInfo}
        />
      );
    }
 }

}

export default App;
