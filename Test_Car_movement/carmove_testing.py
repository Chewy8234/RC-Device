
"""
picarx module has basic functionality of Parker 
Can be used to control steering gear and wheels, and will make the PiCar-X move forward, turn in an S-shape, or shake its head.
"""
"""
forward(): Orders the PiCar-X go forward at a given speed.

set_dir_servo_angle: Turns the Steering servo to a specific angle.

set_camera_servo1_angle: Turns the Pan servo to a specific angle.

set_camera_servo2_angle: Turns the Tilt servo to a specific angle.
"""
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


dir_servo_angle_calibration(0)
def forever():
  forward(50)
  delay(1000)
  backward(50)
  delay(1000)
  forward(50)
  set_dir_servo_angle((-30))
  delay(1000)
  forward(50)
  set_dir_servo_angle(30)
  delay(1000)
  set_dir_servo_angle(0)
  stop()
  delay(2000)

if __name__ == "__main__":
    while True:
        forever()  
