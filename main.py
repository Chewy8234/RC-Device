"""
Program that moves car in set route, when ultrasonic detect something that block its way,car will turn right to avoid it and comes back
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
    count = 0
    def __init__(self, speed, obstacle_dis):
        self.speed = speed
        self.obstacle_dis = obstacle_dis
        

    def avoid:
        for angle in range(0,35):
            px.set_dir_servo_angle(angle)
            time.sleep(0.01)
        for angle in range(35,0,-1):
            px.set_dir_servo_angle(angle)
            time.sleep(0.01)
    
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
                    avoid()
                    count +=1
                else:
                    px.set_dir_servo_angle(0)#no change in direction
    """
    def route:
        try:
            px.px.forward(speed)
            time.sleep(0.5)
            for angle in range(0,35):
                px.set_dir_servo_angle(angle)
                time.sleep(0.01)
            for angle in range(35,0,-1):
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
    """
    def route:
        px.px.forward(speed)


if __name__ == "__main__":
    picar = car(10, 20)
    
    while picar.count < 2: # when car do twice avoid motion, stop the car
        picar.route
        picar.detect
        
    picar.speed = 0


        
