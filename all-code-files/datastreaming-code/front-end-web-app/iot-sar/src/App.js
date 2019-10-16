import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Chart from 'react-google-charts';
import Footer from './components/Footer.js';
import Header from './components/Header.js';
import ApiWeather from './components/ApiWeather.js';

class App extends Component {
  
  constructor (props){
    super(props);
    this.state={
      temperatures:[],
      pressures:[],
      times:[],
      latestTemperature:undefined,
      latestPressure:undefined,
      counter: 0,
    };
  }


  componentDidMount(){
    this.timerID = setInterval(
      () => this.loadData(), 60000
    );
  }

  componentWillUnmount(){
    clearInterval(this.timerID);
  }

  loadData(){
    var newVal = this.state.counter + 1;
    this.setState({
      counter: newVal,
    });
    fetch('http://localhost:4000/sensor')
    .then(results => {
        return results.json();
    }).then(results => {
        var temperature=[];
        var pressure=[];
        var time=[];
        for (var i=0;i<results.data.length;i++){
            temperature.push(results.data[i].temperature)
            pressure.push(results.data[i].pressure)
            time.push(results.data[i].curr_time)
        }
        this.setState( {temperatures: temperature} )
        this.setState( {pressures: pressure} )
        this.setState( {times: time} )
        this.setState( {latestTemperature: temperature[temperature.length-1]} )
        this.setState( {latestPressure: pressure[pressure.length-1]} )
    })
  }
  
  render(){
    var dataArr=[];
    var dataArr2=[];
    
    dataArr.push(['Time', 'Pi Temperature']);
    dataArr2.push(['Time', 'Pi Pressure']);
    for (var i=0; i<this.state.temperatures.length; i++){
      var timeString = String(this.state.times[i]);
      var temperatureVal = this.state.temperatures[i];
      var pressureVal = this.state.pressures[i];
      var arr = [timeString, temperatureVal];
      var arr2 = [timeString, pressureVal];
      dataArr.push(arr);
      dataArr2.push(arr2);

    }
    return (
      <div className="Main">
        <div><Header /></div>
        <br/>
        <div><ApiWeather /></div>
        <h2>Temperature and Pressure data from the Sensor</h2>
        <h4>Total number of updates during this session: {this.state.counter}</h4>
        <p>The latest reported temperature is: {this.state.latestTemperature}</p>
        <div>
          <Chart
          width={'1500px'}
          height={'500px'}
          chartType='LineChart'
          loader={<div>Loading Chart</div>}
          data={dataArr}
          options={{
            title: 'Temperature values',
            hAxis: { title: 'Recording time and date', titleTextStyle: { color: '#333' } },
            vAxis: { minValue: 21.5, maxValue:22.5 },
            backgroundColor: '#D1EAF8',
            chartArea: { width: '75%', height: 'auto' }
          }}
          />
        </div>
        <h4>Total number of updates during this session: {this.state.counter}</h4>
        <p>The latest reported pressure is: {this.state.latestPressure}</p>
        <div>
          <Chart
          width={'1500px'}
          height={'500px'}
          chartType='LineChart'
          loader={<div>Loading Chart</div>}
          data={dataArr2}
          options={{
            title: 'Pressure values',
            hAxis: { title: 'Recording time and date', titleTextStyle: { color: '#333' } },
            vAxis: { minValue: 1016, maxValue:1020 },
            backgroundColor: '#D1EAF8',
            chartArea: { width: '75%', height: 'auto' }
          }}
          />
        </div>        
        <div className="footer">
          <Footer />
        </div> 
      </div>
    );
  }

}

export default App;
