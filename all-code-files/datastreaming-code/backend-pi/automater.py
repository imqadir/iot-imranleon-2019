from bme_extended import takeReading
from paho_client_simple import sendToMqtt
from csv_updater import updateCSV
import time
import json



i=0
while i<10:
    val_array = takeReading()
    humidity_val = round(val_array[0],2)
    pressure_val = round(val_array[1],2)
    temperature_val = round(val_array[2],2)
    #noting the current time
    time_stamp = time.asctime(time.localtime(time.time()))
    #making a python object from measured values
    reading_obj = {
        'humidity' : humidity_val,
        'pressure' : pressure_val,
        'temperature' : temperature_val,
        'curr_time' : time_stamp
        }
    with open('/home/pi/sensor_data/data.json', 'w') as f:
        json.dump(reading_obj, f)
    sendToMqtt()
    #updateCSV()
    print('the loop number at the moment is', i)
    i += 1

print('\nthe loop is now ended', i)


#takeReading()
#makeJson()
#sendToMqtt()
    





