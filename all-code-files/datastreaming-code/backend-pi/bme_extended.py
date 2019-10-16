# takes the reading from the sensor and makes json object

import bme280
import smbus2

port = 1
address = 0x76 # Number 76 is used because our sensor is manufactured by SparkFun 
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

def takeReading ():
    bme280_data = bme280.sample(bus,address)
    humidity  = bme280_data.humidity
    pressure  = bme280_data.pressure
    ambient_temperature = bme280_data.temperature
    return [humidity, pressure, ambient_temperature];






