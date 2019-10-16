import mysql.connector
import json
import time

def mysqlTrans():
    
    link = mysql.connector.connect(
        host='localhost',
        user='project-user',
        passwd='iot2019',
        database='sensor_vals_fixed'
    )
    
    connection = link.cursor()

    sql_copy = "INSERT INTO SensorDataArchive (value_id, humidity, pressure, temperature, curr_time) SELECT value_id, humidity, pressure, temperature, curr_time FROM SensorData ORDER BY value_id ASC LIMIT 1"

    connection.execute(sql_copy)

    link.commit()
   
    sql = "DELETE FROM SensorData ORDER BY value_id ASC LIMIT 1"
    
    connection.execute(sql)
    
    link.commit()





