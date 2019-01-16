from __future__ import print_function

import datetime
import sys
import time

from bluepy.btle import BTLEException
from bluepy.sensortag import SensorTag

# configurations to be set accordingly
SENSORTAG_ADDRESS = "54:6C:0E:4D:AC:00"

def enable_sensors(tag):
    """Enable sensors so that readings can be made."""
    tag.IRtemperature.enable()
    tag.accelerometer.enable()
    tag.humidity.enable()
    tag.magnetometer.enable()
    tag.barometer.enable()
    tag.gyroscope.enable()
    tag.keypress.enable()
    tag.lightmeter.enable()
    # tag.battery.enable()

    # Some sensors (e.g., temperature, accelerometer) need some time for initialization.
    # Not waiting here after enabling a sensor, the first read value might be empty or incorrect.
    time.sleep(1.0)

def disable_sensors(tag):
    """Disable sensors to improve battery life."""
    tag.IRtemperature.disable()
    tag.accelerometer.disable()
    tag.humidity.disable()
    tag.magnetometer.disable()
    tag.barometer.disable()
    tag.gyroscope.disable()
    tag.keypress.disable()
    tag.lightmeter.disable()
    tag.battery.disable()


def get_readings(tag):
    """Get sensor readings and collate them in a dictionary."""
    try:
        enable_sensors(tag)
        readings = {}
        readings["accel_x"], readings["accel_y"],readings["accel_z"] = tag.accelerometer.read()
        # IR sensor
        readings["ir_temp"], readings["ir"] = tag.IRtemperature.read()
        # humidity sensor
        readings["humidity_temp"], readings["humidity"] = tag.humidity.read()
        # barometer
        readings["baro_temp"], readings["pressure"] = tag.barometer.read()
        # luxmeter
        readings["light"] = tag.lightmeter.read()
        # battery
        #readings["battery"] = tag.battery.read()
        disable_sensors(tag)

        # round to 2 decimal places for all readings
        readings = {key: round(value, 2) for key, value in readings.items()}
        return readings

    except BTLEException as e:
        print("Unable to take sensor readings.")
        print(e)
        return {}


def reconnect(tag):
    try:
        tag.connect(tag.deviceAddr, tag.addrType)

    except Exception as e:
        print("Unable to reconnect to SensorTag.")
        raise e

def main():
    temp=[]
    humid=[]
    light=[]
    data=[[]]
    print('Connecting to {}'.format(SENSORTAG_ADDRESS))
    tag = SensorTag(SENSORTAG_ADDRESS)
    print('Press Ctrl-C to quit.')
    while True:
        # get sensor readings
        readings = get_readings(tag)
        if not readings:
            print("SensorTag disconnected. Reconnecting.")
            reconnect(tag)
            continue
        sleepScore = 0
        workScore = 0
        
        """Implementation of basic UI"""
        print("------------------------------------------")
        print("Temperature:\t\t{}".format(readings["ir_temp"]))
        if readings["ir_temp"] < 16:
            if readings["ir_temp"] < 12:
                print("It's way too cold. Raise to at least 16 C.")
            else:
                print("It's cold. Raise to at least 16 C.")
        elif readings["ir_temp"] > 26:
            if readings["ir_temp"] > 30:
                print("It's way too warm. Lower to at least 26 C.")
            else:
                print("It's warm. Lower to at least 26 C.")
        else:                
            print("Temperature is ideal for sleep.") 
            
        print("\nHumidity:\t\t{}".format(readings["humidity"]))
        if readings["humidity"] < 60:
            print("It's too dry.")
        elif readings["humidity"] > 85:
            print("It's too humid")
        else:                
            print("Humidity levels are good.")
        
        print("\nLight levels:\t\t{}".format(readings["light"]))
        if readings["light"] < 5:
            print("ok : Sleep | X : Work ")
        elif readings["light"] < 200:
            print("X : Sleep | X : Work ")
        else:
            print("X : Sleep | ok : Work")
        print("------------------------------------------")
        
#        temp.append(readings["ir_temp"])
#        humid.append(readings["humidity"])
#        light.append(readings["light"])
        
        
if __name__ == "__main__":
    main()
