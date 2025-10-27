from pioneer_sdk import *
import time

mk=Pioneer()
while True:
    cl=mk.get_dist_sensor_data()-0.1
    if cl<0:
        cl=0
    if cl>1:
        cl=1
    mk.led_control(255, 1-cl, cl, 0)
    time.sleep(0.2)