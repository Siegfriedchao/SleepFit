# fitHome
Using Sensor Tag 2650 &amp; Raspberry Pi to provide real time monitoring of environment/room conditions.

This repository contains the following
* Python code used to read and display sensor readings from the TI SensorTag 2650
* HTML file containing the handle attributes and addresses
* Sample measurement data 

This project was developed with Python 2.7 on Raspbian Stretch.
## Setup
1. Install the standard Raspbian OS on to a Raspberry Pi

2. Allow the automatic updates to complete on first boot (if any) then reboot (should prompt you).

3. Open terminal and run the following code.

```bash
#Run
sudo apt-get install libglib2.0-0 libglib2.0-dev 
#Install;
sudo pip install bluepy
```

4. Set bluetooth address on fitHome.py (to find your SensorTag's address for [this guide](https://developer.ibm.com/recipes/tutorials/ti-sensor-tag-and-raspberry-pi/) a similar guide can also be found in the requirement.md file within this repo.

```bash
SENSORTAG_ADDRESS = "54:6C:0E:4D:AC:00" #insert your address instead, within the quote ("") marks
```

5. Save changes & execute (and switch on SensorTag)
```bash
python fitHome.py
```
## Configuring
As the SensorTag contains a myriad of other sensors too, it could be easily adapted for other purposes. Below is a list of other commands which could be used to access the 
- Barometer 
- Accelerometer
- Magnetometer
- Gyroscope
They have been commented out but can be implemented similarly by uncommenting them within ;
```bash
def enable_sensors(tag):
  ...

def disable_sensors(tag):
  ...
  
def get_readings(tag):
  ...
```

## Credits
- Bluepy
-- [Ian Harvey](github.com/IanHarvey)

- Raspberry Weather Station
-- [YuXuan Tay](github.com/yxtay)
