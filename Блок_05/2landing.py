from pioneer_sdk import *
import time

mk=Pioneer()
mk.arm()
time.sleep(1)
mk.takeoff()
try:
    mk.go_to_local_point(0, 0, 1.5, 0)
    time.sleep(5)
    while mk.get_dist_sensor_data()>0.2:
        time.sleep(0.2)
finally:
    mk.land()
    time.sleep(2)
    mk.disarm()