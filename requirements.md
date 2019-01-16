# To run the Python Script
1. Run;
```bash
sudo apt-get install libglib2.0-0 libglib2.0-dev 
```
2. Install;
```bash
bluepy (https://github.com/IanHarvey/bluepy)
```
# To find Bluetooth Address
1. Run,
```bash 
wget http://www.kernel.org/pub/linux/bluetooth/bluez-5.32.tar.xz 
```

2. Then run,
```bash 
sudo apt-get install libglib2.0-0 libglib2.0-dev 

sudo apt-get install libdbus-1-dev 

sudo apt-get install libudev-dev 

sudo apt-get install libical-dev 

sudo apt-get install libreadline-dev

sudo apt-get install libusb-1.0-0-dev
```
3. Unpack bluez package and open directory.

4. Run,
```
bash sudo ./configure --prefix=/usr --mandir=/usr/share/man --sysconfdir=/etc --localstatedir=/var --with-systemdsystemunitdir --with-systemduserunitdir --enable-library 
```
 
5. Run,
```bash 
sudo make 
```

6. Run,
```bash 
sudo cp attrib/gatttool /usr/local/bin
```

7. Scan bluetooth devices near by;
```bash
sudo hcitool lescan 
```

8. Look for your SensorTag and note the address (as below);
```bash
C4:BE:78:A6:09 CC2650 Sensor Tag 
```


More details can be found here,
https://github.com/IanHarvey/bluepy
https://github.com/yxtay/raspberry-pi-sensortag
