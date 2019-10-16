# gets the data from json and appends it as a new row in the csv file

import json
import csv


# creating an array from the json file


def updateCSV():
    with open('/home/ubuntu/received_data.json', 'r') as f:
        py_dict = json.load(f)
    humidity = py_dict.get('humidity')
    pressure = py_dict.get('pressure')
    temperature = py_dict.get('temperature')
    curr_time = py_dict.get('curr_time')
    csv_record = [humidity, pressure, temperature, curr_time]
    file_name = '/home/ubuntu/csv_register_linux.csv'
    with open(file_name, 'a') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(csv_record)


#file_name = '/home/ubuntu/csv_register_linux.csv'
#field_names = ['humidity', 'pressure', 'temperature', 'current time']

#with open(file_name, 'w') as csvfile:
#    csvwriter = csv.writer(csvfile)
#    csvwriter.writerow(field_names)
#    csvwriter.writerow(csv_record)


