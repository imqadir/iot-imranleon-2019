import React, { Component } from 'react';

class ApiWeather extends Component {
    constructor(){
        super();
        this.state={
            city: undefined,
            pressure: undefined,
            temp: undefined,
        };
        this.getWeather();
    }

    getWeather = async() => { 
        const api_call = await fetch("http://api.openweathermap.org/data/2.5/weather?q=Oulu&appid=58b1f072de0327f45be91ce1a819c2fe");

    const response = await api_call.json();

    this.setState({
        city: response.name,
        pressure: response.main.pressure,      
        temp: Math.round(response.main.temp-273.15),
    })
}

    render() {
        return (
            <div className="localweather">
                <h2>Information from OpenWeatherMap API for {this.state.city}</h2>
                Pressure: {this.state.pressure} hPa             <br/>
                Current temperature: {this.state.temp} °C       <br/>
                                                                <br/>
                Please refresh the page to see new values.      <br/>   
            </div>
        );
    }
}

export default ApiWeather;
