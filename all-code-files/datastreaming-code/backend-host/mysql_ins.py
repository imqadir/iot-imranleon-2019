import mysql.connector
import json
from mysql_trans import mysqlTrans

def mysqlUpdater():
    with open('/home/imranq/Desktop/iot_final/received_data.json', 'r') as f:
        py_dict = json.load(f)
    val_one = py_dict.get('humidity')
    val_two = py_dict.get('pressure')
    val_three = py_dict.get('temperature')
    val_four = py_dict.get('curr_time')

    link = mysql.connector.connect(
        host='localhost',
        user='project-user',
        passwd='iot2019',
        database='sensor_vals_fixed'
    )
    connection = link.cursor()
    sql = "INSERT INTO SensorData (humidity, pressure, temperature, curr_time) VALUES (%s, %s, %s, %s)"
    val = (val_one, val_two, val_three, val_four)
    connection.execute(sql, val)
    link.commit()

    mysqlTrans()


    

#print("Total number of records is: ", connection.rowcount)

#connection.execute("SELECT * FROM SensorData")

#all_rows = connection.fetchall()

#for x in all_rows:
    #print(x)



