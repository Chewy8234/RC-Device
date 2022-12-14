
## RC-Device
RC device project is a class project for CNT 4104 - Software Proj Comp Networks.<br />
The purpose of this project is through building and programming real life remote device, learning knowledge on network.<br />

## Device used
* Raspberry Pi 4 Model B 2019 Quad Core 64 Bit WiFi Bluetooth (4GB)<br />
![Sample Image](Device_structure_image/rpi.png)<br />
* SunFounder Raspberry Pi Smart Video Robot Car Kit for Raspberry Pi, Python/Blockly (Like Scratch), Web Control, Line Tracking, Raspberry Pi Robot Kits for Teens and Adults (Raspberry Pi NOT Included) <br />
![Sample Image](Device_structure_image/picar.png)<br />

## Application used
* Putty - a network protocol used to allow secure access to a UNIX terminal

## Language used
* Python

## Acknowledgments/ Reference
* https://github.com/sunfounder/picar-x.git

## Steps
### 1. Connect the Raspberry Pi to the Internet. 
* You need to modify a Wi-Fi configuration file wpa_supplicant.conf in the Micro SD card by your PC that is located in the directory /etc/wpa_supplicant/
* For linux: access the directory directly to modify the configuration file
* For windows:if your PC use Windows system, then you can’t access the directory and what you need next is to go to the directory, /boot/ to create a new file with the same name, wpa_supplicant.conf.
```
# replace “Wi-Fi-A” with your custom name of WiFi and “Sunfounder” with your password. 
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=GB
network={
ssid=”Wi-Fi-A” 
psk=”Sunfounder”
key_mgmt=WPA-PSK
priority=1
}
```
### 2. Get the IP Address
* Checking via Router
* Network Segment Scanning

### 3. Build connection for remote control by Putty
* Open PuTTY. Enter the IP address of the RPi in the text box under Host Name (or IP address) and 22 under Port (by default it is 22). Click Open<br />
![Sample Image](Device_structure_image/step3.png)
* When the PuTTY window prompts “login as:”, type in “pi” (the user name of theRPi), and password: “raspberry” (the default one, if you haven’t changed it). <br />
![Sample Image](Device_structure_image/step4.png)
### 4. Send .py to the car to work through putty
Example with 1.move.py:
```
sudo python3 1.move.py
```
![Sample Image](Device_structure_image/step5.png)
### 5. Result
https://user-images.githubusercontent.com/54412715/206800803-4047e9b6-db4c-42cb-80c5-cb8a6eee0dc3.mp4

