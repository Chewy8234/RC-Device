#!/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')
from ezblock import __reset_mcu__
import time
__reset_mcu__()
time.sleep(0.01)

from picarmini import dir_servo_angle_calibration
from picarmini import forward
from ezblock import delay
from picarmini import backward
from picarmini import set_dir_servo_angle
from picarmini import stop

states = { 
        "w": "move forward",
        "a": "turn left",
        "s": "backword",
        "d": "turn right",
        "stop": "stopthe car"
        }

"""
initialize the car and return initialized car status
"""
def init():
    dir_servo_angle_calibration(0) #initialize car wheel to the front
    return""


def askcontrol():
    userinput = input("Welcome to car control!\n Enter the control[w/a/s/d/stop]: ").lower()
    return userinput

def update(carstate,userinput):
    """
    Update car movement state by using finite state machine
    parameters:
      * carstate: the state of the car
      * userinput: user input on car state
    return:
      * carstate: the state of the car
    """
    if userinput == "w":
        carstate = "w"
    elif  userinput == "a":
        carstate = "a"
    elif  userinput == "s":
        carstate = "s"
    elif  userinput== "d":
        carstate = "d"
    elif userinput == "stop":
        carstate = "stop"

    return carstate


def move(carstate):
    if carstate == "w":
        forward(50)
    elif carstate == "a":
        delay(1000)
        set_dir_servo_angle((-30))
    elif carstate == "s":
        delay(1000)
        backward(50)
    elif carstate == "d":
        delay(1000)
        set_dir_servo_angle(30)
    elif carstate == "stop":
        stop()


def carcontrol():
    carstate = init()
    while carstate != "stop":
        userinput = askcontrol()
        carstate = update(carstate,userinput)
        move(carstate)

if __name__ == "__main__":
    carcontrol()
