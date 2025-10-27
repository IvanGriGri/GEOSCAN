from pioneer_sdk import *
import time

mk=Pioneer()
while True:
    cl=mk.get_dist_sensor_data()
    if cl<0.5:
        mk.led_control(255, 1, 0, 0)
    elif cl>0.5 and cl<1:
        mk.led_control(255, 0, 1, 0)
    elif cl>1:
        mk.led_control(255, 0, 0, 1)
    time.sleep(0.2)