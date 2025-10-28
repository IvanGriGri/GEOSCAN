from pioneer_sdk import *
import time, random

fl=False

mk=Pioneer()
mk.arm()
time.sleep(1)
mk.takeoff()
try:
    mk.go_to_local_point_body_fixed(0, 0, 1.5, 0)
    mk.led_control(255, random.randint(0, 100)/100, random.randint(0, 100)/100, random.randint(0, 100)/100)
    time.sleep(5)
    while True:
        dist=mk.get_dist_sensor_data()
        if dist==None:
            continue
        if dist<0.5:
            if fl==False:
                mk.led_control(255, random.randint(0, 100)/100, random.randint(0, 100)/100, random.randint(0, 100)/100)
            fl=True
        else:
            fl=False
        time.sleep(0.1)
finally:
    mk.land()
    mk.led_control(255, 0, 0, 0)
    time.sleep(5)
    mk.disarm()