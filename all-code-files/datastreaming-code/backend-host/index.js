const express = require('express');
const cors = require('cors');
const mysql = require('mysql');

const app= express();

const DATABASE_QUERY = 'SELECT * FROM SensorData';

const connection = mysql.createConnection({
    host:'localhost',
    user:'project-user',
    password:'iot2019',
    database:'sensor_vals_fixed'
});

connection.connect(err => {
    if(err){
        return err;
    }
});

app.use(cors());

app.get('/', (req, res)=>{
    res.send('The sensor server homepage')
});
/*
app.get('/sensor/add', (req, res)=>{
    const { humidity, pressure, temperature, curr_time } = req.query;
    const INSERT_DATA_QUERY = `INSERT INTO SensorData (humidity, pressure, temperature, curr_time) VALUES ('${humidity}', '${pressure}', '${temperature}', '${curr_time}')`;
    connection.query(INSERT_DATA_QUERY, (err, results) => {
        if(err){
            return res.send(err)
        }
        else{
            return res.send('successfully added data')
        }
    });

});
*/

app.get('/sensor', (req, res)=>{
    connection.query(DATABASE_QUERY, (err, results)=>{
        if(err){
            return res.send(err)
        }
        else{
            return res.json({
                data: results
            })
        }

    });

});

app.listen(4000, () => {
    console.log('sensor server listening at port 4000')
});
