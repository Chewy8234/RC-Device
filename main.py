"""
Program that moves car in set route, when ultrasonic detect something that block its way,car will turn left to avoid it
"""
"""
car movement method:

px.forward(speed)
px.set_dir_servo_angle(angle)


"""

from picarx import Picarx
import time

class car:
    px = Picarx()
    speed = int()
    obstacle_dis = int()
    angle = int() #control the angle of the car turn

        
 """
function detect()
purpose: keep checking whether there are obstacle ahead of the car in set distance
"""   
    def detect():
        while True:
            # px = Picarx(ultrasonic_pins=['D2','D3']) # tring, echo
            distance = px.ultrasonic.read()
            print("distance: ",distance)
            if distance > 0 and distance < 300:
                if distance < obstacle_dis:
                    px.set_dir_servo_angle(-35)#turn left
                else:
                    px.set_dir_servo_angle(0)#no change in direction
    
    def route:
        try:
            px.px.forward(speed)
            time.sleep(0.5)
            for angle in range(0,35):
                px.set_dir_servo_angle(angle)
                time.sleep(0.01)
            for angle in range(0,35):
                px.set_dir_servo_angle(angle)
                time.sleep(0.01)
            for angle in range(0,35):
                px.set_dir_servo_angle(angle)
                time.sleep(0.01)
            for angle in range(0,35):
                px.set_dir_servo_angle(angle)
                time.sleep(0.01)
        finally:
            px.forward(0)



if __name__ == "__main__":
        


        
